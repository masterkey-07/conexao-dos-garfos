from os import system, name as os_name
from cli.context import Context
from cli.command import Command

class Commander:
    def __init__(self, context: Context, commands: list[Command], context_name:str = "fork>"):
        self.__context = context
        self._context_name = context_name
        self.__commands = {str(index + 1): cmd for index, cmd in enumerate(commands)}
    
    def _help(self):
        self._clear_log()

        print(self._context_name, "\n")

        print("Available commands:")

        for key in self.__commands.keys():
            print('\t', key, '-' , self.__commands[key])

        print("\t help - Display available commands")
        print("\t clear - Clear console log")
        print("\t exit - Exit context")
        print()

    def _execute(self, command_index: str):
        command = self.__commands.get(command_index)
        
        if command:
            self._help()
            print("Selected Command:", command_index, '-', command, "\n")
            command.execute(self.__context)
            print()
        else:
            print(f"Unknown command: {command_index}")

    def _clear_log(self):
        system("cls" if os_name == "nt" else "clear")

    def run(self):

        self._help()
        while True:
            try:
                command_index = input("command: ").strip()
                
                if command_index == "clear":
                    self._clear_log()
                    continue

                if not command_index:
                    continue

                if command_index == "help":
                    self._help()
                elif command_index == "exit":
                    break
                else:
                    self._execute(command_index)
            except (KeyboardInterrupt, EOFError):
                self._help()
                break
            except Exception as exception:
                print("Unexpected Error:", exception)