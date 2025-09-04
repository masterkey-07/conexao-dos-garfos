from collections import deque

from graph.core.edge import Edge
from graph.core.node import Node
from graph.utils.node_pool import NodePool
from graph.error.graph import GraphNameNotValidError


class Graph:
    def __init__(self, name: str,data: dict = None):
        self.name = name
        self._edges = []
        self._node_pool = NodePool()

        if not isinstance(name, str) or not name:
            raise GraphNameNotValidError()
        
        if len(name) == 0:
            raise GraphNameNotValidError()

        self.__process_data(data)

    def __process_data(self, data: dict):
        if data is None:
            return

        self.name = data.get("name", self.name)

        for node in data.get("nodes", []):
            self.add_node(node["id"], node.get("properties"))

        for edge in data.get("edges", []):
            self.add_edge(edge["first_node"], edge["second_node"], edge.get("properties"))

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

    def remove_node(self, node_id:str):
        try:
            self._node_pool.delete(node_id)
        except:
            return False

        self._edges = [edge for edge in self._edges if edge.first_node.node_id != node_id and edge.second_node.node_id != node_id]

        return True
    
    def add_edge(self, first_node_id:str, second_node_id:str, properties = None):
        first_node = self._node_pool.get(first_node_id)
        second_node = self._node_pool.get(second_node_id)

        if first_node is None or second_node is None:
            return None

        edge = Edge(first_node, second_node, properties)

        self._edges.append(edge)

        return edge

    def remove_edge(self, first_node_id: str, second_node_id: str):
        has_remove = False
        
        for edge in self._edges:
            first_case = edge.first_node.node_id == first_node_id and edge.second_node.node_id == second_node_id
            second_case = edge.first_node.node_id == second_node_id and edge.second_node.node_id == first_node_id

            if (first_case) or (second_case):
                has_remove = True
                
                self._edges.remove(edge)

        return has_remove
    
    def to_dict(self) -> dict:
        nodes = [
            {
                "id": node.node_id,
                "properties": node.properties
            }
            for node in self.get_nodes()
        ]
        
        edges = [
            {
                "first_node": edge.first_node.node_id,
                "second_node": edge.second_node.node_id,
                "properties": edge.properties
            }
            for edge in self.get_edges()
        ]
        
        return {"nodes": nodes, "edges": edges, "name": self.name}

    def is_tree(self) -> bool:
        nodes = self.get_nodes()
        edges = self.get_edges()
        
        length_nodes = len(nodes)
        
        length_edges = len(edges)

        if length_nodes == 0:
            return False
        
        if length_edges != length_nodes - 1:
            return False
        
        visited = set()
        
        adjacencies = {node.node_id: set() for node in nodes}
        
        for edge in edges:
            adjacencies[edge.first_node.node_id].add(edge.second_node.node_id)
            adjacencies[edge.second_node.node_id].add(edge.first_node.node_id)
        
        queue = deque()
        
        start = nodes[0].node_id
        
        queue.append(start)
        
        visited.add(start)

        while queue:
            current = queue.popleft()
            for neighbor in adjacencies[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return len(visited) == length_nodes