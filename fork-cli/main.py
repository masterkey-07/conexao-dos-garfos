from cli.commands.root import ROOT_COMMANDS

from os import path, mkdir
from config import FORK_PATH
from cli.commander import Commander
from cli.context import Context

if not path.exists(FORK_PATH):
    mkdir(FORK_PATH)

commander = Commander(commands=ROOT_COMMANDS, context=Context())

commander.run()