from graph.node import Node
from graph.exceptions import *

class NodePool:
    def __init__(self):
        self._pool = dict()

    def _check_id(self, id:str):
        if not isinstance(id, str):
            raise WrongNodeIdException()

        return id in self._pool

    def set(self, node:Node):
        if not isinstance(node, Node):
            raise WrongNodeTypeException()

        if node.id in self._pool:
            raise DuplicateNodeException()

        self._pool[node.id] = node

    def get(self, id:str):
        has_id = self._check_id(id)

        if not has_id:
            return None

        return self._pool[id]
    
    def delete(self, id:str):
        has_id = self._check_id(id)

        if not has_id:
            raise NodeNotFoundException()
        
        del self._pool[id]