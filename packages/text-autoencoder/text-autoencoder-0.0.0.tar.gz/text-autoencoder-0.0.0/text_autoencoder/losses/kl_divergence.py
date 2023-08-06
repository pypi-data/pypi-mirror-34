from typing import Tuple

import tensorflow as tf
from tensorflow.python.framework import ops


def kl_divergence(
        z_mean: tf.Tensor,
        z_std: tf.Tensor,
        scale: float = 1.0,
        anneal: float = 0.0,
        dtype: tf.DType = tf.float32,
        name='kl_divergence_loss',
        loss_collection: str = ops.GraphKeys.LOSSES,
    ) -> Tuple[tf.Tensor, tf.Tensor]:

    kl_div_loss = 0.5 * tf.reduce_sum(
        tf.exp(z_std) + z_mean**2 - 1. - z_std,
        axis=1,
    )
    mean_kl_div = tf.cast(
        tf.reduce_mean(kl_div_loss),
        dtype=dtype,
    )
    scaled_annealed_kl = anneal * scale * mean_kl_div
    scaled_annealed_kl = tf.identity(scaled_annealed_kl, name=name)

    tf.add_to_collection(
        name=loss_collection,
        value=scaled_annealed_kl,
    )
    return mean_kl_div, scaled_annealed_kl
