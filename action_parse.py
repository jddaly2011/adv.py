import cmd
import world, tiles, items
from player import Player
from helpa import helpa


def action_parser(action_input, available_actions, player, room):
   # if  isinstance(room, (tiles.LockedDoorRoom)) and room.solved:
   #    available_actions = room.available_actions()
   #    room.exits_text()


   room.moves = room.moves + 1
#   room.mydefault()
   if action_input == "i":
       player.print_inventory()
       return
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
         room.mydefault()
         return

   else:
      room.mydefault()

      with open("commands", "r") as f:
         valid_commands = f.read()
         f.close()
         valid_commands = valid_commands.split("\n")
         valid_commands = filter(None, valid_commands)
         

      commands = action_input.split()
      if commands[0] not in valid_commands:
         print "\tI do not understand {}".format(action_input)
         return

      with open("things", "r") as f:
         things = f.read()
         f.close()
         things = things.split("\n")
         things = filter(None, things)

      if commands[0] == "examine" and len(commands) < 2:
         print "\tUsage: examine [item]"
         return

      if commands[0] == "examine" and player.inventory is not None and commands[1] in things:
         for item in player.inventory:
            if commands[1] in item.shortnames:
               player.describe_an_item(item)
               return
         else:
            print "\tYou do not have {}".format(commands[1])
            return
      
      if commands[0] == "examine" and len(commands) > 1:
         print "\tIt is a {}".format(commands[1])
         return
         

      if commands[0] == "npc" and isinstance(room, (tiles.NPCRoom)):
        print room.describe_npc()

      if commands[0] == "help":
         print "\tfetching help"
         helpa()


      if commands[0] == "look":
         print "\t{}".format(room.intro_text())
         room.intro_text()
         if room.inventory is not None:
            for item in room.inventory:
               print "\t{} is here.".format(item.name)
         room.exits_text()      


      if commands[0] == "take" and len(commands) < 2:
         print "\tUsage: take [item]"

      else:
         if commands[0] == "take":
            if room.inventory is None:
               print "\tThere is nothing to take!"

            if room.inventory is not None:
               for item in room.inventory:
                  if commands[1] in item.shortnames:
                     player.inventory.append(item)
                     print "\t{} taken".format(item.shortnames[0])
                     room.inventory.remove(item)

      if commands[0] == "drop" and len(commands) < 2:
         print "\tUsage: drop [item]"

      else:
         if commands[0] == "drop":
            if player.inventory is None:
               print "There is nothing to drop!"

            if player.inventory is not None:
               for item in player.inventory:
                  if commands[1] in item.shortnames:
                     player.inventory.remove(item)
                     print "\t{} dropped".format(item.shortnames[0])
                     room.inventory.append(item)


      if commands[0] == 'wear':
         print '\tOK, wearing badge'
         # badge = True
         # print "badge is {}".format(badge)
         if  isinstance(room, (tiles.LockedDoorRoom)):
            print "\tThe receptionist unlocks the door"
            room.solved = True
            available_actions = room.available_actions()
            room.exits_text()
         else:
            for x in range (100):
               for y in range (100):
                  if isinstance(world.tile_exists(x, y), tiles.Reception):
                     world.tile_exists(x,y).solved = True
                     print x, y, "exists"
                     

   
#            room.Solved()
#            room = world.tile_exists(player.location_x, player.location_y-1)


            # else:
        #         print "you cannot take {}!".format(commands[1])
        # # else:
        #     print "\tNot Found!!!"
