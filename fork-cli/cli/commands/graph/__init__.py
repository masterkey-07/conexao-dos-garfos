from cli.commands.graph.add_edge_command import AddEdgeCommand
from cli.commands.graph.remove_edge_command import RemoveEdgeCommand
from cli.commands.graph.remove_node_command import RemoveNodeCommand
from cli.commands.graph.add_node_command import AddNodeCommand
from cli.commands.graph.select_representation_command import SelectRepresentationCommand
from cli.commands.graph.generate_dot_command import GenerateDotCommand
from cli.commands.graph.save_graph_command import SaveGraphCommand

GRAPH_COMMANDS = [
    AddEdgeCommand(), 
    AddNodeCommand(), 
    GenerateDotCommand(),
    RemoveEdgeCommand(), 
    RemoveNodeCommand(),
    SaveGraphCommand(),
    SelectRepresentationCommand(), 
]