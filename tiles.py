#!/usr/bin/python
import actions, world, items, npcs

global badge
badge = False

class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inventory =[]
        self.moves = 0

    def mydefault(self):
        raise NotImplementedError()

        
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
        myroom = world.tile_exists(self.x, self.y)
    
        if world.tile_exists(self.x + 1, self.y):
           moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
           # myroom= world.tile_exists(self.x + 1, self.y)
           # if type(myroom).__name__ == LockedNorth:
           #     pass
           # else:
           #     moves.append(actions.MoveNorth())

        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        
        # myroom = world.tile_exists(self.x, self.y)
        # if isinstance(myroom, LockedDoorRoom):
        #      print "door is locked"
        #      print myroom.door

        if isinstance(myroom, LockedDoorRoom) and not myroom.solved:
             for move in moves:
                if isinstance(move, actions.MoveNorth) and myroom.door == "north":
                    moves.remove(move)
                if isinstance(move, actions.MoveSouth) and myroom.door == "south":
                    moves.remove(move)
                if isinstance(move, actions.MoveEast) and myroom.door == "east":
                    moves.remove(move)
                if isinstance(move, actions.MoveWest) and myroom.door == "west":
                    moves.remove(move)
        

#        print moves
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

        myroom = world.tile_exists(self.x, self.y)
#        print myroom.room_name()
        if isinstance(myroom, LockedDoorRoom) and not myroom.solved:
             mydoor = myroom.door
             exits.remove(mydoor)
        

        if len(exits) == 1:
            print "\tThere is an exit to the {}".format(exits[0])
        elif len(exits) == 2:
            print "\tThere are exits to the {} and {}".format(exits[0], exits[1])
        elif len(exits) == 3:
            print "\tThere are exits to the {}, {}, and {}".format(exits[0], exits[1], exits[2])
        elif len(exits) == 4:
            print "\tThere are exits to the {}, {}, {}, and {}".format(exits[0], exits[1], exits[2], exits[3])
        else:
            if isinstance(myroom, Elevator):
                print "\tThe elevator door is closed"
                         
            else:
                print "\tThere appears to be no way out"
            

#        return exits


class NPCRoom(MapTile):
    def __init__(self, x, y, npc):
        self.npc = npc
        super(NPCRoom, self).__init__(x, y)

    def describe_npc(self):
        raise NotImplementedError()

    def mydefault(self):
        pass

   
class CFOOffice(NPCRoom):
    def __init__(self, x, y):
        super(CFOOffice,self).__init__(x, y, npcs.CFO())
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


class LockedDoorRoom(MapTile):
    def __init__(self, x, y):
        super(LockedDoorRoom, self).__init__(x, y)
        self.door = ""
    def return_exits(self):
        raise NotImplementedError()
        

class Reception(LockedDoorRoom):
    def __init__(self, x, y):
        super(Reception, self).__init__(x, y)
        self.solved = False 
        self.door = "north"
#        print self.moves

    def mydefault(self):
        print ""
    def intro_text(self):
        if self.solved:
            return """
        You are at Reception.
        There is a receptionist here 
        """
        else:
            return """
        You are at Reception.
        There is a receptionist here.
        There is locked door to the  north.
        """

            
    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tReception"


class Elevator(LockedDoorRoom):
    def __init__(self, x, y):
        super(Elevator,self).__init__(x, y)
        self.inventory = [items.id_badge()]
        self.solved = False 
        self.door = "north"

    #self.inventory = [items.cake()]

    def intro_text(self):
        if self.moves == 0:
            return """
            You find yourself in an elevator.It is acending
        """
        elif self.moves == 1:
            print "\tThe elevator is ascending. You notice a screen on the wall. It says '65% of NPCs read this screen'"
        elif self.moves == 2:
            print "\tThe elevator is slowing."

        elif self.moves == 3:
            print "\tThe elevator comes to a stop and the door opens."
        else:    
            return """
            You are in an elevator. There is a button and a keyhole.
        """


    def modify_player(self, player):
        #Room has no action on player
        pass

    def room_name(self):
        return "\t\tElevator"

    def mydefault(self):

        if self.moves == 0:
            print "\tYou are in an elevator. The elevator is ascending"

        if self.moves == 1:
            print "\tThe elevator is ascending. You notice a screen on the wall. It says '65% of NPCs read this screen'"
        if self.moves == 2:
            print "\tThe elevator is slowing."

        if self.moves == 3:
            self.solved=True
            print "\tThe elevator comes to a stop and the door opens."
            available_actions = self.available_actions()
            self.exits_text()




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

    def mydefault(self):
        pass



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
    def mydefault(self):
        pass
    

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
    
    def mydefault(self):
        pass

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
        
    def mydefault(self):
        pass


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

    def mydefault(self):
        pass


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
    def mydefault(self):
        pass

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

    def mydefault(self):
        pass


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
    def mydefault(self):
        pass



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
 
    def mydefault(self):
        pass

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

    def mydefault(self):
        pass

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

    def mydefault(self):
        pass

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


    def mydefault(self):
        pass


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

    def mydefault(self):
        pass



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

    def mydefault(self):
        pass
