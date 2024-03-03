from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from Backend.ExperimentTree.treeview_manager import *
import pyqtgraph as pg
import numpy as np
from Frontend.CustomWidget.draggable_lines import DraggableLines
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import Signal
# inheritage from qobject required for use of signal
from Backend.OfflineAnalysis.AnalysisFunctions.AnalysisFunctionRegistration import  AnalysisFunctionRegistration

class PlotWidgetManager(QRunnable):
    """ A class to handle a specific plot widget and it'S appearance, subfunctions, cursor bounds, .... """


    def __init__(self,vertical_layout_widget,database,tree_view,detection, frontend_style, toolbar_widget = None, toolbar_layout = None):
        """
        INIT:
        :param vertical_layout_widget: layout to be filled with the plotwidget created by this class
        :param manager_object: can be either online or offline analysis manager object
        :param tree_view:
        :param mode: can be either 0 (online analysis) or 1 (offline analysis)
        mode 0: values will be read directly from the .dat file
        mode 1: values will be read from the database provided from the offline manager object
        """
        pg.setConfigOption('foreground', 'k')
        self.plot_widget = pg.PlotWidget()
        self.detection_mode = detection

        try:
            print("removed old widget")
            vertical_layout_widget.takeAt(0)

        except Exception as e:
            print(e)

        self.frontend_style = frontend_style
        self.check_style()

        #self.show_pgf_plot_button = None
        self.show_pgf_plot = True
        self.show_plot_grid = True
        self.make_3d_plot = False
        self.ax1_si_prefix = ""
        self.si_prefix_handler = {"":1, "m":1000, "mu":1000**2, "n":1000**3, "p":1000**4, "f":1000**5}
        self.shift_sweeps = None

        self.canvas = FigureCanvas(Figure(figsize=(5,3)))
        self.vertical_layout = vertical_layout_widget

        self.toolbar_widget = toolbar_widget

        self.tree_view = tree_view

        self.database_handler = database
        self.time = None
        # neccessary for succesfull signal emitting
        super().__init__()

        self.left_bound_changed = CursorBoundSignal()
        self.right_bound_changed = CursorBoundSignal()

        #This can help for changing the dark theme correctly
        # all tuples of left and right bounds that will be plotted .. identified by its row number as a key
        self.coursor_bound_tuple_dict = {}

        # slot for the analysis function table widget: might be assigned to allow live plots
        # e.g. max_current | 1 | 10 | change | configure | checkbox
        self.analysis_functions_table_widget = None

        self.default_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

        self.live_analysis_info = None

    def check_style(self):
        # that the style sheet for the plot class
        if self.frontend_style.default_mode == 0:
            self.frontend_style.set_mpl_style_dark()
            self.draw_color = "white"
            self.ax_color = "white"
            try:
                self.canvas.figure.set_facecolor("#121212")
            except Exception as e:
                print("there might be no canvas")

        else:
            self.frontend_style.set_mpl_style_white()
            self.draw_color = "black"
            self.ax_color = "black"
            try:
                self.canvas.figure.set_facecolor("white")
            except Exception as e:
                print("there might be no canvas")
    def set_analysis_functions_table_widget(self,analysis_functions_table_widget):
        self.analysis_functions_table_widget = analysis_functions_table_widget
        print("table widget was set")


    def update_live_analysis_info(self,live_analysis_info):
        """
        update from extern functions and classes, such as analysis function seletion manager
        """
        #self.live_plot_info = pd.DataFrame(columns=["page", "col", "func_name", "left_cursor", "right_cursor"])
        self.live_analysis_info = live_analysis_info

    def check_live_analysis_plot(self, experiment_name, identifier, sweep_number = None):
        """
        calculate values to be plotted in the "live plot" feature during analysis
        @param item:
        @param table_widget:
        @return:
        @author: dz, 29.09.2022
        """
        print("checking live analysis")

        if  self.live_analysis_info is not None:

            for index,row in  self.live_analysis_info.iterrows():

                row_nr = row["page"]
                column = row["col"]
                fct = row["func_name"]
                lower_bound = row["left_cursor"]
                upper_bound = row["right_cursor"]
                live_plot = row["live_plot"]
                cursor_bound  = row["cursor_bound"]

                if cursor_bound:

                    self.show_draggable_lines((row_nr,column))

                    # only show live plot if also cursor bounds were selected
                    if live_plot:

                        analysis_class_object = AnalysisFunctionRegistration().get_registered_analysis_class(fct)

                        x_y_tuple = analysis_class_object().live_data(lower_bound, upper_bound, experiment_name,identifier, self.database_handler, None)
                        print(type(x_y_tuple))

                        if sweep_number:
                            sweep_number = sweep_number.split("_")
                            sweep_number = int(sweep_number[1])
                            x_y_tuple = [x_y_tuple[sweep_number-1]]

                        if x_y_tuple is not None:

                                    for tuple in x_y_tuple:
                                        if isinstance(tuple[1],list):
                                            y_val_list = [item * self.si_prefix_handler.get(self.ax1_si_prefix)  for item in tuple[1]]
                                            self.ax1.plot(tuple[0], y_val_list , c=self.default_colors[row_nr+column], linestyle='dashed')
                                        else:
                                            res = tuple[1]*self.si_prefix_handler.get(self.ax1_si_prefix)             
                                            self.ax1.plot(tuple[0], res, c=self.default_colors[row_nr+column], marker="o")
                        else:
                                    self.loggger.error("Tuple was None: is live plot function for" + fct + "already implemented ?")
                             
                else:
                    self.remove_dragable_lines(row_nr)

    def show_pgf_segment_buttons(self, experiment_name, series_identifier):


        # get the upper and most right ax value (lowest y and smallest x at [0])
        current_ax_height = self.ax1.get_ylim()[1]
        current_ax_length = self.ax1.get_xlim()[1]

        pgf_table = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name, series_identifier)
        pgf_table = pgf_table[pgf_table["selected_channel"] == pgf_table["selected_channel"].tolist()[0]]
        
        self.rect_list = []
        self.text_list = []
        total_duration = 0
        for d in range(len(pgf_table['duration'].values)):
            max_len = float(pgf_table['duration'].values[d]) * 1000

            rect = plt.Rectangle((total_duration+1/5*max_len, current_ax_height),  3/5*max_len , 3, facecolor='w', edgecolor='grey', alpha=1,label='Section 1')
            text = self.ax1.text(total_duration+0.5*max_len, current_ax_height + 1.5, f'Seg. {d+1}', fontsize=10, ha='center', va='center')

            self.rect_list.append(rect)
            self.text_list.append(text)

            self.ax1.add_patch(rect)
            total_duration += max_len

        # Variable to keep track of the currently clicked rectangle
        clicked_rect = None
        self.canvas.draw_idle()

    def onclick(self,event):
        global clicked_rect
        # Find which rectangle was clicked
        for rect, text in zip(self.rect_list, self.text_list):

            if rect.contains(event)[0]:

                # Set the color of the clicked rectangle to red and the others to white
                for r in self.rect_list:
                    r.set_facecolor('w')

                rect.set_facecolor('red')

                self.canvas.draw_idle()
                print(f'Clicked on rectangle with label: {text.get_text()}')
                break

    
    def extract_experiment_series_id(self,experiment_name, series_identifier):
        """
        extract_experiment_series_id _summary_

        Args:
            experiment_name (_type_): _description_
            series_identifier (_type_): _description_

        Returns:
            _type_: _description_
        """
        #print(experiment_name)
        #print(series_identifier)
        #print(sweep_name)
        # 1. extract the experiment name
        experiment_name = experiment_name.split("::")
        experiment_name = experiment_name[len(experiment_name)-1]
        #2. extract the series identifier
        series_identifier = series_identifier.split("::")
        series_identifier = series_identifier[len(series_identifier)-1]
        return experiment_name, series_identifier
    
    def table_view_sweep_clicked_load_from_database(self, experiment_name, series_identifier, sweep_name):
        """
        visualizes the sweep when clicked on it in the treeview
        @param item: treeview item, contains text at pos 0 and data request information at pos 3,0
        @return:
        :author: dz, modified 29.09.2022
        """
        print("sweep clicked")
        self.check_style() # either white or darkmode
        experiment_name, series_identifier = self.extract_experiment_series_id( experiment_name, series_identifier)
        series_df = self.database_handler.get_sweep_table_for_specific_series(experiment_name, series_identifier)
        series_df,self.ax1_si_prefix = self.scale_plot_data(series_df)

        #print(series_df)
        # get the meta data to correctly display y values of traces
        meta_data_df = self.database_handler.get_meta_data_table_of_specific_series(experiment_name,
                                                                 series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)

        self.time = self.get_time_from_meta_data(meta_data_df)

        self.create_new_subplots()

        data = series_df[sweep_name].values.tolist()
        data = np.array(data)

        if self.y_unit == "V":
            y_min, y_max = self.get_y_min_max_meta_data_values(meta_data_df, sweep_name)
            data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
            data = data*1000
       
        self.ax1.plot(self.time, data, self.draw_color)

        pgf_table_df = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name,
                                                                                        series_identifier)

        sweep_number = sweep_name.split("_")
        sweep_number = int(sweep_number[1])

        protocol_steps = self.plot_pgf_signal(pgf_table_df, data, sweep_number)

        print("Protocol Steps")
        print(protocol_steps)

        # @todo fix this asap replace 3 by len(protocol_steps)
        for x in range(0, 3):
            x_pos = int(protocol_steps[x] + sum(protocol_steps[0:x]))
            print(x_pos)
            self.ax1.axvline(x_pos, c='tab:gray')

        self.handle_plot_visualization(self.ax1_si_prefix)

    def table_view_series_clicked_load_from_database(self,experiment_name:str, series_identifier:str):
        """
        table_view_series_clicked_load_from_database _summary_
            plot the data for the current selection - either in 2d or 3d mode, with or without pgf
        Args:
            experiment_name (str): _description_
            series_identifier (str): _description_
        """
        self.check_style() # adjust the mpl figures to either white or darkmode
        experiment_name, series_identifier = self.extract_experiment_series_id(experiment_name, series_identifier)
        series_df = self.database_handler.get_sweep_table_for_specific_series(experiment_name, series_identifier)
        
        # to display e.g. 1*10-9 A as nA - the plotting data are adjusted to the biggest value in all column
        # this is dynamic, so 10-3 becomes mA and so on .. 
        series_df,self.ax1_si_prefix = self.scale_plot_data(series_df)
        # make sure to work with ther renamed series name
        series_name = self.database_handler.database.execute(f"select renamed_series_name from series_analysis_mapping where experiment_name = '{experiment_name}' and series_identifier = '{series_identifier}' and analysis_id = {self.database_handler.analysis_id} ").fetchdf()
        series_name = series_name["renamed_series_name"].unique()[0]
        # get the meta data to correctly display y values of traces
        meta_data_df = self.database_handler.get_meta_data_table_of_specific_series(experiment_name, series_identifier)
        self.y_unit = self.get_y_unit_from_meta_data(meta_data_df)
        self.time = self.get_time_from_meta_data(meta_data_df)
        column_names = series_df.columns.values.tolist()
        self.create_new_subplots()
        
        plot_offset = 0
        time_offset = 0
        # plot for each sweep
       
        for name in column_names:
            data = series_df[name].values.tolist()
            data = np.array(data)

            if self.y_unit == "V":
                y_min, y_max = self.get_y_min_max_meta_data_values(meta_data_df,name)
                data = np.interp(data, (data.min(), data.max()), (y_min, y_max))
                data = data*1000 # @todo weird heka property ! we have to double check for axon data !  
                
            if self.make_3d_plot:
                plot_offset += max(data) - min(data) # get the total distance
                time_offset += len(self.time)*0.005 # empirically determined
                self.show_pgf_plot = False

            self.ax1.plot(self.time+ time_offset, data + plot_offset, self.draw_color)

        # 3d plotting will add some offset to y and x and therefore the overlap wth the pgf signal is no given anymore
        if not self.make_3d_plot:
            # finally also the pgf file needs to be added to the plot
            # load the table
            pgf_table = self.database_handler.get_entire_pgf_table_by_experiment_name_and_series_identifier(experiment_name, series_identifier)
            pgf_table = pgf_table[pgf_table["selected_channel"] == pgf_table["selected_channel"].tolist()[0]]
            
            protocol_steps = self.plot_pgf_signal(pgf_table,data)
            for x in range(0,len(protocol_steps)):

                x_pos =  int(protocol_steps[x] + sum(protocol_steps[0:x]))
                print(x_pos)
                self.ax1.axvline(x_pos, c = 'tab:gray')

            
        self.vertical_layout.addWidget(self.canvas)
        self.handle_plot_visualization(self.ax1_si_prefix)

    def scale_plot_data(self,data_df:pd.DataFrame):
        """
        To display e.g. 1*10-9 A as nA - the plotting data are adjusted to the biggest value in all column
        The scaling is dynamic, so 10-3 becomes mA and so on .. 
        Args:
            data_df (_type_): df with data - each column represents one sweep
        Returns:
            _type_: scaled data df, 
        """
        max_df_value = max(data_df.max()) #identify the max value in the entire df and scale all data accordingly
        si_prefixes = ["","m","mu","n","p","f","a"] # milli, mikro, nano, pico,fempto, atto
        si_offset = 0
        while abs(max_df_value) < 1:
            max_df_value *= 1000
            si_offset += 1
        if si_offset>0:
            data_df = data_df*1000**si_offset
        return data_df,si_prefixes[si_offset]

    def create_new_subplots(self):
        """
        Create new subplots for data and pgf view. If pgf view is deseleted, ax 1 will be maximized
        """

        fig = self.canvas.figure
        fig.clf()

        axes = self.canvas.figure.subplots(nrows=2, ncols=1, sharex=True, sharey=False)
        self.ax1 = axes[0]
        self.ax2 = axes[1]
        self.ax2.set_visible(self.show_pgf_plot)
        if not self.show_pgf_plot:
            self.ax1.set_position([0.1, 0.1, 0.8, 0.8])  # Maximize ax1

    def handle_plot_visualization(self,si_prefix=None):
        """git s
        handle visualizations of the data and pgf plot
        @return:
        @author: dz, 21.07.2022
        """
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)

        self.ax2.spines['top'].set_visible(False)
        self.ax2.spines['right'].set_visible(False)
        #self.ax1.patch.set_alpha(0)
        #self.ax2.patch.set_alpha(0)
        # todo check for white or dakr mode
        ax_color = self.ax_color
        self.ax1.spines['bottom'].set_color(ax_color)
        self.ax1.spines['left'].set_color(ax_color)
        self.ax2.spines['bottom'].set_color(ax_color)
        self.ax2.spines['left'].set_color(ax_color)
        self.ax2.xaxis.label.set_color(ax_color)
        self.ax2.yaxis.label.set_color(ax_color)
        self.ax2.tick_params(axis='x', colors=ax_color)
        self.ax2.tick_params(axis='y', colors=ax_color)
        self.ax1.xaxis.label.set_color(ax_color)
        self.ax1.yaxis.label.set_color(ax_color)
        self.ax1.tick_params(axis='x', colors=ax_color)
        self.ax1.tick_params(axis='y', colors=ax_color)
        self.ax1.set_xticklabels(self.ax2.get_xticklabels())

        #plt.subplots_adjust(left=0.8, right=0.9, bottom=0.8, top=0.9)
        #self.ax1.autoscale()
        #self.ax2.autoscale()
        #self.canvas.figure.tight_layout()

        #self.canvas.figure.patch.set_alpha(0)
        #self.canvas.figure.tight_layout()
        if self.show_pgf_plot:
            self.ax2.set_xlabel('Time [ms]')
        else:
            self.ax1.set_xlabel('Time [ms]')
            
        if self.y_unit == "V":
            self.ax1.set_ylabel('Voltage [mV]')
            self.ax2.set_ylabel('Current [pA]')
        else:
            if si_prefix is not None:
                self.ax1.set_ylabel('Current [' + si_prefix + 'A]')
            else:
                self.ax1.set_ylabel('Current [A]')
            self.ax2.set_ylabel('Voltage [mV]')

        self.ax1.grid(self.show_plot_grid)
        self.ax2.grid(self.show_plot_grid)

        
        self.canvas.draw_idle()

    def plot_pgf_signal(self,pgf_table_df,data,sweep_number=None):
        """
        Function to decide whether step protocol or simple protocol needs to be created
        @param pgf_table_df:
        @param data:
        @return:
        @author: dz, 21.07.2022
        """
        increments = pgf_table_df['increment'].values.tolist()
        increments = np.array(increments, dtype=float)

        if np.all(increments ==0):
            return self.plot_pgf_simple_protocol(pgf_table_df,data)
        
        else:
            return self.plot_pgf_step_protocol(pgf_table_df,data,sweep_number)
 

    def plot_pgf_step_protocol(self,pgf_table_df,data, sweep_number_of_interest = None):
        """
        Create plots for multiple single traces according to information from the pgf dataframe
        @param pgf_table_df:
        @param data:
        @return:
        @author: dz, 21.07.2022
        """

        if sweep_number_of_interest is not None:
            # @todo: better bugfix ?
            sweep_number_of_interest = sweep_number_of_interest - 1

        # is there one step interval or are there multiple ones ?
        increments = pgf_table_df['increment'].values.tolist()
        increments = np.array(increments, dtype=float)

        # according to the number n of intervals sweep_number * n signals need to be created
        increment_intervals = np.where((increments>0)| (increments <0))[0]
        increment_interval_amount = len(increment_intervals)

        durations = pgf_table_df['duration'].values.tolist()
        if "start_time" in pgf_table_df.columns: # this is a bugfix for abf files ... 
            if pgf_table_df["start_time"].tolist()[0] != 0:
                durations[0] = float(durations[0]) - float(pgf_table_df["start_time"].tolist()[0])
        voltages = pgf_table_df['voltage'].values.tolist()
        holding = pgf_table_df['holding_potential'].values.tolist()


        number_of_sweeps = pgf_table_df['sweep_number'].values.tolist()

        # create a singal for each sweep
        for sweep_number in range(0,int(number_of_sweeps[0])):

            pgf_signal = np.zeros(len(data))
            total_duration = 0
            start_pos = 0
            protocol_steps = []

            # create signal over all blocks to cover the entire duration
            for n in range(0, len(durations)):
                
                d = 1000 * float(durations[n])
                total_duration += d
                protocol_steps.append(d)
                try:
                    end_pos = np.where(self.time > total_duration)[0][0]
                except IndexError:
                    # print("index error")
                    end_pos = len(data)

                if increments[n]!=0: # if the current block has no steps
                    max_val  =1000 * float(voltages[n]) + sweep_number *  1000 * float(increments[n])
                    #@todo read from the pgf table whether its a ramp or not 
                    if "Rheoramp" in pgf_table_df['series_name'].unique(): # here we have to create a ramp signal
                            starting_value = pgf_signal[1] 
                            x_steps = end_pos - start_pos
                            y_steps = max_val-starting_value
                            step_size = y_steps/x_steps
                            for n in range(start_pos,end_pos+1):
                                pgf_signal[n]=starting_value+(n-start_pos)*step_size    
                    else:
                            pgf_signal[start_pos:end_pos] = max_val
                else: # if the current block has no steps
                    if float(voltages[n]) == 0:
                        pgf_signal[start_pos:end_pos] = 1000 * float(holding[n])
                        #print(1000 * float(holding[n]))
                    else:
                        pgf_signal[start_pos:end_pos] = 1000 * float(voltages[n])
                        #print(1000*float(voltages[n]))

                start_pos = end_pos
            self.check_style()
            if sweep_number_of_interest is not None:
                if sweep_number != sweep_number_of_interest:
                    self.ax2.plot(self.time, pgf_signal, c='tab:gray')
                else:
                    self.ax2.plot(self.time, pgf_signal, c='r')
            else:
                self.ax2.plot(self.time, pgf_signal, c=self.draw_color)
            #print("finished sweep %s", sweep_number)

        return protocol_steps

    def plot_pgf_simple_protocol(self,pgf_table_df, data):
        """
        create a simple pgf trace signal
        @param pgf_table_df: df containign pgf information
        @param data:
        @return:
        @author: dz, 21.07.2022
        """

        # concat the y points where in the data plot slight grey lines should be drawn do indicate start of a pulse
        protocol_steps = []

        pgf_signal = np.zeros(len(data))

        try:
            # create traces

            durations = pgf_table_df['duration'].values.tolist()
            if pgf_table_df["start_time"].tolist()[0] != 0:
                durations[0] = float(durations[0]) - float(pgf_table_df["start_time"].tolist()[0])
            voltages = pgf_table_df['voltage'].values.tolist()
            holding = pgf_table_df['holding_potential'].values.tolist()
            total_duration = 0
            start_pos = 0
            for n in range(0,len(durations)):
                d = 1000 * float(durations[n])
                total_duration += d
                protocol_steps.append(d)

                try:
                    end_pos = np.where(self.time > total_duration)[0][0]
                except IndexError:
                    #print("index error")
                    end_pos = len(data)
                print(end_pos)
                if float(voltages[n])==0:
                    pgf_signal[start_pos:end_pos] = 1000 * float(holding[n])
                else:
                    pgf_signal[start_pos:end_pos] = 1000 * float(voltages[n])
                start_pos = end_pos

        except Exception as e:
            print(e)
        self.check_style()
        self.ax2.plot(self.time, pgf_signal, c = self.draw_color)

        return protocol_steps

    def get_recording_mode(self,meta_data):
        meta_dict = self.get_dict(meta_data)
        print(meta_dict)
        byte_repr = meta_dict.get('RecordingMode')
        print("found", byte_repr)
        if byte_repr == 3:
            print("recording mode : Voltage Clamp")
            return "Voltage Clamp"
        else:
            print("recording mode : Current Clamp")
            return "Current Clamp"

    def get_y_min_max_meta_data_values(self,meta_data_frame,sweep_name):
        """
        Return specific ymin and ymax for each sweep
        :param meta_data_frame:
        :param sweep_name:
        :return:
        """
        pos = meta_data_frame['Parameter'].tolist().index('Ymin')
        y_min = meta_data_frame[sweep_name].tolist()[pos]

        pos = meta_data_frame['Parameter'].tolist().index('Ymax')
        y_max = meta_data_frame[sweep_name].tolist()[pos]

        return float(y_min), float(y_max)

    def get_dict(self,meta_data):
        """ checks type of meta_data and returns anyway the dictionary of the meta data array"""
        if not isinstance(meta_data, dict):
            return dict(meta_data)
        else:
           return meta_data

    def get_y_min_max_meta_data_dict_values(self,meta_data_dict):

        y_min = float(meta_data_dict.get('Ymin'))
        y_max = float(meta_data_dict.get('Ymax'))

        return y_min,y_max

    def get_y_unit_from_meta_data_dict(self,meta_data_dict):
        return meta_data_dict.get('YUnit')

    def get_y_unit_from_meta_data(self,meta_data_frame):
        """
        YUnit is equal for all sweeps
        :param meta_data:
        :return:
        """
        ind = meta_data_frame['Parameter'].tolist().index('YUnit')
        return meta_data_frame['sweep_1'].tolist()[ind]

    def get_time_from_dict(selfself,dict):
        x_start = float(dict.get('XStart'))
        x_interval = float(dict.get('XInterval'))
        number_of_datapoints = int(dict.get('DataPoints'))
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        return time

    def get_time_from_meta_data(self,meta_data_frame):
        """
        handle database loading with a data frame
        @param meta_data_frame:
        @return:
        """
        x_start_pos = meta_data_frame['Parameter'].tolist().index('XStart')

        x_interval_pos = meta_data_frame['Parameter'].tolist().index('XInterval')

        number_of_points_pos = meta_data_frame['Parameter'].tolist().index('DataPoints')

        #bandwidth = meta_data_frame['Parameter'].tolist().index('Bandwidth')
        
        x_start= float(meta_data_frame['sweep_1'].tolist()[x_start_pos])
        x_interval = float(meta_data_frame['sweep_1'].tolist()[x_interval_pos])
        number_of_datapoints = int(meta_data_frame['sweep_1'].tolist()[number_of_points_pos])
        time = np.linspace(x_start, x_start + x_interval * (number_of_datapoints - 1) * 1000, number_of_datapoints)
        print("Xinterval = %d", x_start)
        print("Xinterval = %d", x_interval)
        print("Xinterval = %d", number_of_datapoints)
        return time

    def create_dragable_lines(self,row_col_tuple,rgb_color):
        """
        create_dragable_lines: as indicated by the name: this function creates two dragable line objects

        Args:
            row_col_tuple (_type_): _description_
            rgb_color (_type_): _description_

        Returns:
            _type_: _description_
        """

        print("creating new dragable lines")
        left_val =  0.2*max(self.time) +  5* (row_col_tuple[0] + row_col_tuple[1])
        right_val = 0.8*max(self.time) +  5 * (row_col_tuple[0] + row_col_tuple[1])

        scaling_factor = self.si_prefix_handler.get(self.ax1_si_prefix)
        left_coursor = DraggableLines(self.ax1, "v", left_val, self.canvas, self.left_bound_changed,row_col_tuple,scaling_factor ,rgb_color)
        right_coursor  = DraggableLines(self.ax1, "v", right_val, self.canvas, self.right_bound_changed,row_col_tuple, scaling_factor,rgb_color)

        self.left_coursor = left_coursor
        self.right_coursor = right_coursor

        print("adding", row_col_tuple, " to the dict")
        self.coursor_bound_tuple_dict[row_col_tuple] = (self.left_coursor,self.right_coursor)
        print(self.coursor_bound_tuple_dict.keys())


        #self.canvas.draw_idle()

        return left_val,right_val

    def show_draggable_lines(self,row_col_tuple,rgb_color=None):
        """
        showing existing courspr bounds
        @param row_number:
        @return:
        """

        

        coursor_tuple = self.coursor_bound_tuple_dict.get(row_col_tuple)

        left_val = coursor_tuple[0].XorY
        right_val = coursor_tuple[1].XorY
        
        if rgb_color is None: # if the color is none, it was already set 
            rgb_color = coursor_tuple[0].rgb_color

        self.left_coursor  =  DraggableLines(self.ax1, "v", left_val, self.canvas, self.left_bound_changed,row_col_tuple, self.ax1.get_ylim(),rgb_color)
        self.right_coursor  = DraggableLines(self.ax1, "v", right_val, self.canvas, self.right_bound_changed,row_col_tuple, self.ax1.get_ylim(),rgb_color)

        self.coursor_bound_tuple_dict.pop(row_col_tuple)
        self.coursor_bound_tuple_dict[row_col_tuple] = (self.left_coursor,self.right_coursor)

        #self.canvas.draw_idle()

        #self.ax1.draw_artist(self.left_coursor)
        #self.canvas.blit()
        #self.canvas.flush_events()


    def on_press(self,event):
        self.left_coursor.clickonline(event)
        self.right_coursor.clickonline(event)

    def remove_dragable_lines(self,row):
        print("row number")
        print(row)
        print(self.coursor_bound_tuple_dict)
        try:
            tuples_to_remove = []
            for k in self.coursor_bound_tuple_dict.keys():
                if k[0]==row:
                    tuples_to_remove.append(k)

            for t in tuples_to_remove:

                coursor_tuple = self.coursor_bound_tuple_dict.get(t)
                self.ax1.get_lines().remove(coursor_tuple[0].line)
                self.ax1.get_lines().remove(coursor_tuple[1].line)
                #self.coursor_bound_tuple_dict.pop(t)

            self.canvas.draw_idle()
        except Exception as e:
            print("all good")
            print(e)

# from QCore
class CursorBoundSignal(QObject):
    cursor_bound_signal = Signal(tuple)
