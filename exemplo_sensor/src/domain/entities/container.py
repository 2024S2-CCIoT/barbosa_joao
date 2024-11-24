from abstract.entity import AbstractEntity

class Container(AbstractEntity):
    _name: str
    _image: str
    _status: str
    _cpu_spec: str
    _memory_size_mb: float
    _storage_size_mb: float
    _logs_location: str

    def __init__(self, id = None):
        super().__init__(id)
