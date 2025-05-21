from cli.commands.representation.display_representation_command import DisplayRepresentationCommand
from cli.commands.representation.count_edges_command import CountEdgesCommand
from cli.commands.representation.count_nodes_command import CountNodesCommand
from cli.commands.representation.has_simple_path_command import HasSimplePathCommand
from cli.commands.representation.node_degree_command import NodeDegreeCommand
from cli.commands.representation.nodes_degrees_command import NodesDegreesCommand
from cli.commands.representation.is_subgraph_command import IsSubgraphCommand
from cli.commands.representation.has_edge_command import HasEdgeCommand
from cli.commands.representation.has_cycle_command import HasCycleCommand

REPRESENTATION_COMMANDS = [
    CountEdgesCommand(),
    CountNodesCommand(),
    DisplayRepresentationCommand(),
    HasCycleCommand(),
    HasEdgeCommand(),
    HasSimplePathCommand(),
    IsSubgraphCommand(),
    NodeDegreeCommand(),
    NodesDegreesCommand()
]