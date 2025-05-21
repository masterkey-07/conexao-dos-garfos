from cli.command import Command

class CountNodesCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph selected. Please select a graph first.")
            return

        number = context.current_representation.number_of_vertices()
        
        print(f"Number of nodes in graph '{context.current_graph.name}': {number}")

    def __str__(self):
        return "Count the number of nodes in the current graph"