from typing import List, Dict, Tuple
import json
import pickle as pkl
from os.path import dirname

import umsgpack
from tqdm import tqdm
import numpy as np
from mkdir_p import mkdir_p
from sklearn.preprocessing import normalize
from bistiming import SimpleTimer
from tokenizer_hub import *  # noqa
from text_normalizer.text_normalizer_collection_library import *  # noqa

from .build_vocabulary import build_vocabulary
from .expand_vocabulary import expand_vocabulary
from .sentence_to_indices import sentence2indices
from .indices_to_string import indices2string


class Preprocessor:

    def __init__(
            self,
            sos_token: str = '<SOS>',
            eos_token: str = '<EOS>',
            unk_token: str = '<UNK>',
            pad_token: str = '<PAD>',
            normalizer_id: str = 'u_zh_en_text_normalizer_collection_1',
            tokenizer_id: str = 'ChineseCharTokenizer',
            word2index_path: str = None,
            word_embedding_path: str = None,
            data_path: str = None,
            vocab_size: int = None,
            embedding_size: int = None,
            maxlen: int = None,
            logger=None,
            skip_init: bool = False,
        ) -> None:

        if not skip_init:
            self.sos_token = sos_token
            self.eos_token = eos_token
            self.unk_token = unk_token
            self.pad_token = pad_token

            self.normalizer_id = normalizer_id
            self.tokenizer_id = tokenizer_id

            self.maxlen = maxlen
            self.logger = logger

            if (word2index_path is None) and (word_embedding_path is None):
                self.word2index, real_maxlen = build_vocabulary(
                    data_path=data_path,
                    vocab_size=vocab_size,
                    logger=logger,
                )
                self.word_embedding = self.build_random_embedding(
                    embedding_size=embedding_size,
                )
            else:
                self.word2index = self.load_word2index(word2index_path)
                self.word_embedding = self.load_word_embedding(
                    word_embedding_path)

            self.word2index, self.word_embedding = self.expand_vocabulary()
            self.vocab_size, self.embedding_size = self.word_embedding.shape

            self.logger.info('vocabulary size = {}'.format(self.vocab_size))

            if self.maxlen is None:
                self.maxlen = real_maxlen + 2

            self.load_module()

    def load_module(self):
        self.normalizer = self.load_normalizer(self.normalizer_id)
        self.tokenizer = self.load_tokenizer(self.tokenizer_id)

    @staticmethod
    def load_normalizer(normalizer_id):
        normalizer = globals()[normalizer_id]
        return normalizer

    @staticmethod
    def load_tokenizer(tokenizer_id):
        tokenizer = globals()[tokenizer_id]()
        return tokenizer

    @staticmethod
    def load_word2index(word2index_path: str) -> Dict[str, int]:
        with open(word2index_path, 'r') as filep:
            word2index = json.load(filep)
        return word2index

    @staticmethod
    def load_word_embedding(word_embedding_path: str) -> np.ndarray:
        with open(word_embedding_path, 'rb') as filep:
            word_embedding = pkl.load(filep)
        return word_embedding

    def build_random_embedding(
            self,
            embedding_size: int,
        ) -> np.array:

        embedding = normalize(
            np.random.rand(
                len(self.word2index),
                embedding_size,
            ),
        ).astype('float32')
        return embedding

    def build_vocabulary(
            self,
            data_path: str,
            vocab_size: int = None,
        ) -> Dict[str, int]:

        if data_path is None:
            raise ImportError(
                "text data is needed for building vocabulary",
            )
        vocab_dict, maxlen = build_vocabulary(
            input_path=data_path,
            max_size=vocab_size,
            sos_token=self.sos_token,
            eos_token=self.eos_token,
            unk_token=self.unk_token,
            pad_token=self.pad_token,
        )
        if self.logger is not None:
            self.logger.info(
                'Build vocabulary for data [{}], and its size is {}.'.format(
                    data_path, len(vocab_dict)),
            )
            self.logger.info(
                'Max length of data [{}] is {}'.format(data_path, maxlen),
            )
        return vocab_dict, maxlen

    def expand_vocabulary(self):

        return expand_vocabulary(
            word2index=self.word2index,
            word_embedding=self.word_embedding,
            sos_token=self.sos_token,
            eos_token=self.eos_token,
            unk_token=self.unk_token,
            pad_token=self.pad_token,
            logger=self.logger,
        )

    def batch_preprocessing(
            self,
            sentences: List[str],
        ) -> List[str]:

        output = []
        for sent in tqdm(
            sentences,
            ascii=True,
            desc='preprocess-sentences',
        ):
            nor_sent = self.normalizer.normalize(sent)[0].strip()
            tokens = ' '.join(self.tokenizer.lcut(nor_sent))
            output.append(tokens)
        return output

    def batch_sent2indices(
            self,
            sentences: List[str],  # split by space
        )-> Tuple[np.ndarray, np.array]:

        num_sent = len(sentences)
        indices_array = np.zeros(shape=(num_sent, self.maxlen))
        seqlen_array = np.zeros(shape=(num_sent))

        count = 0
        for sentence in tqdm(
            sentences,
            ascii=True,
            desc='sentence2indices',
        ):
            if len(sentence) > 0:
                indices, seqlen = sentence2indices(
                    sentence=sentence.split(' '),
                    sos_token=self.sos_token,
                    eos_token=self.eos_token,
                    unk_token=self.unk_token,
                    pad_token=self.pad_token,
                    word2index=self.word2index,
                    maxlen=self.maxlen,
                )
                indices_array[count, :] = indices
                seqlen_array[count] = seqlen
                count += 1

        return indices_array[: count + 1].astype('int32'), \
            seqlen_array[: count + 1].astype('int32')

    def batch_indices2str(
            self,
            word_indices_list: List[List[str]],
            seqlen_list: List[int] = None,
        ) -> List[str]:

        output = []
        for i, word_indices in tqdm(
            enumerate(word_indices_list),
            ascii=True,
            desc='indices2str',
        ):

            if seqlen_list is None:
                seqlen = None
            else:
                seqlen = seqlen_list[i]

            sentence = indices2string(
                word_indices=word_indices,
                seqlen=seqlen,
            )
            output.append(sentence)
        return output

    @classmethod
    def load(cls, input_path: str, logger=None):
        with SimpleTimer(
            'Loading preprocessor from {}_pre.msg'.format(input_path),
            logger=logger,
        ):
            with open('{}_pre.msg'.format(input_path), 'rb') as filep:
                params_dict = umsgpack.unpack(
                    filep,
                )
                params_dict['logger'] = logger
                pre = cls(skip_init=True)
                pre.__dict__.update(params_dict)
                pre.load_module()
        return pre

    def save(self, output_path: str):
        output_dict = {
            'sos_token': self.sos_token,
            'eos_token': self.eos_token,
            'unk_token': self.unk_token,
            'pad_token': self.unk_token,
            'normalizer_id': self.normalizer_id,
            'tokenizer_id': self.tokenizer_id,
            'word2index': self.word2index,
            'vocab_size': self.vocab_size,
            'embedding_size': self.embedding_size,
            'maxlen': self.maxlen,
        }
        with SimpleTimer(
            'Saving preprocessor to {}_pre.msg'.format(output_path),
            logger=self.logger,
        ):
            mkdir_p(dirname(output_path))
            with open('{}_pre.msg'.format(output_path), 'wb') as filep:
                umsgpack.pack(output_dict, filep)
