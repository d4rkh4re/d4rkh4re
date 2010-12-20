###############################################################################
# TilemapEditor
# William C. Morris
# <d4rkh4re@gmail.com>
###############################################################################
###############################################################################
# About:
# This editor is composed of both a Tilemap and Tileset. A Tilemap is a digital
# copy of the map itself. It contains the size of the map, the number of layers
# and a tile id for each tile in the map. The Tileset contains the actual tile 
# images and they are referenced by a tile id. Once both a Tilemap and Tileset
# are opened, the map is displayed according to how the tile ids found in the
# Tilemap, are mapped to the images in the Tileset. Tilemaps are saved in xml
# format and can be opened with any Tileset. This allows game map art to be
# developed separate from the actual game map.
#
###############################################################################
# Example:
# First load one of the provided Tilesets. To do this go File>Load Tileset.
# Let's load "tile.gif". tile.gif is 2 tiles wide, 2 tiles high, and the tiles
# are 32x32 px. Ensure that these values are entered correctly, then press load.
#
# You will notice a Tilemap has already been created for
# you by default. It is 3x3 and has 1 layer with a fill value of zero. You can
# also create a new Tilemap with the dimentions you want with File>New Tileset.
#
# Note:
# If the Tilemap fails to change upon double click be sure to have the top
# layer selected. If you created a map with more than 1 layer, all layers
# are filled with the default value. Since this is the case, use -1 for 
# creating an empty Tilemap.
#
# If you would like to see a more complicated example, load "space.gif".
# space.gif is 2 tiles wide, 6 tiles high, and the tiles
# are 32x32 px. Next open the Tilemap saved at "space.xml"
###############################################################################