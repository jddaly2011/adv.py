#!/usr/bin/python
import actions, world, items, npcs


class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory =[]
    def intro_text(self):
        raise NotImplementedError()

    def room_name(self):
        raise NotImplementedError()

    def list_items(self):
        for item in self.inventory:
            print item

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.DescribeItem())
#        moves.append(actions.DescribeAnItem(item=item))

        return moves

    def exits_text(self):
        """Returns all move actions for adjacent tiles."""
        exits = []
        if world.tile_exists(self.x + 1, self.y):
            exits.append("east")
        if world.tile_exists(self.x - 1, self.y):
            exits.append("west")
        if world.tile_exists(self.x, self.y - 1):
            exits.append("north")
        if world.tile_exists(self.x, self.y + 1):
            exits.append("south")
        if len(exits) == 1:
            print "\tYou may exit to the {}".format(exits[0])
        elif len(exits) == 2:
            print "\tThere are exits to the {} and {}".format(exits[0], exits[1])
        elif len(exits) == 3:
            print "\tThere are exits to the {}, {}, and {}".format(exits[0], exits[1], exits[2])
        else:
            print "\tThere are exits to the {}, {}, {}, and {}".format(exits[0], exits[1], exits[2], exits[3])
            

#        return exits


class NPCRoom(MapTile):
    def __init__(self, x, y, npc):
        self.npc = npc
        super(NPCRoom, self).__init__(x, y)
#        NPCRoom.__init__(x, y, npc)

    def describe_npc(self):
        raise NotImplementedError()
    
class CFOOffice(NPCRoom):
    def __init__(self, x, y):
        super(CFOOffice,self).__init__(x, y, npcs.CFO())
#       CFOOffice.__init__(x, y, npcs.CFO())
        self.inventory = [items.USB()]
        
    def intro_text(self):
        return """
        You are in a a CFO's office.
        A CFO is here
        """

    def describe_npc(self):
        return """
        You rudely start to examine the CFO, who is a large white rabbit wearing a top hat and waistcoat. He is muttering to himself something about being late and fretfully looking at a small gold pocket-watch.
        """


 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tThe CFO's office"



class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tStarting Room"

class ConfRoomNorth(MapTile):
    def __init__(self, x, y):
        super(ConfRoomNorth,self).__init__(x, y)
        self.inventory = [items.cake()]

    #self.inventory = [items.cake()]

    def intro_text(self):
        return """
        You are in a conference room. The lights flicker eerily. There is a whiteboard kere.
        You wonder how do paragraphs display.
        """

 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room North"


class ConfRoomNorth1(MapTile):
    def intro_text(self):
        return """
        A conference room. the lights are flickering and there is a case of water bottles here
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room North 1"
    

class ConfRoomNorth2(MapTile):
    def intro_text(self):
        return """
        An unremarkable conference room. There is a man on a screen looking at you.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Romm North 2"
    

class ConfRoom(MapTile):
    def intro_text(self):
        return """
        You are in another goddamn conference room
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tConference Room"
        


class Room(MapTile):
    def intro_text(self):
        return """
        You are in a room. A hideous room. 
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tRoom"""


class OfficeManagerOffice(MapTile):
    def intro_text(self):
        return """
        You are in the office manager's office.
        """

 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tOffice Manager's office"

class StorageCloset(MapTile):
    def intro_text(self):
        return """
        You are in a storage closet. There are stores here
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tStorage Closet"



class Hallway(MapTile):
    def intro_text(self):
        return """
        You are in an empty beige hallway. You feel empty inside.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tHallway"



class CIOOffice(MapTile):
    def intro_text(self):
        return """
        You are in the CIO's office
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tCIO's office"
 

class SmallKitchen(MapTile):
    def intro_text(self):
        return """
        You are in a wee kitchen
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tSmall Kitchen"

class CopierRoom(MapTile):
    def intro_text(self):
        return """
        You are in a copier room.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    def room_name(self):
        return "\t\tCopier Room"

class MensBathroom(MapTile):
    def intro_text(self):
        return """
        You are in a filthy mens room
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tMens Bathroom"

class MensStall(MapTile):
    def intro_text(self):
        return """
        You are in a bathroom stall. There is graffiti on the walls.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
    def room_name(self):
        return "\t\tBathroom Stall"

class MensUrinal(MapTile):
    def intro_text(self):
        return """
        This is a men's unrinal.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    def room_name(self):
        return "\t\tMens Urinal"

