from cli.command import Command

class IsEulerCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        # Eulerian: all nodes have even degree and the graph is connected
        nodes = context.current_graph.get_nodes()
        edges = context.current_graph.get_edges()

        # Build adjacency list
        adj = {node.node_id: set() for node in nodes}
        for edge in edges:
            adj[edge.first_node.node_id].add(edge.second_node.node_id)
            adj[edge.second_node.node_id].add(edge.first_node.node_id)

        # Check if all degrees are even
        all_even = all(len(adj[node.node_id]) % 2 == 0 for node in nodes)
        
        if not all_even:
            print("The graph is NOT Eulerian (not all nodes have even degree).")
            return

        # Check if the graph is connected (ignoring isolated nodes)
        visited = set()
        def dfs(v):
            visited.add(v)
            for u in adj[v]:
                if u not in visited:
                    dfs(u)

        # Start DFS from a node with degree > 0
        start = next((n.node_id for n in nodes if len(adj[n.node_id]) > 0), None)
        if start is not None:
            dfs(start)
            connected = all((len(adj[n.node_id]) == 0 or n.node_id in visited) for n in nodes)
        else:
            connected = True  # Empty graph is trivially Eulerian

        if all_even and connected:
            print("The graph IS Eulerian (all nodes have even degree and the graph is connected).")
        else:
            print("The graph is NOT Eulerian (the graph is not connected).")

    def __str__(self):
        return "Check if the current graph is Eulerian"