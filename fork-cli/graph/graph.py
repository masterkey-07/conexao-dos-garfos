from graph.node import Node
from graph.utils.node_pool import NodePool

class Graph:
    def __init__(self):
        self._edges = []
        self._node_pool = NodePool()

    def add_node(self, id:str, properties:dict = None) -> bool:
        new_node = Node(id, properties)
        
        self._node_pool.set(new_node)

    def get_node(self, id:str):
        return self._node_pool.get(id)
    
    def delete_node(self, id:str):
        return self._node_pool.delete(id)
    
    