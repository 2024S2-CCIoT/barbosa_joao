from abstract.entity import AbstractEntity
from typing import List
from valueobjects.email import Email

class Alert(AbstractEntity):
    _type: str
    _message: str
    _recipients: List[Email]
    _priority: int

    def __init__(self, id = None):
        super().__init__(id)
