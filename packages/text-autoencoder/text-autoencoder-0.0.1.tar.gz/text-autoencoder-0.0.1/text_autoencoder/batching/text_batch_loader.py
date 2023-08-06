from typing import Callable
from queue import Queue
import random

from .shuffle_bucket import ShuffleBucket


class TextBatchLoader:

    def __init__(
            self,
            data_path: str,
            batch_size: int = 32,
            data_processor: Callable = None,
            shuffle: bool = False,
            random_seed: int = 2018,
        ) -> None:

        self.data_path = data_path
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.data_processor = data_processor

        if self.data_processor is None:
            self.data_processor = lambda x: x

        self.data_iterator = iter(open(data_path, 'r'))

        if self.shuffle:
            random.seed(random_seed)
            self.n_buckets = 5
        else:
            self.n_buckets = 1

        self._shuffle_buckets = [
            ShuffleBucket(
                max_size=self.batch_size,
            )for i in range(self.n_buckets)
        ]

        self.data_queue = Queue()
        self.end = False

    def load_data(self):
        while True:
            try:
                line = next(self.data_iterator).strip()
            except StopIteration:
                self.end = True
                break

            if self.shuffle:
                bucket_idx = random.randint(0, self.n_buckets - 1)
            else:
                bucket_idx = 0

            self._shuffle_buckets[bucket_idx].add(line)

            if self._shuffle_buckets[bucket_idx].full:
                self.data_queue.put(
                    self._shuffle_buckets[bucket_idx].dump(),
                )
                self._shuffle_buckets[bucket_idx].reset()
                break

    def last_batch(self):
        for buk in self._shuffle_buckets:
            if not buk.empty:
                self.data_queue.put(buk.dump())

    def __call__(self):
        while not self.end:
            if self.data_queue.empty():
                self.load_data()
            yield self.data_processor(self.data_queue.get())

        # for last batch
        while not self.data_queue.empty():
            yield self.data_processor(self.data_queue.get())
