from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromSymmetryCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        # Ask user for the names of the two graphs to compute the symmetry difference
        graph1_name = input("First graph name: ").strip()
        graph2_name = input("Second graph name: ").strip()
        result_graph_name = input("Result graph name: ").strip()

        graph1 = context.current_project.get_graph(graph1_name)
        graph2 = context.current_project.get_graph(graph2_name)

        if not graph1:
            print(f"Graph '{graph1_name}' not found in project.")
            return
        if not graph2:
            print(f"Graph '{graph2_name}' not found in project.")
            return
        if context.current_project.get_graph(result_graph_name):
            print(f"A graph named '{result_graph_name}' already exists in the project.")
            return

        # Symmetric difference of nodes: nodes present in one graph or the other, but not both
        nodes1 = {node.node_id: node.properties or {} for node in graph1.get_nodes()}
        nodes2 = {node.node_id: node.properties or {} for node in graph2.get_nodes()}
        sym_nodes_ids = set(nodes1.keys()) ^ set(nodes2.keys())
        nodes = {nid: (nodes1.get(nid) or nodes2.get(nid)) for nid in sym_nodes_ids}

        # Symmetric difference of edges: edges present in one graph or the other, but not both (undirected)
        edges1 = set(tuple(sorted([e.first_node.node_id, e.second_node.node_id])) for e in graph1.get_edges())
        edges2 = set(tuple(sorted([e.first_node.node_id, e.second_node.node_id])) for e in graph2.get_edges())

        sym_edges = edges1 ^ edges2

        edges = []
        for first_node, second_node in sym_edges:
            edge_props = {}

            edges.append({
                "first_node": first_node,
                "second_node": second_node,
                "properties": edge_props
            })

        data = {
            "name": result_graph_name,
            "nodes": [{"id": node_id, "properties": {}} for node_id in nodes],
            "edges": edges
        }

        result_graph = Graph(name=result_graph_name, data=data)
        context.current_project.save_graph(result_graph)
        print(f"Graph '{result_graph_name}' created as the symmetric difference of '{graph1_name}' and '{graph2_name}'.")

    def __str__(self):
        return "Create a new graph as the symmetric difference two graphs"