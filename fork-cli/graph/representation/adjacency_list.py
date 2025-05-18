from collections import deque
from graph.core.graph import Graph

from graph.representation.abstract_graph_representation import AbstractGraphRepresentation

class AdjacencyList(AbstractGraphRepresentation):
    def __init__(self, graph:Graph):
        self._adjacency_list = {}

        for node in graph.get_nodes():
            self._adjacency_list[node.node_id] = []

        for edge in graph.get_edges():
            first_node_id = edge.first_node.node_id
            second_node_id = edge.second_node.node_id
            
            self._adjacency_list[first_node_id].append(second_node_id)
            
            self._adjacency_list[second_node_id].append(first_node_id)

    def number_of_vertices(self):
        return len(self._adjacency_list.keys())
    
    def number_of_edges(self):
        quantity = 0

        visited = set()

        for key in self._adjacency_list.keys():
            for subkey in self._adjacency_list[key]:
                if subkey not in visited:
                    quantity += 1
            
            visited.add(key)

        return quantity
    
    def adjacent_vertices(self, node_id:str):
        if node_id not in self._adjacency_list:
            return []

        return self._adjacency_list[node_id]

    def has_node(self, node_id):
        return node_id in self._adjacency_list

    def has_edge(self, first_node_id, second_node_id):
        if first_node_id not in self._adjacency_list:
            return False

        return second_node_id in self._adjacency_list[first_node_id]
    
    def degree(self, node_id):
        if node_id not in self._adjacency_list:
            return 0

        return len(self._adjacency_list[node_id])
    
    def degrees(self) -> list[tuple[str, int]]:
        return [(key, len(self._adjacency_list[key])) for key in self._adjacency_list.keys()]

    def __str__(self):
        output = ''

        for key in self._adjacency_list:
            output += key + ' : ' + ', '.join(self._adjacency_list[key]) + '\n'

        return 'Adjacency List\n' + output