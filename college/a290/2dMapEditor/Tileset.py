###############################################################################
# Tileset.py
# William C. Morris
# <d4rkh4re@gmail.com>
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
        self.tileset = dict()
        self.tile_count = 0

        for i in range(height):
            for j in range(width):
                li_width = tile_width*j
                ti_height = tile_height*i
                ri_width = tile_width*(j+1)
                bi_height = tile_height*(i+1)
                self.tileset[self.tile_count] = self.subimage(self.tileset_source, li_width, ti_height, ri_width, bi_height)
                self.tile_count += 1
                
    def get_tile(self, tile_key):
        """
        Returns the PhotoImage from self.tileset with the key tile_key.
        """
        return self.tileset.get(tile_key)
    
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
