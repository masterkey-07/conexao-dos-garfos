from cli.command import Command

class NodesDegreesCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        degrees = context.current_representation.degrees()
        if not degrees:
            print("No nodes found in the current representation.")
            return

        print("Degrees of all nodes:")
        for node_id, degree in degrees:
            print(f"Node '{node_id}': {degree}")

    def __str__(self):
        return "Show the degree of all nodes in the current representation"