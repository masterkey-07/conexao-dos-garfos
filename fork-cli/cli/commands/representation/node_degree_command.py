from cli.command import Command

class NodeDegreeCommand(Command):
    @property
    def symbol(self) -> str:
        return "nd"

    def execute(self, context, args):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        if not args:
            print("Usage: nd <node_id>")
            return

        node_id = args[0]
        if not context.current_representation.has_node(node_id):
            print(f"Node '{node_id}' does not exist in the current representation.")
            return

        degree = context.current_representation.degree(node_id)
        print(f"Degree of node '{node_id}': {degree}")

    def __str__(self):
        return "nd <node_id> - Show the degree of a node in the current representation"