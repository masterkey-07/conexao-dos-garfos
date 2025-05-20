import os
from config import FORK_PATH
from cli.command import Command
from cli.project import Project
from cli.commander import Commander
from cli.commands.project import PROJECT_COMMANDS
from cli.context import Context

class SelectProjectCommand(Command):
    @property
    def symbol(self) -> str:
        return "sp"

    def execute(self, context, args):
        if not args:
            print("Usage: sp <project_name>")
            return

        project_name = args[0]

        project_path = os.path.abspath(os.path.join(FORK_PATH, project_name))

        if not os.path.isdir(project_path):
            print(f"Project '{project_name}' does not exist at {project_path}")
            return

        try:
            project = Project(project_name)
        except Exception as e:
            print(f"Could not load project '{project_name}': {e}")
            return

        print(f"Project '{project_name}' selected at {project.folder_path}")
        # Create a new context with the selected project
        new_context = Context()
        new_context.current_project = project

        # Start a new Commander session for the selected project
        commander = Commander(commands=PROJECT_COMMANDS, context=new_context, context_name=project_name + ">")
        commander.run()

        print(f"Exited project '{project_name}'")

    def __str__(self):
        return "sp <project_name> - Select and work on a project"