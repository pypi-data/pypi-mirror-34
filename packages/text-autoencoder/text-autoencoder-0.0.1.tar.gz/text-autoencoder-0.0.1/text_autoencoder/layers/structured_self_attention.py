from typing import Tuple

import tensorflow as tf
from tensorflow.python.framework import ops


def tf_structured_self_attention(
        input_: tf.Tensor,
        hidden_size: int,
        hops: int,
        initializer: tf.initializers = tf.truncated_normal_initializer(),
        dtype: tf.DType = tf.float32,
        name: str = 'attentive',
    ) -> Tuple[tf.Tensor, tf.Tensor]:
    '''
    Reference: A Structured Self-Attentive Sentence Embedding
    Link: https://arxiv.org/pdf/1703.03130.pdf

    input_ (tensor: batch_size * maxlen * embedding_size):
        data to be attention
    hops (int): multiple hops of attention

    Returns:
        attentive input (tensor: batch_size * hops * embedding_size):
            attentive data
        annotation matrix (tensor: batch_size * maxlen * hops):
            learned attention parameters

    '''
    maxlen = tf.shape(input_)[1]
    input_dim = input_.shape[2]
    weight_1 = tf.get_variable(
        shape=[input_dim, hidden_size],
        name='weight_1',
        initializer=initializer,
        dtype=dtype,
    )
    weight_2 = tf.get_variable(
        shape=[hidden_size, hops],
        name='weight_2',
        initializer=initializer,
        dtype=dtype,
    )

    reshaped_input = tf.reshape(
        tensor=input_,
        shape=[-1, input_dim],
    )
    # tanh(Ws1 * H)
    nonlinear_trans = tf.nn.tanh(tf.matmul(reshaped_input, weight_1))
    # A = Ws2 * tanh(Ws1 * H)
    annotation_matrix = tf.nn.softmax(
        tf.reshape(
            tensor=tf.matmul(nonlinear_trans, weight_2),
            shape=[-1, maxlen, hops],
        ),
        axis=1,
        name='annotation_matrix',
    )
    # M = A * H
    attentive_input_transposed = tf.matmul(
        tf.transpose(input_, perm=[0, 2, 1]),
        annotation_matrix,
    )
    attentive_input = tf.transpose(
        attentive_input_transposed,
        perm=[0, 2, 1],
        name='{}_{}'.format(name, input_.name[:-2]),
    )
    return attentive_input, annotation_matrix


def tf_structured_self_attention_penalty(
        annotation_matrix: tf.Tensor,
        name: str = 'self_attention_penalty',
        loss_collection: str = ops.GraphKeys.LOSSES,
    ) -> tf.Tensor:
    batch_size = tf.shape(annotation_matrix)[0]
    # A * A^T - I
    diff = tf.matmul(
        a=annotation_matrix,
        b=tf.transpose(annotation_matrix, perm=[0, 2, 1]),
    ) - tf.eye(
        num_rows=tf.shape(annotation_matrix)[1],
        batch_shape=[batch_size],
        dtype=annotation_matrix.dtype,
    )
    # |A* A^T - I|_F
    batch_annotation_penalty = tf.norm(
        tensor=diff,
        axis=(1, 2),
        ord='fro',
    )
    annotation_penalty = tf.reduce_mean(batch_annotation_penalty, name=name)
    tf.add_to_collection(loss_collection, annotation_penalty)
    return annotation_penalty
