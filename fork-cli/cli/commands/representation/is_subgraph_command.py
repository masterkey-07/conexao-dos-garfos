from graph.representation.adjacency_list import AdjacencyList
from graph.representation.adjacency_matrix import AdjacencyMatrix
from graph.representation.incidency_matrix import IncidencyMatrix
from cli.command import Command

class IsSubgraphCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        other_graph = input("other_graph: ")
        other_representation_name = input("representation: ")

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
        
        if is_sub == True:
            print("The current representation is a subgraph of the given representation.")
        else:
            missing_nodes, missing_edges = is_sub
            print("The current representation is NOT a subgraph of the given representation.")

            if len(missing_nodes) > 0:
                print(f"Missing nodes: {', '.join(missing_nodes)}")
            if len(missing_edges) > 0:
                print(f"Missing edges: {', '.join([f'{edge[0]}-{edge[1]}' for edge in missing_edges])}")

    def __str__(self):
        return "Check if the current representation is a subgraph of another representation from another graph"