from typing import Dict, Tuple

import numpy as np
from sklearn.preprocessing import normalize


def expand_vocabulary(
        word2index: Dict[str, int],
        word_embedding: np.array,
        sos_token: str = '<SOS>',
        eos_token: str = '<EOS>',
        unk_token: str = '<UNK>',
        pad_token: str = '<PAD>',
        logger=None,
    ) -> Tuple[Dict[str, int], np.array]:

    tokens = [sos_token, eos_token, unk_token, pad_token]
    max_index = len(word2index)
    embedding_size = word_embedding.shape[1]

    augmented_word_embedding = [word_embedding]
    for token in tokens:
        if token not in word2index:
            assigned_index = max_index
            logger.info(
                'Token {} is not in word2index and it would be automatically assign to {}.'.format(
                    token, assigned_index),
            )
            word2index[token] = assigned_index
            augmented_word_embedding.append(
                normalize(np.random.rand(1, embedding_size)),
            )
            max_index += 1

    word_embedding = np.vstack(
        augmented_word_embedding).astype('float32')

    return word2index, word_embedding
