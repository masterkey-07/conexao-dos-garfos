from graph.core.edge import Edge
from graph.core.node import Node
from graph.error.node import NodeNotFoundError
from graph.utils.node_pool import NodePool

class Graph:
    def __init__(self):
        self._edges = []
        self._node_pool = NodePool()

    def add_node(self, id:str, properties:dict = None):
        new_node = Node(id, properties)
        
        try:
            self._node_pool.set(new_node)

            return new_node
        except:
            return None

    def get_node(self, id:str):
        return self._node_pool.get(id)
    
    def delete_node(self, id:str):
        try:
            self._node_pool.delete(id)
        except:
            return False

        return True
    
    def add_edge(self, first_node_id:str, second_node_id:str, properties = None):
        first_node = self._node_pool.get(first_node_id)
        second_node = self._node_pool.get(second_node_id)
        
        if first_node is None or second_node is None:
            return None

        edge = Edge(first_node, second_node, properties)

        self._edges.append(edge)

        return edge