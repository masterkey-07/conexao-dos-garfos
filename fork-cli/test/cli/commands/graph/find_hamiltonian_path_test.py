import pytest
from cli.commands.graph.find_hamiltonian_path_command import FindHamiltonianPathCommand

class DummyNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.properties = {}

class DummyEdge:
    def __init__(self, first, second):
        self.first_node = DummyNode(first)
        self.second_node = DummyNode(second)
        self.properties = {}

class DummyGraph:
    def __init__(self, nodes, edges):
        self._nodes = [DummyNode(n) for n in nodes]
        self._edges = [DummyEdge(a, b) for a, b in edges]
        self.name = "dummy"

    def get_nodes(self):
        return self._nodes

    def get_edges(self):
        return self._edges

class DummyContext:
    def __init__(self, graph):
        self.graph = graph

def test_hamiltonian_path_found(capsys):
    # Create a triangle (Hamiltonian cycle exists)
    nodes = ["A", "B", "C"]
    edges = [("A", "B"), ("B", "C"), ("C", "A")]
    graph = DummyGraph(nodes, edges)
    context = DummyContext(graph)
    cmd = FindHamiltonianPathCommand()
    
    cmd.execute(context)
    
    captured = capsys.readouterr()
    
    assert "Hamiltonian path found" in captured.out

def test_hamiltonian_path_not_found(capsys):
    # Create a disconnected graph (no Hamiltonian path)
    nodes = ["A", "B", "C"]
    edges = [("A", "B")]
    graph = DummyGraph(nodes, edges)
    context = DummyContext(graph)
    cmd = FindHamiltonianPathCommand()
    cmd.execute(context)
    captured = capsys.readouterr()
    assert "No Hamiltonian path found" in captured.out