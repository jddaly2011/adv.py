import cmd
import world, tiles, items
from player import Player
from helpa import helpa
#from prompt import Prompt


from parse_translate import parse_translate # natural languiage to game speak




# for x in range(100):
#     print "\n"

def action_parser(action_input, available_actions, player, room):
    for action in available_actions:
        if action_input == action.hotkey:
            player.do_action(action, **action.kwargs)
            break
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
    


def play():
    world.load_tiles()
#    pcs = npcs()
    global player
    global room

    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    
#    print vars(room)
    print room.room_name()
    print room.intro_text()
    if room.inventory is not None:
         for item in room.inventory:
             print "\t{} is here.".format(item.name)

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
#            print("Choose an action:\n")
            global available_actions
            available_actions = room.available_actions()
#            print exits
            # for action in available_actions:
            #      print(action)
#           #  print " "
            # print room.room_name()
            # print room.intro_text()
            # if room.inventory is not None:
            #     for item in room.inventory:
            #         print "\t{} is here.".format(item.name)
            # room.exits_text()


            Prompt().cmdloop()
#            action_input = Prompt()
#            print action_input
#            action_input = Prompt()
            # action_input = raw_input('\tWhat would you like to do? :')
#            action_input = parse_translate(action_input)
#            print action_input
#            action_parser(action_input, available_actions, player, room)
            # for action in available_actions:
            #     if action_input == action.hotkey:
            #         player.do_action(action, **action.kwargs)
            #        break
            
        

    # def precmd(self, line):
    #     print 'precmd(%s)' % line
    #     return (line)


class Prompt(cmd.Cmd):
    """Simple command processor example."""
    prompt = '\t> '
            
    def default(self, line):
        action_input = parse_translate(line)
#            print action_input
        action_parser(action_input, available_actions, player, room)

#        print 'default(%s)' % line
        return line




if __name__ == "__main__":
    play()
