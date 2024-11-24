from abstract.entity import AbstractEntity
from valueobjects.ip import IP
from typing import List
from pod import Pod


class EdgeNode(AbstractEntity):
    _name: str
    _model: str
    _so: str  # Sistema operacional
    _cpu_spec: str
    _memory_size_mb: float
    _storage_size_mb: float
    _cpu_usage: float
    _mem_usage: float
    _net_usage: float
    _ip_address: IP
    _comm_protocol: str
    _mac_address: str
    _network_interfaces: List[str]
    _net_status: str
    _status: str
    _pods: List[Pod]

    def __init__(self, id=None):
        super().__init__(id)
