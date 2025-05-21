from cli.command import Command

class AddEdgeCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        first_node_id = input("first_node: ")
        second_node_id = input("second_node: ")
        properties = {}

        edge = context.current_graph.add_edge(first_node_id, second_node_id, properties)
        if edge:
            print(f"Edge added between '{first_node_id}' and '{second_node_id}' in graph '{context.current_graph.name}'.")
        else:
            print(f"Failed to add edge between '{first_node_id}' and '{second_node_id}'.")

    def __str__(self):
        return "Add an edge to the current graph"