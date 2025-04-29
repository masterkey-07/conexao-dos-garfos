from .node import Node
from graph.error.node import WrongNodeTypeError

class Edge:
    def __init__(self, first_node: Node, second_node: Node, properties: dict = None):
        if not (isinstance(first_node, Node) and isinstance(second_node, Node)):
            raise WrongNodeTypeError()
            
        self._first_node = first_node
        self._second_node = second_node
        self._properties = properties or {}

    @property
    def first_node(self) -> dict:
        return self._first_node

    @property
    def second_node(self) -> dict:
        return self._second_node

    @property
    def properties(self) -> dict:
        return self._properties

    @properties.setter
    def properties(self, new_properties: dict):
        if not isinstance(new_properties, dict):
            raise ValueError("Properties must be a dictionary.")
        
        self._properties = new_properties