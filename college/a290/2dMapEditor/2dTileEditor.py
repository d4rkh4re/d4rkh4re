###############################################################################
# 2dTileEditor.py
# William C. Morris
# <d4rkh4re@gmail.com>
###############################################################################

from tkinter import *
from TileMapEditor import *


class TilemapEditorGui(Frame):
    """
    http://docs.python.org/py3k/library/tkinter.html
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/
    """
    
    def __init__(self, master=None):
        Frame.__init__(self)
        
        self.tilemap_editor = TileMapEditor()
        self.tilemap_editor.open_tilemap("file.xml")
        self.tilemap_editor.open_tileset("tile0.gif", 2, 2)
        
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        # Set up option menu for tile selection. I want to change this
        # later from numbers to actual images.
        self.setup_tile_selection()
        
        # Set up option menu for layer selection.
        self.setup_layer_selection()
        
        # Set up canvas for tile display
        self.setup_tilemap_display()
        
        # Add widgets to Tile Editor
        self.pack_widgets()
        
    ###########################################################################
    # create_widgets helper functions.
    ###########################################################################
    
    def setup_tile_selection(self):
        """
        Set up option menu for tile selection by key value.
        """
        availible_tiles = list(self.tilemap_editor.tile_set.get_tileset_keys())
        self.tile_selection = StringVar()
        self.tile_selection.set(availible_tiles[0])
        self.change_selected_tile = OptionMenu(self, self.tile_selection, *availible_tiles)
        
    def setup_layer_selection(self):
        """
        Set up option menu for layer selection.
        """
        editable_layers = [i for i in range(self.tilemap_editor.get_layers())]
        self.layer_selection = StringVar()
        self.layer_selection.set(editable_layers[0])
        self.change_layer = OptionMenu(self, self.layer_selection, *editable_layers)

    def setup_tilemap_display(self):
        # Create tilemap_display.
        self.tilemap_display = Canvas(self, height=500, width=500, bg="pink")
        # Draw open tilemap.
        self.draw_tilemap()
        # Add double-click event handler to canvas.
        self.tilemap_display.bind('<Double-1>', self.onCanvasClick)

    def draw_tilemap(self):
        for layer in range(self.tilemap_editor.get_layers()):
            for i in range(self.tilemap_editor.get_tilemap_height()):
                for j in range(self.tilemap_editor.get_tilemap_width()):
                    self.tilemap_display.create_image(i*32, j*32, anchor=NW, image=self.tilemap_editor.tile_set.get_tile(self.tilemap_editor.tile_map.get_tile(layer, j, i)))

    def pack_widgets(self):
        self.tilemap_display.pack({"side": "left"})
        self.change_selected_tile.pack({"side": "left"})
        self.change_layer.pack({"side": "right"})

    ###########################################################################
    # Event handlers.
    ###########################################################################
    def onCanvasClick(self, event):
        """
        Called when a double-click action is called on self.tilemap_display.
        Edits the tile on the selected layer on the clicked tile.
        """
        self.tilemap_editor.set_selected_layer(int(self.layer_selection.get()))
        self.tilemap_editor.set_selected_texture_id(int(self.tile_selection.get()))
        self.tilemap_editor.edit_tile(int(event.y/32), int(event.x/32))
        self.draw_tilemap()
        self.tilemap_editor.save_tilemap("file.xml")
        print(int(event.x/32), int(event.y/32))
    

        
def main():
    root = Tk()
    app = TilemapEditorGui(master=root)
    app.master.minsize(800, 500)
    app.mainloop()

if __name__ == '__main__':
    main()
