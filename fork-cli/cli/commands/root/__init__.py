from cli.commands.root.create_project_command import CreateProjectCommand
from cli.commands.root.delete_project_command import DeleteProjectCommand
from cli.commands.root.list_projects_command import ListProjectsCommand
from cli.commands.root.select_project_command import SelectProjectCommand

ROOT_COMMANDS = [
    CreateProjectCommand(),
    DeleteProjectCommand(),
    ListProjectsCommand(),
    SelectProjectCommand(),
]