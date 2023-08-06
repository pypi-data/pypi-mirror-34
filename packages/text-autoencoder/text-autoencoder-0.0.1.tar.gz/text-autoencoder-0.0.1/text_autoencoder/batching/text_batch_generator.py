from typing import Callable
from queue import Queue
import random

from .shuffle_bucket import ShuffleBucket


class TextBatchGenerator:

    def __init__(
            self,
            data_path: str,
            batch_size: int = 32,
            n_buckets: int = 5,
            data_processor: Callable = None,
            random_seed: int = 2018,
        ) -> None:

        self.data_path = data_path
        self.batch_size = batch_size
        self.n_buckets = n_buckets

        # set init random seed
        random.seed(random_seed)

        # build data iterator
        self.raw_data_iterator = self._gen_data_iterator()

        if data_processor is None:
            self.data_processor = lambda x: x

        # build cache buckets
        self._shuffle_buckets = [
            ShuffleBucket(
                max_size=self.batch_size,
            )for i in range(self.n_buckets)
        ]
        # build data queue
        self.data_queue = Queue()

    def _gen_data_iterator(self):
        return iter(open(self.data_path, 'r'))

    def load_data(self):
        while True:
            try:
                line = next(self.raw_data_iterator).strip()
            except StopIteration:
                self.raw_data_iterator = self._gen_data_iterator()
                line = next(self.raw_data_iterator)

            bucket_idx = random.randint(0, self.n_buckets - 1)

            self._shuffle_buckets[bucket_idx].add(line)

            if self._shuffle_buckets[bucket_idx].full:
                self.data_queue.put(
                    self._shuffle_buckets[bucket_idx].dump(),
                )
                self._shuffle_buckets[bucket_idx].reset()
                break

    def __call__(self, iterations: int):
        for _ in range(iterations):
            if not self.data_queue.empty():
                yield self.data_processor(self.data_queue.get())
            else:
                self.load_data()
                yield self.data_processor(self.data_queue.get())
