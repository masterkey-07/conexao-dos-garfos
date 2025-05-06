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
        
        id_to_index = {node_id: index for index, node_id in enumerate(node_ids)}
        
        size = len(node_ids)
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for edge in self._edges:
            first_node_id = edge.first_node.id
            second_node_id = edge.second_node.id
        
            first_node_index = id_to_index[first_node_id]
            second_node_index = id_to_index[second_node_id]

            matrix[first_node_index][second_node_index] = 1  
            matrix[second_node_index][first_node_index] = 1  

        adjacent_matrix['data'] = matrix
        
        return adjacent_matrix
    
    def to_incidency_matrix(self):
        node_ids = self._node_pool.get_node_ids()

        edges = self._edges

        incidence_matrix = {'data': [], 'nodes': node_ids, 'edges': []}
        
        id_to_index = {node_id: index for index, node_id in enumerate(node_ids)}
        
        size_nodes = len(node_ids)
        size_edges = len(edges)

        matrix = [[0 for _ in range(size_edges)] for _ in range(size_nodes)]

        for edge_index, edge in enumerate(edges):
            first_node_index = id_to_index[edge.first_node.id]
            second_node_index = id_to_index[edge.second_node.id]
            
            matrix[first_node_index][edge_index] += 1
            matrix[second_node_index][edge_index] += 1
            
            incidence_matrix['edges'].append((edge.first_node.id, edge.second_node.id))

        incidence_matrix['data'] = matrix
        
        return incidence_matrix
    
    def to_adjacency_list(self):
        adjacency_list = {}

        for node_id in self._node_pool.get_node_ids():
            adjacency_list[node_id] = []

        for edge in self._edges:
            first_node_id = edge.first_node.id
            second_node_id = edge.second_node.id
            
            adjacency_list[first_node_id].append(second_node_id)
            
            adjacency_list[second_node_id].append(first_node_id)

        return adjacency_list