import pytest
from graph.core.node import Node
from graph.error.node import WrongNodeIdError

NODE_ID = 'id'
PROPERTY = {'weigh': 1 }

def test_wrong_id_types():
    with pytest.raises(WrongNodeIdError):
        Node(None)

    with pytest.raises(WrongNodeIdError):
        Node(10)

def test_id_value():
    node = Node(NODE_ID)

    assert node.id == NODE_ID

def test_property_value():
    node = Node(NODE_ID, PROPERTY)

    assert node.properties == PROPERTY

def test_property_value_change():
    new_property = { 'weigh': 2 }
    
    node = Node(NODE_ID, PROPERTY)

    node.properties = new_property

    assert node.properties != PROPERTY
    assert node.properties == new_property