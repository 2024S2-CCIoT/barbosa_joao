from abc import ABC, abstractmethod

class AbstractService(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        raise NotImplementedError()
