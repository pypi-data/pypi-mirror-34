from typing import Tuple, Dict, List
import json
import pickle as pkl

import numpy as np
from sklearn.preprocessing import normalize
from bistiming import SimpleTimer


class DataLoader:

    def __init__(
            self,
            data_path: str,
            word2index_path: str,
            word_embedding_path: str,
            sos_token: str = '<SOS>',
            eos_token: str = '<EOS>',
            unk_token: str = '<UNK>',
            pad_token: str = '<PAD>',
            valid_ratio: float = 0.1,
            seed: int = 2018,
        ) -> None:
        np.random.seed(seed)
        self.data_path = data_path
        self.word2index_path = word2index_path
        self.word_embedding_path = word_embedding_path
        self.tokens = {
            'sos': sos_token,
            'eos': eos_token,
            'unk': unk_token,
            'pad': pad_token,
        }
        self.valid_ratio = valid_ratio
        self.load()

    def load(self) -> None:
        self.sentences = self.load_text_data(data_path=self.data_path)
        self.train_sentences, self.valid_sentences = self.train_test_split(
            self.sentences,
            self.valid_ratio,
        )
        self.word2index, self.index2word, self.max_index = self._load_word2index()
        self.word_embedding = self._load_word_embedding()
        vocab_size, self.embedding_size = self.word_embedding.shape
        assert vocab_size == len(self.word2index)
        self._check_basic_token()

    def _check_basic_token(self) -> None:
        augmented_word_embedding = [self.word_embedding]
        for name, token in self.tokens.items():
            if token not in self.word2index:
                assigned_index = self.max_index + 1
                print(
                    '''
                        Token {} is not in word2index and
                        it would be automatically assign to {}.
                    '''.format(name, assigned_index),
                )
                self.word2index[token] = assigned_index
                self.index2word[assigned_index] = token
                augmented_word_embedding.append(
                    normalize(np.random.rand(1, self.embedding_size)),
                )
                self.max_index += 1
        self.word_embedding = np.vstack(
            augmented_word_embedding).astype('float32')

    def _load_word2index(self) -> Tuple[Dict[str, int], Dict[int, str], int]:
        with SimpleTimer(
            'Loading word2index from {}'.format(self.word2index_path),
        ):
            with open(self.word2index_path, 'r') as filep:
                word2index = json.load(filep)
            index2word, max_index = self.gen_index2word(word2index)
        return word2index, index2word, max_index

    def _load_word_embedding(self) -> np.ndarray:
        with SimpleTimer(
            'Loading word embedding from {}'.format(self.word_embedding_path),
        ):
            with open(self.word_embedding_path, 'rb') as filep:
                word_embedding = pkl.load(filep)
        return word_embedding

    @staticmethod
    def load_text_data(data_path: str) -> List[str]:
        sentences = []
        with open(data_path, 'r') as filep:
            for line in filep:
                sentences.append(line.strip())
        return sentences

    @staticmethod
    def train_test_split(data: List[str], ratio: float = 0.0):
        total_size = len(data)
        valid_size = int(total_size * ratio)
        if valid_size > 0.0:
            indices = np.arange(total_size)
            np.random.shuffle(indices)
            shuffled_data = np.array(data)[indices]
            return shuffled_data[valid_size:].tolist(), \
                shuffled_data[0: valid_size].tolist()
        else:
            return data, None

    @staticmethod
    def gen_index2word(
            word2index: Dict[str, int],
        ) -> Tuple[Dict[int, str], int]:
        index2word = {}
        for key, value in word2index.items():
            if value not in index2word:
                index2word[value] = key
            else:
                raise KeyError(
                    'Words ({}, {}) share index {}'.format(
                        index2word[value],
                        key,
                        value,
                    ),
                )
        max_index = max(index2word.keys())
        return index2word, max_index
