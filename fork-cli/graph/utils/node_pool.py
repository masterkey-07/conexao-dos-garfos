from graph.core.node import Node
from graph.error.node import *

class NodePool:
    def __init__(self):
        self._pool = dict()

    def _check_id(self, id:str):
        if not isinstance(id, str):
            raise WrongNodeIdError()

        return id in self._pool

    def set(self, node:Node):
        if not isinstance(node, Node):
            raise WrongNodeTypeError()

        if node.id in self._pool:
            raise DuplicateNodeError()

        self._pool[node.id] = node

    def get(self, id:str):
        has_id = self._check_id(id)

        if not has_id:
            return None

        return self._pool[id]
    
    def delete(self, id:str):
        has_id = self._check_id(id)

        if not has_id:
            raise NodeNotFoundError()
        
        del self._pool[id]