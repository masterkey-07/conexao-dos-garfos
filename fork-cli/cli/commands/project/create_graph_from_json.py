import os
import json
from cli.command import Command
from graph.core.graph import Graph

class CreateGraphFromJsonCommand(Command):
    @property
    def symbol(self) -> str:
        return "cgj"

    def execute(self, context):
        if not hasattr(context, "current_project") or context.current_project is None:
            print("No project selected. Please select a project first.")
            return

        json_file_path = input("json_file_path: ")

        if not os.path.isfile(json_file_path):
            print(f"JSON file '{json_file_path}' does not exist.")
            return

        try:
            with open(json_file_path, "r") as f:
                data = json.load(f)
            
            graph = Graph(name="temp", data=data)
            
            if context.current_project.get_graph(graph.name):
                print(f"Graph '{graph.name}' already exists in project '{context.current_project.project_name}'.")
                return
            
            context.current_project.save_graph(graph)
            
            print(f"Graph '{graph.name}' created from '{json_file_path}' in project '{context.current_project.project_name}'.")
        except Exception as e:
            print(f"Failed to create graph from JSON: {e}")

    def __str__(self):
        return "Create a new graph from a JSON file in the current project"