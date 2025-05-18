from graph.core.edge import Edge
from graph.core.node import Node
from graph.utils.node_pool import NodePool

class Graph:
    def __init__(self):
        self._edges = []
        self._node_pool = NodePool()

    def add_node(self, node_id:str, properties:dict = None):
        new_node = Node(node_id, properties)
        
        try:
            self._node_pool.set(new_node)

            return new_node
        except:
            return None

    def get_node(self, node_id:str):
        return self._node_pool.get(node_id)

    def get_nodes(self) -> list[Node]:
        return self._node_pool.get_all()

    def get_edges(self) -> list[Edge]:
        return list(self._edges)

    def delete_node(self, node_id:str):
        try:
            self._node_pool.delete(node_id)
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