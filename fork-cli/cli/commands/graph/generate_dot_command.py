from cli.command import Command

class GenerateDotCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        filename = input(f"filename [{context.current_graph.name}.dot]: ")

        filename = filename if len(filename.strip()) > 0 else f"{context.current_graph.name}.dot"

        dot_lines = [
            "graph G {"
        ]

        for node in context.current_graph.get_nodes():
            dot_lines.append(f'    "{node.node_id}";')

        for edge in context.current_graph.get_edges():
            dot_lines.append(f'    "{edge.first_node.node_id}" -- "{edge.second_node.node_id}";')

        dot_lines.append("}")

        try:
            with open(filename, "w") as f:
                f.write("\n".join(dot_lines))
            print(f"DOT file generated: {filename}")
        except Exception as e:
            print(f"Failed to write DOT file: {e}")

    def __str__(self):
        return "Generate a DOT file for the current graph (for use in Gephi, Graphviz, etc.)"