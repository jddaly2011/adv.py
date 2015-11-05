import world, tiles
from player import Player
from helpa import helpa


from parse_translate import parse_translate # natural languiage to game speak


for x in range(100):
    print "\n"

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

        # else:
        #     print "\tNot Found!!!"
    

def play():
    world.load_tiles()
#    pcs = npcs()
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
            # for action in available_actions:
            #      print(action)
#            print " "
            action_input = raw_input('\tWhat would you like to do? :')
            action_input = parse_translate(action_input)
#            print action_input
            action_parser(action_input, available_actions, player, room)
            # for action in available_actions:
            #     if action_input == action.hotkey:
            #         player.do_action(action, **action.kwargs)
            #        break
            

if __name__ == "__main__":
    play()
