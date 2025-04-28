class WrongNodeIDException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Node:
    def __init__(self, id: str, properties: dict = None):
        if id is None or not isinstance(id, str):
            raise WrongNodeIDException()
        
        self._id = id

        self._edges = []

        self._properties = properties or {}

    @property
    def id(self) -> str:
        return self._id

    @property
    def properties(self) -> dict:
        return self._properties

    @properties.setter
    def properties(self, new_properties: dict):
        if not isinstance(new_properties, dict):
            raise ValueError("Properties must be a dictionary.")

        self._properties = new_properties