from tkinter import PhotoImage

class TileSet(object):
    """
    """
    
    def __init__(self, tileset_location=None):
        
        # COMEBACK: Remove loaded values.
        if tileset_location == None:
            self.tile_resources = dict()
            self.tileset_location = "tile0.gif"
            
            for i in range(5):
                self.tile_resources[i] = "tile" + str(i) + ".bmp"
        # COMEBACK: Add xml file support. Rather image.* support.
        else:
            self.tile_resources = dict()
            self.tileset_location = tileset_location

        
        
    def get_tile(self, tile_id):
        return self.tile_resources.get(tile_id)
    
    def get_tile_keys(self):
        return self.tile_resources.keys()

    def get_tileset_location(self):
        return self.tileset_location
