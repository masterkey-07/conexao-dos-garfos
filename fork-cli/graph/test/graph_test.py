import pytest
from graph.graph import Graph

def test_is_buildable():
    _ = Graph()

def test_add_node():
    fork = Graph()
    
    props = {'weigh': 10}

    fork.add_node('A', props)

    node = fork.get_node('A')

    assert node.id == 'A'
    assert node.properties == props

def test_delete_node():
    fork = Graph()

    fork.add_node('A')

    fork.delete_node('A')

    node = fork.get_node('A')

    assert node == None