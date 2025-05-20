from graph.representation.adjacency_list import AdjacencyList
from graph.representation.adjacency_matrix import AdjacencyMatrix
from graph.representation.incidency_matrix import IncidencyMatrix
from cli.command import Command

class IsSubgraphCommand(Command):
    @property
    def symbol(self) -> str:
        return "isg"

    def execute(self, context, args):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        if len(args) < 2:
            print("Usage: isg <other_graph> <representation_mode>")
            print("You must provide another graph representation object in the context (e.g., context.other_representation).")
            return

        other_graph = args[0]
        other_representation_name = args[1]

        if other_representation_name not in ("al", "im", "am"):
            print(f"Representation '{other_representation_name}'.")
            return
        
        other_graph_instance = context.current_project.get_graph(other_graph)

        if other_graph_instance is None:
            print(f"Graph '{other_graph}' not found")
            return

        other_representation = None

        if other_representation_name == "al":
            other_representation = AdjacencyList(other_graph_instance)
        if other_representation_name == "am":
            other_representation = AdjacencyMatrix(other_graph_instance)
        if other_representation_name == "im":
            other_representation = IncidencyMatrix(other_graph_instance)

        is_sub = context.current_representation.is_subgraph(other_representation)
        
        if is_sub:
            print("The current representation is a subgraph of the given representation.")
        else:
            print("The current representation is NOT a subgraph of the given representation.")

    def __str__(self):
        return "isg <other_graph_representation> - Check if the current representation is a subgraph of another"