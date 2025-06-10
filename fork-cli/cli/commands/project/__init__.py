from .create_graph_command import CreateGraphCommand
from .create_graph_from_dot import CreateGraphFromDotCommand
from .create_graph_from_intersection_command import CreateGraphFromIntersectionCommand
from .create_graph_from_json import CreateGraphFromJsonCommand
from .create_graph_from_symmetry_command import CreateGraphFromSymmetryCommand
from .create_graph_from_union_command import CreateGraphFromUnionCommand
from .delete_graph_command import DeleteGraphCommand
from .list_graphs_command import ListGraphsCommand
from .select_graph_command import SelectGraphCommand

PROJECT_COMMANDS = [
    CreateGraphCommand(),
    CreateGraphFromDotCommand(),
    CreateGraphFromIntersectionCommand(),
    CreateGraphFromJsonCommand(),
    CreateGraphFromSymmetryCommand(),
    CreateGraphFromUnionCommand(),
    DeleteGraphCommand(),
    ListGraphsCommand(),
    SelectGraphCommand(),
]