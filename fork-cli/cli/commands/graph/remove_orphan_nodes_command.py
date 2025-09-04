from cli.command import Command
from graph.core.graph import Graph

class RemoveOrphanNodesCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        graph = context.current_graph
        nodes = graph.get_nodes()
        edges = graph.get_edges()

        # Find all nodes that are part of at least one edge
        connected_nodes = set()
        
        for edge in edges:
            connected_nodes.add(edge.first_node.node_id)
            connected_nodes.add(edge.second_node.node_id)

        # Find orphan nodes (not in any edge)
        orphan_nodes = [node.node_id for node in nodes if node.node_id not in connected_nodes]

        # Remove orphan nodes
        for node_id in orphan_nodes:
            graph.remove_node(node_id)

        if orphan_nodes:
            print(f"Removed orphan nodes: {', '.join(orphan_nodes)}")
        else:
            print("No orphan nodes found.")

    def __str__(self):
        return "Remove all orphan (disconnected) nodes from the current graph"