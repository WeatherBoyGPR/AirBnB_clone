#!/usr/bin/python3
"""
Contains the entry point of the command interpreter for HBnB
"""

import cmd
import shlex
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """
    Define HBnB console
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit console"""
        return True

    def do_EOF(self, args):
        """EOF signal to exit console"""
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def do_create(self, args):
        """Creates a new instance of class"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Print str representation of instance"""
        args = shlex.split(args)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
            """Deletes an instance based on the class and id"""
            args = shlex.split(args)
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] in classes:
                if len(args) > 1:
                    key = args[0] + "." + args[1]
                    if key in models.storage.all():
                        models.storage.all().pop(key)
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
