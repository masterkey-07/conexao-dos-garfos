from cli.command import Command

class HasSimplePathCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        start_id = input("start_node: ")
        end_id = input("end_node: ")

        path = context.current_representation.simple_path(start_id, end_id)
        if path:
            print(f"Simple path from '{start_id}' to '{end_id}': {' -> '.join(path)}")
        else:
            print(f"No simple path found from '{start_id}' to '{end_id}'.")

    def __str__(self):
        return "Check if a simple path exists between two nodes"