from cli.command import Command
from cli.project import Project

class CreateProjectCommand(Command):
    def execute(self, context):
        project_name = input("project_name: ")

        project = Project(project_name)

        print(f"Project '{project_name}' created at {project.folder_path}")

        context.current_project = project

    def __str__(self):
        return "Create a new project"