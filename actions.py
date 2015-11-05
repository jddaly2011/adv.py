from player import Player
import world, tiles, items
 
class Action(object):
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        Action.__init__(self, method=Player.move_north, name='Move north', hotkey='n')
 
 
class MoveSouth(Action):
    def __init__(self):
        Action.__init__(self, method=Player.move_south, name='Move south', hotkey='s')
 
 
class MoveEast(Action):
    def __init__(self):
        Action.__init__(self, method=Player.move_east, name='Move east', hotkey='e')
 
 
class MoveWest(Action):
    def __init__(self):
        Action.__init__(self, method=Player.move_west, name='Move west', hotkey='w')
 
 
class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super(ViewInventory, self).__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class DescribeItem(Action):
    """Describe Item"""
    def __init__(self):
        super(DescribeItem, self).__init__(method=Player.describe_item, name='Describe item', hotkey='d')

class DescribeAnItem(Action):
    """Describe Item"""
    def __init__(self, item):
        super(DescribeAnItem, self).__init__(method=Player.describe_an_item, name='Describe an item', hotkey="d", item=item)








# class Attack(Action):
#     def __init__(self, enemy):
#         super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)
