from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromNodeFusionCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        graph_name = input("Graph name: ").strip()
        node1_id = input("First node to fuse: ").strip()
        node2_id = input("Second node to fuse: ").strip()
        result_graph_name = input("Result graph name: ").strip()

        graph = context.current_project.get_graph(graph_name)

        if not graph:
            print(f"Graph '{graph_name}' not found in project.")
            return

        if context.current_project.get_graph(result_graph_name):
            print(f"A graph named '{result_graph_name}' already exists in the project.")
            return

        # Copy nodes and edges
        nodes = {node.node_id: node.properties or {} for node in graph.get_nodes()}

        edges = []

        for edge in graph.get_edges():
            edges.append({
                "first_node": edge.first_node.node_id,
                "second_node": edge.second_node.node_id,
                "properties": edge.properties or {}
            })

        # Create new node id for fusion
        fused_node_id = f"{node1_id}_{node2_id}"

        # Remove the two nodes to be fused
        if node1_id not in nodes or node2_id not in nodes:
            print("One or both nodes to fuse do not exist in the graph.")
            return

        fused_properties = {}

        fused_properties.update(nodes[node1_id])
        fused_properties.update(nodes[node2_id])

        del nodes[node1_id]

        del nodes[node2_id]

        nodes[fused_node_id] = fused_properties

        # Update edges: replace node1_id or node2_id with fused_node_id
        new_edges = []

        for edge in edges:
            first = edge["first_node"]
            second = edge["second_node"]
            # Replace node ids with fused node id if needed
            if first == node1_id or first == node2_id:
                first = fused_node_id
            if second == node1_id or second == node2_id:
                second = fused_node_id
            # Avoid self-loops created by fusion
            if first != second:
                # Avoid duplicate edges
                key = tuple(sorted([first, second]))
                if not any(
                    (e["first_node"], e["second_node"]) == key or
                    (e["second_node"], e["first_node"]) == key
                    for e in new_edges
                ):
                    new_edges.append({
                        "first_node": first,
                        "second_node": second,
                        "properties": edge["properties"]
                    })

        data = {
            "name": result_graph_name,
            "nodes": [{"id": node_id, "properties": nodes[node_id]} for node_id in nodes],
            "edges": new_edges
        }

        result_graph = Graph(name=result_graph_name, data=data)
        context.current_project.save_graph(result_graph)
        print(f"Graph '{result_graph_name}' created by fusing '{node1_id}' and '{node2_id}' in '{graph_name}'.")

    def __str__(self):
        return "Create a new graph by fusing two nodes in an existing graph"