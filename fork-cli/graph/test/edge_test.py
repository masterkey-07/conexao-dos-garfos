import pytest
from graph.node import Node
from graph.edge import Edge, WrongNodeTypeException

print(__name__)

NODE_A = Node('A')
NODE_B = Node('B')
PROPERTY = {'weigh': 1 }

def _verity_wrong_node_type_exception(a, b):
    with pytest.raises(WrongNodeTypeException):
        Edge(a, b)

def test_wrong_id_types():
    _verity_wrong_node_type_exception(None, None)
    
    _verity_wrong_node_type_exception(NODE_A, None)
    _verity_wrong_node_type_exception(NODE_A, 10)
    _verity_wrong_node_type_exception(NODE_A, '10')
    _verity_wrong_node_type_exception(NODE_A, {})

    _verity_wrong_node_type_exception(None, NODE_A)
    _verity_wrong_node_type_exception(10, NODE_A)
    _verity_wrong_node_type_exception('10', NODE_A)
    _verity_wrong_node_type_exception({}, NODE_A)

def test_nodes_in_edge():
    edge = Edge(NODE_A, NODE_B)

    assert edge.first_node == NODE_A
    assert edge.second_node == NODE_B

def test_property_value():
    edge = Edge(NODE_A, NODE_B, PROPERTY)

    assert edge.properties == PROPERTY

def test_property_value_change():
    new_property = { 'weigh': 2 }
    
    edge = Edge(NODE_A, NODE_B, PROPERTY)

    edge.properties = new_property

    assert edge.properties != PROPERTY
    assert edge.properties == new_property