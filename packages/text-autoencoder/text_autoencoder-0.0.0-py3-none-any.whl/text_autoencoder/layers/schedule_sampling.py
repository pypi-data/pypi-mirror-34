import tensorflow as tf


def schedule_sampling(
        real_word: tf.Tensor,  # batch_size * dim
        predicted_word: tf.Tensor,  # batch_size * dim
        assist: int = 0,  # 0: use predicted word, 1: use real word
    ) -> tf.Tensor:
    return assist * real_word + (1 - assist) * predicted_word
