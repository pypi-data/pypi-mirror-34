# -*- coding: utf-8 -*-
"""Main module."""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Normal, kl_divergence as kl

from scvi.metrics.log_likelihood import log_zinb_positive, log_nb_positive
from scvi.models.modules import Encoder, DecoderSCVI
from scvi.models.utils import one_hot

torch.backends.cudnn.benchmark = True


# VAE model
class VAE(nn.Module):
    r"""Variational auto-encoder model.

    Args:
        :n_input: Number of input genes.
        :n_batch: Default: ``0``.
        :n_labels: Default: ``0``.
        :n_hidden: Number of hidden. Default: ``128``.
        :n_latent: Default: ``1``.
        :n_layers: Number of layers. Default: ``1``.
        :dropout_rate: Default: ``0.1``.
        :dispersion: Default: ``"gene"``.
        :log_variational: Default: ``True``.
        :reconstruction_loss: Default: ``"zinb"``.

    Examples:
        >>> gene_dataset = CortexDataset()
        >>> vae = VAE(gene_dataset.nb_genes, n_batch=gene_dataset.n_batches * False,
        ... n_labels=gene_dataset.n_labels, use_cuda=True )

    """

    def __init__(self, n_input, n_batch=0, n_labels=0, n_hidden=128, n_latent=10, n_layers=1, dropout_rate=0.1,
                 dispersion="gene", log_variational=True, reconstruction_loss="zinb"):
        super(VAE, self).__init__()
        self.dispersion = dispersion
        self.n_latent = n_latent
        self.log_variational = log_variational
        self.reconstruction_loss = reconstruction_loss
        # Automatically desactivate if useless
        self.n_batch = n_batch
        self.n_labels = n_labels
        self.n_latent_layers = 1

        if self.dispersion == "gene":
            self.px_r = torch.nn.Parameter(torch.randn(n_input, ))
        elif self.dispersion == "gene-batch":
            self.px_r = torch.nn.Parameter(torch.randn(n_input, n_batch))
        elif self.dispersion == "gene-label":
            self.px_r = torch.nn.Parameter(torch.randn(n_input, n_labels))
        else:  # gene-cell
            pass

        self.z_encoder = Encoder(n_input, n_latent, n_layers=n_layers, n_hidden=n_hidden,
                                 dropout_rate=dropout_rate)
        self.l_encoder = Encoder(n_input, 1, n_layers=1, n_hidden=n_hidden, dropout_rate=dropout_rate)
        self.decoder = DecoderSCVI(n_latent, n_input, n_cat_list=[n_batch], n_layers=n_layers, n_hidden=n_hidden,
                                   dropout_rate=dropout_rate)

    def get_latents(self, x, y=None):
        return [self.sample_from_posterior_z(x, y)]

    def sample_from_posterior_z(self, x, y=None):
        x = torch.log(1 + x)
        qz_m, qz_v, z = self.z_encoder(x, y)  # y only used in VAEC
        if not self.training:
            z = qz_m
        return z

    def sample_from_posterior_l(self, x):
        x = torch.log(1 + x)
        ql_m, ql_v, library = self.l_encoder(x)
        if not self.training:
            library = ql_m
        return library

    def get_sample_scale(self, x, batch_index=None, y=None, n_samples=1):
        qz_m, qz_v, z = self.z_encoder(torch.log(1 + x), y)
        qz_m = qz_m.unsqueeze(0).expand((n_samples, qz_m.size(0), qz_m.size(1)))
        qz_v = qz_v.unsqueeze(0).expand((n_samples, qz_v.size(0), qz_v.size(1)))
        z = Normal(qz_m, qz_v).sample()
        px = self.decoder.px_decoder(z, batch_index, y)  # y only used in VAEC - won't work for batch index not None
        px_scale = self.decoder.px_scale_decoder(px)
        return px_scale

    def get_sample_rate(self, x, batch_index=None, y=None, n_samples=1):
        ql_m, ql_v, library = self.l_encoder(torch.log(1 + x), y)
        ql_m = ql_m.unsqueeze(0).expand((n_samples, ql_m.size(0), ql_m.size(1)))
        ql_v = ql_v.unsqueeze(0).expand((n_samples, ql_v.size(0), ql_v.size(1)))
        library = Normal(ql_m, ql_v).sample()
        px_scale = self.get_sample_scale(x, batch_index=batch_index, y=y, n_samples=n_samples)
        return px_scale * torch.exp(library)

    def _reconstruction_loss(self, x, px_rate, px_r, px_dropout, batch_index, y):
        if self.dispersion == "gene-label":
            px_r = F.linear(one_hot(y, self.n_labels), self.px_r)  # px_r gets transposed - last dimension is nb genes
        elif self.dispersion == "gene-batch":
            px_r = F.linear(one_hot(batch_index, self.n_batch), self.px_r)
        elif self.dispersion == "gene":
            px_r = self.px_r

        # Reconstruction Loss
        if self.reconstruction_loss == 'zinb':
            reconst_loss = -log_zinb_positive(x, px_rate, torch.exp(px_r), px_dropout)
        elif self.reconstruction_loss == 'nb':
            reconst_loss = -log_nb_positive(x, px_rate, torch.exp(px_r))
        return reconst_loss

    def forward(self, x, local_l_mean, local_l_var, batch_index=None, y=None):
        # Parameters for z latent distribution
        x_ = x
        if self.log_variational:
            x_ = torch.log(1 + x_)

        # Sampling
        qz_m, qz_v, z = self.z_encoder(x_)
        ql_m, ql_v, library = self.l_encoder(x_)

        px_scale, px_r, px_rate, px_dropout = self.decoder(self.dispersion, z, library, batch_index)

        reconst_loss = self._reconstruction_loss(x, px_rate, px_r, px_dropout, batch_index, y)

        # KL Divergence
        mean = torch.zeros_like(qz_m)
        scale = torch.ones_like(qz_v)

        kl_divergence_z = kl(Normal(qz_m, torch.sqrt(qz_v)), Normal(mean, scale)).sum(dim=1)
        kl_divergence_l = kl(Normal(ql_m, torch.sqrt(ql_v)), Normal(local_l_mean, torch.sqrt(local_l_var))).sum(dim=1)
        kl_divergence = kl_divergence_z + kl_divergence_l

        return reconst_loss, kl_divergence
