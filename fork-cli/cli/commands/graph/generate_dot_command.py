from cli.command import Command

class GenerateDotCommand(Command):
    @property
    def symbol(self) -> str:
        return "gd"

    def execute(self, context, args):
        if not hasattr(context, "current_graph") or context.current_graph is None:
            print("No graph selected. Please select a graph first.")
            return

        filename = args[0] if args else f"{context.current_graph.name}.dot"

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
        return "gd [filename] - Generate a DOT file for the current graph (for use in Gephi, Graphviz, etc.)"