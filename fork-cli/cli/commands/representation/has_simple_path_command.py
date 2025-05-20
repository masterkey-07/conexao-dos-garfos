from cli.command import Command

class HasSimplePathCommand(Command):
    @property
    def symbol(self) -> str:
        return "hsp"

    def execute(self, context, args):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        if len(args) < 2:
            print("Usage: hsp <start_node_id> <end_node_id>")
            return

        start_id = args[0]
        end_id = args[1]

        path = context.current_representation.simple_path(start_id, end_id)
        if path:
            print(f"Simple path from '{start_id}' to '{end_id}': {' -> '.join(path)}")
        else:
            print(f"No simple path found from '{start_id}' to '{end_id}'.")

    def __str__(self):
        return "hsp <start_node_id> <end_node_id> - Check if a simple path exists between two nodes"