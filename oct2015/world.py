_world = {}
# global starting_position
# starting_position = (0, 0)
 
def load_tiles():
    print "loading world..."
    """Parses a file that describes the world space into the _world object"""
    with open('newmap.txt', 'r') as f:
        rows = f.readlines()
        x_max = len(rows[0].split()) # Assumes all rows contain the same number of tabs
        for y in range(len(rows)):
            cols = rows[y].split()
            for x in range(x_max):
                tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
                if not tile_name:
                    print "NO TILE NAME"
                print x, y
                print tile_name
                if tile_name == "CFOOffice":
                    print "StartingRoom Found"
                    global starting_position
                    starting_position = (x, y)
                    
                _world[(x, y)] =  None if tile_name == '0' else getattr(__import__('tiles'), tile_name)(x, y)
                # print _world[(x,y)]
                # print "added"
        
def tile_exists(x, y):
    return _world.get((x, y))
