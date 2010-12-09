###############################################################################
# TilemapEditorGui.py
# William C. Morris
# <d4rkh4re@gmail.com>
###############################################################################

from tkinter import *
from TilemapEditor import *
from tkinter.filedialog import askopenfilename


class TilemapEditorGui(Frame):
    """
    http://docs.python.org/py3k/library/tkinter.html
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/
    """
    
    def __init__(self, master=None):
        Frame.__init__(self)

        self.tilemap_editor = TilemapEditor()
        #self.tilemap_editor.open_tilemap("file.xml")
        self.tilemap_editor.open_tileset("tile0.gif", 2, 2)
        
        self.pack()
        self.create_widgets()
        master.config(menu=self.menubar)
        
    def create_widgets(self):
        # Set up menubar
        self.setup_file_menu()
        
        # Set up option menu for tile selection.
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

    def setup_file_menu(self):
        """
        TODO:
        """
        self.menubar = Menu()

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open Tilemap", command=self.open_tilemap)
        self.filemenu.add_command(label="Save Tilemap", command=self.save_tilemap)
        self.filemenu.add_command(label="Close Tilemap", command=self.close_tilemap)
        self.filemenu.add_command(label="Load Tileset")
        self.filemenu.add_command(label="Exit", command=self.master.quit)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

    def open_tilemap(self):
        filename = askopenfilename(filetypes=[("xmlfiles", "*.xml")])
        self.tilemap_editor.open_tilemap(filename)
        self.change_layer.destroy()
        self.setup_layer_selection()
        self.change_layer.pack(anchor=W, side=TOP)
        self.draw_tilemap()

    def save_tilemap(self):
        self.tilemap_editor.save_tilemap()

    def close_tilemap(self):
        self.tilemap_editor.close_tilemap()
        self.change_layer.destroy()
        self.setup_layer_selection()
        self.change_layer.pack(anchor=W, side=TOP)
        self.tilemap_display.delete(ALL)
        self.draw_tilemap()
    
    def setup_layer_selection(self):
        """
        Set up option menu for layer selection.
        """
        editable_layers = [i for i in range(self.tilemap_editor.get_layers())]
        self.layer_selection = StringVar()
        self.layer_selection.set(editable_layers[0])
        self.change_layer = OptionMenu(self, self.layer_selection, *editable_layers)
        
    def setup_tile_selection(self):
        """
        Set up option menu for tile selection by key value.
        """
        # Create canvas tile_width_pixels, 300
        self.tileset_display = Canvas(self, height=470, width=self.tilemap_editor.get_tile_width(), bg="pink")
        self.tileset_display.bind('<Double-1>', self.onTilesetClick)
        self.draw_tileset()
        
        # Create label == "Tile: tile_id"
        tile_selection = "Tile: " + str(self.tilemap_editor.get_selected_texture_id())
        self.tileset_label = Label(text=tile_selection)

    def draw_tileset(self):
        tiles = self.tilemap_editor.get_tileset_values()
        for i in range(len(tiles)):
            width = self.tilemap_editor.get_tile_width()
            self.tileset_display.create_image(0, i*width, anchor=NW, image=tiles[i])

    def setup_tilemap_display(self):
        # Create tilemap_display.
        self.tilemap_display = Canvas(self, height=500, width=500, bg="pink")
        # Draw open tilemap.
        if self.tilemap_editor.tilemap != None:
            self.draw_tilemap()
        # Add double-click event handler to canvas.
        self.tilemap_display.bind('<Double-1>', self.onTilemapClick)

    def draw_tilemap(self):
        for layer in range(self.tilemap_editor.get_layers()):
            for i in range(self.tilemap_editor.get_tilemap_width()):
                for j in range(self.tilemap_editor.get_tilemap_height()):
                    self.tilemap_display.create_image(i*32, j*32, anchor=NW, image=self.tilemap_editor.get_tile_photoimage(layer, i, j))

    def pack_widgets(self):
        self.tilemap_display.pack(anchor=W, side=LEFT)
        self.tileset_display.pack(anchor=W, side=BOTTOM)
        self.change_layer.pack(anchor=W, side=TOP)
        self.tileset_label.pack(anchor=N, side=TOP)
        
        
    ###########################################################################
    # Event handlers.
    ###########################################################################
    def onTilemapClick(self, event):
        """
        Called when a double-click action is called on self.tilemap_display.
        Edits the tile on the selected layer on the clicked tile.
        """
        self.tilemap_editor.set_selected_layer(int(self.layer_selection.get()))
        self.tilemap_editor.edit_tile(int(event.x/32), int(event.y/32))
        self.draw_tilemap()
        self.tilemap_editor.save_tilemap("file.xml")
        print(int(event.x/32), int(event.y/32))

    def onTilesetClick(self, event):
        """
        Called when a double-click action is called on self.tileset_display.
        Edits the tile on the selected layer on the clicked tile.
        """
        self.tilemap_editor.set_selected_texture_id(int(event.y/32))
        tile_selection = "Tile: " + str(self.tilemap_editor.get_selected_texture_id())
        self.tileset_label["text"] = tile_selection
        print(int(event.y/32))

def main():
    root = Tk()
    app = TilemapEditorGui(master=root)
    app.master.minsize(100, 100)
    app.mainloop()

if __name__ == '__main__':
    main()
