from cli.command import Command

class HasEdgeCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        first_node_id = input("first_node: ")
        second_node_id = input("second_node: ")

        if context.current_representation.has_edge(first_node_id, second_node_id):
            print(f"There is an edge between '{first_node_id}' and '{second_node_id}'.")
        else:
            print(f"There is NO edge between '{first_node_id}' and '{second_node_id}'.")

    def __str__(self):
        return "Check if there is an edge between two nodes in the current representation"