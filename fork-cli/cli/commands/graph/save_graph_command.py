from cli.command import Command

class SaveGraphCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        context.current_project.save_graph(context.current_graph)
        print(f"Graph '{context.current_graph.name}' saved in project '{context.current_project.project_name}'.")

    def __str__(self):
        return "Save the current graph to the current project"