import pytest
from graph.core.edge import Edge
from graph.core.node import Node
from graph.core.graph import Graph
from graph.error.node import WrongNodeIdError
from graph.error.graph import GraphNameNotValidError

@pytest.fixture
def graph():
    return Graph("test_graph")

def test_error_on_empty_name():
    with pytest.raises(GraphNameNotValidError):
        Graph("")
    with pytest.raises(GraphNameNotValidError):
        Graph(None)
    with pytest.raises(GraphNameNotValidError):
        Graph(10)

def basic_setup(graph:Graph):
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')

def test_add_node(graph: Graph):
    node = graph.add_node("A", {"color": "red"})
    assert node is not None
    assert isinstance(node, Node)
    assert node.node_id == "A"
    assert node.properties == {"color": "red"}

def test_get_nodes(graph: Graph):
    nodes = graph.get_nodes()

    assert len(nodes) == 0

    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    
    nodes = graph.get_nodes()

    assert a in nodes
    assert b in nodes
    assert c in nodes

    assert len(nodes) == 3

def test_get_node_existing(graph: Graph):
    graph.add_node("B", {"value": 5})
    node = graph.get_node("B")
    assert node is not None
    assert node.node_id == "B"
    assert node.properties["value"] == 5

def test_get_node_nonexistent(graph: Graph):
    assert graph.get_node("Z") is None

def test_add_edge_success(graph: Graph):
    graph.add_node("A")
    graph.add_node("B")
    edge = graph.add_edge("A", "B", {"weight": 3})
    assert edge is not None
    assert isinstance(edge, Edge)
    assert edge.first_node.node_id == "A"
    assert edge.second_node.node_id == "B"
    assert edge.properties["weight"] == 3

def test_add_edge_with_missing_node(graph: Graph):
    graph.add_node("A")
    
    edge = graph.add_edge("A", "B")
    
    assert edge is None

def test_add_edge_with_wrong_type(graph: Graph):
    with pytest.raises(WrongNodeIdError):
        graph.add_edge(None, 10)

def test_get_edges(graph:Graph):
    edges = graph.get_edges()
    
    assert len(edges) == 0
    
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')

    edges = graph.get_edges()

    assert len(edges) == 2

    assert edges[0].first_node.node_id == 'A'
    assert edges[0].second_node.node_id == 'B'
    assert edges[1].first_node.node_id == 'A'
    assert edges[1].second_node.node_id == 'C'

def test_remove_node(graph:Graph):
    basic_setup(graph)

    assert graph.get_node("A") is not None
    
    assert len(graph.get_edges()) == 2

    result = graph.remove_node("A")
    
    assert result is True

    assert graph.get_node("A") is None
    
    assert all("A" not in (e.first_node.node_id, e.second_node.node_id) for e in graph.get_edges())

def test_remove_node_nonexistent(graph:Graph):
    basic_setup(graph)

    result = graph.remove_node("X")
    assert result is False

def test_remove_edge(graph:Graph):
    basic_setup(graph)

    assert len(graph.get_edges()) == 2
    result = graph.remove_edge("A", "B")
    assert result is True
    assert len(graph.get_edges()) == 1

def test_remove_edge_nonexistent(graph:Graph):
    basic_setup(graph)

    result = graph.remove_edge("B", "C")
    assert result is False
    assert len(graph.get_edges()) == 2

def test_to_dict(graph: Graph):
    graph = Graph("test_graph_2")

    graph.add_node("A", {"color": "red"})
    graph.add_node("B", {"color": "blue"})
    graph.add_edge("A", "B", {"weight": 5})

    graph_dict = graph.to_dict()

    assert "nodes" in graph_dict
    assert "edges" in graph_dict

    assert len(graph_dict["nodes"]) == 2
    assert len(graph_dict["edges"]) == 1

    node_ids = {node["id"] for node in graph_dict["nodes"]}
    
    assert "A" in node_ids
    assert "B" in node_ids

    edge = graph_dict["edges"][0]
    assert edge["first_node"] == "A"
    assert edge["second_node"] == "B"
    assert edge["properties"]["weight"] == 5

def test_graph_from_dict():
    graph_data = {
        "name": "other_graph",
        "nodes": [
            {"id": "A", "properties": {"color": "red"}},
            {"id": "B", "properties": {"color": "blue"}}
        ],
        "edges": [
            {"first_node": "A", "second_node": "B", "properties": {"weight": 5}}
        ]
    }

    graph = Graph("other_graph", graph_data)

    graph_dict = graph.to_dict()

    assert graph_dict == graph_data