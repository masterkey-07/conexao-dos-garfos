from .vertice import Vertice

class Edge:
    def __init__(self, first_vertice: Vertice, second_vertice: Vertice, properties: dict = None):
        self._first_vertice = first_vertice
        self._second_vertice = second_vertice
        self._properties = properties or {}

    @property
    def properties(self) -> dict:
        return self._properties

    @properties.setter
    def properties(self, new_properties: dict):
        if not isinstance(new_properties, dict):
            raise ValueError("Properties must be a dictionary.")
        
        self._properties = new_properties