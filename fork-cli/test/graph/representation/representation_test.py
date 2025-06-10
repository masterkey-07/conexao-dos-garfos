import pytest

from graph.core.graph import Graph
from graph.representation.adjacency_list import AdjacencyList
from graph.representation.adjacency_matrix import AdjacencyMatrix
from graph.representation.incidency_matrix import IncidencyMatrix
from graph.representation.abstract_graph_representation import AbstractGraphRepresentation

@pytest.fixture(params=[AdjacencyList, AdjacencyMatrix, IncidencyMatrix])
def simple_representation(request):
    g = Graph("test_graph")

    g.add_node('A')
    g.add_node('B')
    g.add_node('C')

    g.add_edge('A', 'B')
    g.add_edge('B', 'C')

    ConcreceGraphRepresentation:AbstractGraphRepresentation = request.param

    return ConcreceGraphRepresentation(g)

@pytest.fixture(params=[AdjacencyList, AdjacencyMatrix, IncidencyMatrix])
def Representation(request):
    return request.param

def test_number_of_vertices_and_edges(simple_representation: AbstractGraphRepresentation):
    assert simple_representation.number_of_vertices() == 3
    assert simple_representation.number_of_edges() == 2

def test_adjacency(simple_representation: AbstractGraphRepresentation):
    assert set(simple_representation.adjacent_vertices("A")) == {"B"}
    assert set(simple_representation.adjacent_vertices("B")) == {"A", "C"}
    assert set(simple_representation.adjacent_vertices("C")) == {"B"}

def test_has_edge(simple_representation: AbstractGraphRepresentation):
    assert simple_representation.has_edge("A", "B")
    assert simple_representation.has_edge("B", "C")
    assert not simple_representation.has_edge("A", "C")

def test_degrees(simple_representation: AbstractGraphRepresentation):
    assert simple_representation.degree("A") == 1
    assert simple_representation.degree("B") == 2
    assert simple_representation.degree("C") == 1
    
    degrees_dict = dict(simple_representation.degrees())
    
    assert degrees_dict == {"A": 1, "B": 2, "C": 1}

def test_simple_path(simple_representation: AbstractGraphRepresentation):
    path = simple_representation.simple_path("A", "C")

    assert path == ["A", "B", "C"] or path == ["C", "B", "A"]
    assert simple_representation.simple_path("A", "A") == ["A"]

def test_cycle_detection(Representation):
    g = Graph("test_graph_2")

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")

    g.add_edge('A', "B")
    g.add_edge('B', "C")
    g.add_edge('C', "D")
    g.add_edge('D', "A")
    g.add_edge('E', "D")

    representation: AbstractGraphRepresentation = Representation(g)

    cycle = representation.cycle_containing_node("A")

    assert cycle is not None
    assert set(cycle).issubset({"A", "B", "C", "D"})

def test_empty_cycle_detection(Representation):
    g = Graph("test_graph")

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")

    g.add_edge('A', "B")
    g.add_edge('B', "C")
    g.add_edge('C', "D")
    g.add_edge('D', "A")
    g.add_edge('E', "D")

    representation: AbstractGraphRepresentation = Representation(g)

    non_cycle = representation.cycle_containing_node("E")
    
    assert non_cycle is None

def test_is_supergraph_and_subgraph(simple_representation, Representation):
    supergraph = Graph("supergraph")
    supergraph.add_node("A")
    supergraph.add_node("B")
    supergraph.add_node("C")
    supergraph.add_node("D")
    
    supergraph.add_edge("A", "B")
    supergraph.add_edge("B", "C")
    supergraph.add_edge("D", "C")
    supergraph.add_edge("C", "A")

    rep1 = Representation(supergraph)

    rep2 = simple_representation

    assert rep1.is_supergraph(rep2) == True
    assert rep2.is_subgraph(rep1) == True
    
    nodes, edges = rep2.is_supergraph(rep1)

    assert set(nodes).issubset({"D"})
    assert set(edges).issubset({("D", "C"), ("C", "A"),("C", "D"), ("A", "C")})