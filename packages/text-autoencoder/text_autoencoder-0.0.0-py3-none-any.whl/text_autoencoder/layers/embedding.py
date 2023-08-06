import tensorflow as tf
import numpy as np


def get_embedding(
        embedding_array: np.ndarray = None,
        vocab_size: int = None,
        embedding_size: int = None,
        trainable: bool = True,
        name: str = 'embedding',
        dtype: tf.DType = tf.float32,
    ) -> tf.Tensor:

    if embedding_array is not None:
        embedding = tf.get_variable(
            name=name,
            dtype=dtype,
            initializer=embedding_array.astype('float32'),
            trainable=trainable,
        )
    else:
        if (not vocab_size) or (not embedding_size):
            raise KeyError(
                '''
                vocab_size and embedding_size are required to create
                a random initialized embedding.
                ''',
            )
        embedding = tf.get_variable(
            name=name,
            shape=[vocab_size, embedding_size],
            dtype=dtype,
            trainable=trainable,
            initializer=tf.truncated_normal_initializer(stddev=1.0),
        )
    return embedding
