import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

from .base_layer_test_case import BaseLayerTestCase
from ..structured_self_attention import (
    tf_structured_self_attention,
    tf_structured_self_attention_penalty,
)


class SelfAttentionTestCase(BaseLayerTestCase):

    def test_input_with_tensor(self):
        with self.test_session() as sess:
            result = tf_structured_self_attention(
                input_=tf.random_normal((20, 30, 128)),
                hidden_size=20,
                hops=5,
                initializer=tf.truncated_normal_initializer(stddev=0.1),
            )
            sess.run(tf.global_variables_initializer())
            self.assertAllEqual((20, 5, 128), result[0].eval().shape)
            self.assertAllEqual((20, 30, 5), result[1].eval().shape)
            self.assertEqual('attentive_random_normal:0', result[0].name)
            self.assertEqual('annotation_matrix:0', result[1].name)
            self.assertEqual(tf.float32, result[0].dtype)
            self.assertEqual(tf.float32, result[1].dtype)

    def test_input_with_placeholder(self):
        with self.test_session() as sess:
            input_place = tf.placeholder(
                shape=[None, 30, 128],
                dtype=tf.float32,
            )
            attentive_input, annotation_matrix = tf_structured_self_attention(
                input_=input_place,
                hidden_size=20,
                hops=5,
                initializer=tf.truncated_normal_initializer(stddev=0.1),
            )
            sess.run(tf.global_variables_initializer())
            output_attentive_input, output_annotation_matrix = sess.run(
                [attentive_input, annotation_matrix],
                feed_dict={
                    input_place:
                        np.random.rand(20, 30, 128).astype('float32'),
                },
            )
            self.assertAllEqual((20, 5, 128), output_attentive_input.shape)
            self.assertEqual(np.float32, output_attentive_input.dtype)
            self.assertEqual('attentive_Placeholder:0', attentive_input.name)

            self.assertAllEqual((20, 30, 5), output_annotation_matrix.shape)
            self.assertEqual(np.float32, output_annotation_matrix.dtype)
            self.assertEqual('annotation_matrix:0', annotation_matrix.name)

    def test_penalty(self):
        with self.test_session() as sess:
            input_ = 2 * tf.eye(5, batch_shape=[20])
            penalty = tf_structured_self_attention_penalty(
                annotation_matrix=input_,
            )
            sess.run(tf.global_variables_initializer())
            self.assertEqual('self_attention_penalty:0', penalty.name)
            self.assertAlmostEqual(6.7082043, penalty.eval(), places=3)
            self.assertAlmostEqual(
                6.7082043,
                tf.get_collection(ops.GraphKeys.LOSSES)[0].eval(),
                places=3,
            )
