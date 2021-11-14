#!/usr/bin/python3
"""
Contains the entry point of the command interpreter for HBnB
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Define HBnB console
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit console"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit console"""
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
