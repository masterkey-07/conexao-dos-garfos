from cli.command import Command
from cli.commander import Commander
from graph.representation.adjacency_list import AdjacencyList
from graph.representation.adjacency_matrix import AdjacencyMatrix
from graph.representation.incidency_matrix import IncidencyMatrix
from cli.commands.representation import REPRESENTATION_COMMANDS

class SelectRepresentationCommand(Command):
    @property
    def symbol(self) -> str:
        return "sr"

    def execute(self, context, args):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        if not args:
            print("Usage: sr <representation>")
            print("Available representations: al (adjacency_list), am (adjacency_matrix), im (incidency matrix)")
            return

        representation = args[0]
        valid_representations = ["al", "am", "im"]

        if representation not in valid_representations:
            print(f"Invalid representation '{representation}'.")
            print("Available representations: adjacency_list, adjacency_matrix, incidency_matrix")
            return

        if representation == "al":
            context.current_representation = AdjacencyList(context.current_graph)
        elif representation == "am":    
            context.current_representation = AdjacencyMatrix(context.current_graph)
        elif representation == "im":
            context.current_representation = IncidencyMatrix(context.current_graph)

        print(f"Graph representation set to '{representation}' for graph '{context.current_graph.name}'.")

        # Start a new Commander session for representation commands if needed
        commander = Commander(commands=REPRESENTATION_COMMANDS, context=context, context_name=context.current_project.project_name + "/" + context.current_graph.name + "/" + representation + ">")
        commander.run()

        context.current_representation = None

        print(f"Exited from graph representation.")

    def __str__(self):
        return "sr <representation> - Select the representation for the current graph: al (adjacency_list), am (adjacency_matrix), im (edge_list)"