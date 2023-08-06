import numpy as np
import tensorflow as tf


class Data:

    def get_data(self):
        self.batch_size = 2
        self.maxlen = 20
        self.vocab_size = 50
        self.embedding_size = 300
        self.latent_size = 33

        self.latent_input = np.random.rand(
            self.batch_size, self.latent_size).astype('float32')
        self.real_indices = np.random.randint(
            self.vocab_size,
            size=(self.batch_size, self.maxlen),
        ).astype('int32')

        self.latent_place = tf.placeholder(
            shape=[None, self.latent_size],
            dtype=tf.float32,
        )
        self.real_indices_place = tf.placeholder(
            shape=[None, self.maxlen],
            dtype=tf.int32,
        )

        self.embedding = np.random.rand(
            self.vocab_size, self.embedding_size).astype('float32')
