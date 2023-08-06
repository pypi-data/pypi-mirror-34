import tensorflow as tf

from .base_layer_test_case import BaseLayerTestCase
from ..schedule_sampling import schedule_sampling


class ScheduleSamplingTestCase(BaseLayerTestCase):

    def test_schedule_sampling_default(self):
        with self.test_session():
            result = schedule_sampling(
                real_word=tf.constant([[1, 2, 3]]),
                predicted_word=tf.constant([[7, 8, 9]]),
            )
            self.assertAllEqual([[7, 8, 9]], result.eval())

    def test_schedule_sampling_assist(self):
        with self.test_session():
            result = schedule_sampling(
                real_word=tf.constant([[1, 2, 3]]),
                predicted_word=tf.constant([[7, 8, 9]]),
                assist=1,
            )
            self.assertAllEqual([[1, 2, 3]], result.eval())
