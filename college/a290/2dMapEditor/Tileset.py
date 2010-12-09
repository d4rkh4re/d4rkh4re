###############################################################################
# Tileset.py
# Jonathan M. Stout
# <jonstout@indiana.edu>
###############################################################################

from tkinter import PhotoImage

class Tileset(object):    
    def __init__(self, tileset_source, width, height, \
                 tile_width, tile_height):
        """
        tileset_source: Image saved as a .gif containing tiles in Tileset
        tileset_width: Width of tiles in tileset_source
        tileset_height: Height of tiles in tileset_source
        tile_width: Width in pixels of each tile
        tile_height: Height in pixels of each tile
        """
        self.tileset_source = PhotoImage(file=tileset_source)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tileset = dict()
        self.tile_count = 0

        # Place each tile into self.tileset and assign an tile id to each.
        for i in range(height):
            for j in range(width):
                li_width = tile_width*j
                ti_height = tile_height*i
                ri_width = tile_width*(j+1)
                bi_height = tile_height*(i+1)
                self.tileset[self.tile_count] = self.subimage(self.tileset_source, li_width, ti_height, ri_width, bi_height)
                self.tile_count += 1
                
    def get_tile(self, tile_id):
        """
        Returns the PhotoImage from self.tileset with the key tile_key.

        tile_id: key used to reference PhotoImage value
        """
        return self.tileset.get(tile_id)
    
    def get_tile_width(self):
        """
        Returns the width of tiles in self.tileset in pixels.
        """
        return self.tile_width

    def get_tile_height(self):
        """
        Returns the height of tiles in self.tileset in pixels.
        """
        return self.tile_height

    def get_tileset_values(self):
        """
        Returns a list of all tile values.
        """
        return list(self.tileset.values())

    def get_tileset_keys(self):
        """
        Returns a list of all tile keys.
        """
        return self.tileset.keys()

    def subimage(self, src, l, t, r, b):
        """
        Returns a subimage of self.tileset_source.

        Source: http://tkinter.unpythonic.net/wiki/PhotoImage
        """
        dst = PhotoImage()
        dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
        return dst
