from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromUnionCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        # Ask user for the names of the two graphs to union
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

        # Create union of nodes
        nodes = {}
        
        for node in graph1.get_nodes():
            nodes[node.node_id] = node.properties or {}
        
        for node in graph2.get_nodes():
            nodes[node.node_id] = node.properties or {}

        # Create union of edges (avoid duplicates)
        edge_set = set()
        
        edges = []
        
        for edge in graph1.get_edges() + graph2.get_edges():
            key = tuple(sorted([edge.first_node.node_id, edge.second_node.node_id]))
        
            if key not in edge_set:
                edge_set.add(key)
        
                edges.append({
                    "first_node": edge.first_node.node_id,
                    "second_node": edge.second_node.node_id,
                    "properties": edge.properties or {}
                })

        # Prepare data for new graph
        data = {
            "name": result_graph_name,
            "nodes": [{"id": node_id, "properties": props} for node_id, props in nodes.items()],
            "edges": edges
        }

        result_graph = Graph(name=result_graph_name, data=data)

        context.current_project.save_graph(result_graph)

        print(f"Graph '{result_graph_name}' created as the union of '{graph1_name}' and '{graph2_name}'.")

    def __str__(self):
        return "Create a new graph as the union of two graphs"