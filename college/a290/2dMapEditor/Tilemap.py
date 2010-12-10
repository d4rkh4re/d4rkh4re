###############################################################################
# Tilemap.py
# William C. Morris
# <d4rkh4re@gmail.com>
###############################################################################

import xml.dom.minidom

class Tilemap(object):
    def __init__(self, height=3, width=3, layers=1, tile_id=0, xml_tilemap=None):
        """
        Create a Tilemap object. If xml_tilemap is defined all other
        parameters are ignored and the object is created from source xml file.

        height: height in tiles of Tilemap
        width:  width in tiles of Tilemap.
        layers: number of layers in TileMap.
        texture_id: default texture fill for game map.
        texturemap: source xml file.
        """
        if xml_tilemap == None:
            self.height = height
            self.width = width
            self.layers = layers
            self.tile_map = [[tile_id for i in range(height*width)] \
                                for i in range(layers)]
            self.xml_tilemap = "default.xml"
        else:
            self.tile_map = list()
            self.parse_from_xml(xml_tilemap)
            self.xml_tilemap = xml_tilemap

    def get_filename(self): 
        return self.xml_tilemap

    def get_tile(self, layer, x, y):
        """
        Returns the tile id at layer, x, y for this Tilemap.

        layer: tile layer to edit.
        x: position of tile in the x coordinate
        y: position of tile in the y coordinate
        """
        # If layer, x, y in range set tile_id.
        if y < self.height and y >= 0 and x < self.width and x >= 0 \
           and layer < self.layers and layer >= 0:
            return self.tile_map[layer][y*self.height + x]
        else:
            return -1

    def edit_tile(self, layer, tile_id, x, y):
        """
        Edit the tile id at layer, x, y for this Tilemap.

        layer: Tile layer to edit.
        tile_id: New tile id of the tile at layer, x, y
        x: position of tile in the x coordinate
        y: position of tile in the y coordinate
        """        
        # If layer, x, y in range set tile_id.
        if y < self.height and y >= 0 and x < self.width and x >= 0 \
           and layer < self.layers and layer >= 0:
            self.tile_map[layer][y*self.height + x] = tile_id
            return True
        else:
            return False

    def parse_from_xml(self, tilemap_xml):
        """
        Create TileMap object from p_xml_tilemap.

        tilemap_xml: File path of xml file to read from

        Online Documentation:
        http://docs.python.org/release/3.0.1/library/xml.dom.minidom.html
        http://docs.python.org/dev/library/xml.dom.html
        """
        # Open xml file.
        f = open(tilemap_xml, "r")

        # Get xml data.
        xml_string = f.read()        
        dom = xml.dom.minidom.parseString(xml_string)

        # Get data stored in <tilemap> tags.
        # NOTE: There should only be one of these in the xml source file.
        tilemap_parameters = dom.getElementsByTagName("tilemap")
        for t in tilemap_parameters:
            self.layers = int(t.getAttribute("layers"))
            self.height = int(t.getAttribute("height"))
            self.width = int(t.getAttribute("width"))

        # Get data stored in <layer> tags.
        tilemap_layers = dom.getElementsByTagName("layer")
        for layer in tilemap_layers:
            self.tile_map.append( [int(c) for c in layer.childNodes[0].data if c != ' '])
        
        # Close xml file.
        f.close()

    def parse_to_xml(self, tilemap_xml=None):
        """
        Write tile id data stored in self.tile_map to tilemap_xml.

        tilemap_xml: File path of xml file to write to
        """
        # Create root xml Node object.
        doc = xml.dom.minidom.Document()

        # Create tilemap element and set attributes.
        tilemap = doc.createElement("tilemap")
        tilemap.setAttribute("height", str(self.height))
        tilemap.setAttribute("width", str(self.width))
        tilemap.setAttribute("layers", str(self.layers))

        # Add tilemap element to xml Node object.
        doc.appendChild(tilemap)

        # Create layer element(s).
        for layer in self.tile_map:
            map_layer = doc.createElement("layer")
            layer_string = self.list_to_str(layer)
            tile_representation = doc.createTextNode(layer_string)

            # Add tile_repersentation to map_layer Node object.
            map_layer.appendChild(tile_representation)
            # Add map_layer to tilemap Node object.
            tilemap.appendChild(map_layer)

        # Write xml data to tilemap_xml.
        if tilemap_xml == None:
            f = open(self.xml_tilemap, "w")
        else:
            self.xml_tilemap = tilemap_xml
            f = open(self.xml_tilemap, "w")
        doc.writexml(f, encoding="utf-8")
        print(self.xml_tilemap)

        f.close()

    def list_to_str(self, layer):
        """
        Take a list of tile id's and turn them into a string.
        """
        result = ""
        for char in layer:
            result += str(char) + " "
        return result
