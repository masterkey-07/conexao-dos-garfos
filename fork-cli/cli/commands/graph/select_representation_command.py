from cli.command import Command
from cli.commander import Commander
from graph.representation.adjacency_list import AdjacencyList
from graph.representation.adjacency_matrix import AdjacencyMatrix
from graph.representation.incidency_matrix import IncidencyMatrix
from cli.commands.representation import REPRESENTATION_COMMANDS

REP_MAP = {
    "al": "Adjacency List",
    "am": "Adjacency Matrix",
    "im": "Incidency Matrix"
}

class SelectRepresentationCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        representation = input("representation: ")
        valid_representations = ["al", "am", "im"]

        if representation not in valid_representations:
            print(f"Invalid representation '{representation}'.")
            print("Available representations: \n\tal (Adjacency List)\n\tam (Adjacency Matrix)\n\tim (Incidency Matrix)")
            return

        if representation == "al":
            context.current_representation = AdjacencyList(context.current_graph)
        elif representation == "am":    
            context.current_representation = AdjacencyMatrix(context.current_graph)
        elif representation == "im":
            context.current_representation = IncidencyMatrix(context.current_graph)

        print(f"Graph representation set to '{representation}' for graph '{context.current_graph.name}'.")

        context_name = "Project: " + context.current_project.project_name + " - Graph: " + context.current_graph.name + " - Representation: " + REP_MAP[representation]

        commander = Commander(commands=REPRESENTATION_COMMANDS, context=context, context_name=context_name)
        commander.run()

        context.current_representation = None

        print(f"Exited from graph representation.")

    def __str__(self):
        return "Select the representation for the current graph: \n\t\tal (Adjacency List)\n\t\tam (Adjacency Matrix)\n\t\tim (Incidency Matrix)"