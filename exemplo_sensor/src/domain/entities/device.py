from abstract.entity import AbstractEntity
from typing import Tuple
import datetime
from valueobjects.id import ID

class Device(AbstractEntity):
    _controller_id: ID
    _port: int
    _port_type: str
    _name: str
    _series: str
    _measuring_unity: str
    _model: str
    _manufacturer: str
    _type: str
    _precision: str
    _weight: float
    _height: float
    _measuring_interval: Tuple[float, float]
    _material: str
    _conectivity_type: str
    _temperature_limit_interval: Tuple[float, float]
    _data_format: str
    _calibration_status: str
    _last_calibration_date: datetime
    _status: str
    _installation_date: datetime
    _last_maintenance_date: datetime
    _location: str
    _firmware_version: str
    _min_alert: str
    _max_alert: str
    _guarantee_date: datetime
    
    def __init__(self, id = None):
        super().__init__(id)

    def __eq__(self, other):
        if not isinstance(other, Device):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Device(id={self.id}, name='{self._name}')"

    def get_id(self):
        return self.id