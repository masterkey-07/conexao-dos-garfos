import pytest
from graph.core.edge import Edge
from graph.core.node import Node
from graph.core.graph import Graph
from graph.error.node import NodeNotFoundError

@pytest.fixture
def graph():
    return Graph()

def test_add_node(graph: Graph):
    node = graph.add_node("A", {"color": "red"})
    assert node is not None
    assert isinstance(node, Node)
    assert node.id == "A"
    assert node.properties == {"color": "red"}

def test_get_node_existing(graph: Graph):
    graph.add_node("B", {"value": 5})
    node = graph.get_node("B")
    assert node is not None
    assert node.id == "B"
    assert node.properties["value"] == 5

def test_get_node_nonexistent(graph: Graph):
    assert graph.get_node("Z") is None

def test_delete_node(graph: Graph):
    graph.add_node("C")
    deleted = graph.delete_node("C")
    assert deleted is True
    assert graph.get_node("C") is None

def test_delete_node_nonexistent(graph: Graph):
    deleted = graph.delete_node("X")
    
    print(deleted)

    assert deleted is False

def test_add_edge_success(graph: Graph):
    graph.add_node("A")
    graph.add_node("B")
    edge = graph.add_edge("A", "B", {"weight": 3})
    assert edge is not None
    assert isinstance(edge, Edge)
    assert edge.first_node.id == "A"
    assert edge.second_node.id == "B"
    assert edge.properties["weight"] == 3

def test_add_edge_with_missing_node(graph: Graph):
    graph.add_node("A")
    
    edge = graph.add_edge("A", "B")
    
    assert edge is None

def test_to_adjacent_matrix(graph: Graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    matrix_data = graph.to_adjacent_matrix()

    nodes = matrix_data['nodes']
    data = matrix_data['data']

    id_to_index = {node_id: i for i, node_id in enumerate(nodes)}

    expected = [[0 for _ in nodes] for _ in nodes]
    expected[id_to_index["A"]][id_to_index["B"]] = 1
    expected[id_to_index["B"]][id_to_index["C"]] = 1

    assert data == expected, f"Expected matrix {expected}, but got {data}"
