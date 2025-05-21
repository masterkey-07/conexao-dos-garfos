import os
from cli.command import Command
from config import FORK_PATH

class ListProjectsCommand(Command):
    def execute(self, context):
        if not os.path.isdir(FORK_PATH):
            print("No projects directory found.")
            return

        projects = [
            name for name in os.listdir(FORK_PATH)
            if os.path.isdir(os.path.join(FORK_PATH, name))
        ]

        if not projects:
            print("No projects found.")
            return

        print("Projects:")
        for project in projects:
            print(f"- {project}")

    def __str__(self):
        return "List all projects"