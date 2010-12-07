from TileMap import *
from TileSet import *

class TileMapEditor(object):
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
        
    def get_layers(self):
        return self.tile_map.layers
    
    def get_tileset_keys(self):
        return self.tile_set.get_tile_keys()

    def set_selected_layer(self, layer):
        """
        Sets selected_layer to @layer.
        """
        self.selected_layer = layer

    def get_selected_layer(self):
        """
        Returns selected_layer.
        """
        return self.selected_layer
    
    def set_selected_texture_id(self, texture_id):
        """
        Sets selected_texture_id to @texture_id.
        """
        self.selected_texture_id = texture_id

    def get_selected_texture_id(self):
        """
        Returns selected_texture_id.
        """
        return self.selected_texture_id

    def get_tilemap_data(self):
        """
        Returns 2d representation of underlying texture map found in tile_map.
        """
        return self.tile_map.texture_map

    def get_tilemap_height(self):
        """
        Returns height of tile_map.
        """
        return self.tile_map.height

    def get_tilemap_width(self):
        """
        Returns height of tile_map.
        """
        return self.tile_map.width

    def open_tilemap(self, xml_tilemap):
        """
        Creates a TileMap object from @xml_tilemap and sets selected_layer to
        zero.
        """
        self.selected_layer = 0
        self.tile_map = TileMap(xml_tilemap=xml_tilemap)

    def save_tilemap(self, xml_tilemap):
        """
        Writes xml representation of tile_map to @xml_tilemap.
        """
        self.tile_map.parse_to_xml(xml_tilemap)

    def close_tilemap(self):
        """
        Assigns None to tile_map.
        """
        self.tile_map = None

    def open_tileset(self, tileset_source, width, height, tile_width=32, tile_height=32):
        """
        Creates a TileSet object from @png_tileset and sets selected_texture_id
        to Zero.
        """
        self.selected_texture_id = 0
        self.tile_set = Tileset(tileset_source, width, height, tile_width, tile_height)

    def close_tileset(self):
        """
        Assings None to tile_set.
        """
        self.tile_set = TileSet()

    def edit_tile(self, x, y):
        """
        Edits replaces current texutre id at layer, x, y with selected_texture_id.
        """
        self.tile_map.edit_tile(self.get_selected_layer(), self.get_selected_texture_id(), x, y)
        