"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson'
import world, tiles
from player import Player


def play():
    world.load_tiles()
    
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
#    print(room.tile_name())
#    print vars(room)
    print room.room_name()
    print room.intro_text()
    
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
#            print("Choose an action:\n")
            available_actions = room.available_actions()
            room.exits_text()
#            print exits
            for action in available_actions:
                 print(action)
#            print " "
            action_input = raw_input('\tWhat would you like to do? :')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
