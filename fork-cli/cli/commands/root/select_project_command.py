import os
from config import FORK_PATH
from cli.command import Command
from cli.project import Project
from cli.commander import Commander
from cli.commands.project import PROJECT_COMMANDS
from cli.context import Context

class SelectProjectCommand(Command):
    def execute(self, context):
        project_name = input("project_name: ")

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

        new_context = Context()
        new_context.current_project = project

        context_name = "Project: " + project_name

        commander = Commander(commands=PROJECT_COMMANDS, context=new_context, context_name=context_name)
        commander.run()

        print(f"Exited project '{project_name}'")

    def __str__(self):
        return "Select and work on a project"