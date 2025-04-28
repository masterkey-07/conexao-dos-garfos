from .node import Node
from .node_pool import NodePool

class Graph:
    def __init__(self):
        self._edges = []
        self._node_pool = NodePool()

    def add_node(self, id:str, properties:dict = None):
        new_node = Node(id, properties)
        
        try:
            self._node_pool.add_vertice(new_node)
        except:
            pass