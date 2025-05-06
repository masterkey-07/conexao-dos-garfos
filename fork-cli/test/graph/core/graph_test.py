import pytest
from graph.core.edge import Edge
from graph.core.node import Node
from graph.core.graph import Graph
from graph.error.node import WrongNodeIdError

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

def test_add_edge_with_wrong_type(graph: Graph):
    with pytest.raises(WrongNodeIdError):
        graph.add_edge(None, 10)

def test_to_adjacent_matrix_with_no_edges(graph: Graph):
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")

    matrix_data = graph.to_adjacent_matrix()

    nodes = matrix_data['nodes']
    data = matrix_data['data']

    expected = [[0 for _ in nodes] for _ in nodes]

    assert data == expected, f"Expected matrix {expected}, but got {data}"

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
    expected[id_to_index["B"]][id_to_index["A"]] = 1
    expected[id_to_index["B"]][id_to_index["C"]] = 1
    expected[id_to_index["C"]][id_to_index["B"]] = 1

    assert data == expected, f"Expected matrix {expected}, but got {data}"

    graph.add_edge("A", "C")

    matrix_data = graph.to_adjacent_matrix()

    data = matrix_data['data']

    expected[id_to_index["A"]][id_to_index["C"]] = 1
    expected[id_to_index["C"]][id_to_index["A"]] = 1

    assert data == expected, f"Expected matrix {expected}, but got {data}"

def test_incidency_matrix():
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")

    g.add_edge("A", "B")
    g.add_edge("B", "C")

    matrix = g.to_incidency_matrix()

    expected = [[1, 0], [1, 1], [0, 1]]

    assert list(matrix['nodes']) == ['A', 'B', 'C']
    assert list(matrix['edges']) == [('A', 'B'), ('B', 'C')]
    assert matrix['data'] == expected

    g.add_edge("B", "B")

    expected = [[1, 0, 0], [1, 1, 2], [0, 1, 0]]

    matrix = g.to_incidency_matrix()

    assert list(matrix['nodes']) == ['A', 'B', 'C']
    assert list(matrix['edges']) == [('A', 'B'), ('B', 'C'), ('B', 'B')]
    assert matrix['data'] == expected

def test_adjacency_list():
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")

    adjacency_list = g.to_adjacency_list()

    expected = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A"],
        "D": ["B"]
    }

    assert adjacency_list == expected