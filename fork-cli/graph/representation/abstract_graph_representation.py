from collections import deque
from graph.core.graph import Graph

from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class AbstractGraphRepresentation(ABC):
    @abstractmethod
    def __init__(self, graph: Graph):
        super().__init__()

    @abstractmethod
    def number_of_vertices(self) -> int:
        """Returns the number of vertices in the graph."""
        pass

    @abstractmethod
    def number_of_edges(self) -> int:
        """Returns the number of edges in the graph."""
        pass

    @abstractmethod
    def adjacent_vertices(self, node_id: str) -> List[str]:
        """Returns the adjacent vertices of a given node_id."""
        pass

    @abstractmethod
    def has_node(self, node_id: str) -> bool:
        """Returns whether there is an edge between first_node_id and second_node_id."""
        pass

    @abstractmethod
    def has_edge(self, first_node_id: str, second_node_id: str) -> bool:
        """Returns whether there is an edge between first_node_id and second_node_id."""
        pass

    @abstractmethod
    def degree(self, node_id: str) -> int:
        """Returns the degree of a given node_id."""
        pass

    @abstractmethod
    def degrees(self) -> Dict[str, int]:
        """Returns a dictionary with the degree of each node_id."""
        pass

    @abstractmethod
    def __str__(self):
        """Returns a str output to be printed."""
        pass

    def simple_path(self, start_id: str, end_id: str, exceptions = []):
        if not(self.has_node(start_id) and self.has_node(end_id)):
            return None
    
        visited = set(exceptions)
    
        queue = deque([[start_id]])

        while queue:
            path = queue.popleft()
        
            node = path[-1]
        
            if node == end_id:
                return path

            if node in visited:
                continue

            visited.add(node)
    
            for neighbor in self.adjacent_vertices(node):
                if neighbor not in path:
                    queue.append(path + [neighbor])
        
        return None

    def cycle_containing_node(self, node_id:str):
        if not self.has_node(node_id):
            return None

        visited = set()

        neighbors = self.adjacent_vertices(node_id)

        for first_neighbor in neighbors:
            visited.add(first_neighbor)

            for second_neighbor in neighbors:
                if second_neighbor in visited:
                    continue

                simple_path = self.simple_path(first_neighbor, second_neighbor, [node_id])

                if simple_path is not None:
                    return [node_id] + simple_path + [node_id]

        return None

    def is_supergraph(self, other: 'AbstractGraphRepresentation'):
        missing_edges = []
        missing_nodes = []

        for node_id in other.degrees():
            if not self.has_node(node_id[0]):
                missing_nodes.append(node_id[0])
    
        for node_id, _ in other.degrees():
            for neighbor in other.adjacent_vertices(node_id):
                if not self.has_edge(node_id, neighbor):
                    missing_edges.append((node_id, neighbor))
    
        if len(missing_edges) > 0 or len(missing_nodes) > 0:
            return missing_nodes, missing_edges

        return True
    
    def is_subgraph(self, other: 'AbstractGraphRepresentation'):
        return other.is_supergraph(self)
    