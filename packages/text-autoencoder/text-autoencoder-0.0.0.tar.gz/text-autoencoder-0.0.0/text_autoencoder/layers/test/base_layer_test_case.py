import tensorflow as tf


class BaseLayerTestCase(tf.test.TestCase):

    def tearDown(self):
        tf.reset_default_graph()
