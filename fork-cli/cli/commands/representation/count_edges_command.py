from cli.command import Command

class CountEdgesCommand(Command):
    @property
    def symbol(self) -> str:
        return "ce"

    def execute(self, context, args):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        number = context.current_graph.number_of_edges()
        print(f"Number of edges in graph '{context.current_graph.name}': {number}")

    def __str__(self):
        return "ce - Count the number of edges in the current graph"