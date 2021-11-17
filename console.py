#!/usr/bin/python3
"""
Contains the entry point of the command interpreter for HBnB
"""

import cmd
import models
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
        args = models.split(args)
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
        args = models.split(arg)
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
<<<<<<< HEAD
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

    def do_update(self, args):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(args)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
=======
        """Deletes an instance based on the class and id"""
        args = models.split(args)
>>>>>>> 607f56ddf8031ec5e6d0c8ce2328d9f835dc6b5f
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
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
        models.storage.reload()
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
            elif len(load) < 4:
                print("** value missing **")
                return
            else:
                key = (load[0] + "." + load[1])
                try:
                    objs[key].__dict__[load[2]] = load[3]
                    objs[key].__dict__[
                        "updated_at"] = datetime.now()
                    models.storage.save()
                except KeyError:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
