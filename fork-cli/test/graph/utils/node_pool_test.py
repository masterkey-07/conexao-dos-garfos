import pytest
from graph.core.node import Node
from graph.error.node import *
from graph.utils.node_pool import NodePool

NODE_A = Node('A')

NODE_B = Node('B')

def test_is_buildable():
    pool = NodePool()

def test_set_node_type_error():
    pool = NodePool()

    with pytest.raises(WrongNodeTypeError):
        pool.set(None)

def test_wrong_id_on_get():
    pool = NodePool()
    
    with pytest.raises(WrongNodeIdError):
        pool.get(None)

    with pytest.raises(WrongNodeIdError):
        pool.get(10)

    with pytest.raises(WrongNodeIdError):
        pool.get(Node('B'))

def test_set_and_get_node():
    pool = NodePool()
    
    assert pool.get('None') == None

    pool.set(NODE_A)

    assert pool.get('A') == NODE_A

    pool.set(NODE_B)

    assert pool.get('B') == NODE_B

def test_del_node():
    pool = NodePool()

    pool.set(NODE_A)
    pool.set(NODE_B)

    pool.delete('A')

    assert pool.get('A') == None

    pool.delete('B')

    assert pool.get('B') == None

    with pytest.raises(NodeNotFoundError):
        pool.delete('A')

    with pytest.raises(NodeNotFoundError):
        pool.delete('B')