###############################################################################
# TilemapEditorGui.py
# William C. Morris
# <d4rkh4re@gmail.com>
###############################################################################
# Usage: To use you must load a tileset. To do this go File>Load Tileset. A
# Tilset has been provided ("tile.gif"). Use width:2 height:2 pixel_width:32
# and pixel_height=32. You will notice a Tilemap has already been created for
# you by default. It is 3x3 and has 1 layer with a fill value of zero. You can
# also create a new Tilemap with the dimentions you want with File>New Tileset.
# If the tilemap fails to change upon double click be sure to have the top
# layer selected if you created a map with more than 1 layer.
###############################################################################

from tkinter import *
from TilemapEditor import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


class TilemapEditorGui(Frame):
    """
    http://docs.python.org/py3k/library/tkinter.html
    http://infohost.nmt.edu/tcc/help/pubs/tkinter/
    """
    
    def __init__(self, master=None):
        Frame.__init__(self)

        self.tilemap_editor = TilemapEditor()
        #self.tilemap_editor.open_tilemap("file.xml")
        #self.tilemap_editor.open_tileset("tile0.gif", 2, 2)
        
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
        self.filemenu.add_command(label="New Tilemap", command=self.new_tilemap)
        self.filemenu.add_command(label="Open Tilemap", command=self.open_tilemap)
        self.filemenu.add_command(label="Save Tilemap", command=self.save_tilemap)
        self.filemenu.add_command(label="Save as Tilemap", command=self.save_as_tilemap)
        self.filemenu.add_command(label="Close Tilemap", command=self.close_tilemap)
        self.filemenu.add_command(label="Load Tileset", command=self.load_tileset)
        self.filemenu.add_command(label="Exit", command=self.master.destroy)

        self.menubar.add_cascade(label="File", menu=self.filemenu)

    def new_tilemap(self):
        """
        TODO:
        """
        self.new_dialog = Toplevel()
        self.new_dialog.title("New Tilemap...")

        # Create width label
        nw_label = Label(self.new_dialog, text="Width: ")
        nw_label.pack()
        # Create width entry
        self.nw_entry = Entry(self.new_dialog)
        self.nw_entry.pack()
        # Create height label
        nh_label = Label(self.new_dialog, text="Height: ")
        nh_label.pack()
        # Create height entry
        self.nh_entry = Entry(self.new_dialog)
        self.nh_entry.pack()
        # Create layer label
        l_label = Label(self.new_dialog, text="Layer: ")
        l_label.pack()
        # Create layer entry
        self.l_entry = Entry(self.new_dialog)
        self.l_entry.pack()
        # Create tile fill label
        fl_label = Label(self.new_dialog, text="Fill id: ")
        fl_label.pack()
        # Create tile fill entry
        self.fl_entry = Entry(self.new_dialog)
        self.fl_entry.pack()

        new_button = Button(self.new_dialog, text="Create", command=self.create_tilemap)
        new_button.pack()

        cancel_button = Button(self.new_dialog, text="Cancel", command=self.new_dialog.destroy)
        cancel_button.pack()

    def create_tilemap(self):
        self.tilemap_editor.open_tilemap(int(self.nh_entry.get()), int(self.nw_entry.get()), \
                                         int(self.l_entry.get()), int(self.fl_entry.get()))
        self.tilemap_display.delete(ALL)
        self.new_dialog.destroy()
        self.draw_tilemap()
        self.change_layer.destroy()
        self.setup_layer_selection()
        self.change_layer.pack(anchor=W, side=TOP)
        
    def load_tileset(self):
        """
        TODO:
        """
        # Create load_dialog pop-up.
        self.load_dialog = Toplevel()
        self.load_dialog.title("Load tileset...")
        # Warning message to user for tilset loading.
        warning_msg = Message(self.load_dialog, text="All fields must be accurate for proper execution.")
        warning_msg.pack()
        # Create tileset_source label
        t_label = Label(self.load_dialog, text="Tileset: ")
        # Create tileset_source entry
        self.t_entry = Entry(self.load_dialog)
        self.t_entry.pack()
        # Create tileset_source browse button

        # Create width label
        w_label = Label(self.load_dialog, text="Width: ")
        w_label.pack()
        # Create width entry
        self.w_entry = Entry(self.load_dialog)
        self.w_entry.pack()
        # Create height label
        h_label = Label(self.load_dialog, text="Height: ")
        h_label.pack()
        # Create height entry
        self.h_entry = Entry(self.load_dialog)
        self.h_entry.pack()
        # Create pixel width label
        pw_label = Label(self.load_dialog, text="Pixel width: ")
        pw_label.pack()
        # Create pixel width entry
        self.pw_entry = Entry(self.load_dialog)
        self.pw_entry.pack()
        # Create pixel height label
        ph_label = Label(self.load_dialog, text="Pixel height: ")
        ph_label.pack()
        # Create pixel height entry
        self.ph_entry = Entry(self.load_dialog)
        self.ph_entry.pack()
        # Create load button.
        load_button = Button(self.load_dialog, text="Load", command=self.open_tileset)
        load_button.pack()

        cancel_button = Button(self.load_dialog, text="Cancel", command=self.load_dialog.destroy)
        cancel_button.pack()

    def open_tileset(self):
        self.tilemap_editor.open_tileset(self.t_entry.get(), int(self.w_entry.get()), int(self.h_entry.get()), \
                                         int(self.pw_entry.get()), int(self.ph_entry.get()))
        self.tileset_display.delete(ALL)
        self.load_dialog.destroy()
        self.draw_tileset()
        self.draw_tilemap()
        self.change_layer.destroy()
        self.setup_layer_selection()
        self.change_layer.pack(anchor=W, side=TOP)
        
    def open_tilemap(self):
        filename = askopenfilename(filetypes=[("xmlfiles", "*.xml")])
        self.tilemap_editor.open_tilemap(filename)
        self.change_layer.destroy()
        self.setup_layer_selection()
        self.change_layer.pack(anchor=W, side=TOP)
        self.draw_tilemap()

    def save_tilemap(self):
        self.tilemap_editor.save_tilemap()

    def save_as_tilemap(self):
        f = asksaveasfilename(parent=self.master, filetypes=[('xmlfiles', '*.xml')], title="Save Tilemap as...")
        self.tilemap_editor.save_tilemap(xml_tilemap=f)
        print("File saved to: ", f)

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
        #self.tilemap_editor.save_tilemap("file.xml")
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
