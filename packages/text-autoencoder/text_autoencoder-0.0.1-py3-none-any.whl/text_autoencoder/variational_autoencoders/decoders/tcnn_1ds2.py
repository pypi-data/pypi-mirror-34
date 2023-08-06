import math
from typing import List, Tuple

import tensorflow as tf
from layers.linear import tf_linear


def tCNN1ds2(
        input_: tf.Tensor,  # tf.placeholder
        input_dropout: float,
        maxlen: int,
        output_size: int,
        filter_structures: List[Tuple[int]],
        is_training: bool = False,
    ) -> Tuple[tf.Tensor, tf.Tensor]:
    '''transposed CNN 1D Stride 2
    input_: batch_size * latent size
    filter_structures: [(filter_size, output_channels)]
    '''
    batch_size = tf.shape(input_)[0]

    init_seqlen = math.ceil(maxlen / 2 ** len(filter_structures))
    init_dim = input_.shape[1].value // init_seqlen
    refined_size = init_dim * init_seqlen

    refined_input = tf_linear(
        input_value=input_,
        name='refined_input',
        output_width=refined_size,
        initializer=tf.random_normal_initializer(stddev=0.1),
    )
    refined_input_with_dropout = tf.nn.dropout(
        x=refined_input,
        keep_prob=(1.0 - input_dropout),
    )

    mid_value = tf.reshape(
        refined_input_with_dropout,
        shape=[-1, 1, init_seqlen, init_dim],
    )

    for i, (filter_size, output_channels) in enumerate(filter_structures):
        input_channels = mid_value.shape[-1]

        filter_ = tf.get_variable(
            name='filter_{}'.format(i),
            shape=[1, filter_size, output_channels, input_channels],
            dtype=tf.float32,
            initializer=tf.random_normal_initializer(stddev=0.1),
        )
        output_seq_len = math.ceil(
            maxlen / 2 ** (len(filter_structures) - i - 1))

        tconv = tf.nn.conv2d_transpose(
            mid_value,
            filter_,
            output_shape=[batch_size, 1, output_seq_len, output_channels],
            strides=[1, 1, 2, 1],
            padding='SAME',
            name='tconv_{}'.format(i),
        )
        mid_value = tf.nn.relu(
            tf.contrib.layers.batch_norm(
                tconv,
                decay=0.99,
                center=True,
                scale=True,
                updates_collections=None,
                is_training=True,
                scope='batch_norm_{}'.format(i),
            ),
            name='activated_tconv_{}'.format(i),
        )

    conv_output = tf.reshape(
        mid_value,
        shape=[-1, mid_value.shape[-1]],
    )
    output = tf_linear(
        input_value=conv_output,
        name='logits_to_be_reshaped',
        output_width=output_size,
        initializer=tf.random_normal_initializer(stddev=0.1),
    )
    output_logits = tf.reshape(
        output,
        shape=[-1, mid_value.shape[-2], output_size],
        name='logits',
    )
    output_word_indices = tf.argmax(
        output_logits,
        axis=-1,
        name='word_indices',
        output_type=tf.int32,
    )
    return output_logits, output_word_indices
