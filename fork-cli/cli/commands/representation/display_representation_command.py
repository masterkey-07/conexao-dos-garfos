from cli.command import Command

class DisplayRepresentationCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        representation = getattr(context, "current_representation", None)

        if not representation:
            print("No representation selected. Please select a representation first (use 'sr').")
            return

        print(context.current_representation)

    def __str__(self):
        return "Display the current graph in the selected representation"