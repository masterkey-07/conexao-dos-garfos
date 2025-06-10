import os
import tempfile
from cli.project import Project
from cli.commands.project.create_graph_from_dot import CreateGraphFromDotCommand

class DummyContext:
    def __init__(self, project):
        self.current_project = project

def test_create_graph_from_dot_command(monkeypatch):
    dot_content = """
    graph G {
        A -- B [label="a"];
        B -- C [label="a"];
        C -- A [label="a"];
        D [label="a"];
    }
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        dot_path = os.path.join(tmpdir, "test_graph.dot")

        monkeypatch.setattr("builtins.input", lambda _: dot_path)

        with open(dot_path, "w") as f:
            f.write(dot_content)

        # Create a dummy project in a temp directory
        project_name = "test_project"
        project_path = os.path.join(tmpdir, project_name)
        os.makedirs(project_path)
        project = Project(project_name=project_name)
        project.folder_path = project_path  # Override to use temp dir

        context = DummyContext(project)

        cmd = CreateGraphFromDotCommand()

        cmd.execute(context)

        # Check if the graph was created and saved
        graph = context.current_project.get_graph("test_graph")
        assert graph is not None
        assert set(node.node_id for node in graph.get_nodes()) == {"A", "B", "C", "D"}
        edge_nodes = {(e.first_node.node_id, e.second_node.node_id) for e in graph.get_edges()}
        assert ("A", "B") in edge_nodes or ("B", "A") in edge_nodes
        assert ("B", "C") in edge_nodes or ("C", "B") in edge_nodes
        assert ("C", "A") in edge_nodes or ("A", "C") in edge_nodes

        # Check if the file was saved
        saved_file = os.path.join(project_path, "test_graph.json")
        assert os.path.isfile(saved_file)