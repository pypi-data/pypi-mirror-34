from typing import List, Dict
import sys
from os.path import abspath, dirname

import tensorflow as tf
import numpy as np


def add_parent_path():
    ROOT_DIR = dirname(dirname(abspath(__file__)))
    sys.path.insert(0, ROOT_DIR)


def indices2sent(
        word_indices: List[int],
        seqlen: int,
        index2word: Dict[int, str],
    ) -> str:
    output_str = ''
    for j, ind in enumerate(word_indices):
        if j >= seqlen:
            break
        output_str += index2word[ind]
    return output_str


def show_decoder_output(
        real_word_indices: np.ndarray,
        gen_word_indices: np.ndarray,
        seqlen: np.ndarray,
        index2word: Dict[int, str],
    ) -> None:
    num_seq = len(real_word_indices)
    print('[real] -----> [generated]')
    for row_i in range(num_seq):
        real_seq = real_word_indices[row_i, :].tolist()
        gen_seq = gen_word_indices[row_i, :].tolist()
        print(
            '[{}] -----> [{}]'.format(
                indices2sent(
                    word_indices=real_seq,
                    seqlen=seqlen[row_i],
                    index2word=index2word,
                ),
                indices2sent(
                    word_indices=gen_seq,
                    seqlen=seqlen[row_i],
                    index2word=index2word,
                ),
            ),
        )
    print('======================================')


def load_data(
        batch_size,
        iterations,
        maxlen,
    ):
    from toolkit.data_loader import DataLoader
    from toolkit.batch_loader import BatchGenerator, BatchLoader

    data_path = '/mnt/data/texts/ai_challenger_translation_train_20170912/' + \
        'translation_train_20170912/train_traditional_cleaned.zh'
    data = DataLoader(
        data_path=data_path,
        word2index_path='/home/en/vae/embedding/model_0507_word2index_char.json',
        word_embedding_path='/home/en/vae/embedding/model_0507_vectors_char.pkl',
        sos_token='sos',
        eos_token='eos',
        unk_token='<UNK>',
        pad_token='eos',
        valid_ratio=0.05,
    )
    subtrain_batch_gen = BatchGenerator(
        sentences=data.train_sentences,
        word2index=data.word2index,
        batch_size=batch_size,
        iterations=iterations,
        maxlen=maxlen,
        sos_token='sos',
        eos_token='eos',
        unk_token='<UNK>',
        pad_token='eos',
    )
    valid_batch_gen = BatchLoader(
        sentences=data.valid_sentences,
        word2index=data.word2index,
        batch_size=batch_size,
        maxlen=maxlen,
        sos_token='sos',
        eos_token='eos',
        unk_token='<UNK>',
        pad_token='eos',
    )
    return data, subtrain_batch_gen, valid_batch_gen


def sample_from_gaussion(
        mean: tf.Tensor,
        std: tf.Tensor,
    ) -> tf.Tensor:

    eps = tf.random_normal(shape=tf.shape(mean))
    return mean + tf.exp(std / 2) * eps
