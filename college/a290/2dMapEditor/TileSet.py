class TileSet(object):
    """
    """
    
    def __init__(self, xml_tile_set=None):
        
        # COMEBACK: Remove loaded values.
        if xml_tile_set == None:
            self.tile_resources = dict()
            
            for i in range(24):
                self.tile_resources[i] = i
        # COMEBACK: Add xml file support. Rather image.* support.
        else:
            self.tile_resources = dict()
        
    def get_tile(self, tile_id):
        return self.tile_resources.get(tile_id)
    
    def get_tile_keys(self):
        return self.tile_resources.keys()