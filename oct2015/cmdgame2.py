import cmd
import world, tiles, items
from player import Player
from helpa import helpa
#from prompt import Prompt
from action_parse import action_parser

from parse_translate import parse_translate # natural languiage to game speak

    


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
    room.exits_text()         
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
#            print("Choose an action:\n")
            global available_actions
            available_actions = room.available_actions()
            Prompt().cmdloop()

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
