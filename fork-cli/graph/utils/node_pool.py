from graph.core.node import Node
from graph.error.node import *

class NodePool:
    def __init__(self):
        self._pool = dict()

    def _check_id(self, node_id:str):
        if not isinstance(node_id, str):
            raise WrongNodeIdError()

        return node_id in self._pool

    def set(self, node:Node):
        if not isinstance(node, Node):
            raise WrongNodeTypeError()

        if node.node_id in self._pool:
            raise DuplicateNodeError()

        self._pool[node.node_id] = node

    def get(self, node_id:str):
        has_id = self._check_id(node_id)

        if not has_id:
            return None

        return self._pool[node_id]
    
    def get_all(self) -> list[Node]:
        return list(self._pool.values())

    def delete(self, node_id:str):
        has_id = self._check_id(node_id)

        if not has_id:
            raise NodeNotFoundError()
        
        del self._pool[node_id]
    
    def get_node_ids(self):
        return self._pool.keys()