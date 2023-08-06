from typing import List, Iterable, Dict
import numpy as np


def train_test_split(
        iterables: List[Iterable],
        ratio: int = 0.1,
        seed: int = 2017,
        shuffle: bool = True,
        logger: object = None,
    ) -> Dict[str, np.ndarray]:

    lengths = [len(item) for item in iterables]
    if len(set(lengths)) != 1:
        lengths = list(map(str, lengths))
        raise ValueError(
            'items in iterables should have the same datasize',
            'Now item shapes are: ' + ', '.join(lengths),
        )
    total_size = iterables[0].shape[0]
    num_valid = int(total_size * ratio)
    if (ratio > 0.0) and (num_valid == 0):
        num_valid = 1
    if shuffle:
        np.random.seed(seed=seed)
        index = np.arange(total_size)
        np.random.shuffle(index)
        for idx in range(len(iterables)):
            iterables[idx] = iterables[idx][index]

    if logger is not None:
        logger.info(
            'size of subtrain set is [{}], size of validation set is [{}]'.format(
                total_size - num_valid,
                num_valid,
            ),
        )

    return {
        'test': tuple([element[:num_valid] for element in iterables]),
        'train': tuple([element[num_valid:] for element in iterables]),
    }
