from cli.command import Command

class AddEdgeCommand(Command):
    @property
    def symbol(self) -> str:
        return "ae"

    def execute(self, context, args):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if len(args) < 2:
            print("Usage: ae <first_node_id> <second_node_id> [key=value ...]")
            return

        first_node_id = args[0]
        second_node_id = args[1]
        properties = {}

        for arg in args[2:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                properties[key] = value

        edge = context.current_graph.add_edge(first_node_id, second_node_id, properties)
        if edge:
            print(f"Edge added between '{first_node_id}' and '{second_node_id}' in graph '{context.current_graph.name}'.")
        else:
            print(f"Failed to add edge between '{first_node_id}' and '{second_node_id}'.")

    def __str__(self):
        return "ae <first_node_id> <second_node_id> [key=value ...] - Add an edge to the current graph"