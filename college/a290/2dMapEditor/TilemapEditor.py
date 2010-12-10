###############################################################################
# TilemapEditor.py
# Jonathan M. Stout
# <jonstout@indiana.edu>
###############################################################################

from Tilemap import *
from Tileset import *

class TilemapEditor(object):
    """
    Contains all actions the user can make from GUI.
    """

    def __init__(self):
        """
        Creates a TileEditor.
        IMPORTANT: open_tilemap() and open_tileset() must both be called
        before close_tilemap, close_tileset(), and edit_tile() are used.
        """
        self.selected_layer = 0
        self.selected_texture_id = 0
        self.tilemap = Tilemap()
        self.tileset = None
        
    def get_layers(self):
        return self.tilemap.layers
    
    def get_tileset_keys(self):
        return self.tileset.get_tile_keys()

    def set_selected_layer(self, layer):
        """
        Sets self.selected_layer to layer.
        """
        self.selected_layer = layer

    def set_selected_texture_id(self, texture_id):
        """
        Sets selected_texture_id to @texture_id.
        """
        self.selected_texture_id = texture_id

    def get_selected_texture_id(self):
        """
        Returns selected texture_id.
        """
        return self.selected_texture_id

    def get_tilemap_data(self):
        """
        Returns 2d representation of underlying tilemap as tile ids.
        """
        return self.tilemap.texture_map

    def get_tileset_keys(self):
        """
        Returns a list of all tile keys.
        """
        return self.tileset.get_tileset_keys()

    def get_tileset_values(self):
        """
        Returns a list of all tile values.
        """
        if self.tileset == None:
            return list()
        else:
            return self.tileset.get_tileset_values()

    def get_tile_photoimage(self, layer, x, y):
        """
        Returns the PhotoImage mapped to tile_id.
        """
        if self.tileset == None:
            return PhotoImage()
        else:
            return self.tileset.get_tile(self.tilemap.get_tile(layer, x, y))

    def get_tilemap_height(self):
        """
        Returns height of tilemap.
        """
        return self.tilemap.height

    def get_tilemap_width(self):
        """
        Returns height of tilemap.
        """
        return self.tilemap.width

    def get_tile_width(self):
        """
        Returns the width of a tile in pixels.
        """
        if self.tileset == None:
            return 32
        else:
            return self.tileset.get_tile_width()

    def open_tilemap(self, h, w, l, t_id):
        """
        Creates a TileMap object from @xml_tilemap and sets selected_layer to
        zero.
        """
        self.selected_layer = 0
        self.tilemap = Tilemap(height=h, width=w, layers=l, tile_id=t_id)

    def save_tilemap(self, xml_tilemap=None):
        """
        Writes xml representation of tilemap to @xml_tilemap.
        """
        self.tilemap.parse_to_xml(xml_tilemap)

    def close_tilemap(self):
        """
        Assigns None to tilemap.
        """
        self.tilemap = Tilemap()

    def open_tileset(self, tileset_source, width, height, tile_width=32, tile_height=32):
        """
        Creates a TileSet object from @png_tileset and sets selected_texture_id
        to Zero.
        """
        self.selected_texture_id = 0
        self.tileset = Tileset(tileset_source, width, height, tile_width, tile_height)

    def close_tileset(self):
        """
        Assings None to tile_set.
        """
        self.tileset = None

    def edit_tile(self, x, y):
        """
        Edits replaces current texutre id at layer, x, y with selected_texture_id.
        """
        self.tilemap.edit_tile(self.selected_layer, self.selected_texture_id, x, y)
        