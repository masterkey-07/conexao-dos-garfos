from .create_graph_command import CreateGraphCommand
from .create_graph_from_dot import CreateGraphFromDotCommand
from .create_graph_from_intersection_command import CreateGraphFromIntersectionCommand
from .create_graph_from_difference_command import CreateGraphFromDifferenceCommand
from .create_graph_from_json import CreateGraphFromJsonCommand
from .create_graph_from_node_fusion import CreateGraphFromNodeFusionCommand
from .create_graph_from_node_fusion import CreateGraphFromNodeFusionCommand
from .create_graph_from_other_graph_by_removing_edge import CreateGraphFromOtherGraphByRemovingEdgeCommand
from .create_graph_from_other_graph_by_removing_node import CreateGraphFromOtherGraphByRemovingNodeCommand
from .create_graph_from_symmetry_command import CreateGraphFromSymmetryCommand
from .create_graph_from_union_command import CreateGraphFromUnionCommand
from .delete_graph_command import DeleteGraphCommand
from .list_graphs_command import ListGraphsCommand
from .select_graph_command import SelectGraphCommand

PROJECT_COMMANDS = [
    CreateGraphCommand(),
    CreateGraphFromDifferenceCommand(),
    CreateGraphFromDotCommand(),
    CreateGraphFromIntersectionCommand(),
    CreateGraphFromJsonCommand(),
    CreateGraphFromNodeFusionCommand(),
    CreateGraphFromOtherGraphByRemovingEdgeCommand(),
    CreateGraphFromOtherGraphByRemovingNodeCommand(),
    CreateGraphFromSymmetryCommand(),
    CreateGraphFromUnionCommand(),
    DeleteGraphCommand(),
    ListGraphsCommand(),
    SelectGraphCommand(),
]