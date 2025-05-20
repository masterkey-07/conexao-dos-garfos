from cli.command import Command

class AddNodeCommand(Command):
    @property
    def symbol(self) -> str:
        return "an"

    def execute(self, context, args):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if not args:
            print("Usage: an <node_id> [key=value ...]")
            return

        node_id = args[0]
        properties = {}

        for arg in args[1:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                properties[key] = value

        node = context.current_graph.add_node(node_id, properties)
        if node:
            print(f"Node '{node_id}' added to graph '{context.current_graph.name}'.")
        else:
            print(f"Failed to add node '{node_id}'. It may already exist.")

    def __str__(self):
        return "an <node_id> [key=value ...] - Add a node to the current graph"