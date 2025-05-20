from cli.commands.graph.add_edge_command import AddEdgeCommand
from cli.commands.graph.remove_edge_command import RemoveEdgeCommand
from cli.commands.graph.remove_node_command import RemoveNodeCommand
from cli.commands.graph.add_node_command import AddNodeCommand
from cli.commands.graph.select_representation_command import SelectRepresentationCommand

GRAPH_COMMANDS = [AddEdgeCommand(), AddNodeCommand(), SelectRepresentationCommand(), RemoveEdgeCommand(), RemoveNodeCommand()]