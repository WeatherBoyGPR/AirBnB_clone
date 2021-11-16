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
    Define HBnB console:
    Class contains command interpreter's entry point
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

    
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        str_list = []
        objs = models.storage.reload.all()
        try:
            if len(args) != 0:
                eval(args)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return

        args.strip()
        for key, value in objs.items():
            if len(args) != 0:
                if type(value) is eval(args):
                    value = str(objs[key])
                    str_list.append(value)
            else:
                value = str(objs[key])
                str_list.append(value)

        print(str_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        load = args.split()
        objs = models.storage.all()

        if len(load) == 0:  # If the class name is missing
            print("** class name missing **")
            return
        if load[0] in model.classes:
            if len(load) < 2:  # If the id is missing
                print("** instance id missing **")
                return
            elif len(load) <3:  # If the attribute name is missing
                print("** attribute name missing **")
                return



if __name__ == '__main__':
    HBNBCommand().cmdloop()
