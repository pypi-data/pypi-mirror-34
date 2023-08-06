import tensorflow as tf
from tensorflow.python.framework import ops


def batch_encoder_loss(
        latent_vector: tf.Tensor,  # batch_size * latent_size
        recon_latent_vector: tf.Tensor,  # batch_size * latent_size
        name: str = 'batch_encoder_loss',
    ) -> tf.Tensor:
    '''
    https://cs224d.stanford.edu/reports/OshriBarak.pdf
    '''
    batch_loss = tf.losses.cosine_distance(
        labels=latent_vector,
        predictions=recon_latent_vector,
        axis=1,
    )
    batch_loss = tf.identity(batch_loss, name=name)
    return batch_loss


def mean_encoder_loss(
        latent_vector: tf.Tensor,  # batch_size * latent_size
        recon_latent_vector: tf.Tensor,  # batch_size * latent_size
        dtype: tf.DType = tf.float32,
        name: str = 'mean_encoder_loss',
        loss_collection: str = ops.GraphKeys.LOSSES,
    ) -> tf.Tensor:
    batch_enco_loss = batch_encoder_loss(
        latent_vector=latent_vector,
        recon_latent_vector=recon_latent_vector,
    )
    mean_enco_loss = tf.cast(
        tf.reduce_mean(
            batch_enco_loss,
            name=name,
        ),
        dtype=dtype,
    )
    tf.add_to_collection(
        name=loss_collection,
        value=mean_enco_loss,
    )
    return mean_enco_loss

## Wait: geodesic
