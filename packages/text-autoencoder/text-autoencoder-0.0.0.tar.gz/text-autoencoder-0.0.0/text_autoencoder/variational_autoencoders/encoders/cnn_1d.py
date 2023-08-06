from typing import List, Tuple

import tensorflow as tf

from layers.linear import tf_linear


def CNN1D(
        input_: tf.Tensor,
        embedding_table: tf.Tensor,  # np.ndarray
        input_dropout: float,
        output_size: int,
        filter_structures: List[Tuple[int]],
        is_training: bool = False,
    ) -> Tuple[tf.Tensor, tf.Tensor]:
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
        filter_ = tf.get_variable(
            name='cnn_filter_{}'.format(i),
            shape=[filter_size, input_channels, output_channels],
            dtype=tf.float32,
            initializer=tf.random_normal_initializer(stddev=0.1),
        )
        conv = tf.nn.conv1d(
            mid_value,
            filter_,
            stride=stride,
            padding='VALID',
            data_format='NWC',
            name='conv_{}'.format(i),
        )
        mid_value = tf.nn.relu(
            features=tf.contrib.layers.batch_norm(
                conv,
                decay=0.99,
                center=True,
                scale=True,
                updates_collections=None,
                is_training=is_training,
                scope='batch_norm_{}'.format(i),
            ),
            name='activated_conv_{}'.format(i),
        )

    conv_out = tf.reshape(
        mid_value,
        shape=[-1, mid_value.shape[-1] * mid_value.shape[-2]],
        name='conv_output',
    )
    output_mean = tf_linear(
        input_value=conv_out,
        name='mean_vector',
        output_width=output_size,
        initializer=tf.random_normal_initializer(stddev=0.1),
    )
    output_std = tf_linear(
        input_value=conv_out,
        name='std_vector',
        output_width=output_size,
        initializer=tf.random_normal_initializer(stddev=0.1),
    )
    return output_mean, output_std
