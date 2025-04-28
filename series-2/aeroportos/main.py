import networkx as nx

# Carrega o grafo a partir do arquivo DOT
graph = nx.drawing.nx_pydot.read_dot("subaeroportos.dot")

# Converte para grafo simples, se necessário
G = nx.Graph(graph)  # Use nx.DiGraph(graph) se for direcionado

# Converte para grafo simples, se necessário
G = nx.Graph(graph)  # Use nx.DiGraph(graph) se for direcionado

V = list(G.nodes)[:10]
E = list(G.edges)[:10]
print("Vértices (aeroportos):", V)
print("Arestas (conexões):", E)

n = G.number_of_nodes()
m = G.number_of_edges()
print("n (vértices):", n)
print("m (arestas):", m)

graus = dict(G.degree())
print("Graus dos vértices:", graus)

grau_max = max(graus.values())
grau_min = min(graus.values())
print("Grau máximo:", grau_max)
print("Grau mínimo:", grau_min)

from itertools import combinations

# Exibe caminhos simples entre alguns pares
for u, v in list(combinations(G.nodes, 2))[:5]:  # só os 5 primeiros pares para exemplo
    try:
        paths = list(nx.all_simple_paths(G, source=u, target=v, cutoff=4))
        if paths:
            print(f"Caminhos simples de {u} para {v}:", paths[:2])  # mostra até 2
    except:
        continue

for u, v in list(combinations(G.nodes, 2))[:5]:
    try:
        path = nx.shortest_path(G, source=u, target=v)
        print(f"Caminho mínimo de {u} para {v}:", path)
    except:
        continue

# Exemplo: subgrafo com os primeiros 5 aeroportos
sub_nodes = V[:5]
subG = G.subgraph(sub_nodes)

print("Subgrafo vértices:", list(subG.nodes))
print("Subgrafo arestas:", list(subG.edges))
# É um subgrafo pois mantém todos os nós e arestas entre eles no grafo original.

ciclos = list(nx.cycle_basis(G))  # para grafo não direcionado
print("Ciclos encontrados:", ciclos[:5])  # mostra até 5

longest_path = []
for node in G.nodes:
    for target in G.nodes:
        if node != target:
            try:
                paths = list(nx.all_simple_paths(G, source=node, target=target))
                for path in paths:
                    if len(path) > len(longest_path):
                        longest_path = path
                        
            except:
                continue

print("Caminho simples mais longo:", longest_path)
print("Número de cidades (vértices) no caminho:", len(longest_path))