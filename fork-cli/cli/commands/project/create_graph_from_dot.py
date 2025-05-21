import os
from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromDotCommand(Command):
    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        dot_file_path = input("dot_file_path: ")

        if not os.path.isfile(dot_file_path):
            print(f"DOT file '{dot_file_path}' does not exist.")
            return

        try:
            with open(dot_file_path, "r") as f:
                lines = f.readlines()

            nodes = set()
            edges = []
            for line in lines:
                line = line.strip()
                if line.startswith("graph") or line == "{" or line == "}":
                    continue
                
                try:
                    i = line.index("[")
                    line = line[:i].strip()
                except:
                    pass

                if "--" in line:
                    parts = line.replace(";", "").replace('"', '').split("--")
                    first_node = parts[0].strip()
                    second_node = parts[1].strip()
                    nodes.add(first_node)
                    nodes.add(second_node)
                    edges.append({"first_node": first_node, "second_node": second_node, "properties": {}})
                elif line:
                    node = line.replace(";", "").replace('"', '').strip()
                    nodes.add(node)

            graph_name = os.path.splitext(os.path.basename(dot_file_path))[0]
            data = {
                "name": graph_name,
                "nodes": [{"id": n, "properties": {}} for n in nodes],
                "edges": edges
            }

            graph = Graph(name=graph_name, data=data)

            if context.current_project.get_graph(graph.name):
                print(f"Graph '{graph.name}' already exists in project '{context.current_project.project_name}'.")
                return

            context.current_project.save_graph(graph)
            print(f"Graph '{graph.name}' created from '{dot_file_path}' in project '{context.current_project.project_name}'.")
        except Exception as e:
            print(f"Failed to create graph from DOT: {e}")

    def __str__(self):
        return "Create a new graph from a DOT file in the current project"