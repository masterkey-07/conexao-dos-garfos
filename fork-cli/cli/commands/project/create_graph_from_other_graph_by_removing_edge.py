from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromOtherGraphByRemovingEdgeCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        graph_name = input("Graph name: ").strip()
        first_node_id = input("First node of the edge to remove: ").strip()
        second_node_id = input("Second node of the edge to remove: ").strip()
        result_graph_name = input("Result graph name: ").strip()

        graph = context.current_project.get_graph(graph_name)

        if not graph:
            print(f"Graph '{graph_name}' not found in project.")
            return

        if context.current_project.get_graph(result_graph_name):
            print(f"A graph named '{result_graph_name}' already exists in the project.")
            return

        # Copy nodes
        nodes = {node.node_id: node.properties or {} for node in graph.get_nodes()}

        # Copy edges, excluding the one to remove (undirected)
        new_edges = []
        for edge in graph.get_edges():
            nodes_pair = {edge.first_node.node_id, edge.second_node.node_id}

            if nodes_pair == {first_node_id, second_node_id}:
                continue

            new_edges.append({
                "first_node": edge.first_node.node_id,
                "second_node": edge.second_node.node_id,
                "properties": edge.properties or {}
            })

        data = {
            "name": result_graph_name,
            "nodes": [{"id": nid, "properties": nodes[nid]} for nid in nodes],
            "edges": new_edges
        }

        result_graph = Graph(name=result_graph_name, data=data)
        context.current_project.save_graph(result_graph)
        print(f"Graph '{result_graph_name}' created by removing edge ({first_node_id}, {second_node_id}) from '{graph_name}'.")

    def __str__(self):
        return "Create a new graph by removing an edge from an existing graph"