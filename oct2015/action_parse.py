import cmd
import world, tiles, items
from player import Player
from helpa import helpa


def action_parser(action_input, available_actions, player, room):
   directions = ['n','s','e','w']
   valid = []
   for action in available_actions:
      valid.append(action.hotkey)
   if action_input in directions:
      if action_input in valid:
         for action in available_actions:
            if action_input == action.hotkey:
               player.do_action(action, **action.kwargs)

      else:
         print "\tYou walk into a wall."
   else:
      commands = action_input.split()
      if commands[0] == "examine" and player.inventory is not None:
        for item in player.inventory:
    #                if commands[1] in item.description:
           if commands[1] in item.shortnames:
              player.describe_an_item(item)
      if commands[0] == "npc" and isinstance(room, (tiles.NPCRoom)):
        print room.describe_npc()
    #            player.describe_npc("CFO")
      if commands[0] == "help":
         print "\tfetching help"
         helpa()

      if commands[0] == "look":
         print "\t{}".format(room.intro_text())
         if room.inventory is not None:
            for item in room.inventory:
               print "\t{} is here.".format(item.name)
         room.exits_text()      


      if commands[0] == "take" and len(commands) < 2:
         print "\tUsage: take [item]"

      else:
         if commands[0] == "take":
            if room.inventory is None:
               print "There is nothing to take!"

            if room.inventory is not None:
               for item in room.inventory:
                  if commands[1] in item.shortnames:
                     player.inventory.append(item)
                     print "\t{} taken".format(item.name)
                     room.inventory.remove(item)

            # else:
        #         print "you cannot take {}!".format(commands[1])
        # # else:
        #     print "\tNot Found!!!"
