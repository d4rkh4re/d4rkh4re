import xml.dom.minidom

class TileMap(object):

    def __init__(self, xml_tilemap):
        """
        Create a TextureMap object from <texturemap> specifications.
        p_texturemap: Source xml file.
        """
        map_data = parse_xml(xml_tilemap)

        self.height = map_data.height
        self.width = map_data.width
        self.layers = map_data.layers
        self.texture_map = map_data.texture_map

    def __init__(self, height, width, layers, texture_id):
        """
        Create a TextureMap object.
        p_height: Width of TextureMap.
        p_width: Height of TextureMap.
        p_layers: Number of layers in TileMap.
        p_texture_id: Default texture fill for game map.
        """
        self.height = height
        self.width = width
        self.layers = layers
        self.texture_map = [[texture_id for i in range(height*width)] \
                            for i in range(layers)]

    def edit_tile(self, layer, texture_id, x, y):
        """
        Edit texture_id of tile in self.texture_map at specified
        x and y coordinates. Returns True if successful.
        p_layer: Tile layer to edit.
        p_texture_id: Edit texture_id of tile.
        """
        
        """ If p_layer, p_x, and p_y in range set texture_id. """
        if x < self.width and x >= 0 and y < self.height and y >= 0 \
           and layer < self.layers and layer >= 0:
            self.texture_map[layer][x*self.width + y] = texture_id
            return True
        else:
            return False

    """
    TODO:
    """
    def parse_from_xml(self, xml_tilemap):
        """
        Create TileMap object from p_xml_tilemap.
        p_xml_tilemap: File path of xml file to read from.
        """
        
        f = open(xml_tilemap, "r")

        xml_string = f.read()
        
        dom = xml.dom.minidom.parseString(xml_string)

        tilemap_parameters = dom.getElementsByTagName("tilemap")

        for t in tilemap_parameters:
            self.layers = t.getAttribute("layers")
            self.height = t.getAttribute("height")
            self.width = t.getAttribute("width")

        tilemap_layers = dom.getElementsByTagName("layer")

        for layer in tilemap_layers:
            self.texture_map.append( [int(c) for c in layer.childNodes[0].data if c != ' '])
            
        f.close()
            
        """
        Documentation:
        http://docs.python.org/release/3.0.1/library/xml.dom.minidom.html
        http://docs.python.org/dev/library/xml.dom.html
        """

    def parse_to_xml(self, xml_tilemap):
        """
        Write self to p_xml_tilemap.
        p_xml_tilemap: File path of xml file to write to.
        """
        
        """ Create xml Node object. """
        doc = xml.dom.minidom.Document()

        """ Create tilemap element and set attributes. """
        tile_map = doc.createElement("tilemap")
        tile_map.setAttribute("height", str(self.height))
        tile_map.setAttribute("width", str(self.width))
        tile_map.setAttribute("layers", str(self.layers))

        """ Add tilemap element to xml Node object. """
        doc.appendChild(tile_map)

        """ Add layer element(s) to tile_map Node object. """
        for layer in self.texture_map:
            map_layer = doc.createElement("layer")
            layer_string = self.list_to_str(layer)
            tile_representation = doc.createTextNode(layer_string)

            map_layer.appendChild(tile_representation)
            tile_map.appendChild(map_layer)

        """ Write xml  to p_xml_tilemap. """
        f = open(xml_tilemap, "w")
        doc.writexml(f, encoding="utf-8")
        f.close()

    def list_to_str(self, layer):
        result = ""
        for char in layer:
            result += str(char) + " "
        return result
