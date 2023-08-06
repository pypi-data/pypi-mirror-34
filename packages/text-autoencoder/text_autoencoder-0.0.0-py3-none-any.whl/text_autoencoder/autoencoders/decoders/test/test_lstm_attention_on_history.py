import numpy as np
import tensorflow as tf

from .data import Data
from ..lstm_attention_on_history import LSTM_LatentVec_InitState_AttentiveHistory


class LSTM_LatentVec_InitState_AttentiveHistoryTestCase(Data, tf.test.TestCase):

    def setUp(self):
        self.get_data()

    def tearDown(self):
        tf.reset_default_graph()

    def test_input_with_tensor_default(self):
        with self.test_session() as sess:
            logits, word_indices = LSTM_LatentVec_InitState_AttentiveHistory(
                latent_input=tf.convert_to_tensor(self.latent_input),
                real_indices=tf.convert_to_tensor(self.real_indices),
                embedding_table=self.embedding,
                history_size=50,
                attention_hidden_size=30,
                attention_hops=5,
                state_size=37,
                assist=0,
            )
            sess.run(tf.global_variables_initializer())

            self.assertAllEqual(
                (self.batch_size, self.maxlen, self.vocab_size),
                logits.eval().shape,
            )
            self.assertEqual(np.float32, logits.dtype)
            self.assertEqual('logits:0', logits.name)

            self.assertAllEqual(
                (self.batch_size, self.maxlen),
                word_indices.eval().shape,
            )
            self.assertEqual(np.int32, word_indices.dtype)
            self.assertEqual('word_indices:0', word_indices.name)

    def test_input_with_init_state(self):
        with self.test_session() as sess:
            logits, word_indices = LSTM_LatentVec_InitState_AttentiveHistory(
                latent_input=tf.convert_to_tensor(self.latent_input),
                real_indices=tf.convert_to_tensor(self.real_indices),
                embedding_table=self.embedding,
                history_size=50,
                attention_hidden_size=30,
                attention_hops=5,
                init_state=tf.contrib.rnn.LSTMStateTuple(
                    *(
                        tf.random_normal((self.batch_size, 49)),
                        tf.random_normal((self.batch_size, 49)),
                    ),
                ),
                assist=0,
            )
            sess.run(tf.global_variables_initializer())

            self.assertAllEqual(
                (self.batch_size, self.maxlen, self.vocab_size),
                logits.eval().shape,
            )
            self.assertEqual(np.float32, logits.dtype)
            self.assertEqual('logits:0', logits.name)

            self.assertAllEqual(
                (self.batch_size, self.maxlen),
                word_indices.eval().shape,
            )
            self.assertEqual(np.int32, word_indices.dtype)
            self.assertEqual('word_indices:0', word_indices.name)

    def test_input_with_placeholder_assisted(self):
        with self.test_session() as sess:
            logits, word_indices = LSTM_LatentVec_InitState_AttentiveHistory(
                latent_input=self.latent_place,
                real_indices=self.real_indices_place,
                embedding_table=self.embedding,
                history_size=50,
                attention_hidden_size=30,
                state_size=37,
                assist=1,
            )
            sess.run(tf.global_variables_initializer())
            output_logits, output_word_indices = sess.run(
                [logits, word_indices],
                feed_dict={
                    self.latent_place: self.latent_input,
                    self.real_indices_place: self.real_indices,
                },
            )
            self.assertAllEqual(
                (self.batch_size, self.maxlen, self.vocab_size),
                output_logits.shape,
            )
            self.assertEqual(np.float32, output_logits.dtype)
            self.assertEqual('logits:0', logits.name)

            self.assertAllEqual(
                (self.batch_size, self.maxlen),
                output_word_indices.shape,
            )
            self.assertEqual(np.int32, output_word_indices.dtype)
            self.assertEqual('word_indices:0', word_indices.name)
