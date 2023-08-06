from abc import ABC, abstractmethod


class BaseAutoencoder(ABC):

    @abstractmethod
    def fit(self):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError

    @abstractmethod
    def encode(self):
        raise NotImplementedError

    def description(self):
        pass

    def decode(self):
        pass
