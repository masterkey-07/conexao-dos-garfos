from cli.command import Command

class RemoveEdgeCommand(Command):
    @property
    def symbol(self) -> str:
        return "re"

    def execute(self, context, args):
        if not hasattr(context, "graph") or context.graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if len(args) < 2:
            print("Usage: re <first_node_id> <second_node_id>")
            return

        first_node_id = args[0]
        second_node_id = args[1]

        removed = context.graph.remove_edge(first_node_id, second_node_id)
        if removed:
            print(f"Edge between '{first_node_id}' and '{second_node_id}' removed from graph '{context.graph.name}'.")
        else:
            print(f"No edge found between '{first_node_id}' and '{second_node_id}' in graph '{context.graph.name}'.")

    def __str__(self):
        return "re <first_node_id> <second_node_id> - Remove an edge from the current graph"