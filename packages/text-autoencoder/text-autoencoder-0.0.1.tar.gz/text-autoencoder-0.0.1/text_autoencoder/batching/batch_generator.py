import numpy as np
from typing import List, Iterable, Tuple


class BatchGenerator(object):

    def __init__(
            self,
            iterables: List[Iterable],
            batch_size: int = 32,
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

    def __call__(self, iterations: int) -> Tuple[np.ndarray]:
        for _ in range(iterations):
            random_indices = np.random.choice(
                self.data_size, self.batch_size)
            yield (item[random_indices] for item in self.np_iterables)
