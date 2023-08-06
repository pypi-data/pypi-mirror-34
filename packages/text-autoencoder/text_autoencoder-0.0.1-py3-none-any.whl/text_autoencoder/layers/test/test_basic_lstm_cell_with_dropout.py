import tensorflow as tf

from .base_layer_test_case import BaseLayerTestCase
from ..basic_lstm_cell_with_dropout import (
    basic_lstm_cell_with_dropout,
)


class BasicLSTMWithDropoutTestCase(BaseLayerTestCase):

    def test_not_given_init_state(self):
        with self.test_session():
            cell, state = basic_lstm_cell_with_dropout(
                state_size=20,
                batch_size=2,
                output_dropout=0.1,
                state_dropout=0.0,
                input_dropout=0.1,
                init_state=None,
            )
            self.assertAllEqual((2, 20), state.h.eval().shape)
            self.assertEqual(tf.float32, state.h.dtype)

            self.assertAllEqual((2, 20), state.c.eval().shape)
            self.assertEqual(tf.float32, state.c.dtype)
