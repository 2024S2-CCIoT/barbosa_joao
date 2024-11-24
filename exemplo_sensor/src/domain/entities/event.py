from abstract.entity import AbstractEntity

class Event(AbstractEntity):
    _type: str
    _description: str

    def __init__(self, id = None):
        super().__init__(id)
