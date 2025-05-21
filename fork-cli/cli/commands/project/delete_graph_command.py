import os
from cli.command import Command

class DeleteGraphCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        graph_name = input("graph_name: ")
        graph_file = graph_name if graph_name.endswith(".json") else graph_name + ".json"
        file_path = os.path.join(context.current_project.folder_path, graph_file)

        if not os.path.isfile(file_path):
            print(f"Graph '{graph_name}' does not exist in project '{context.current_project.project_name}'.")
            return

        try:
            os.remove(file_path)

            if graph_name in context.current_project.graphs:
                del context.current_project.graphs[graph_name]
            elif graph_file in context.current_project.graphs:
                del context.current_project.graphs[graph_file]
            print(f"Graph '{graph_name}' deleted from project '{context.current_project.project_name}'.")
        except Exception as e:
            print(f"Failed to delete graph: {e}")

    def __str__(self):
        return "Delete a graph from the current project"