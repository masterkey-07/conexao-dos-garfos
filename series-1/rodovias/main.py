import geopandas as gpd
import networkx as nx
from shapely.geometry import Point, LineString

# Load the shapefile (update the path accordingly)
shapefile_path = "rodovia-estadual.shp"
gdf = gpd.read_file(shapefile_path)

# Create a graph
G = nx.Graph()

edges = dict()
nodes = set()

for idx, row in gdf.iterrows():
    if row.sigla is None:
        continue

    geom = row.geometry

    if isinstance(geom, LineString):
        start = Point(geom.coords[0])
        end = Point(geom.coords[-1])

        nodes.add(row.sigla)

        start_edge_index = (start.x, start.y)
        end_edge_index = (end.x, end.y)

        if edges.get(start_edge_index) is None:
            edges[start_edge_index] = []

        if edges.get(end_edge_index) is None:
            edges[end_edge_index] = []

        edges[start_edge_index].append(row.sigla)
        edges[end_edge_index].append(row.sigla)

for node in nodes:
    G.add_node(node)

for edge in edges:
    length = len(edges[edge])

    for i in range(length):
        for j in range(length):
            if i == j:
                continue

            first_node = edges[edge][i]
            second_node = edges[edge][j]

            G.add_edge(first_node, second_node)

# Export to DOT format
nx.drawing.nx_pydot.write_dot(G, "highways_graph.dot")
print("DOT file exported: highways_graph.dot")