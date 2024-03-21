#!/usr/bin/python3
"""This is a console module. The entry point of the command interpreter"""

import cmd
import re
import json
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""

    prompt = "(hbnb) "

    def default(self, line):
        """Picks up unrecognized commands"""
        self.pre_cmd(line)

    def pre_cmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        same = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not same:
            return line
        name = same.group(1)
        method = same.group(2)
        args = same.group(3)

        same_id_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if same_id_args:
            uid = same_id_args.group(1)
            one_or_dict = same_id_args.group(2)
        else:
            uid = args
            one_or_dict = False

        one_and_value = ""
        if method == "update" and one_or_dict:
            same_dict = re.search('^({.*})$',one_or_dict)
            if same_dict:
                self.update_dict(name, uid, same_dict.group(1))
                return ""
            same_one_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$', one_or_dict)
            if same_one_and_value:
                one_and_value = (same_one_and_value.group(
                    1) or "") + " " + (same_one_and_value.group(2) or "")
                command = method + " " + name + " " + uid + one_and_value
                self.onecmd(command)
                return command
            
            def dict_update(self, classname, uid, s_dict):
                """These are method's helpers for update() with a dictionary"""
                str = s_dict.replace("'", '"')
                dict = json.loads(str)
                if not classname:
                    print("** class name missing **")
                elif classname not in storage.classes():
                    print("** class doesn't exist **")
                elif uid is None:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(classname, uid)
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        ch = storage.attributes()[classname]
                        for attribute, value in dict.items():
                            if attribute in ch:
                                value = ch[attribute](value)
                            setattr(storage.all()[key], attribute, value)
                        storage.all()[key].save()

            def emptyline(self):
                """This makes the enter key do nothing"""
                pass

            def do_create(self, line):
                """This creates an instance"""
                if line == "" or line is None:
                    print("** class name missing **")
                elif line not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    store = storage.classes()[line]()
                    store.save()
                    print(store.id)

            def do_show(self, line):
                """Prints the official string rep of an instance"""

                if line == "" or line is None:
                    print("** class name missing **")
                else:
                    lines = line.split(' ')
                    if lines[0] not in storage.classes():
                        print("** class doesn't exist **")
                    elif len(lines) < 2:
                        print("** instance id missing **")
                    else:
                        key = "{}.{}".format(lines[0], lines[1])
                        if key not in storage.all():
                            print("** no instance found **")
                        else:
                            print(storage.all()[key])

            def do_EOF(self, line):
                """This handles the End Of File character"""
                print()
                return True
            
            def do_quit(self, line):
                """This helps exit the program"""
                return True

            def do_destroy(Self, line):
                """This deletes, using class name and id, an instance"""
                if line == "" or line is None:
                    print("** class name missing **")
                else:
                    lines = line.split(' ')
                    if lines[0] not in storage.classes():
                        print("** class doesn't exist **")
                    elif len(lines) < 2:
                        print("** instance id missing **")
                    else:
                        key = "{}.{}".format(lines[0], lines[1])
                        if key not in storage.all():
                            print("** no instance found **")
                        else:
                            del storage.all()[key]
                            storage.save()

            def do_all(self, line):
                """This prints every official string rep"""

                if line != "":
                    lines = line.split(' ')
                    if lines[0] not in storage.classes():
                        print("** class doesn't exist **")
                    else:
                        rep = [str(obj) for key, obj in storage.all().items()
                               if type(obj).__name__ == lines[0]]
                        print(rep)
                else:
                    new = [str(obj) for key, obj in storage.all().items()]
                    print(new)

            def do_count(self, line):
                """This counts the instance of a class"""
                lines = line.split(' ')
                if not lines[0]:
                    print("** class name is missing **")
                elif lines[0] not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    same = [
                        a for a in storage.all() if a.startswith(
                            lines[0] + '.')]
                    print(len(same))

                def do_update(Self, line):
                    """This removes or adds attributes to an instance"""
                    if line == "" or line is None:
                        print("** class name missing **")
                        return
                    
                    rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
                    same = re.search(rex, line)
                    classname = same.group(1)
                    uid = same.group(2)
                    attribute = same.group(3)
                    value = same.group(4)
                    if not same:
                        print("** class name missing **")
                    elif classname not in storage.classes():
                        print("** class doesn't exist **")
                    elif uid is None:
                        print("** instance id missing **")
                    else:
                        key = "{}.{}".format(classname, uid)
                        if key not in storage.all():
                            print("** no instance found **")
                        elif not attribute:
                            print("** attribute name missing **")
                        elif not value:
                            print("** value missing **")
                        else:
                            cast = None
                            if not re.search('^".*"$', value):
                                if '.' in value:
                                    cast = float
                                else:
                                    cast = int
                            else:
                                value = value.replace('"', '')
                            attributes = storage.attributes()[classname]
                            if attribute in attributes:
                                value = attributes[attribute](value)
                            elif cast:
                                try:
                                    value = cast(value)
                                except ValueError:
                                    pass  # fine, stay a string then
                            setattr(storage.all()[key], attribute, value)
                            storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
