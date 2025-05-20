from cli.command import Command

class CountEdgesCommand(Command):
    @property
    def symbol(self) -> str:
        return "ce"

    def execute(self, context, args):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph selected. Please select a graph first.")
            return

        number = context.current_representation.number_of_edges()
        print(f"Number of edges in graph '{context.current_graph.name}': {number}")

    def __str__(self):
        return "ce - Count the number of edges in the current graph"