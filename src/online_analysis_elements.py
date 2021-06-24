import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.widgets import RectangleSelector
import raw_analysis as ra
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import math
import meta_data_dialog
from tkinter import filedialog
from matplotlib.lines import Line2D
from tkintertable import TableCanvas, TableModel
import pandas as pd
from tksheet import Sheet
from tkinter_camera import * 



class OnlineAnalysisElements():
    '''Frontend Handling of the online analysis: all button user interaction is orchestrated through this class.
       It will be always new initiated when reloaded in contrast to the online anlysis manager class'''

    def __init__(self, appearance):
        self.canvas_frame = None
        self.x1 = None
        self.x2 = None
        self.ax2 = None
        self.axis_list = []
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None
        self.xzoom = True
        self.yzoom = True
        self.comment_column = None
        self.image_labbook = None

        # view settings
        self._view_pgf_data_merged =0
        self._view_pgf_data_splitted =0
        self.dat_treeview = None
        self.table = None
        self.bool_list = None
        self.display_grid = None
        self.appearance = appearance

        if self.appearance == "azure":
            self.bg_color = "#ffffff"
            self.fg_color = "#000000"

        else:
            self.bg_color = "#333333"
            self.fg_color = "#ffffff"

    def select_online_file(self, note, online_manager, window):

        window.option_add("*foreground", "black")
        self.note = note

        self.note_live = note.frames[0]
        print(self.image_labbook)
        self.raw_frame = ttk.Frame(master=note.frames[0])
        self.raw_frame.rowconfigure(0, weight = 1)
        self.raw_frame.columnconfigure(0, weight = 1)
        self.labbook_frame = ttk.Frame(master=note.frames[1])
        self.raw_frame.grid(sticky = "ew")
        self.labbook_frame.grid()

        self.online_manager = online_manager

        # trial
        # for functions:
        self.button_grid = ttk.Frame(self.raw_frame)
        self.button_grid.grid(column=2, row=5)

        

        #buttons to transfer to offline_analysis
        self.off_frame = ttk.Frame(self.raw_frame)
        self.off_frame.grid(column = 1, row = 9, columnspan = 3, sticky = "w")

        #button grid
        self.tree_grid = ttk.Frame(self.raw_frame)
        self.tree_grid.grid(column=1, row=3, sticky=tk.N)
        #self.tree_grid.grid_columnconfigure(0, weight=1)
        #self.tree_grid.grid_rowconfigure(0, weight=1)

        # make an extra grid for the tree in the labbook to align
        self.tree_labbook = ttk.Frame(self.labbook_frame)
        self.tree_labbook.grid(column = 1, row = 1, sticky = "n", pady = 10)
        
        #grid for the drawn labbook 
        self.labbook_grid = ttk.LabelFrame(self.labbook_frame, text = "Labbook Entries")
        self.labbook_grid.grid(column=2, row=1, sticky="n", padx  = 10, pady = 10)
        #self.labbook_grid.grid_columnconfigure(0, weight=1)
        #self.labbook_grid.grid_rowconfigure(0, weight=1)

        #labbook_button like Add metadata, Remove Discarded Data
        self.button_lab = ttk.Frame(self.labbook_frame)
        self.button_lab.grid(column = 2, row = 5, sticky = "w")

        # Add the frame for the image captured in the configuraiton
        self.camera_grid = ttk.LabelFrame(self.labbook_frame, text = "Image of the Experiment", width = 350, height = 383)
        self.camera_grid.grid(column = 3, row = 1, sticky = "n", padx = 10, pady = 10)

    
        # bind the labbook key 
        self.note.note.bind("<<NotebookTabChanged>>", self.test_call)

        # Loading buttons
        button_layout = ttk.Frame(self.raw_frame)
        button_layout.grid(column = 1, row = 1, columnspan = 2, sticky = tk.W)

        self.tree = ttk.Treeview(master=self.tree_grid)

        self.read_data_file_format = ttk.Button(master=button_layout, text="Select a .Dat File:",
                                                command=lambda: self.read_dat_file(self.tree, 'new'),
                                                width=20,
                                                style="AccentButton")

        self.labbook_button = ttk.Button(master=button_layout, text="Write to Labbook",
                                                command=lambda: self.switch_to_labbook(self.labbook_grid),
                                                width=20,
                                                style="ToggleButton")

        
        self.read_data_file_format.grid(column=1, row=1, padx=5, pady=5, sticky = tk.W)

        self.labbook_button.grid(column=2, row=1, padx=5, pady=5, sticky = tk.W)


        if self.online_manager._dat_file_name:
            self.labbook_button.configure(state="normal")
            self.labbook_button.configure(style="AccentButton")
        else:
            self.labbook_button.configure(state="disable")
            self.labbook_button.configure(style="ToggleButton")

        ttk.Separator(self.raw_frame, orient=tk.HORIZONTAL).grid(row=2, sticky="ew", columnspan = 6)

        if self.online_manager._node_list_STATE:
            self.data_tree = self.reload_data_tree_view(self.online_manager, self.tree_grid)
            self.built_discard_button(self.tree_grid)
            self.reload_discarded_tree_view(self.online_manager, self.tree_grid)

            self.start_text = ttk.Label(self.raw_frame,
                                        text="To see details of your series recording, \n click the concerning series in the treeview!")
            self.start_text.configure(font=("Times", 22))
            self.start_text.grid(column=2, row=3, rowspan=1, columnspan=1, sticky=tk.N, padx=200, pady=150)
        else:
            print("was empty")

    def test_call(self,event):
        '''not finished yet - will be implemented soon'''
        #@TODO (dz) continue here
        # rewrote this
        #print("something happened")
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Labbook":
            if self.dat_treeview: # here I need a better comment 
                self.switch_to_labbook(self.labbook_grid)
            else:
                tk.messagebox.showerror(title = "Data Selection",message = "Please first select the File to Analyze, since it is not transfered from the configuration")
                self.note.note.select(self.note_live)


    def on_configure(self,event):
        canvas = event.widget
        canvas.itemconfigure(canvas.fram_n_canvas_iid, width=canvas.winfo_width())


    def read_dat_file(self,tree, mode):
        '''read a .dat file and get a filled tkinter treeview
         @input: - tree [TKinterTreeView]-> an empty tree to be filled by this function. It is input to keep tkinter objects away from manager class
                 - mode [String] -> can be either new to read a new .dat file. Otherwise an already read .dat file will be chosen
         @return none
         @author dz'''

        # print(self.raw_frame)
        self.dat_treeview = self.online_manager.read_dat_tree_structure(tree, mode)
        # print(self.dat_treeview)
        self.init_draw = self.dat_treeview.get_children()[-1]
        self.dat_treeview.item(self.init_draw, open=True)
        self.dat_treeview.heading("#0", text="Data in experiment " + self.online_manager.dat_file_name)
        self.dat_treeview.grid(column=1, row=3, sticky=tk.N, columnspan=2, padx=5, pady=20)
        self.dat_treeview.bind('<ButtonRelease-1>',
                               lambda event: self.selected_node_data_tree(self.online_manager, self.dat_treeview))

        self.start_text = ttk.Label(self.raw_frame,
                                    text="To see details of your series recording, \n click the concerning series in the treeview!")
        self.start_text.configure(font=("Times", 22))
        self.start_text.grid(column=2, row=3, rowspan=1, columnspan=1, sticky=tk.N, padx=200, pady=150)
        self.labbook_button.configure(state="normal")
        self.labbook_button.configure(style="AccentButton")

    def selected_node_data_tree(self, online_manager, tree):
        self.selected_node(self.online_manager, tree, "Discard")

    def selected_node_discard_tree(self, online_manager, tree):
        self.selected_node(self.online_manager, tree, "Retrieve")

    def selected_node(self, online_manager, tree, mode):
        ''' A function that displays a selected element of the tree: only trace 1 of each sweep has a value list > 0
        location -> name of the master widget where the canvas will be printed to
        bm -> instance of backend_manager class
        '''
        self.start_text.destroy()
        self.node_info = None
        self.node_info = tree.focus()
        print(f"this is the selecte node {self.node_info}")  # returns a dictionary
        # print(self.node_info)
        # print(tree.item(self.node_info))

        self.built_discard_button(self.tree_grid, self.node_info)

        if self.canvas_frame:
            self.canvas_frame.destroy()

        self.canvas_frame = ttk.Frame(self.raw_frame)
        self.canvas_frame.grid(column=2, row=3, rowspan=2, columnspan=2, sticky="nw", pady=0)


        '''series level = 2 '''
        if len(tree.item(self.node_info)['values']) == 2:

            series_name = tree.item(self.node_info)["text"]

            if mode == "Discard":
                self.discard_button.configure(state="normal")
                self.discard_button.configure(style="AccentButton")
                self.discard_button.configure(text="Discard " + series_name)
                self.retrieve_selection.configure(state="disabled")
                self.retrieve_selection.configure(style="ToggleButton")
            else:
                self.discard_button.configure(state="disabled")
                self.discard_button.configure(style="ToggleButton")
                self.retrieve_selection.configure(text="Retrieve " + series_name)
                self.retrieve_selection.configure(state="normal")
                self.retrieve_selection.configure(style="AccentButton")

            self.recording_mode = self.online_manager.get_series_recording_mode(self.node_info)
            print(f"this is the recording mode {self.recording_mode}")
            self.show_data_display_options(self.button_grid,tree)

            

            self.sweep_amount = self.online_manager.read_series_from_dat_file(tree, self.node_info)

            # print('sweep amount updated')
            # print(self.sweep_amount)
            if self._view_pgf_data_splitted:
                self.show_data_pgf_splitted_view(tree)
            else:
                if self._view_pgf_data_merged:
                    self.show_data_pgf_merged_view(tree)
                else:
                    self.fig = Figure(figsize=(10, 6), dpi=90)
                    self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.95, top=0.97, wspace=0.3, hspace=0.3)
                    self.draw_canvas_figure(111, self.online_manager, tree)
                    self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
                    self.canvas.get_tk_widget().grid(pady=0, sticky="nw")  # A tk.DrawingArea.
                    self.canvas.draw()

                    #self.split_pgf_and_data_plot(tree)
                    self.canvas.mpl_connect("scroll_event", self.zoom)
                    self.toggler(tree)

            if not self.RS.active:
                self.move = self.fig.canvas.mpl_connect('button_press_event', self.onPress)
                self.release = self.fig.canvas.mpl_connect('button_release_event', self.onRelease)
                self.mot = self.fig.canvas.mpl_connect('motion_notify_event', self.onMotion)
                self.fig.canvas.mpl_connect('pick_event', lambda x: self.onpick(x, 0))

        #@TODO (dz) - ad series view to sweep level

        if len(tree.item(self.node_info)['values']) == 4:  # trace level = 4

            [time, data] = self.online_manager.read_data_from_dat_file(self.tree.item(self.node_info)['values'])
            time, data = self.interpolate_scale_data_time(time, data, self.online_manager, self.node_info, self.node_info)
            fig = Figure(figsize=(10, 6), dpi=100)
            fig.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.97, wspace=0.3, hspace=0.3)
            ax = fig.add_subplot(111)
            ax.plot(time, data)
            ax.set_xlabel("Time (ms)")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(sticky=tk.W, padx=3, pady=5)

    def interpolate_scale_data_time(self, time, data, online_manager, node, node_info):
        #print(online_manager.get_series_recording_mode(node_info))
        #ToDO we need this function also for the offline manager
        ymin = self.online_manager.get_Ymin_metadata(node)
        ymax = self.online_manager.get_Ymax_metadata(node)
        xstart = self.online_manager.get_XStart_metadata(node)
        xint = self.online_manager.get_XInterval_metadata(node)

        if self.online_manager.get_series_recording_mode(node_info) == "Current Clamp":
            time = np.linspace(xstart, xstart + xint * (len(data) - 1) * 1000, len(data))
            data = np.interp(data, (data.min(), data.max()), (ymin, ymax))

            return time, data

        time = np.linspace(xstart, xstart + xint * (len(data) - 1) * 1000, len(data))
        return time, data

    def built_discard_button(self, grid, node_identifier=None, ):

        button_text = "Discard "
        self.discard_button = ttk.Button(master=grid, text=button_text,
                                         command=lambda: self.discard_and_update_view(self.online_manager, node_identifier),
                                         width="20", style="ToggleButton")

        self.retrieve_selection = ttk.Button(master=grid, text="Retrieve",
                                             command=lambda: self.retrieve_and_update_view(self.online_manager,
                                                                                           node_identifier),
                                             width="20",
                                             style="ToggleButton")
        self.discard_button.grid(column=1, row=4, sticky=tk.N, pady=10)
        self.retrieve_selection.grid(column=1, row=5, sticky=tk.N, pady=10)
        ttk.Separator(master = self.raw_frame).grid(row=7, sticky="ew", columnspan = 10, ipadx=100)
        self.discard_button.configure(state="disabled")
        self.retrieve_selection.configure(state="disabled")

    def show_data_display_options(self,master_frame,tree):
        ''' Display checkbuttons for the user to add a plot of the pgf files and to seperate overlaying plots into a splitted view '''

        # destroy the display grid
        if self.display_grid:
            self.display_grid.destroy()
        
        #for splitview button and merge button
        self.display_grid = ttk.LabelFrame(self.raw_frame, text = "Options")
        self.display_grid.grid(column = 4, row = 3, sticky = "nw", pady = 10)
        #self.display_grid.columnconfigure(0, weight = 3)
        #self.display_grid.columnconfigure(1, weight = 3)
        
        # Label 1
        display_options_frame_title = ttk.Label(self.display_grid, text="Display Options:")
        display_options_frame_title.grid(column=1, row=1, sticky = tk.W, pady = 10)

        display_pgf_value = tk.BooleanVar()
        if self._view_pgf_data_merged:
            display_pgf_value.set(True)
        else:
            display_pgf_value.set(False)

        self.display_pgf_splitted = tk.BooleanVar()
        if self._view_pgf_data_splitted:
            self.display_pgf_splitted.set(True)
        else:
            self.display_pgf_splitted.set(False)

        # show pgf pulses
        self.display_pgf = ttk.Checkbutton(self.display_grid,
                                                  text="Display Pulse Protocol",
                                                  style="Switch",
                                                  var = display_pgf_value,
                                                  command = lambda: self.switch_pgf_display_view(tree)
                                                      )

        # split pgf and data view
        self.split_view= ttk.Checkbutton(self.display_grid,
                                                  text="Split Data and PGF",
                                                  style="Switch",
                                                  var = self.display_pgf_splitted,
                                                  command = lambda: self.switch_splitted_view(tree)
                                                )

        self.display_pgf.grid(pady=10, padx=5, column=1, row=2, sticky = tk.W)
        self.split_view.grid(pady=10, padx=5, column=1, row=3, sticky = tk.W)


    def show_recording_mode_analysis_functions(self, recording_mode):
        """ function is still a mess need to redo this """
        print("show_recordings")
        self.bool_list = []
        
        # function for the image analysis
        self.function_listing = [self.cursor_bounds, None, None, None]
        image_options = ["Set Cursor Bounds","Panning","Zooming", "Moving"]
        

        self.tool_box_frame_tile = ttk.Label(self.display_grid, text="Image Option:")
        self.tool_box_frame_tile.grid(pady=10, padx=5, column=1, row=5, sticky = "w")
        self.function_list = ra.AnalysisRaw().get_elements(self.recording_mode)
        self.image_mode_button_list = []
        self.recoding_mode_specific_button_list = []


        for i in range(0, len(image_options)):
            self.toggle = tk.BooleanVar()
            self.bool_list.append(self.toggle)
        for i in range(0, len(image_options)):
            self.analyzer = ttk.Checkbutton(master=self.display_grid,
                                            text=image_options[i],
                                            command=self.function_listing[i],
                                            width=15,
                                            style="Switch",
                                            var=self.bool_list[i],
                                            )

            self.image_mode_button_list.append(self.analyzer)

            self.image_mode_button_list[i].grid(column=1, row = 6+i,
                                                            sticky="nw", pady=5, padx=10)

        # Make a Set of Analysis options for the selected area
        self.tool_box_analysis = ttk.Label(self.display_grid, text="Analysis Options:")
        self.tool_box_analysis.grid(pady=10, padx=5, column=1, row=11, sticky = "w")
        for i in range(0, len(self.function_list)):
            self.analyzer = ttk.Checkbutton(master=self.display_grid,
                                            text=self.function_list[i],
                                            width=15,
                                            style="ToggleButton",
                                            )

            self.recoding_mode_specific_button_list.append(self.analyzer)

            self.recoding_mode_specific_button_list[i].grid(column=1, row = 15+i,
                                                            sticky="nesw", pady=5, padx=10)


        # add offline analysis transfer buttons
        self.tool_box_frame_tile = ttk.Label(self.raw_frame, text="Offline Analysis Transfer:")
        self.tool_box_frame_tile.grid(pady=10, padx=5, column=1, row=8, sticky = "w")
        self.off_button = ttk.Button(self.off_frame,
                                    text = "Transfer Experiment to Offline Analysis",
                                    width = 20)
        self.save_button = ttk.Button(self.off_frame,
                                    text = "Save selected Trace",
                                    width = 20)
        self.discard_button = ttk.Button(self.off_frame,
                                    text = "Remove Discarded Data",
                                    width = 20)
        self.off_button.grid(pady = 10, padx = 5, column = 2, row = 18, sticky = "w",ipady = 15)
        self.save_button.grid(pady = 10, padx = 5, column = 3, row = 18, sticky = "w",ipady = 15)
        self.discard_button.grid(pady = 10, padx = 5, column = 4, row = 18, sticky = "w",ipady = 15)


    def draw_canvas_figure(self, subplots, online_manager, tree,viewmode=None):
        '''draw canvas of a series or a trace.
        @input viewmode:    None or 0: only data will be plotted,
                            1:  merged view with two ordinates will be plotted
                            '''
        # @TODO super uggly implementation: redo self.node_info better !

        self.ax = self.fig.add_subplot(subplots)
        self.time_list = []
        self.data_list = []

        if viewmode == 1:
            self.ax2 = self.ax.twinx()
            self.ax2.set_ylabel("Voltage (mV)")
        
        self.show_recording_mode_analysis_functions(self.recording_mode)


        [time_pgf, pgf] = self.online_manager.get_pgf_voltage(self.node_info) # e.g. Group1_Series1

        print(self.sweep_amount)

        for i in range(self.sweep_amount):
            self.trace_index = tree.item(self.node_info)['values'] + [i, 0]
            #print(self.node_info)
            count = i + 1
            identifier = self.node_info + "_Sweep" + str(count) + "_Trace1"
            [time, data] = self.online_manager.read_data_from_dat_file(self.trace_index, self.online_manager.bundle)
            time, data = self.interpolate_scale_data_time(time, data, self.online_manager, identifier, self.node_info)
            self.time_list.append(time)
            self.data_list.append(data)

            self.ax.plot(time, data, picker = True)
            self.ax.set_xlabel("Time (ms)")
            self.ax.set_ylabel("Current (pA)")
            #print(count-1)

            if viewmode==1:
                if len(pgf) == 1:  # no step iterative step protocol
                    self.ax2.plot(time, pgf[0])
                else:
                    self.ax2.plot(time, pgf[count-1])


            self.time = time

        if all([self.x2, self.x1]):
            self.ax.vlines(self.x1, self.ax.get_ylim()[0], self.ax.get_ylim()[1], color="white")
            self.ax.vlines(self.x2, self.ax.get_ylim()[0], self.ax.get_ylim()[1], color="white")
            self.x2 = None
            self.x1 = None

    def toggler(self, tree,viewmode=None):
        """ implements the Rectangle Selector for bound selection
        input --> tree with Data Structures
        viewmode --> if splitted or not
         """

        ax = self.ax

        if viewmode==1:
            ax = self.ax2

        self.RS = RectangleSelector(ax, lambda eclick, erelease: self.line_callback(eclick, erelease, tree),
                                    drawtype='box', useblit=True,
                                    button=[1, 3],
                                    minspanx=2, minspany=2,
                                    spancoords='pixels',
                                    interactive=True)

        if self.bool_list[0].get() is True:
            self.RS.set_active(True)
        else:
            self.RS.set_active(False)

    def zoom(self, event):
        """ Implements zooming of the canvas using hte mouse wheel, zooming in and zooming out possible
        maybe add to a button to activate tmpl_connecthe zooming with the wheel"""

        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()

        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if (xdata is None):
            return ()
        if (ydata is None):
            return ()

        if event.button == 'down':
            # deal with zoom in
            scale_factor = 1 / 2.
        elif event.button == 'up':
            # deal with zoom out
            scale_factor = 2.
        else:
            # deal with something that should never happen
            scale_factor = 1
            #print(event.button)

        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])

        if (self.xzoom):
            self.ax.set_xlim([xdata - new_width * (1 - relx), xdata + new_width * (relx)])
        if (self.yzoom):
            self.ax.set_ylim([ydata - new_height * (1 - rely), ydata + new_height * (rely)])
        self.canvas.draw()
        self.canvas.flush_events()

    def onPress(self, event):
        """ on press event when the plot is pressed by the mouse key """
        if event.inaxes != self.ax:
            return
        self.cur_xlim = self.ax.get_xlim()
        self.cur_ylim = self.ax.get_ylim()
        self.press = self.x0, self.y0, event.xdata, event.ydata
        self.x0, self.y0, self.xpress, self.ypress = self.press

    def onMotion(self, event):
        """ on motion event as long as the button is pressed """
        if self.press is None:
            return
        if event.inaxes != self.ax:
            return
        dx = event.xdata - self.xpress
        dy = event.ydata - self.ypress
        self.cur_xlim -= dx
        self.cur_ylim -= dy
        self.ax.set_xlim(self.cur_xlim)
        self.ax.set_ylim(self.cur_ylim)

        self.canvas.draw()

    def onRelease(self, event):
        """ reaction when mouse click is release """
        self.press = None
        self.canvas.draw()

    def line_callback(self, eclick, erelease, tree):
        """ get the drawing rectangle and the x and y coordinates """

        self.x1, y1 = eclick.xdata, eclick.ydata
        self.x2, y2 = erelease.xdata, erelease.ydata
        self.trace_analysis(self.x1, self.x2, tree)

    def cursor_bounds(self):

        """ activate or deactivate the RS selector """
        #print(self.bool_list[0].get())
        # defines if the toggle is on or not
        if self.bool_list[0].get() is True:
            #print(' RectangleSelector activated.')
            self.RS.set_active(True)
            self.fig.canvas.mpl_disconnect(self.move)
            self.fig.canvas.mpl_disconnect(self.release)
            self.fig.canvas.mpl_disconnect(self.mot)
        else:
            #print(' RectangleSelector deactivated.')
            self.RS.set_active(False)
            self.move = self.fig.canvas.mpl_connect('button_press_event', self.onPress)
            self.release = self.fig.canvas.mpl_connect('button_release_event', self.onRelease)
            self.mot = self.fig.canvas.mpl_connect('motion_notify_event', self.onMotion)


    def trace_analysis(self, lower, upper, tree):

        """ implements the connection to raw analysis, drawing max, min, mean current from the selection
        of the cursor bounds
        input --> 
        lower, upper bounds
        and the tree for the data structure """

        current_dictionary = {"voltage": [], "max": [], "min": [], "mean": [], "area": []}
        vol = -65  # still a workaround we need still the voltage inputs from the protocol
        for i, t in zip(self.time_list, self.data_list):

            understanding = zip(self.time_list, self.data_list)

            # just as test case
            vol += 5
            #print(vol)
            current_dictionary["voltage"].append(vol)

            trace = ra.AnalysisRaw(i, t)
            trace._lower_bounds = lower
            trace._upper_bounds = upper
            trace.construct_trace()
            trace.slice_trace()
            min_current = trace.min_current()
            max_current = trace.max_current()
            area_current = trace.get_area()
            mean_current = trace.mean_current()

            current_dictionary["max"].append(max_current)  # maybe search for another solution to this problem
            current_dictionary["min"].append(min_current)
            current_dictionary["mean"].append(mean_current)
            current_dictionary["area"].append(area_current)
     
        self.plot_analysis(current_dictionary, tree)

    def plot_analysis(self, current_dictionary, tree):
        """ check if the plots are already drawn if not draw the analysis plots iteratively based on the current dictionary """

        if len(self.axis_list) > 0:
            self.canvas_frame.destroy()
            plt.close(self.fig)
            for i in self.axis_list:
                i.clear()

        self.canvas_frame.destroy()
        self.canvas_frame = ttk.Frame(self.raw_frame)
        self.canvas_frame.grid(column=2, row=3, rowspan=2, columnspan=2, sticky="nw", pady=0)
        self.fig = Figure(figsize=(10, 6), dpi=90)
        self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.95, top=0.95, wspace=0.3, hspace=0.3)
        self.draw_canvas_figure(231, self.online_manager, tree)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(pady=0, sticky="nswe")
        self.toggler(tree)

        for i, keys in enumerate(current_dictionary.keys()):
            self.ax2 = self.fig.add_subplot(2, 3, i + 2)
            self.axis_list.append(self.ax2)
            self.ax2.plot(current_dictionary["voltage"], current_dictionary[keys])
            self.ax2.set_title(keys)


        self.canvas.draw()

    def retrieve_and_update_view(self, online_manager, node_info):
        self.online_manager.retrieve(node_info)
        self.update_view(self.online_manager)

    def discard_and_update_view(self, online_manager, node_info):
        self.online_manager.discard(node_info)
        self.update_view(self.online_manager)

    def update_view(self, online_manager):
        # @TODO destroy tree view
        #self.dat_treeview.destroy()
        self.reload_data_tree_view(self.online_manager,self.tree_grid)
        self.reload_discarded_tree_view(self.online_manager,self.tree_grid)

    def reload_discarded_tree_view(self, online_manager,grid):
        tree = ttk.Treeview(master=grid)
        discarded_elements_tree = self.online_manager.get_discarded_data_tree(tree, '')

        #if tree != discarded_elements_tree:
        discarded_elements_tree.heading("#0", text="Discarded data")
        item = discarded_elements_tree.get_children()[-1]
        discarded_elements_tree.item(item, open=True)
        discarded_elements_tree.grid(column=1, row=6, sticky=tk.N, padx=5, pady=20)
        discarded_elements_tree.bind('<ButtonRelease-1>',
                                              lambda event: self.selected_node_discard_tree(self.online_manager,
                                                                                            discarded_elements_tree))

        self.retrieve_selection.configure(state="disable")
        self.retrieve_selection.configure(style="ToggleButton")

    def reload_data_tree_view(self, online_manager, grid):
        tree = ttk.Treeview(master=grid)
        dat_treeview_reloaded = self.online_manager.read_dat_tree_structure(tree, '')
        re_item = dat_treeview_reloaded.get_children()[-1]
        dat_treeview_reloaded.item(re_item, open=True)
        dat_treeview_reloaded.heading("#0", text="Data in experiment " + self.online_manager.dat_file_name)
        dat_treeview_reloaded.grid(column=1, row=3, sticky=tk.N, padx=5, pady=20)
        dat_treeview_reloaded.bind('<ButtonRelease-1>', lambda event: self.selected_node_data_tree(self.online_manager,
                                                                                                   dat_treeview_reloaded))
        #@ TODO try catch
        #self.discard_button.configure(state="disable")
        #self.discard_button.configure(style="ToggleButton")

        return tree

    def switch_to_labbook(self,grid=None):
        # @TODO rework this
        grid = self.tree_labbook
        
        #print("executed switch")
        if self.online_manager._node_list_STATE:
            self.labbook_tree = self.reload_data_tree_view(self.online_manager, grid)
            self.built_discard_button(grid)

            if self.online_manager._discardet_nodes_STATE:
                self.reload_discarded_tree_view(self.online_manager,grid)


            self.extend_meta_data_list =ttk.Button(master=self.button_lab,command=self.add_meta_data, text="Add Metadata",
                       width=30,
                       style="AccentButton")
            
            self.save_labbook =ttk.Button(master=self.button_lab, command = self.save_labbook, text="Save Labbook",
                       width=30,
                       style="AccentButton")

            self.extend_meta_data_list.grid(column=1, row=1, sticky="w", pady=10, padx = 10)
            self.save_labbook.grid(column=2, row=1, sticky="w", pady=10, padx = 10)

            
            self.table_frame = ttk.Frame(self.labbook_frame)
            self.table_frame.grid(column = 1)
            self.create_labbook_table()
                      
            

            if self.image_labbook is None:
                image_label = ttk.Label(self.camera_grid, text = "NO Image found")
                image_label.grid(column = 1, row = 1, sticky = "nswe")
                
            
            else:
                self.canvas = tk.Canvas(self.camera_grid, width = 400, height = 400)
                self.canvas.grid(column = 1, row = 1, sticky = "nswe")
                imgs = Image.fromarray(self.image_labbook)
                image = imgs.resize((400,400), Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=image)
                self.canvas.create_image(20,20, anchor=tk.NW, image=imgtk)
                self.canvas.image = imgtk
           


    def create_labbook_table(self,additional_meta_data=None):
        """Creates a pandas Dataframe which can be then transferred into a list of lists and used as input for the Tk.sheet packages
        --input: additional meta-data as selected
        --output: draws the table in the master frame"""
        columns_names, table_content = self.online_manager.write_series_and_metadata_to_labbook(additional_meta_data)
        self.labbook_table = pd.DataFrame(table_content) # make a table frame
        self.labbook_table.columns = ["Series"] + columns_names # add the headers

        if self.comment_column is None:
            self.labbook_table["comment"] = ""

        else:
            self.labbook_table["comment"] = self.comment_column

        self.labbook_table = self.labbook_table.set_index("Series").round(3)
    

        if self.table: # if table already there than only redraw with new metadata parameter and add hte comment list
            self.table.set_sheet_data(data = self.labbook_table.values.tolist(),
                                        reset_col_positions = True,
                                        reset_row_positions = True,
                                        redraw = True,
                                        verify = False,
                                        reset_highlights = False)
            self.table.headers(newheaders = self.labbook_table.columns, reset_col_positions = False, show_headers_if_not_sheet = True)
            self.table.row_index(self.labbook_table.index, reset_row_positions = False, show_index_if_not_sheet = True)
            
        else:
            self.table = Sheet(self.labbook_grid,
                               data = self.labbook_table.values.tolist(),
                               frame_bg = self.bg_color,
                               table_grid_fg = self.fg_color,
                               table_bg = self.bg_color,
                               table_fg = self.fg_color,
                               header_bg = self.bg_color,
                               header_border_fg = self.fg_color,
                               header_fg = self.fg_color,
                               index_bg = self.bg_color,
                               index_border_fg = self.fg_color,
                               index_fg = self.fg_color,
                               top_left_bg = self.bg_color,
                               top_left_fg = self.fg_color,
                               outline_color = self.fg_color,
                               show_x_scrollbar = False,
                               show_vertical_grid = False,
                               width = 1000,
                               height = 370,
                               row_height = "2", 
                               header_height = "2"
                               
                               )

            self.table.headers(newheaders = self.labbook_table.columns,
                               reset_col_positions = False,
                               show_headers_if_not_sheet = True)
            self.table.enable_bindings(("single_select",
                                    "edit_cell"
                                    ))
            self.table.align(align = "center")
            self.table.extra_bindings("cell_select", self.edit_cell)
            self.table.edit_bindings(enable = False)

            self.table.row_index(self.labbook_table.index, reset_row_positions = False, show_index_if_not_sheet = True)
            self.table.grid(row = 1, column = 2, sticky = "nswe")
        
    def edit_cell(self,event):
        """ construct the cell_editor based on the click within the cell"""
        r, c = self.table.get_currently_selected()
        self.table.row_height(row = r, height = "text", only_set_if_too_small = True, redraw = False)
        self.table.column_width(column = c, width = "text", only_set_if_too_small = True, redraw = True)
        self.table.create_text_editor(row = r,
                                      column = c,
                                      text = self.table.get_cell_data(r, c),
                                      set_data_ref_on_destroy = False,
                                      binding = self.end_edit_cell)


    def end_edit_cell(self, event = None):
        """ End the editor within the cell of the dataframe """
        newtext = self.table.get_text_editor_value(event,
                                                   r = event[0],
                                                   c = event[1],
                                                   set_data_ref_on_destroy = True,
                                                   move_down = True,
                                                   redraw = True,
                                                   recreate = True)


        self.comment_column = [i for i in self.table.get_column_data(event[1], return_copy = True)]
        #print (print(self.comment_column))

    def add_meta_data(self):
        ''' Executed when "add meta data" button in labbook tab  was clicked.
        @inut:  none
        @return: none
        @author dz '''

        additionial_meta_data_list = meta_data_dialog.MetaDataDialog(self.labbook_frame)
        #print(additionial_meta_data_list.identifier_list)

        self.create_labbook_table(additionial_meta_data_list.identifier_list)


    def set_table_head(self,columns):
        '''Set strings as heading to the first row of the labbook table.
        @inut:  columns [int] -> number of columns of the table
        @return: none
        @author dz  '''
        self.table_frame.grid(column=3, row=3, rowspan=2, columnspan=columns, sticky=tk.N, pady=30, padx=100)
        self.e = ttk.Entry(self.table_frame, width=20)
        self.e.grid(row=0, column=columns)
        self.e.insert(tk.END, "Additional Comment")

    def save_labbook(self):
        '''Save the displayed labbook selection to a file.
        @inut:  none
        @return: none
        @author dz  '''

        # @TODO (dz) for now it's just an empty file, add single table frame rows from labbook table in here

        name = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
        self.labbook_table.to_csv(name)
        

    def split_pgf_and_data_plot(self,tree):
        '''Checks the last selected data view state (by default: merged view) and therefore provides toggle button text
        and the correct viewing.
        @inut:  tree [TKinterTreeView]->the current tkinter tree object, not needed in this function, just piped to the next function
        @return: none
        @author dz  '''

        if self.online_manager._data_view_STATE:    # mode 1 = splitted view
            prnt_text = "Merge data and step protocol"
            self.show_data_pgf_splitted_view(tree)
        else:
            prnt_text= "Split data and step protocol" # mode 0 = merged view
            self.show_data_pgf_merged_view(tree)
        try:
            self.switch_voltage_view.destroy()
        except:
            pass


    def show_data_pgf_merged_view(self,tree):
        '''Function to show data and pgf subpplots merged in a single plot. Left axis will show current values, right axis will show voltage values.
        @inut:  tree [TKinterTreeView]->the current tkinter tree object, not needed in this function, just piped to the next function
        @return: none
        @author dz  '''

        self.canvas_frame.destroy()
        self.canvas_frame = ttk.Frame(self.raw_frame)
        self.canvas_frame.grid(column=2, row=3, rowspan=2, columnspan=2, sticky=tk.W, pady=0)
        self.fig = Figure(figsize=(10, 6), dpi=90)
        self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.90, top=0.97, wspace=0.3, hspace=0.3)

        self.draw_canvas_figure(111, self.online_manager, tree,1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(pady=0, sticky="nswe")  # A tk.DrawingArea.
        self.canvas.draw()
        self.toggler(tree,1)


    def show_data_pgf_splitted_view(self,tree):
        '''Function to show data and pgf subpplots below each other. The upper one will show trace's current, the lower one will show
        the pgf voltage.
        @inut:  tree [TKinterTreeView]->the current tkinter tree object, not needed in this function, just piped to the next function
        @return: none
        @author dz  '''

        self.canvas_frame.destroy()
        self.canvas_frame = ttk.Frame(self.raw_frame)
        self.canvas_frame.grid(column=2, row=3, rowspan=2, columnspan=2, sticky=tk.W, pady=0)
        self.fig = Figure(figsize=(10, 6), dpi=90)
        self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.98, top=0.95, wspace=0.1, hspace=0.3)

        # draw the upper figure
        self.draw_canvas_figure(211, self.online_manager, tree)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(pady=0, sticky="nswe")
        self.canvas.draw()


        # enable courser bounds
        self.toggler(tree)

        self.ax2 = self.fig.add_subplot(2, 1, 2)
        [time_pgf, data_pgf] = self.online_manager.get_pgf_voltage(self.node_info)  # e.g. Group1_Series1

        if len(data_pgf) == 1:  # if 1, no stepwise voltage incrementation has been performed
                self.ax2.plot(self.time, data_pgf[0])
        else:
           for i in range(0, len(data_pgf)):
              self.ax2.plot(self.time, data_pgf[i])

        self.ax2.set_ylabel("Voltage (mV)")
        self.canvas.draw()

        self.fig.canvas.mpl_connect('pick_event', lambda x: self.onpick(x,1))



        # @TODO (dz->mz) check whether it is possibe to link the concerning series trace and pgf sequence when there are multiple sweeps (plotting 21 sweeps, colors are not sufficient any more)

    def switch_pgf_display_view(self,tree):
        '''will be called when the toggle button is pressed'''

        if self._view_pgf_data_merged == 0:  # means disabled
            #print("disabled")
            self.show_data_pgf_merged_view(tree)
            self._view_pgf_data_merged = 1
            self._view_pgf_data_splitted = 0
            self.display_pgf_splitted.set(False)

        else:
            #print("enabled")
            self.canvas_frame.destroy()
            self.canvas_frame = ttk.Frame(self.raw_frame)
            self.canvas_frame.grid(column=2, row=3, rowspan=2, columnspan=2, sticky=tk.W, pady=0)
            self.fig = Figure(figsize=(10, 6), dpi=90)
            self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.98, top=0.95, wspace=0.1, hspace=0.3)

            self.draw_canvas_figure(111, self.online_manager, tree)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
            self.canvas.get_tk_widget().grid(pady=0, sticky="w")  # A tk.DrawingArea.
            self.canvas.draw()
            self.toggler(tree)
            self.enable_matplotlib_options()
            self._view_pgf_data_merged = 0
            self._view_pgf_data_splitted = 0
            self.display_pgf_splitted.set(False)
            self.fig.canvas.mpl_connect('pick_event', lambda x: self.onpick(x,0))

    def enable_matplotlib_options(self):
        """ enables the matplotlib function like zooming, panning, moving, whenever cursor bounds are not toggled """ 
        self.RS.set_active(False)
        self.move = self.fig.canvas.mpl_connect('button_press_event', self.onPress)
        self.release = self.fig.canvas.mpl_connect('button_release_event', self.onRelease)
        self.mot = self.fig.canvas.mpl_connect('motion_notify_event', self.onMotion)
        self.zoom = self.fig.canvas.mpl_connect("scroll_event", self.zoom)
        return print("panning, zomming and movement activated")

    def switch_splitted_view(self,tree):
        '''will be called when the toggle button is pressed'''
        if self._view_pgf_data_splitted == 0:

            self.show_data_pgf_splitted_view(tree)
            self._view_pgf_data_splitted = 1

        else:
            self.show_data_pgf_merged_view(tree)
            self._view_pgf_data_splitted = 0



    # seems to be unused ..
    def switch_step_protocol_view(self,tree):
        '''When the toggle button to switch between merged and splitted data view is toggled, the text of the button as
        well as the data view will be changed immediately.
        @inut:  tree [TKinterTreeView]->the current tkinter tree object, not needed in this function, just piped to the next function
        @return: none
        @author dz '''
        self.show_recording_mode_analysis_functions("Voltage Clamp")
        if self.online_manager._data_view_STATE:    # splitted view-> change to merged view
            prnt_text = "Split data and step protocol"
            self.show_data_pgf_merged_view(tree)
            self.online_manager._data_view_STATE = 0
        else:
            prnt_text= "Merge data and step protocol" # merged view -> change to splitted view
            self.show_data_pgf_splitted_view(tree)
            self.online_manager._data_view_STATE = 1

        self.switch_voltage_view.configure(text=prnt_text)


    def onpick(self,event, viewmode):
        """Picks the line of the chart and redraws/recolors it when clicked
        input -> viewmode (not-splitted or splitted) """
        if isinstance(event.artist, Line2D):
            if viewmode == 0:
                for line in self.ax.lines:
                    #print(line)
                    if event.artist is line:
                        ind = event.ind[0]
                        #print(line)
                        line.set_color('white')
                        self.fig.canvas.draw_idle()
                    else:
                        ind = event.ind[0]
                        line.set_color("black")
                        line.set_alpha(0.5)
                        self.fig.canvas.draw_idle()

            else:
                for data_line,pgf_line in zip(self.ax.lines, self.ax2.lines):
                    if event.artist is data_line:
                        ind = event.ind[0]

                        # set the selection as highlighted white color
                        data_line.set_color('white')
                        data_line.set_linewidth(3)
                        data_line.set_alpha(1)

                        #same for the PGF file
                        pgf_line.set_color("white")
                        pgf_line.set_alpha(1)
                        pgf_line.set_linewidth(3)
                        self.fig.canvas.draw_idle()
                    else:
                        ind = event.ind[0]

                        # set the other traces in black and backgroundy
                        data_line.set_color("black")
                        data_line.set_alpha(0.5)
                        pgf_line.set_color("black")
                        pgf_line.set_alpha(0.5)
                        self.fig.canvas.draw_idle()

        

        


