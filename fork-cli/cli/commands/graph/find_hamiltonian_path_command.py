from cli.command import Command

class FindHamiltonianPathCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        nodes = context.current_graph.get_nodes()
        edges = context.current_graph.get_edges()

        number_of_nodes = len(nodes)

        node_ids = [node.node_id for node in nodes]

        adj = {node.node_id: set() for node in nodes}
        
        for edge in edges:
            adj[edge.first_node.node_id].add(edge.second_node.node_id)
            adj[edge.second_node.node_id].add(edge.first_node.node_id)

        def hamiltonian_backtrack(path, visited):
            if len(path) == number_of_nodes + 1:
                return path

            last_node = path[-1]

            for neighbor in adj[last_node]:
                if len(path) == number_of_nodes and neighbor == path[0]:
                    return path + [neighbor]
                elif neighbor not in visited:
                    visited.add(neighbor)
        
                    result_path = hamiltonian_backtrack(path + [neighbor], visited)
        
                    if result_path:
                        return result_path
        
                    visited.remove(neighbor)

            return None

        for start in node_ids:
            path = hamiltonian_backtrack([start], {start})
            
            if path:
                print("Hamiltonian path found:")
                print(" -> ".join(path))
                return

        print("No Hamiltonian path found in the current graph.")

    def __str__(self):
        return "Find a Hamiltonian path in the current graph"