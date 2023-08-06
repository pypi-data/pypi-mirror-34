import numpy as np
import tensorflow as tf


class Data:

    def get_data(self):
        self.input_ = np.array(
            [
                [1, 4, 10, 3],
                [1, 7, 3, 0],
                [1, 20, 3, 0],
                [1, 20, 44, 3],
                [1, 11, 23, 3],
            ],
            dtype=np.int32,
        )
        self.seqlen = np.array([4, 3, 3, 4, 4], np.int32)
        self.embedding = np.random.rand(50, 300).astype('float32')
        self.input_place = tf.placeholder(shape=[None, 4], dtype=tf.int32)
        self.seqlen_place = tf.placeholder(shape=[None], dtype=tf.int32)
