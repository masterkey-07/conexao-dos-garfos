from cli.command import Command

class ListGraphsCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        graphs = context.current_project.list_graphs()
        if not graphs:
            print(f"No graphs found in project '{context.current_project.project_name}'.")
            return

        print(f"Graphs in project '{context.current_project.project_name}':")
        for graph in graphs:
            print(f"- {graph}")

    def __str__(self):
        return "List all graphs in the current project"