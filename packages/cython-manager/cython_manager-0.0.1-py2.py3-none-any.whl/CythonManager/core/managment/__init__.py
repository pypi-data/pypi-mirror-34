import sys
from .commands.build import build

class ManageUtil:
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def execute(self):
        subcommand = self.argv[1]

        if subcommand == 'build':
            build()



def execute_from_command_line(argv=None):
    util = ManageUtil(argv)
    util.execute()
