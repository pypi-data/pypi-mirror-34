import numpy as np
import tensorflow as tf

from ..lstm_latent_vector_as_init_state import LSTM_LatentVectorAsInitState


class LSTMLatentVectorAsInitStateTestCase(tf.test.TestCase):

    def setUp(self):
        self.embedding = np.random.rand(50, 300).astype('float32')

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor_default(self):
        with self.test_session() as sess:
            logits, word_indices = LSTM_LatentVectorAsInitState(
                latent_vectors=tf.random_normal((10, 128)),
                real_indices=tf.random_uniform(
                    shape=[10, 20],
                    minval=0,
                    maxval=50,
                    dtype=tf.int32,
                ),
                lstm_input_dropout=0.1,
                lstm_output_dropout=0.1,
                lstm_state_dropout=0.2,
                embedding_table=self.embedding,
                assist=0,
            )
            sess.run(tf.global_variables_initializer())

            self.assertAllEqual((10, 20, 50), logits.eval().shape)
            self.assertEqual(np.float32, logits.dtype)
            self.assertEqual('logits:0', logits.name)

            self.assertAllEqual((10, 20), word_indices.eval().shape)
            self.assertEqual(np.int32, word_indices.dtype)
            self.assertEqual('word_indices:0', word_indices.name)

    def test_input_with_placeholder_assisted(self):
        with self.test_session() as sess:
            latent_vectors = tf.placeholder(
                shape=[None, 128],
                dtype=tf.float32,
            )
            real_indices = tf.placeholder(
                shape=[None, 20],
                dtype=tf.int32,
            )
            logits, word_indices = LSTM_LatentVectorAsInitState(
                latent_vectors=latent_vectors,
                real_indices=real_indices,
                lstm_input_dropout=0.1,
                lstm_output_dropout=0.1,
                lstm_state_dropout=0.2,
                embedding_table=self.embedding,
                assist=1,
            )
            sess.run(tf.global_variables_initializer())
            output_logits, output_word_indices = sess.run(
                [logits, word_indices],
                feed_dict={
                    latent_vectors:
                        np.random.rand(10, 128).astype('float32'),
                    real_indices:
                        np.random.randint(50, size=(10, 20)).astype('int32'),
                },
            )
            self.assertAllEqual((10, 20, 50), output_logits.shape)
            self.assertEqual(np.float32, output_logits.dtype)
            self.assertEqual('logits:0', logits.name)

            self.assertAllEqual((10, 20), output_word_indices.shape)
            self.assertEqual(np.int32, output_word_indices.dtype)
            self.assertEqual('word_indices:0', word_indices.name)
