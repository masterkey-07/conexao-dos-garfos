from cli.command import Command

class HasCycleCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_representation") or context.current_representation is None:
            print("No graph representation selected. Please select a representation first.")
            return

        node_id = input("node: ")
        
        if not context.current_representation.has_node(node_id):
            print(f"Node '{node_id}' does not exist in the current representation.")
            return

        cycle = context.current_representation.cycle_containing_node(node_id)

        if cycle:
            print(f"Cycle containing node '{node_id}': {' -> '.join(cycle)}")
        else:
            print(f"No cycle found containing node '{node_id}'.")

    def __str__(self):
        return "Check if the given node is part of a cycle in the current representation"