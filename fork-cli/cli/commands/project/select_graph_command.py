from cli.command import Command
from cli.commander import Commander
from cli.commands.graph import GRAPH_COMMANDS  # Make sure this is a list of graph-related commands

class SelectGraphCommand(Command):
    def execute(self, context):
        if context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        graph_name = input("graph_name: ")
        graph = context.current_project.get_graph(graph_name)
        
        if not graph:
            print(f"Graph '{graph_name}' does not exist in project '{context.current_project.project_name}'.")
            return

        context.current_graph = graph

        print(f"Graph '{graph_name}' selected in project '{context.current_project.project_name}'.")

        context_name = "Project: " + context.current_project.project_name + " - Graph: " + graph_name

        commander = Commander(commands=GRAPH_COMMANDS, context=context, context_name=context_name)
        
        commander.run()

        context.current_project.save_graph(graph)

        context.current_graph = None

        print(f"Exited graph '{graph_name}' and saved it.")

    def __str__(self):
        return "Select a graph in the current project"