import os
import shutil
from cli.command import Command
from config import FORK_PATH

class DeleteProjectCommand(Command):
    def execute(self, context):
        project_name = input("project_name: ")

        folder_path = os.path.abspath(os.path.join(FORK_PATH, project_name))

        if not os.path.isdir(folder_path):
            print(f"Project '{project_name}' does not exist at {folder_path}")
            return

        try:
            shutil.rmtree(folder_path)
            print(f"Project '{project_name}' deleted from {folder_path}")
        except Exception as e:
            print(f"Error deleting project: {e}")

    def __str__(self):
        return "Delete a project"