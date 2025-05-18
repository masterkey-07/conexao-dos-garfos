from os import system

from graph.core.graph import Graph
from graph.representation.adjacency_list import AdjacencyList
from graph.representation.incidency_matrix import IncidencyMatrix
from graph.representation.adjacency_matrix import AdjacencyMatrix

graph = Graph()

print('commands:')
print('\tadd node: n {node_id}')
print('\tadd edge: e {node_id} {node_id}')
print('\tsee adjace: e {node_id} {node_id}')
print('\tsee adjacency list: al')
print('\tsee incidency matrix: im')
print('\tsee adjacency matrix: am')
print('\n')

while True:
    entry = input('insert command\n')

    system('clear')

    if entry.startswith('n '):
        node = entry[2:].strip()
        graph.add_node(node)

    elif entry.startswith('e '):
        edges = entry[2:].split(' ')

        if len(edges) != 2:
            continue

        graph.add_edge(edges[0], edges[1])

    elif entry == 'al':
        print(AdjacencyList(graph))
        print('\n')

    elif entry == 'im':
        print(IncidencyMatrix(graph))
        print('\n')

    elif entry == 'am':
        print(AdjacencyMatrix(graph))
        print('\n')

    elif entry == 'dot':
        dot = 'graph {\n'

        for node in graph.get_nodes():
            dot += node.node_id + ';\n'

        for edge in graph.get_edges():
            dot += f'{edge.first_node.node_id} -- {edge.second_node.node_id};\n'

        dot += '}'

        open('output.dot', '+w').write(dot)