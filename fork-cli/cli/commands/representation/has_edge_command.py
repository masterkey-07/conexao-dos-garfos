from cli.command import Command

class HasEdgeCommand(Command):
    @property
    def symbol(self) -> str:
        return "he"

    def execute(self, context, args):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        if len(args) < 2:
            print("Usage: he <first_node_id> <second_node_id>")
            return

        first_node_id = args[0]
        second_node_id = args[1]

        if context.current_representation.has_edge(first_node_id, second_node_id):
            print(f"There is an edge between '{first_node_id}' and '{second_node_id}'.")
        else:
            print(f"There is NO edge between '{first_node_id}' and '{second_node_id}'.")

    def __str__(self):
        return "he <first_node_id> <second_node_id> - Check if there is an edge between two nodes in the current representation"