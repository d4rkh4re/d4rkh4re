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

    def add_tile(self, tile_key, tile_value):
        self.tile_resources[tile_key] = tile_value

    def set_tile_resources(self, photoimage):
        self.photoimage_tileset = PhotoImage(file=self.get_tileset_location())

        self.add_tile(0, self.subimage(self.photoimage_tileset, 32, 0, 63, 32))
        self.add_tile(1, self.subimage(self.photoimage_tileset, 0, 0, 32, 32))
        
    def get_tile(self, tile_id):
        return self.tile_resources.get(tile_id)
    
    def get_tile_keys(self):
        return self.tile_resources.keys()

    def get_tileset_location(self):
        return self.tileset_location

    def subimage(self, src, l, t, r, b):
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
        return dst
