#!/usr/bin/python3
"""Defines the AirBnB command interpreter."""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter class.

    This class handles both interactive and non-interactive modes
    of the AirBnB clone command interpreter.
    """

    prompt = '(hbnb) ' if sys.stdin.isatty() else ''

    def emptyline(self):
        """Do nothing when receiving empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program.
        
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program.
        
        Usage: Ctrl+D (Unix) or Ctrl+Z (Windows)
        """
        print()
        return True

    def do_help(self, arg):
        """Show help documentation.
        
        Usage: help [command]
        """
        super().do_help(arg)

    def default(self, line):
        """Handle unknown commands.
        
        Args:
            line: The input command line
        """
        print(f"*** Unknown syntax: {line}")

    def postcmd(self, stop, line):
        """Execute after command processing.
        
        Args:
            stop: Flag indicating if command loop should stop
            line: The input command line
        Returns:
            bool: Whether to stop the command loop
        """
        if not sys.stdin.isatty():
            print(self.prompt, end='')
        return stop


if __name__ == '__main__':
    HBNBCommand().cmdloop()
