import tensorflow as tf
from tensorflow.python.framework import ops


def l2_regularization(
        scale: float = 1e-5,
        dtype: tf.DType = tf.float32,
        name: str = 'l2_regularization',
        loss_collection: str = ops.GraphKeys.LOSSES,
    ) -> tf.Tensor:
    tvars = tf.trainable_variables()
    l2_regularizer = tf.contrib.layers.l2_regularizer(
        scale=scale,
    )
    regularization_term = tf.contrib.layers.apply_regularization(
        regularizer=l2_regularizer,
        weights_list=tvars,
    )
    regularization_term = tf.identity(regularization_term, name=name)
    tf.add_to_collection(
        name=loss_collection,
        value=regularization_term,
    )
    return regularization_term
