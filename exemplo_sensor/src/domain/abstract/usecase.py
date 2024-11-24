from abc import ABC, abstractmethod

class AbstractUseCase(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError()