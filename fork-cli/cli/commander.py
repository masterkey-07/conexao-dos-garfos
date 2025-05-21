import readline
import atexit
from config import FORK_PATH
from cli.context import Context
from cli.command import Command
from os import system, name as os_name, path


HISTFILE = path.join(FORK_PATH, ".fork_cli_history")

try:
    readline.read_history_file(HISTFILE)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, HISTFILE)

class Commander:
    def __init__(self, context: Context, commands: list[Command], context_name:str = "fork>"):
        self.__context = context
        self._context_name = context_name
        self.__commands = {cmd.symbol: cmd for cmd in commands}

        self._symbols = list(self.__commands.keys()) + ["help", "exit", "clear"]
        readline.set_completer(self._completer)
        readline.parse_and_bind("tab: complete")

    def _completer(self, text, state):
        # Get the current input line
        line = readline.get_line_buffer()
        parts = line.strip().split()

        # If typing the command (first word)
        if len(parts) == 0 or (len(parts) == 1 and not line.endswith(' ')):
            options = [cmd for cmd in self._symbols if cmd.startswith(text)]
        else:
            # Typing an argument: find the command and ask it for completions
            cmd_symbol = parts[0]
            cmd = self.__commands.get(cmd_symbol)
            if cmd and hasattr(cmd, "completions"):
                # Pass context and current args to the command's completions method
                options = [c for c in cmd.completions(self.__context, parts[1:]) if c.startswith(text)]
            else:
                options = []
        if state < len(options):
            return options[state]
        return None

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
                user_input = input(self._context_name).strip()
                
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