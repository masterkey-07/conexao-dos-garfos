from os import system, name as os_name
from cli.context import Context
from cli.command import Command

class Commander:
    def __init__(self, context: Context, commands: list[Command]):
        self.__context = context
        self.__commands = {cmd.symbol: cmd for cmd in commands}

    def help(self):
        for cmd in self.__commands.values():
            print(cmd)

        print("clear - Clear console log")
        print("exit - Exit context")

    def execute(self, command: str, args: list[str] = []):
        cmd = self.__commands.get(command)
        
        if cmd:
            cmd.execute(self.__context, args)
        else:
            print(f"Unknown command: {command}")

    def run(self):
        while True:
            try:
                user_input = input("> ").strip()
                
                if user_input == "clear":
                    system("cls" if os_name == "nt" else "clear")
                    continue

                if not user_input:
                    continue

                parts = user_input.split()

                cmd_symbol = parts[0]

                args = parts[1:]

                if cmd_symbol in ("help", "h", "?"):
                    self.help()
                elif cmd_symbol == "exit":
                    break
                else:
                    self.execute(cmd_symbol, args)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                
                break
            except Exception as exception:
                print("Unexpected Error:", exception)