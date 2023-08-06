import numpy as np
from typing import List, Tuple, Iterable


class BatchLoader(object):

    def __init__(
            self,
            iterables: List[Iterable],
            batch_size: int = 32,
            shuffle: bool = True,
            seed: int = 2017,
        ) -> None:

        lengths = [item.shape[0] for item in iterables]
        if len(set(lengths)) != 1:
            lengths = list(map(str, lengths))
            raise ValueError(
                'items in iterables should have the same datasize',
                'Now item shapes are: ' + ', '.join(lengths),
            )
        self.np_iterables = [np.array(item) for item in iterables]
        self.batch_size = batch_size
        self.data_size = self.np_iterables[0].shape[0]

        self.shuffle = shuffle
        if self.shuffle:
            np.random.seed(seed)

    def __call__(self) -> Tuple[np.ndarray]:
        if self.shuffle:
            data_index = np.random.permutation(self.data_size)
        else:
            data_index = np.arange(self.data_size)

        for start_idx in range(0, self.data_size, self.batch_size):
            end_idx = start_idx + self.batch_size
            target_idxs = data_index[start_idx: end_idx]
            yield (item[target_idxs] for item in self.np_iterables)
