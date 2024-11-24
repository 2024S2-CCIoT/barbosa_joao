from abstract.entity import AbstractEntity
from valueobjects.ip import IP

class Pod(AbstractEntity):
    _name: str
    _namespace: str
    _status: str
    _image: str
    _cpu_spec: str
    _allocated_mem: str
    _allocated_storage: str
    _logs_location: str
    _ip_address: IP
    _k8s_version: str

    def __init__(self, id = None):
        super().__init__(id)