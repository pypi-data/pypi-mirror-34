from abc import ABC, abstractmethod


class BaseVariationalAutoencoder(ABC):

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
    def encode(self):
        raise NotImplementedError

    @abstractmethod
    def get_latent_vector(self):
        raise NotImplementedError

    def description(self):
        pass

    def decode(self):
        pass
