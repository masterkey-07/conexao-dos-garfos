from cli.command import Command

class RemoveNodeCommand(Command):
    @property
    def symbol(self) -> str:
        return "rn"

    def execute(self, context, args):
        if not hasattr(context, "graph") or context.graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if not args:
            print("Usage: rn <node_id>")
            return

        node_id = args[0]
        removed = context.graph.remove_node(node_id)
        if removed:
            print(f"Node '{node_id}' removed from graph '{context.graph.name}'.")
        else:
            print(f"Node '{node_id}' could not be removed (it may not exist).")

    def __str__(self):
        return "rn <node_id> - Remove a node from the current graph"