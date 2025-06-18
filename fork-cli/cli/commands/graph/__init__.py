from cli.commands.graph.add_edge_command import AddEdgeCommand
from cli.commands.graph.add_node_command import AddNodeCommand
from cli.commands.graph.find_hamiltonian_path_command import FindHamiltonianPathCommand
from cli.commands.graph.generate_dot_command import GenerateDotCommand
from cli.commands.graph.is_euler_command import IsEulerCommand
from cli.commands.graph.remove_edge_command import RemoveEdgeCommand
from cli.commands.graph.remove_node_command import RemoveNodeCommand
from cli.commands.graph.save_graph_command import SaveGraphCommand
from cli.commands.graph.select_representation_command import SelectRepresentationCommand

GRAPH_COMMANDS = [
    AddEdgeCommand(), 
    AddNodeCommand(), 
    FindHamiltonianPathCommand(),
    GenerateDotCommand(),
    IsEulerCommand(),
    RemoveEdgeCommand(), 
    RemoveNodeCommand(),
    SaveGraphCommand(),
    SelectRepresentationCommand(), 
]