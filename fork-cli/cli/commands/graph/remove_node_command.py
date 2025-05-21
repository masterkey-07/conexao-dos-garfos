from cli.command import Command

class RemoveNodeCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        node_id = input("node: ")
        removed = context.current_graph.remove_node(node_id)
        if removed:
            print(f"Node '{node_id}' removed from graph '{context.current_graph.name}'.")
        else:
            print(f"Node '{node_id}' could not be removed (it may not exist).")

    def __str__(self):
        return "Remove a node from the current graph"