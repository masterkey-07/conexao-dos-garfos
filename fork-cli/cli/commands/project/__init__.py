from .create_graph_command import CreateGraphCommand
from .create_graph_from_json import CreateGraphFromJsonCommand
from .create_graph_from_dot import CreateGraphFromDotCommand
from .delete_graph_command import DeleteGraphCommand
from .select_graph_command import SelectGraphCommand
from .list_graphs_command import ListGraphsCommand

PROJECT_COMMANDS = [
    CreateGraphCommand(),
    CreateGraphFromDotCommand(),
    CreateGraphFromJsonCommand(),
    DeleteGraphCommand(),
    ListGraphsCommand(),
    SelectGraphCommand(),
]