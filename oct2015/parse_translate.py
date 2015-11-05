#!/usr/bin/python

import re
import sys
def parse_translate(action_input):
   action_input = action_input.strip()
   action_input = action_input.lower()
   
   if action_input == "l":
      action_input="look"
   
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

   
   return action_input
