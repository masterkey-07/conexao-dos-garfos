import os
import json
from config import FORK_PATH
from graph.core.graph import Graph

class Project:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.folder_path = os.path.abspath(os.path.join(FORK_PATH, project_name))

        self.graphs = {}  

        self._load_graphs()

    def _load_graphs(self):
        if not os.path.isdir(self.folder_path):
            os.makedirs(self.folder_path)

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".json"):
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, "r") as f:
                    data = json.load(f)
                    graph_name = os.path.splitext(filename)[0]
                    self.graphs[filename.replace(".json", "")] = Graph(name=graph_name, data=data)

    def save_graph(self, graph: Graph):
        file_path = os.path.join(self.folder_path, graph.name + ".json")

        with open(file_path, "w") as f:
            json.dump(graph.to_dict(), f, indent=2)

        self.graphs[graph.name] = graph

    def get_graph(self, name: str) -> Graph:
        return self.graphs.get(name)

    def list_graphs(self):
        return list(self.graphs.keys())