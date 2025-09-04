from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromDifferenceCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        # Ask user for the names of the two graphs
        graph1_name = input("Base graph (minuend) name: ").strip()
        graph2_name = input("Graph to subtract (subtrahend) name: ").strip()
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

        # Difference of nodes: nodes in graph1 not in graph2
        nodes1 = {node.node_id: node.properties or {} for node in graph1.get_nodes()}
        nodes2_ids = {node.node_id for node in graph2.get_nodes()}

        diff_node_ids = set(nodes1.keys()) - nodes2_ids
        nodes = {nid: nodes1[nid] for nid in diff_node_ids}

        # Difference of edges: only edges in graph1 not in graph2 (undirected)
        edges1 = set(tuple(sorted([e.first_node.node_id, e.second_node.node_id])) for e in graph1.get_edges())
        edges2 = set(tuple(sorted([e.first_node.node_id, e.second_node.node_id])) for e in graph2.get_edges())

        diff_edges = edges1 - edges2

        # Include only edges whose both nodes remain in the difference node set
        edges = []
        for first_node, second_node in diff_edges:
            if first_node in nodes and second_node in nodes:
                edges.append({
                    "first_node": first_node,
                    "second_node": second_node,
                    "properties": {}
                })

        data = {
            "name": result_graph_name,
            "nodes": [{"id": node_id, "properties": props} for node_id, props in nodes.items()],
            "edges": edges
        }

        result_graph = Graph(name=result_graph_name, data=data)
        context.current_project.save_graph(result_graph)

        print(f"Graph '{result_graph_name}' created as the difference between '{graph1_name}' and '{graph2_name}'.")

    def __str__(self):
        return "Create a new graph as the difference between two graphs"
