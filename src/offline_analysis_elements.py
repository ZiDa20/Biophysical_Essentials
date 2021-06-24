import tkinter.ttk as ttk
import tkinter as tk
from offline_analysis_manager import OfflineManager
import pandas as pd
from pandastable import Table, TableModel
from online_analysis_elements import OnlineAnalysisElements
from series_selection_dialog import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from multiple_series_in_a_file_dialog import *
from dialog_select_analysis_function import *

from dialog_fitting import *
from plot_series_traces import *
from gui_elements import ToolBar
from slider_widget import Slider
import meta_data_dialog
import raw_analysis as ra
from draggable_lines import DraggableLines

class OfflineElements():
    
    def __init__(self, appearance):

        self.frame = None
        self.appearance = appearance
        self.meta_path = None
        self.offline_manager = OfflineManager()
        self.dat_files = None
        self.dat_var = None
        self.dat_menu = None
        self.online = OnlineAnalysisElements(self.appearance)

        #@TODO (dz) maybe these settings can be saved and exported/reimported to shorten the selection process in case of repetitive analysis
        self.compare_series = tk.IntVar()
        self.compare_series.set(0)

        self.view_experiment_properties = tk.IntVar()
        self.view_experiment_properties.set(0)

        self.view_single_series = tk.IntVar()
        self.view_single_series.set(0)


    def offline_elements(self, frame):

        """ create the GUI for the offline Analysis """ 
        self.Note = frame
        self.metadataframe = ttk.Frame(self.Note.frames[0])
        self.metadataframe.grid(column = 1, row = 1)
        self.table_frame = ttk.Frame(self.Note.frames[0])
        self.table_frame.grid(column = 1, row = 2)


        self.offline_gui = ttk.Frame(self.Note.frames[1])
        self.offline_gui.grid()

        # DZ: just an initialization required here -> gridding will be performed in the specific functions
        self.canvas_frame = ttk.Frame(self.offline_gui)

        self.select_offline_analysis_directory_button = ttk.Button(self.offline_gui,
                                         text ="START NEW EMPTY ANALYSIS ",
                                         command = self.ask_directory)

        self.select_offline_analysis_directory_button.grid(row=1,column=1,columnspan=8,padx = 450, pady = 350, ipadx = 120, ipady = 60)

        #button for meta_data_path
        self.meta_entry = ttk.Entry(self.metadataframe, text = "Select your metadata file")
        self.meta_button = ttk.Button(self.metadataframe,
                                      text = "Select path for metadata",
                                      command = lambda: self.ask_file(self.meta_entry))
        ttk.Separator(self.metadataframe, orient=tk.HORIZONTAL).grid(row=2, columnspan=20, sticky="ew")
        
        self.meta_entry.grid(column = 1, row = 1, padx = 5, pady = 10)
        self.meta_button.grid(column = 2, row = 1, padx = 5, pady = 10)




        '''
        self.offline_button = ttk.Button(self.offline_gui,
                                         text ="Select a directory",
                                         command = lambda: self.ask_directory(self.tree))

        self.get_series_button = ttk.Button(self.offline_gui,
                                         text ="Select Series to Compare",
                                         command = self.show_series)

        ttk.Separator(self.offline_gui, orient=tk.HORIZONTAL).grid(row=2, columnspan=20, sticky="ew")
        self.offline_button.grid(column = 2, row = 1, pady = 10)
        self.parameter_list = ["Rseries","Cslow","Baseline","Cfast"]

        self.get_series_button.grid(column = 4, row = 1, pady = 10)

        self.parameter = ttk.Frame(self.Note.frames[1])
        self.parameter.grid()
        count = 1
        for i in self.parameter_list:
            label = ttk.Label(self.parameter, text = i)
            entry = ttk.Entry(self.parameter, text = "Default")
            label.grid(column = 1, row = count, pady = 2)
            entry.grid(column = 1, row = count + 1, pady = 2)
            count += 2
        '''
        # Beta implementation
        if len(self.offline_manager.directory_content_list)>1: # this will be only displayed if a selection has been made
            self.show_selection_window_1()


    def show_selection_window_1(self):
        experiments_overview = ttk.LabelFrame(master=self.offline_gui, text="Select your analysis type", width = 600, height = 80)
        experiments_overview.grid(column=2, row=3, columnspan = 2,rowspan = 2, sticky=tk.W, pady = 10,  padx = 20)
        experiments_overview.grid_propagate(0)

        # toggle button enable series view
        self.get_series_button = ttk.Checkbutton(master=experiments_overview,
                                                    style="Switch",
                                                    var=self.compare_series,
                                                    text ="Compare Series",
                                                    command = self.create_selected_series_notebook)#self.show_series)

        #self.get_series_button.grid(column=4, row=3, pady=10, padx = 10)
        self.get_series_button.grid(row=0,column = 0,padx = 20, pady = 20)

        self.view_series = ttk.Checkbutton(master=experiments_overview,
                                                    style="Switch",
                                                    var=self.view_experiment_properties,
                                                    text ="View Experiment Properties",
                                                    command = self.show_properties_filter_frame
                                                    )

        self.view_series.grid(row=0,column = 1,padx = 20, pady = 20)

        self.examine_directory = ttk.Checkbutton(master=experiments_overview,
                                                    style="Switch",
                                                    var=self.view_single_series,
                                                    text ="View Single Series",
                                                    )

        self.examine_directory.grid(row=0,column = 2,padx = 20, pady = 20)

        # toggle button open experiment evaluation
        # toggle button to compare series

        '''
        #overview_elements = ["Number of files", "C Slow Distribution", "Seal Values", "Pipette Resistence"]
        self.label_frame_1_selection = overview_elements[:]
        for i in overview_elements:
            text = ttk.Label(experiments_overview, text=i)
            text.grid(row=0, column=overview_elements.index(i) + 1)
            l = ttk.Checkbutton(experiments_overview, variable=self.label_frame_1_selection[overview_elements.index(i)])
            l.grid(row=0, column=overview_elements.index(i), padx=(10, 5))
        '''

    def show_properties_filter_frame(self):

        default_val = [2]
        default_val_name = ["Total number of files"]

        filter_frame = ttk.LabelFrame(master=self.offline_gui, text="Selected Experiment Properties Filters")
        for i in default_val_name:
            filter_list = ttk.Label(master = filter_frame,text=default_val_name[default_val_name.index(i)])
        add_filter_button = ttk.Button(master=filter_frame, text="Add a new filter")


        if self.canvas_frame:
            self.canvas_frame.destroy()

        self.canvas_frame = ttk.Frame(self.offline_gui)
        self.canvas_frame.grid(column=2, row=5, rowspan=3, columnspan=4, sticky=tk.N, pady=0)

        self.fig = Figure(figsize=(10, 7), dpi=90)
        self.axes = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()
        self.axes.bar(default_val_name,default_val, width = 0.25)



        '''
        self.add_filter_button =
        self.filter_frame_content = ttk.Label(filter_frame, text=self.dat_path)
        self.directory_frame_content.grid(pady=10, padx=5)
        directory_frame.grid(column=2, row=1, sticky=tk.W, padx=20) '''


    def create_selected_series_notebook(self):
        '''creates a new notebook with tabs according to the user selected series to be analyzed, a database to handle all the analysis will be initialized '''

        self.series_notebook_frame = ttk.LabelFrame(master=self.offline_gui, text="Compare Series Analysis", width=600,
                                           height=200)

        self.series_notebook = ToolBar(self.series_notebook_frame)

        series_names = self.offline_manager.get_available_series_names()
        s = SeriesSelectionDialog(series_names, self.offline_gui)

        # INIT (new, reload, overwrite) an analysis database
        self.offline_manager.init_database()

        # add the selected series to the database
        self.offline_manager.write_analysis_series_types_to_database(s.identifier_list)

        self.series_in_analysis_notebook = s.identifier_list

        self.series_notebook.event_handler(self.series_in_analysis_notebook, self.series_notebook_frame)

        self.series_notebook_frame.grid_propagate(0)
        self.series_notebook_frame.grid(column=2, row=5, columnspan=5, rowspan = 5,sticky=tk.NW, padx=20)

        self.series_notebook.note.bind("<<NotebookTabChanged>>", self.series_tab_changed)
        #
        # click the first tab to open --> self.series_notebook.frames[0]

    def series_tab_changed(self,event):
        ''' will be called whenever the tab is changed -> the tab specific side will be rebuilt "live" without any saved data'''

        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        frame_number = self.series_in_analysis_notebook.index(tab_text)
        master_frame = self.series_notebook.frames[frame_number]

        self.create_series_specific_analysis_view(master_frame,tab_text)

    def create_series_specific_analysis_view(self,master_frame,series_name):
        '''creates the shown elements for each tab according to the series (type)'''

        try:
            self.filter_label_frame.destroy()
        except:
            pass

        # recording mode frame
        label_text = ["Recording Mode of " + series_name]
        recording_mode_label_frame = ttk.LabelFrame(master=master_frame, text=label_text[0], width=100,
                                           height=100)

        recording_mode_label_frame_content = ttk.Label(recording_mode_label_frame,text="VoltageClamp")


        recording_mode_label_frame.grid(column=0,row=0)
        recording_mode_label_frame_content.pack()

        # filter frame
        self.filter_label_frame= ttk.LabelFrame(master=master_frame, text="Filter Options", width=100,
                                        height=100)


        # @TODO there is a need for global list to save the filter settings when switchign between tabs

        self.filter_label_frame.grid(column = 0, row=1 )
        self.create_filter_frontend_view(self.filter_label_frame,series_name)

        # tree view ?
        self.series_treeview_label_frame = ttk.LabelFrame(master=master_frame, text="Series selection")
        self.series_treeview_label_frame.grid(column=0,row =3)
        # create treeview from sublist ?

        specific_series_tree=ttk.Treeview(master = self.series_treeview_label_frame)
        data_list, specific_series_tree  = self.offline_manager.get_series_specific_treeview(specific_series_tree, series_name)

        # convert data list into database
        self.offline_manager.write_series_type_specific_experiment_and_sweep_information(data_list, series_name)

        specific_series_tree.pack()
        specific_series_tree.bind('<ButtonRelease-1>', lambda event: PlotSeriesTraces().selected_node(master_frame, specific_series_tree, 1, data_list, self.offline_manager.dat_files, 1, 1))
        # connect to series plot
        child_id = specific_series_tree.get_children()[-1]
        specific_series_tree.focus(child_id)
        specific_series_tree.item(child_id, open=True)
        subchilds=specific_series_tree.get_children(child_id)[-1]
        specific_series_tree.focus(subchilds)
        #specific_series_tree.item(subchilds, open=True)
        specific_series_tree.selection_set(subchilds)

        self.ax = PlotSeriesTraces().selected_node(master_frame, specific_series_tree, 1, data_list, self.offline_manager.dat_files, 1, 1)

        # select analysis functions according to the recording mode in a popup dialog

        self.analysis_label_frame = ttk.LabelFrame(master=master_frame, text="Analysis Function")
        self.analysis_label_frame.grid(column=3,row =1)

        analysis_functions_text = ""
        analysis_button_text = ""

        self.selected_analysis_text = ttk.Label(master = self.analysis_label_frame)
        self.selected_analysis_text.grid(column = 0, row = 0)

        self.select_analysis_function_button = ttk.Button(master=self.analysis_label_frame, command = lambda: self.get_analysis_function(master_frame,series_name,"Voltage Clamp"))
        self.select_analysis_function_button.grid(column=0,row=1)

        self.set_analysis_text(series_name)

        #select_coursor_bounds_button = ttk.Button(master = self.analysis_label_frame,text="Select Analysis Interval", command = lambda: self.activate_coursor_bounds)
        #select_coursor_bounds_button.grid(column=0,row=3)
        # set coursor bounds



        # apply filter and outsort data
        # trace plot
        # analysis functions plot

    def show_coursor_bound_selection_options(self, series_name, bound_number = None):
        if not bound_number:
            bound_number = 1

        self.left_bound = DraggableLines(self.ax, "v", 200)
        self.right_bound = DraggableLines(self.ax, "v", 300)

        l = len(self.offline_manager.series_specific_analysis_list)

        coursor_bound_label = ttk.Label(master=self.analysis_label_frame,text="Coursor Bounds " + str(bound_number) +" Selection")
        coursor_bound_label.grid(column=0,row=2, pady = 10)

        left_bound_label = ttk.Label(master=self.analysis_label_frame, text = "Left (ms): " + str(self.left_bound.XorY))
        left_bound_label.grid(column=0,row=3)

        left_bound_slider = Slider(master=self.analysis_label_frame, width = 100, height = 60, min_val = 0, max_val = 100, init_lis = [0], show_value = True)
        left_bound_slider.grid(column=0,row=4)


        right_bound_label=ttk.Label(master=self.analysis_label_frame,text="Right (ms): "+ str(self.right_bound.XorY))
        right_bound_label.grid(column=0,row=5)

        right_bound_slider = Slider(master=self.analysis_label_frame, width = 100, height = 60, min_val = 0, max_val = 100, init_lis = [0], show_value = True)
        right_bound_slider.grid(column=0, row=6)
        right_bound_slider.bind("<<Button-1>>", self.update_coursor_bounds)

        add_bounds_button = ttk.Button(master=self.analysis_label_frame,text="Add Coursor Bounds", command= lambda: self.add_coursor_bounds(series_name,self.left_bound.XorY,self.right_bound.XorY))
        add_bounds_button.grid(column=0,row=7)

        start_analysis_button = ttk.Button(master = self.analysis_label_frame, text = "Run " + series_name + " analysis only", command = lambda: self.start_single_series_analysis(series_name,self.left_bound.XorY,self.right_bound.XorY))
        start_analysis_button.grid(column =0, row = 8)

        start_fit_button = ttk.Button




    def add_coursor_bounds(self,series_name,lower_bound,upper_bound):
        for d in self.offline_manager.series_specific_analysis_list:
            if series_name in d[0][0]:
                tuple_list = []
                for multiples in d:
                    local_list = list(multiples)
                    number_of_bounds = len(local_list)
                    if local_list[number_of_bounds-2]==0 & local_list[number_of_bounds-1]==0:
                        # overwrite the initiation
                        local_list[number_of_bounds-2]=lower_bound
                        local_list[number_of_bounds-1]=upper_bound
                    else:
                        # append additional boundaries
                        local_list.append(lower_bound)
                        local_list.append(upper_bound)
                    tuple_list.append( tuple(local_list))
            self.offline_manager.series_specific_analysis_list[self.offline_manager.series_specific_analysis_list.index(d)]= tuple_list

        print("updated coursor bounds")

    def update_coursor_bounds(self):
        print("I have to update coursor bounds")


    def start_single_series_analysis(self,series_name,left_coursor, right_coursor):
        ''' Function to analyse a single type of series
         @input series_name (string),
                left_courser (int),
                right_coursor(int)
        @global '''

        self.offline_manager.write_coursor_bounds_to_database(left_coursor, right_coursor, series_name)
        self.offline_manager.read_trace_data_and_write_to_database(series_name)
        self.offline_manager.calculate_single_series_results_and_write_to_database(series_name)

        '''
        # update coursor bounds again
        self.add_coursor_bounds(series_name, left_coursor, right_coursor)



        # get series specific data traces
        series_data = self.offline_manager.get_multiple_series_data([series_name])

        # @TODO write these data into the datbase

        # each block of sweeps of one specific series will end with the realated time array
        time_array_positions = [z for z, d in enumerate(series_data) if "Time" in d[2]]

        # iterate through all series
        for time_position in time_array_positions:

            print("series " + str(time_array_positions.index(time_position)))
            array_pos = time_array_positions.index(time_position)
            if array_pos==0:
                start_v = 0
            else:
                start_v = time_array_positions[array_pos-1]+1

            # iterate through all sweeps of a specific series
            for sweep in range(start_v,time_position):
                print("sweep " + str(sweep))
                time = series_data[time_position][3]
                data = series_data[sweep][3]
                raw_analysis_class_object = ra.AnalysisRaw(time,data)
                result_list = []

                # iterate through list of series specific analysis functions and coursor bounds
                for d in self.offline_manager.series_specific_analysis_list:

                    if series_name in d[0][0]:
                        for analysis_function in range(1,len(d)):
                            print("Analysis function " + d[analysis_function][0])
                            # run through all analysis functions

                            for coursor_bound_iteration in range(1,len(d[analysis_function]),2):
                                # run through all coursor bounds of a specific analysis function

                                print("Left Bound" + str(d[analysis_function][coursor_bound_iteration]))
                                print("Right Bound" + str(d[analysis_function][coursor_bound_iteration+1]))


                                raw_analysis_class_object.lower_bounds=d[analysis_function][coursor_bound_iteration]
                                raw_analysis_class_object.upper_bounds=d[analysis_function][coursor_bound_iteration+1]

                                raw_analysis_class_object.construct_trace()
                                raw_analysis_class_object.slice_trace()

                                result = raw_analysis_class_object.call_function_by_string_name(d[analysis_function][0])

                                print("result: " + str(result))
                                result_list.append(result)

                series_data[sweep].append(result_list)
        '''


    def plot_single_series_analysis_results(self):
        '''to be continued here'''
        print("in development")


    def show_single_analysis_button(self,series_name):


        for d in self.offline_manager.series_specific_analysis_list:
            if not series_name in d[0][0]:
               tk.messagebox.showerror("Invalid Coursor Bounds Error", "You have not set valid coursor bounds")


    def set_analysis_text(self,series_name):
        tmp_str = ""
        function_list = self.offline_manager.read_series_type_specific_analysis_functions_from_database(series_name)

        if function_list:
            for f in function_list:
                tmp_str = tmp_str + f + " \n "

            analysis_functions_text = "You have selected: \n" + tmp_str
            analysis_button_text = "Change"
            self.show_coursor_bound_selection_options(series_name)
        else:
            analysis_functions_text = "You have to select a function first"
            analysis_button_text = "Select Analysis Function"

        '''
        if self.offline_manager.series_specific_analysis_list:
            tmp_str = ""
            for d in self.offline_manager.series_specific_analysis_list:
                if series_name in d[0][0]:
                    for z in range(1,len(d)):
                        tmp_str= tmp_str + d[z][0] + " \n "
            analysis_functions_text = "You have selected: \n" + tmp_str
            analysis_button_text = "Change"
            self.show_coursor_bound_selection_options(series_name)

        else:
            analysis_functions_text = "You have to select a function first"
            analysis_button_text = "Select Analysis Function"
        '''
        self.selected_analysis_text.configure(text=analysis_functions_text)
        self.select_analysis_function_button.configure(text=analysis_button_text)


    def get_analysis_function(self,master,series_name,recording_mode):
        # open pop up series selection dialog
        function_list = ra.AnalysisRaw().get_elements(recording_mode)
        s=SeriesSelectionDialog(function_list,master)
        function_selection = s.identifier_list

        self.offline_manager.write_analysis_function_to_database(function_selection, series_name)

        if self.offline_manager.series_specific_analysis_list:
            for d in self.offline_manager.series_specific_analysis_list:
                if d[0][0]==series_name:
                    local_list = []
                    local_list.append((series_name, 0, 0))
                    for sel in function_selection:
                        local_list.append((sel, 0, 0))
                    self.offline_manager.series_specific_analysis_list[self.offline_manager.series_specific_analysis_list.index(d)]=local_list
        else:
            # list is still empty
            local_list = []
            local_list.append((series_name,0,0))
            for sel in function_selection:
                local_list.append((sel, 0, 0))
            self.offline_manager.series_specific_analysis_list.append(local_list)

        print(function_selection)
        self.set_analysis_text(series_name)


    def create_series_specific_tree_view(self,master,treeview,series_name):
        tree = self.offline_manager.get_series_specific_treeview(treeview, series_name)


    def create_filter_frontend_view(self,master,series_name):

        for triple in self.offline_manager.filter_list:
                elem = triple[0]
                text = ttk.Label(master,text=elem)
                text.grid(column=1, row = self.offline_manager.filter_list.index(triple))

                slider = Slider(master, width = 200, height = 60, min_val = -100, max_val = 100, init_lis = [triple[1],triple[2]], show_value = True)
                slider.grid(column=2, row = self.offline_manager.filter_list.index(triple))

        self.add_filter_options_button = ttk.Button(master,text="Add Filter", command = lambda: self.add_series_filter_popup_handler(master,series_name))
        self.add_filter_options_button.grid(column=1, row = len(self.offline_manager.filter_list))
        #master.grid()

    def add_series_filter_popup_handler(self,master,series_name):
        try:
            self.add_filter_options_button.destroy()
        except:
            pass

        additional_filter_elements= meta_data_dialog.MetaDataDialog(master).identifier_list
        for i in additional_filter_elements:
                # @TODO (dz) maybe you should add more appropriate default values according to their use in analysis
                self.offline_manager.filter_list.append((i, -5, +5))

        self.create_filter_frontend_view(master,series_name)

    def show_series(self):

        try:
            self.filter_frame.grid_forget()
        except:
            pass

        # de-toggle all other analysis options
        self.view_single_series.set(0)
        self.view_experiment_properties.set(0)

        # show all available series in a pop up
        series_names = self.offline_manager.get_available_series_names()
        input_list = []
        input_list.append(self.offline_gui)
        input_list.append(series_names)

        s = SeriesSelectionDialog(series_names,self.offline_gui)
        print(s.identifier_list)

        # select series to compare and get data


        additional_height = 0
        if len(s.identifier_list)>2:
            additional_height = 20 * (len(s.identifier_list)-2)

        self.filter_frame = ttk.LabelFrame(master=self.offline_gui, text="Compare Series Analysis", width = 600, height = 100+additional_height)
        label_text = ["Selected Series: \n   "]

        for i in s.identifier_list:
            label_text = [label_text[0] + i + "\n   "]

        filter_list = ttk.Label(master=self.filter_frame, text=label_text[0])

        #change_series_selection = ttk.Button(master=self.filter_frame,text="Change Series",command=self.show_series)

        #start_comparisson_button = ttk.Button(master=self.filter_frame,text="Select Analysis Function(s)",command = lambda:  self.get_data_arrays(s.identifier_list))

        action_potential_fitting_button = ttk.Button(master = self.filter_frame, text = "Action Potential Fitting",command = lambda: self.open_fitting_procedure_from_dialog(self.data_struct) )

        self.filter_frame.grid_propagate(0)
        self.filter_frame.grid(column=1, row=10, columnspan = 1, sticky=tk.NW, padx = 20)


        filter_list.grid(column=1,row=1, padx = 20, pady = 10)
        #change_series_selection.grid(column=2, row = 1, padx = 40)
        #start_comparisson_button.grid(column=3, row = 1, padx = 40)
        action_potential_fitting_button.grid(column=3, row = 2, padx = 40)

    def open_fitting_procedure_from_dialog(self, data_list):
        print(data_list)
        fitting = DialogFittingClamp(self.offline_gui,data_list,"Current Clamp")

    def get_offline_analysis_functions_from_dialog(self,series_list,data_list):
        d = DialogSelectAnalysisFunction(self.offline_gui,series_list,data_list)


#    self.get_data_arrays(s.identifier_list))
    def get_data_arrays(self,series_names_list):
        '''@input series_names_list: list of names as strings'''

        if True: #self.meta.check_for_multiple_series_in_a_file(self.meta.directory_content_list,series_names_list):
          d = MultipleSeriesInAFileDialog(self.offline_gui)
          print(d.decission)


        self.data_struct = self.offline_manager.get_multiple_series_data(series_names_list)
        print(self.data_struct)

        #self.get_offline_analysis_functions_from_dialog(series_names_list,data_struct)

    def ask_file(self, widget):
        """ set the metadata place """ 
        self.meta_path = self.offline_manager.ask_file(self.Note.frames[0])
        widget.delete(0,"end")
        widget.insert(0,self.meta_path)
        self.drawing()

    def ask_directory(self):

        self.tree_grid = ttk.Frame(self.offline_gui)
        self.tree_grid.grid(column=1, row=5, sticky=tk.N)
        self.tree_grid.grid_columnconfigure(0, weight=1)
        self.tree_grid.grid_rowconfigure(0, weight=1)

        try:
            self.filter_frame.destroy()
        except:
            pass

        try:
            self.directory_frame.destroy()
        except:
            pass

        tree = ttk.Treeview(master=self.tree_grid)

        self.dat_files, self.dat_path, tree = self.offline_manager.ask_directory(self.Note.frames[1], tree)

        self.select_offline_analysis_directory_button.destroy()
        #self.dat_options(self.dat_files)
        tree.heading("#0", text="Files in directory")
        tree.grid(column=1, row=6, sticky=tk.N, padx=5, pady=20)
        tree.bind('<ButtonRelease-1>', lambda event: self.treeview_clicked(self.offline_gui, tree, 1, self.offline_manager.directory_content_list,
                                                                           self.offline_manager.dat_files, 2, 5))
        self.tree = tree
        self.show_selection_window_1()

        self.directory_frame = ttk.LabelFrame(master=self.offline_gui, text= "Selected Directory")
        self.directory_frame_content = ttk.Label(self.directory_frame, text = self.dat_path)
        self.directory_frame_content.grid(pady=10, padx=5)
        self.directory_frame.grid(column=2, row=1, sticky=tk.W, padx = 20)

        self.change_directory_button = ttk.Button(self.offline_gui,
                                         text ="Change directory",
                                         command = self.ask_directory)

        self.change_directory_button.grid(column=3, row=1, sticky=tk.W)


    def treeview_clicked(self,master,tree,mode,data_list,data_path,column,row):
        if len(tree.item(tree.focus())['values']) > 1:
            self.set_displayed_analysis_mode(0,0,1)
        PlotSeriesTraces().selected_node(master, tree, mode, data_list,
                                         data_path,column,row)

    def set_displayed_analysis_mode(self,cmp_series,vw_exprmnt,vw_srs):
        ''' all input variables must be either 0 or 1'''
        self.compare_series.set(cmp_series)
        self.view_experiment_properties.set(vw_exprmnt)
        self.view_single_series.set(vw_srs)

    def dat_options(self, data):

        """ get the dropdown menu for the detected dat files """
        if self.dat_menu:
            self.dat_menu.destroy()

        if len(data) > 0:
            self.dat_var = tk.StringVar()
            self.dat_menu = ttk.OptionMenu(self.offline_gui,self.dat_var, *data, command = self.get_dat)
            self.dat_menu.grid(column = 1, row = 1, padx = 10, pady = 10)
            self.checkbox = ttk.Checkbutton(self.offline_gui, text = "Use as representative:", command = self.get_dat)
            self.checkbox.grid(column = 3, row = 1, padx = 5, pady = 10)
        else:
            tk.messagebox.showinfo("Invalid Path", "Please use a path that contains .dat files for the analysis")

    def get_dat(self,dropdown_file):
        print("here is the current selection")
        print(dropdown_file)
        print(self.dat_path + "/" + dropdown_file)

    def drawing(self):
        """ Draw an Example Trace that might be later used for the Analysis
        """
        """ What is missing?: Function selector? """
        #print the table for the metadata
        self.metadata = pd.read_csv(self.meta_path, delimiter = "\t")
        pt = Table(self.table_frame ,dataframe = self.metadata, showtoolbar = True)
        pt.redraw()
        pt.show()


