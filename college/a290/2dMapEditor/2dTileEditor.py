###############################################################################
# 2dTileEditor.py
# William C. Morris
# <d4rkh4re@gmail.com>

from tkinter import *
from TileMapEditor import *


class TileEditor(Frame):
    """
    http://docs.python.org/py3k/library/tkinter.html
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/
    """
    
    def __init__(self, master=None):
        Frame.__init__(self)
        
        self.tile_map_editor = TileMapEditor()
        
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        # Set up option menu for tile selection. I want to change this
        # later from numbers to actual images.
        self.setup_tile_selection()
        
        # Set up option menu for layer selection.
        self.setup_layer_selection()
        
        # Set up canvas for tile display
        self.setup_tile_display()
        
        # Add widgets to Tile Editor
        self.pack_widgets()
        
    def setup_tile_selection(self):
        """
        Set up option menu for tile selection by key value.
        """
        availibe_tiles = list(self.tile_map_editor.get_tileset_keys())
        self.v = StringVar()
        self.v.set(availibe_tiles[0])
        self.change_selected_tile = OptionMenu(self, self.v, *availibe_tiles)
        
    def setup_layer_selection(self):
        """
        Set up option menu for layer selection.
        """
        editable_layers = [i for i in range(self.tile_map_editor.get_layers())]
        self.v = StringVar()
        self.v.set(editable_layers[0])
        self.change_layer = OptionMenu(self, self.v, *editable_layers)

    def setup_tile_display(self):
        self.display_tilemap = Canvas(self, height=100, width=300, bg="red")
        
    def pack_widgets(self):
        self.display_tilemap.pack({"side": "left"})
        self.change_selected_tile.pack({"side": "left"})
        self.change_layer.pack({"side": "right"})
        
        
def main():
    root = Tk()
    app = TileEditor(master=root)
    app.master.minsize(1000, 500)
    app.mainloop()

if __name__ == '__main__':
    main()
