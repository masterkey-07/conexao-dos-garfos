from cli.command import Command
from cli.project import Project

class CreateProjectCommand(Command):
    @property
    def symbol(self) -> str:
        return "cp"

    def execute(self, context, args):
        if not args:
            print("Usage: cp <project_name>")
            return

        project_name = args[0]

        project = Project(project_name)

        print(f"Project '{project_name}' created at {project.folder_path}")

        context.current_project = project

    def __str__(self):
        return "cp <project_name> - Create a new project"