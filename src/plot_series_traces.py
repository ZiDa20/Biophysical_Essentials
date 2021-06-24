import tkinter.ttk as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from online_analysis_manager import *

class PlotSeriesTraces():

    def __init__(self):
        necessary = 0.0

    def selected_node(self, master_frame, tree, mode, data_list, directory_path, grid_column,grid_row):
        ''' A function that displays the selected series of the tree:
            @input  master_frame: the frame where the plot is intended to be placed
                    tree: the tkinter tree object where a the focused object can be gathered
                    mode: ? maybe unneeded
                    data_list: the datalist that was created when the treeview was created
                    directory_path: directory path: the path of the directory where the .dat file is stored
                    grid_coloumn: column where the plot should appear
                    grid_row:   row where the plot should appear
            @return ?
        '''

        # self.start_text.destroy()
        node_info = None
        node_info = tree.focus()  # returns a dictionary
        # print(self.node_info)
        # print(tree.item(self.node_info))

        # self.built_discard_button(self.tree_grid, self.node_info)

        #if self.canvas_frame:
         #   self.canvas_frame.destroy()

        self.trace_view_canvas = ttk.Frame(master_frame)
        self.trace_view_canvas.grid(column=grid_column, row=grid_row, rowspan=4, columnspan=2, sticky="n", pady=0)
        laenge = len(tree.item(node_info)['values'])
        values = tree.item(node_info)['values']
        print(tree.item(node_info))


        if len(tree.item(node_info)['values']) == 2:    #series level = 2
            series_name = tree.item(node_info)["text"]

            self.fig = Figure(figsize=(10, 6), dpi=90)
            self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.95, top=0.97, wspace=0.3, hspace=0.3)

            splitted_node_info = node_info.split(".dat_", 1)

            series_begin = [d for d, x in enumerate(data_list) if
                            x[0] == splitted_node_info[1] and x[1] ==series_name ]

            # in case of multiple series, check for the correct .dat file
            for d in series_begin:
                if data_list[data_list[d-1][0]==splitted_node_info[0]+".dat"]:
                    s_b = series_begin[series_begin.index(d)]

            for i in data_list[s_b+1:len(data_list)]:
                if "Series" in i[0]:
                    next_series_pos = data_list.index(i)
                    break
                else:
                    next_series_pos = len(data_list)

            file_path = [directory_path +"/"+splitted_node_info[0].split("Group",1)[1]+".dat"]
            data_bundle = heka_reader.Bundle(file_path[0])
            sweep_amount = (next_series_pos-s_b-1)//3
            self.draw_canvas_figure(111, tree, node_info, sweep_amount, data_bundle)

            '''
            if mode == 0:
                
            else:

                data_array = ['default']
                sweep_amount = 2

            self.draw_canvas_figure(111,data_array,sweep_amount,node_info,1,data_array)
            '''
            self.trace_view_canvas = FigureCanvasTkAgg(self.fig, master=self.trace_view_canvas)
            self.trace_view_canvas.get_tk_widget().grid(pady=0, sticky="nw")  # A tk.DrawingArea.
            self.trace_view_canvas.draw()

            return self.ax

            '''
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

            self.show_data_display_options(self.button_grid, tree)

            self.sweep_amount = self.online_manager.read_series_from_dat_file(tree, self.node_info)
            '''
            # print('sweep amount updated')
            # print(self.sweep_amount)
            '''
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

                    # self.split_pgf_and_data_plot(tree)
                    self.canvas.mpl_connect("scroll_event", self.zoom)
                    self.toggler(tree)

            if not self.RS.active:
                self.move = self.fig.canvas.mpl_connect('button_press_event', self.onPress)
                self.release = self.fig.canvas.mpl_connect('button_release_event', self.onRelease)
                self.mot = self.fig.canvas.mpl_connect('motion_notify_event', self.onMotion)
                self.fig.canvas.mpl_connect('pick_event', lambda x: self.onpick(x, 0))
            '''
        # @TODO (dz) - ad series view to sweep level

        '''
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
        '''

    def draw_canvas_figure(self, subplots, tree, node_info, sweep_amount, bundle = None):
        '''draw canvas of a series or a trace.
        @input viewmode:    None or 0: only data will be plotted,
                            1:  merged view with two ordinates will be plotted

                            '''
        # @TODO super uggly implementation: redo self.node_info better !

        self.ax = self.fig.add_subplot(subplots)
        self.time_list = []
        self.data_list = []

        '''if viewmode == 1:
            self.ax2 = self.ax.twinx()
            self.ax2.set_ylabel("Voltage (mV)")
        '''
        # self.show_recording_mode_analysis_functions(self.recording_mode)

        # [time_pgf, pgf] = self.online_manager.get_pgf_voltage(self.node_info)  # e.g. Group1_Series1

        print(sweep_amount)


        for i in range(sweep_amount):
            trace_index = tree.item(node_info)['values'] + [i, 0]
            # print(self.node_info)
            count = i + 1
            identifier = node_info + "_Sweep" + str(count) + "_Trace1"


            [time, data] = OnlineAnalysisManager().read_data_from_dat_file(trace_index,bundle)
                 #time, data =   OnlineAnalysisManager.interpolate_scale_data_time(time, data, self.online_manager, identifier, node_info)


            self.time_list.append(time)
            self.data_list.append(data)

            self.ax.plot(time, data, picker=True)
            self.ax.set_xlabel("Time (ms)")
            self.ax.set_ylabel("Current (pA)")
            # print(count-1)

            '''if viewmode == 1:
                if len(pgf) == 1:  # no step iterative step protocol
                    self.ax2.plot(time, pgf[0])
                else:
                    self.ax2.plot(time, pgf[count - 1])

            self.time = time
            '''
        '''if all([self.x2, self.x1]):
            self.ax.vlines(self.x1, self.ax.get_ylim()[0], self.ax.get_ylim()[1], color="white")
            self.ax.vlines(self.x2, self.ax.get_ylim()[0], self.ax.get_ylim()[1], color="white")
            self.x2 = None
            self.x1 = None
        '''