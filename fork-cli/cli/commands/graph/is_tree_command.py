from cli.command import Command

class GotoTreeRepresentationCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if not context.current_graph.is_tree():
            print(f"The graph '{context.current_graph.name}' is not a tree.")
            return

        print(f"The graph '{context.current_graph.name}' is a tree.")

    def __str__(self):
        return "Is the current graph a tree?"