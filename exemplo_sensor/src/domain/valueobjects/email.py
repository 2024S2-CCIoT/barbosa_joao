from abstract.valueobject import AbstractValueObject
import re

class Email(AbstractValueObject):
    def __init__(self, email_address):
        if not self.validar_email(email_address):
            raise ValueError(f"Endereço de e-mail inválido: {email_address}")
        self._email_address = email_address

    def __str__(self):
        return self._email_address

    @staticmethod
    def validar_email(email):
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao_email, email))

    def __eq__(self, other):
        if isinstance(other, Email):
            return self._email_address.lower() == other._email_address.lower()
        return False
    
    def __hash__(self):
        return hash(self._email_address)

    def __repr__(self):
        f'{self.__class__.__name__}({str(self)})'