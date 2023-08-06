from typing import List, Tuple

import tensorflow as tf

from layers.linear import tf_linear


def StackedCNN(
        input_: tf.Tensor,
        embedding_table: tf.Tensor,  # np.ndarray
        input_dropout: float,
        output_size: int,
        filter_structures: List[Tuple[int]],
        is_training: bool = False,
        seed: int = 2018,
        dtype: tf.DType = tf.float32,
    ) -> tf.Tensor:
    '''
    filter_structures: filter_size, stride, output_channels
    '''
    input_with_embedding = tf.nn.embedding_lookup(
        params=embedding_table,
        ids=input_,
    )
    input_with_dropout = tf.nn.dropout(
        x=input_with_embedding,
        keep_prob=(1.0 - input_dropout),
    )
    mid_value = input_with_dropout

    for i, (filter_size, stride, output_channels) in enumerate(
        filter_structures):
        input_channels = mid_value.shape[-1]
        filter_variable = tf.get_variable(
            name='cnn_filter_{}'.format(i),
            shape=[filter_size, input_channels, output_channels],
            dtype=dtype,
            initializer=tf.keras.initializers.lecun_normal(seed=seed),
        )
        conv = tf.nn.conv1d(
            mid_value,
            filter_variable,
            stride=stride,
            padding='SAME',
            data_format='NWC',
            name='conv_{}'.format(i),
        )
        normed_conv = tf.contrib.layers.batch_norm(
            conv,
            decay=0.99,
            center=True,
            scale=True,
            is_training=is_training,
            scope='batch_norm_{}'.format(i),
        )
        mid_value = tf.nn.relu(
            features=normed_conv,
            name='activated_conv_{}'.format(i),
        )

    conv_out = tf.reshape(
        mid_value,
        shape=[-1, mid_value.shape[-1] * mid_value.shape[-2]],
        name='conv_output',
    )
    output_latent_vector = tf_linear(
        input_value=conv_out,
        name='latent_vector',
        output_width=output_size,
        initializer=tf.random_normal_initializer(
            stddev=0.1,
            seed=seed,
        ),
    )
    return output_latent_vector
