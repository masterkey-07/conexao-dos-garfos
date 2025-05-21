from cli.command import Command

class AddNodeCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        node_id = input("node: ")
        properties = {}

        node = context.current_graph.add_node(node_id, properties)
        if node:
            print(f"Node '{node_id}' added to graph '{context.current_graph.name}'.")
        else:
            print(f"Failed to add node '{node_id}'. It may already exist.")

    def __str__(self):
        return "Add a node to the current graph"