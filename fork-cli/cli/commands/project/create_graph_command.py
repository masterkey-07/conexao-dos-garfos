from cli.command import Command
from graph.core.graph import Graph

class CreateGraphCommand(Command):
    @property
    def symbol(self) -> str:
        return "cg"

    def execute(self, context, args):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        if not args:
            print("Usage: cg <graph_name>")
            return

        graph_name = args[0]

        # Check if graph already exists
        if context.current_project.get_graph(graph_name):
            print(f"Graph '{graph_name}' already exists in project '{context.current_project.project_name}'.")
            return

        graph = Graph(name=graph_name)
        
        context.current_project.save_graph(graph)
        
        print(f"Graph '{graph_name}' created in project '{context.current_project.project_name}'.")

    def __str__(self):
        return "cg <graph_name> - Create a new graph in the current project"