from abstract.valueobject import AbstractValueObject

class ID(AbstractValueObject):
    def __init__(self, id: str):
        if not isinstance(id, str):
            raise ValueError("O ID deve ser uma string!")
        
        self._id = id

    def __eq__(self, other):
        if not isinstance(other, ID):
            return False
        
        return self._id == other._id
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return self._id