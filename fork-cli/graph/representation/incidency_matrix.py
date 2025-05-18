from collections import deque
from tabulate import tabulate
from graph.core.graph import Graph
from graph.representation.abstract_graph_representation import AbstractGraphRepresentation

class IncidencyMatrix(AbstractGraphRepresentation):
    def __init__(self, graph:Graph):
        self._node_ids = [node.node_id for node in graph.get_nodes()]

        edges = graph.get_edges()
        
        self._edges = []

        self._id_to_index = {node_id: index for index, node_id in enumerate(self._node_ids)}
        
        size_nodes = len(self._node_ids)
        size_edges = len(edges)

        self._matrix = [[0 for _ in range(size_edges)] for _ in range(size_nodes)]

        for edge_index, edge in enumerate(edges):
            first_node_index = self._id_to_index[edge.first_node.node_id]
            second_node_index = self._id_to_index[edge.second_node.node_id]
            
            self._matrix[first_node_index][edge_index] += 1
            self._matrix[second_node_index][edge_index] += 1
            
            self._edges.append((edge.first_node.node_id, edge.second_node.node_id))

    def number_of_vertices(self):
        return len(self._node_ids)
    
    def number_of_edges(self):
        return len(self._edges)
    
    def adjacent_vertices(self, node_id):
        nodes = []

        index = self._id_to_index[node_id]

        for edge_index, value in enumerate(self._matrix[index]):
            if value == 0:
                continue
            
            first_id = self._edges[edge_index][0]
            second_id = self._edges[edge_index][1]

            if first_id == second_id:
                nodes.append(node_id)
            elif first_id == node_id:
                nodes.append(second_id)
            else:
                nodes.append(first_id)

        return nodes
    
    def has_node(self, node_id):
        return node_id in self._node_ids

    def has_edge(self, first_node_id, second_node_id):
        for u, v in self._edges:
            if {u, v} == {first_node_id, second_node_id}:
                return True
        return False

    def degree(self, node_id):
        if node_id not in self._id_to_index:
            return 0
        index = self._id_to_index[node_id]
        return sum(self._matrix[index])

    def degrees(self):
        return [(node_id, self.degree(node_id)) for node_id in self._node_ids]

    def __str__(self):
        return 'Incidency Matrix\n' + tabulate([[self._node_ids[index], *data] for index, data in enumerate(self._matrix)], headers=['Node', *[f'({edge[0]}, {edge[1]})' for edge in self._edges]])