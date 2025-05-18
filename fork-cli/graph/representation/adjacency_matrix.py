from collections import deque
from tabulate import tabulate
from graph.core.graph import Graph
from graph.representation.abstract_graph_representation import AbstractGraphRepresentation

class AdjacencyMatrix(AbstractGraphRepresentation):
    def __init__(self, graph:Graph):
        self._node_ids = [node.node_id for node in graph.get_nodes()]
        
        self._id_to_index = {node_id: index for index, node_id in enumerate(self._node_ids)}
        
        size = len(self._node_ids)

        self._matrix = [[0 for _ in range(size)] for _ in range(size)]

        for edge in graph.get_edges():
            first_node_id = edge.first_node.node_id
            second_node_id = edge.second_node.node_id
        
            first_node_index = self._id_to_index[first_node_id]
            second_node_index = self._id_to_index[second_node_id]

            self._matrix[first_node_index][second_node_index] = 1  
            self._matrix[second_node_index][first_node_index] = 1  

    def number_of_vertices(self):
        return len(self._node_ids)
    
    def number_of_edges(self):
        count = 0
        size = len(self._matrix)
        for i in range(size):
            for j in range(i):
                count += self._matrix[i][j]
        return count
    
    def adjacent_vertices(self, node_id):
        if node_id not in self._id_to_index:
            return []
        index = self._id_to_index[node_id]
        return [self._node_ids[j] for j, val in enumerate(self._matrix[index]) if val == 1]

    def has_node(self, node_id):
        return node_id in self._node_ids

    def has_edge(self, first_node_id, second_node_id):
        if first_node_id not in self._id_to_index or second_node_id not in self._id_to_index:
            return False
        i = self._id_to_index[first_node_id]
        j = self._id_to_index[second_node_id]
        return self._matrix[i][j] == 1

    def degree(self, node_id):
        if node_id not in self._id_to_index:
            return 0
        index = self._id_to_index[node_id]
        return sum(self._matrix[index])
    
    def degrees(self):
        return [(node_id, self.degree(node_id)) for node_id in self._node_ids]
    
    def __str__(self):
        return 'Adjacency Matrix\n' + tabulate([[self._node_ids[index], *data] for index, data in enumerate(self._matrix)], headers=self._node_ids)