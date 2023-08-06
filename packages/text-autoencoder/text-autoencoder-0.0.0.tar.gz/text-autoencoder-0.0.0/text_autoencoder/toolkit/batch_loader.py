from typing import List, Dict

import numpy as np


class BatchLoader:

    def __init__(
            self,
            sentences: List[str],
            word2index: Dict[str, int],
            batch_size: int = 32,
            maxlen: int = 50,
            sos_token: str = '<SOS>',
            eos_token: str = '<EOS>',
            unk_token: str = '<UNK>',
            pad_token: str = '<PAD>',
            valid_ratio: float = 0.0,
            seed: int = 2018,
        ):
        np.random.seed(seed)

        self.sentences = sentences
        self.word2index = word2index
        self.batch_size = batch_size
        self.maxlen = maxlen

        self.sos_token = sos_token
        self.eos_token = eos_token
        self.unk_token = unk_token
        self.pad_token = pad_token

        self.valid_ratio = valid_ratio
        self.total_size = len(self.sentences)

    def sentence2index(
            self,
            sentence: str,
        ) -> np.ndarray:
        eos_index = self.word2index[self.eos_token]
        output_array = eos_index * np.ones(self.maxlen).astype('int32')

        # assign sos index
        output_array[0] = self.word2index[self.sos_token]

        tokens = list(sentence[: self.maxlen - 2])
        for i, token in enumerate(tokens, 1):
            if token not in self.word2index:
                output_array[i] = self.word2index[self.unk_token]
            else:
                output_array[i] = self.word2index[token]
        return output_array, len(tokens) + 2

    def __call__(self) -> np.ndarray:
        self.random_indices = np.arange(len(self.sentences))
        np.random.shuffle(self.random_indices)
        self.random_indices = self.random_indices.tolist()
        n_iter = int(len(self.sentences) / self.batch_size)
        for iter_ in range(n_iter):
            start = iter_ * self.batch_size
            random_indices = self.random_indices[start: start + self.batch_size]
            batch_array = np.zeros((self.batch_size, self.maxlen))
            seqlen_array = np.zeros(self.batch_size)
            for i, row_i in enumerate(random_indices):
                batch_array[i], seqlen_array[i] = self.sentence2index(
                    sentence=self.sentences[row_i],
                )
            yield batch_array.astype('int32'), seqlen_array.astype('int32')


class BatchGenerator(BatchLoader):

    def __init__(
            self,
            sentences: List[str],
            word2index: Dict[str, int],
            batch_size: int = 32,
            iterations: int = 100,
            maxlen: int = 50,
            sos_token: str = '<SOS>',
            eos_token: str = '<EOS>',
            unk_token: str = '<UNK>',
            pad_token: str = '<PAD>',
            valid_ratio: float = 0.0,
            seed: int = 2018,
        ):
            super(BatchGenerator, self).__init__(
                sentences=sentences,
                word2index=word2index,
                batch_size=batch_size,
                maxlen=maxlen,
                sos_token=sos_token,
                eos_token=eos_token,
                unk_token=unk_token,
                pad_token=pad_token,
                valid_ratio=valid_ratio,
                seed=seed,
            )
            self.iterations = iterations

    def __call__(self) -> np.ndarray:
        for _ in range(self.iterations):
            random_indices = np.random.choice(self.total_size, self.batch_size)
            batch_array = np.zeros((self.batch_size, self.maxlen))
            seqlen_array = np.zeros(self.batch_size)
            for i, row_i in enumerate(random_indices):
                batch_array[i], seqlen_array[i] = self.sentence2index(
                    sentence=self.sentences[row_i],
                )
            yield batch_array.astype('int32'), seqlen_array.astype('int32')
