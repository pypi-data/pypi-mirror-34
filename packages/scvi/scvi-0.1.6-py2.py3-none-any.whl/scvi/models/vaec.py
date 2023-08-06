import torch
from torch.distributions import Normal, Categorical, kl_divergence as kl

from scvi.models.classifier import Classifier
from scvi.models.modules import Encoder, DecoderSCVI
from scvi.models.utils import broadcast_labels
from scvi.models.vae import VAE


class VAEC(VAE):
    r"""A semi-supervised Variational auto-encoder model - inspired from M2 model,
    as described in (https://arxiv.org/pdf/1406.5298.pdf)

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
        :y_prior: Default: None, but will be initialized to uniform probability over the cell types if not specified

    Examples:
        >>> gene_dataset = CortexDataset()
        >>> vaec = VAEC(gene_dataset.nb_genes, n_batch=gene_dataset.n_batches * False,
        ... n_labels=gene_dataset.n_labels)

        >>> gene_dataset = SyntheticDataset(n_labels=3)
        >>> vaec = VAEC(gene_dataset.nb_genes, n_batch=gene_dataset.n_batches * False,
        ... n_labels=3, y_prior=torch.tensor([[0.1,0.5,0.4]]))
    """

    def __init__(self, n_input, n_batch, n_labels, n_hidden=128, n_latent=10, n_layers=1, dropout_rate=0.1,
                 y_prior=None, dispersion="gene", log_variational=True, reconstruction_loss="zinb"):
        super(VAEC, self).__init__(n_input, n_batch, n_labels, n_hidden=n_hidden, n_latent=n_latent, n_layers=n_layers,
                                   dropout_rate=dropout_rate, dispersion=dispersion, log_variational=log_variational,
                                   reconstruction_loss=reconstruction_loss)

        self.z_encoder = Encoder(n_input, n_latent, n_cat_list=[n_labels], n_hidden=n_hidden, n_layers=n_layers,
                                 dropout_rate=dropout_rate)
        self.decoder = DecoderSCVI(n_latent, n_input, n_cat_list=[n_batch, n_labels], n_layers=n_layers,
                                   n_hidden=n_hidden, dropout_rate=dropout_rate)

        self.y_prior = torch.nn.Parameter(
            y_prior if y_prior is not None else (1 / n_labels) * torch.ones(1, n_labels), requires_grad=False
        )

        self.classifier = Classifier(n_input, n_hidden, n_labels, n_layers=n_layers, dropout_rate=dropout_rate)

    def classify(self, x):
        x = torch.log(1 + x)
        return self.classifier(x)

    def forward(self, x, local_l_mean, local_l_var, batch_index=None, y=None):
        is_labelled = False if y is None else True

        # Prepare for sampling
        x_ = torch.log(1 + x)
        ql_m, ql_v, library = self.l_encoder(x_)

        # Enumerate choices of label
        ys, xs, library_s, batch_index_s = (
            broadcast_labels(
                y, x, library, batch_index, n_broadcast=self.n_labels
            )
        )

        if self.log_variational:
            xs_ = torch.log(1 + xs)

        # Sampling
        qz_m, qz_v, zs = self.z_encoder(xs_, ys)

        px_scale, px_r, px_rate, px_dropout = self.decoder(self.dispersion, zs, library_s, batch_index_s, ys)

        reconst_loss = self._reconstruction_loss(xs, px_rate, px_r, px_dropout, batch_index_s, ys)

        # KL Divergence
        mean = torch.zeros_like(qz_m)
        scale = torch.ones_like(qz_v)

        kl_divergence_z = kl(Normal(qz_m, torch.sqrt(qz_v)), Normal(mean, scale)).sum(dim=1)
        kl_divergence_l = kl(Normal(ql_m, torch.sqrt(ql_v)), Normal(local_l_mean, torch.sqrt(local_l_var))).sum(dim=1)

        if is_labelled:
            return reconst_loss, kl_divergence_z + kl_divergence_l

        reconst_loss = reconst_loss.view(self.n_labels, -1)

        probs = self.classifier(x_)
        reconst_loss = (reconst_loss.t() * probs).sum(dim=1)

        kl_divergence = (kl_divergence_z.view(self.n_labels, -1).t() * probs).sum(dim=1)
        kl_divergence += kl(Categorical(probs=probs),
                            Categorical(probs=self.y_prior.repeat(probs.size(0), 1)))
        kl_divergence += kl_divergence_l

        return reconst_loss, kl_divergence
