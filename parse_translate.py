#!/usr/bin/python

import re
import sys
def parse_translate(action_input):
   action_input = action_input.strip()
   action_input = action_input.lower()
   
   if action_input == "l":
      action_input="look"
   if action_input == "q":
      action_input="quit"

   
#   print "input is |{}|".format(action_input)
   action_input = re.sub("  ", " ", action_input)
   if action_input == "":
      action_input = "?"
      print "\tExcuse me?"
   if action_input == "quit":
      sys.exit()


   action_input = re.sub("^$", " ", action_input)
   action_input = re.sub("^move ", "", action_input)
   action_input = re.sub("north", "n", action_input)
   action_input = re.sub("south", "s", action_input)
   action_input = re.sub("east", "e", action_input)
   action_input = re.sub("west", "w", action_input)
   action_input = re.sub("look at ", "examine ", action_input)



   with open("commands", "r") as f:
     valid_commands = f.read()
     f.close()
     valid_commands = valid_commands.split("\n")
     valid_commands = filter(None, valid_commands)


     commands = action_input.split()
     if commands[0] not in valid_commands:
        print "\tI do not understand {}".format(action_input)
        return "ERROR"


   
   return action_input
