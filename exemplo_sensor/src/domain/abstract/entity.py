from abc import ABC, abstractmethod
from typing import Optional
from cuid import cuid
from valueobjects.id import ID
from datetime import datetime


class AbstractEntity(ABC):
    def __init__(self, id: Optional[ID] = None):
        self._id = id or cuid()
        self._created_at = datetime.now()
        self._updated_at = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    
    @updated_at.setter
    def updated_at(self, new_date: datetime):
        if not isinstance(datetime, new_date):
            raise ValueError("Data inválida!")
        elif new_date < self._updated_at or new_date < self._created_at:
            raise ValueError("Data inválida!")

        self._updated_at = new_date

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError()

    @abstractmethod
    def __hash__(self):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()
