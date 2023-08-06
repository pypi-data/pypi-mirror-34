from typing import Callable, List


class ShuffleBucket:

    def __init__(
            self,
            max_size: int,
            data_processor: Callable = None,
        ) -> None:

        self.max_size = max_size
        self.data_processor = data_processor

        if self.data_processor is None:
            self.data_processor = lambda x: x

        self.data = []
        self.count = 0

    @property
    def full(self) -> bool:
        if self.count == self.max_size:
            return True
        return False

    @property
    def empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def add(self, datum: object) -> None:
        if not self.full:
            self.data.append(
                self.data_processor(datum))
            self.count += 1
        else:
            raise ValueError('bucket is full')

    def dump(self) -> List[object]:
        return self.data

    def reset(self) -> None:
        self.data = []
        self.count = 0
