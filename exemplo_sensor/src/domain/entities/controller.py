from abstract.entity import AbstractEntity
from typing import Tuple, List
from device import Device
import datetime
from valueobjects.ip import IP


class Controller(AbstractEntity):
    _name: str
    _ip_address: IP
    _model: str
    _firmware_version: str
    _comm_protocol: str
    _interface: str # Ethernet or Wifi
    _mac_address: str
    _status: str
    _cpu_usage: float
    _mem_usage: float
    _net_usage: float
    _net_status: str
    _memory_size_mb: float
    _storage_size_mb: float
    _temperature_limit: Tuple[float, float]
    _connected_devices: List[Device]
    _batch_reading_size: int # Quantidade de itens que devem ser acumulados para envio em lote
    _batch_pre_processing_limit: int # Quantidade de itens que podem ser processados no controller
    _can_process_locally: bool
    _private_key: str
    _encryption_type: str
    _setup_date: datetime
    _last_maintenance_date: datetime
    _guarantee_date: datetime
    _location: str
    _last_alert: str


    def __init__(self, id=None):
        super().__init__(id)
        
    def __eq__(self, other):
        if not isinstance(other, Controller):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Controller(id={self.id}, name='{self._name}')"

    def get_id(self):
        return self.id
