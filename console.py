#!/usr/bin/python3
"""Defines the AirBnB command interpreter."""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter class."""

    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_quit(self, arg):
        """Exit the program.
                Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D).
                Usage: Ctrl+D
        """
        print()
        return True

    def do_help(self, arg):
        """Show help documentation.
            Usage: help [command]
        """
        if not arg:
            # Show all commands when no argument is given
            print("Documented commands (type help <topic>):")
            print("=" * 40)  # Consistent separator line
            commands = [name[3:] for name in self.get_names() 
                       if name.startswith('do_')]
            print("\n".join(sorted(commands)))
        else:
             # Show specific command help
            super().do_help(arg)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
