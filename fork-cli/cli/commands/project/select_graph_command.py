from cli.command import Command
from cli.commander import Commander
from cli.commands.graph import GRAPH_COMMANDS  # Make sure this is a list of graph-related commands

class SelectGraphCommand(Command):
    @property
    def symbol(self) -> str:
        return "sg"

    def execute(self, context, args):
        if context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        if not args:
            print("Usage: sg <graph_name>")
            return

        graph_name = args[0]
        graph = context.current_project.get_graph(graph_name)
        
        if not graph:
            print(f"Graph '{graph_name}' does not exist in project '{context.current_project.project_name}'.")
            return

        context.current_graph = graph

        print(f"Graph '{graph_name}' selected in project '{context.current_project.project_name}'.")

        # Start a new Commander session for the selected graph with graph commands
        commander = Commander(commands=GRAPH_COMMANDS, context=context)
        
        commander.run()

        context.current_project.save_graph(graph)

        context.current_graph = None

        print(f"Exited graph '{graph_name}' and saved it.")

    def __str__(self):
        return "sg <graph_name> - Select a graph in the current project"