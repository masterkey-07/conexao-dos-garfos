from graph.core.edge import Edge
from graph.core.node import Node
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
    
    def to_adjacent_matrix(self):
        node_ids = self._node_pool.get_node_ids()
        
        adjacent_matrix = {'data': [], 'nodes': node_ids}
        
        # Map node ID to index for quick lookup
        id_to_index = {node_id: index for index, node_id in enumerate(node_ids)}
        
        # Initialize the matrix with zeros
        size = len(node_ids)
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        # Populate the matrix with edges
        for edge in self._edges:
            from_id = edge.first_node.id
            to_id = edge.second_node.id
            i = id_to_index[from_id]
            j = id_to_index[to_id]
            matrix[i][j] = 1  # or edge, or edge.weight, depending on your needs

        adjacent_matrix['data'] = matrix
        return adjacent_matrix
