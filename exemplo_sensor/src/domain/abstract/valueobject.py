from abc import ABC, abstractmethod

class AbstractValueObject(ABC):
    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()

    def __repr__(self):
        f'{self.__class__.__name__}({str(self)})'