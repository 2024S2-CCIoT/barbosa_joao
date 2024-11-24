from abstract.valueobject import AbstractValueObject
import socket


class IP(AbstractValueObject):
    def __init__(self, ip: str, version: int):
        if not isinstance(ip, str):
            raise ValueError("O IP deve ser uma string!")

        if not socket.inet_pton(socket.AF_INET, ip) or socket.inet_pton(
            socket.AF_INET6, ip
        ):
            raise ValueError("IP inválido")

        self._ip = ip
        self._version = version

    def __eq__(self, other):
        if not isinstance(other, IP):
            return False

        return self._ip == other._ip

    def __hash__(self):
        return hash(self._ip)

    def __str__(self):
        return self._ip
