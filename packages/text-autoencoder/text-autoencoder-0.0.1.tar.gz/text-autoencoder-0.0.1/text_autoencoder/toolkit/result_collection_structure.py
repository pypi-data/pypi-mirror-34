from typing import Dict
from collections import OrderedDict

import numpy as np


class LossCollection:

    def __init__(
            self,
            name_float_pairs: Dict[str, int],
        ) -> None:

        self.keys = list(name_float_pairs.keys())
        self.values = np.array(list(name_float_pairs.values()))
        self.count = 1

    def merge(self, loss_collection):
        self.count += 1
        self.values += loss_collection.values

    def summary(self):
        output_dict = OrderedDict()
        for i, name in enumerate(self.keys):
            output_dict[name] = self.values[i] / self.count
        return output_dict


class ArrayCollection:

    def __init__(
            self,
            name_array_pairs: Dict[str, np.ndarray],
        ) -> None:
        self.keys = list(name_array_pairs.keys())
        self.values = [
            np.array(list(name_array_pairs.values())),
        ]

    def merge(self, array_collection):
        self.values.extend(array_collection.values)

    def summary(self) -> Dict[str, np.ndarray]:
        output_dict = OrderedDict()
        self.values = np.concatenate(self.values, axis=1)
        for i, name, in enumerate(self.keys):
            output_dict[name] = self.values[i]
        return output_dict
