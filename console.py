#!/bin/env python3
import cmd

"""
Defines a class HBNBCommand
"""
class HBNBCommand(cmd.Cmd):
    """Alx Simple command processor"""

    prompt = '(hbnb)'
    intro = 'Welcome to Airbnb,how may I help you'

    def do_quit(self,line):
        """Quits the program"""
        quit()

    def do_greet(self,person):
        """Greets person"""
        print("Hi, "+ person)

    def do_EOF(self,line):
        return True
    
    def emptyline(self):
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
