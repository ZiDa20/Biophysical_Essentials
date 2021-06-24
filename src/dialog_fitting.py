import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CurrentClamp import *
from online_analysis_manager import *
import statistics
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
#from frontend import GuiEtools



class DialogFittingClamp(tkinter.simpledialog.Dialog):

    def __init__(self, parent,data_list,mode):
        '''
        @input series_list: unique list of selected series
               data_list= all_data_for the selected series
               mode: Current or Voltage clamp
        '''
        self.data_list = data_list
        self.mode = mode
        self.CurrentClamp = CurrentClamp()
        self.canvas = None
        self.parent = parent
        self.OfflineManager = OnlineAnalysisManager()
        self.OfflineManager.fitting_dictionary = None
        tkinter.simpledialog.Dialog.__init__(self, self.parent)
        #self.master = parent

    def body(self, master):

        entry_frame = ttk.Frame(master)
        entry_frame.grid(column = 2, row = 1, sticky = "e")
        experiment = list(set([i[0] for i in self.data_list]))
        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.grid(column = 1, row = 1, rowspan = 2, sticky = "n")
        series = set([i[1] for i in self.data_list])
    
        #self.experiment_options.set(self.experiment)
        self.experiment_list = ttk.Combobox(entry_frame,values = experiment)
        self.experiment_list.current(0)
        self.experiment_list.grid(column = 2, row = 1, sticky = "e", pady = 5)
        self.callback = experiment[0]
        self.plotting_function(master, self.data_list, experiment = self.callback)
        self.experiment_list.bind("<<ComboboxSelected>>", lambda event: self.experiment_callback(event,master))
        
        if self.mode == "Voltage Clamp":
            ap_parameters = ["Slope","Conductance","Vhalf","Vrev"]
            entry_list = []
            for i, t in enumerate(ap_parameters):
                label = ttk.Label(entry_frame, text = t)
                entry = ttk.Entry(entry_frame)
                entry_list.append(entry)
                label.grid(column = 1, row = i+2)
                entry.grid(column = 2, row = i+2)
        
        else:
            start_fitting = ttk.Button(entry_frame, text = "Start Fitting",
                                       width = 18,
                                       command = lambda: self.plotting_function(master,
                                                                                self.data_list,
                                                                                experiment = self.callback,
                                                                                fitting = True))
            start_fitting.grid(column = 3, row = 1, sticky = "e", padx = 5, pady = 5)
            quit_button = ttk.Button(entry_frame, text = "Quit Analysis", command = self.parent.destroy, width = 18)
            quit_button.grid(column = 4, row = 1, sticky = "w", padx = 5, pady = 5)
            ttk.Separator(master = entry_frame).grid(row=2, sticky="ew", columnspan = 10, ipadx=100, pady = 10)
            self.ap_parameter_list = []
            for i,t in enumerate(["Group","Window","Prominence","mv threshold"]):
                ap_fitting_label = ttk.Label(entry_frame, text = t)
                ap_fitting_entry = ttk.Entry(entry_frame)
                ap_fitting_label.grid(column = 2, row = i+3, pady = 5)
                ap_fitting_entry.grid(column = 3, row = i+3, pady = 5)
                self.ap_parameter_list.append(ap_fitting_entry)

            # set the default value for the entries 
            self.ap_parameter_list[1].insert(0,self.CurrentClamp.get_window_length())
            self.ap_parameter_list[2].insert(0,self.CurrentClamp.get_prominence())
            self.ap_parameter_list[3].insert(0,self.CurrentClamp.get_mv_threshold())


            ap_parameters = ["Onset:","Half-Width:","Max Value:","Repolarization Value:","80% Width","Number of Events","dv/dt Max", "dv/dt Min"]
            self.entry_list_mean = []
            self.entry_list_sem = []
            for i, t in enumerate(ap_parameters):
                label = ttk.Label(entry_frame, text = t)
                entry = ttk.Entry(entry_frame)
                entry_2 = ttk.Entry(entry_frame)
                self.entry_list_mean.append(entry)
                self.entry_list_sem.append(entry_2)
                label.grid(column = 2, row = i+7, pady = 5)
                entry.grid(column = 3, row = i+7, pady = 5, padx = 5)
                entry_2.grid(column = 4, row = i+7, pady = 5, padx = 5)
        
        # here we still need to add the commands to got through the fittings
        ttk.Separator(master = entry_frame).grid(row=20, sticky="ew", columnspan = 10, ipadx=100, pady = 10)
        start_analysis_button = ttk.Button(entry_frame, text = "Start Automatic Analysis", width = 18, style = "AccentButton")
        start_analysis_button.grid(column = 3, row = 22, padx = 5, ipady = 15, pady = 5)
        start_manual_analysis_button = ttk.Button(entry_frame, text = "Export Manual Analysis", width = 18, style = "AccentButton")
        start_manual_analysis_button.grid(column = 4, row = 22, padx = 5, ipady = 15, pady = 5)


    def experiment_callback(self,event, experiment):
        self.callback = self.experiment_list.get()
        
        

    def plotting_function(self, master,  data_trace, experiment = None, fitting = None):

        self.OfflineManager.fitting_dictionary = {"onset":{"index": [],"data": []},
                                                "half_width": {"index": [], "data": []},
                                                "max_value":{"index": [], "data": []},
                                                "repolarizing_value": {"index": [], "data": []},
                                                "80% width":{"index": [], "data":[]},
                                                "event number":{"index":[], "data":[]},
                                                "dv/dt max": {"index":[], "data":[]},
                                                "dv/dt min": {"index": [], "data":[]}}

        if self.canvas:
            print("self.canvas found..")
            self.canvas.get_tk_widget().destroy()

        
        ax = self.draw_canvas() # draws the canvas

        self.show_plot(ax,data_trace, experiment)
        
        if fitting:
            self.start_fitting(data_trace,experiment,ax)

    def show_plot(self,ax, data_trace,experiment):

        """ Show the original plot of the data selected """ 
        for i in data_trace:
            if experiment == i[0]:
                if "Series" in i[2]:
                    print("number of series detected..")
                    ax.plot(i[3], picker = True)
                    ax.set_xlabel("Time (ms)")
                    ax.set_ylabel("Current (pA)")
                    self.canvas.draw_idle()

    def start_fitting(self, data,experiment, ax):
        """ fitting Gui for single AP detection """
        try:
            window = int(self.ap_parameter_list[1].get())
            if isinstance(window, int):
                print("Choosing the window for filtering")
                self.CurrentClamp.set_window_length(window)
            
        except:
            print("Please select a integer and not a string")

        try:
            prominence = float(self.ap_parameter_list[2].get())
            if isinstance(prominence, float):
                #ToDo adjust and test mv_threshold changes
                self.CurrentClamp.set_prominence(prominence)

        except: 
            print("no new prominence setted")

        try:
            threshold = float(self.ap_parameter_list[3].get())
            if isinstance(threshold,float):
                self.CurrentClamp.set_mv_threshold(threshold)
        except:
            print("no new threshold setted")

        for i in data:
            """ get the time for the selected series """
            if experiment == i[0]:
                if "Time" in i[2]:
                    deriv_time = self.CurrentClamp.get_time_derivative(i[3])
                    print("the time is %s:", deriv_time)
        
        for i in data:
            "get the data for the selected series"
            if experiment == i[0]:
                if "Series" in i[2]:
                    first_deriv, second_deriv, third_deriv = self.CurrentClamp.get_derivatives_data(i[3])
                    max_index, maxpeak = self.CurrentClamp.get_peak_second_derivative(second_deriv)
                    max_data_index, max_data = self.CurrentClamp.get_max_value_data(i[3])
                    third_index_min, third_min = self.CurrentClamp.get_sliced_third_min(third_deriv)
                    peaks_width_half, peaks_width_eight, event_number,peaks = self.CurrentClamp.get_half_width(i[3])
                    up_slope = self.CurrentClamp.get_slope(first_deriv, deriv_time, max_index, max_data_index)
                    down_slope = self.CurrentClamp.get_slope(first_deriv, deriv_time, max_data_index, third_index_min)
                    print(up_slope)
                    

                    self.OfflineManager.fitting_dictionary["onset"]["index"].append(max_index)
                    self.OfflineManager.fitting_dictionary["onset"]["data"].append(maxpeak)
                    self.OfflineManager.fitting_dictionary["max_value"]["index"].append(max_data_index)
                    self.OfflineManager.fitting_dictionary["max_value"]["data"].append(max_data)
                    self.OfflineManager.fitting_dictionary["repolarizing_value"]["index"].append(third_index_min)
                    self.OfflineManager.fitting_dictionary["repolarizing_value"]["data"].append(third_min)
                    self.OfflineManager.fitting_dictionary["dv/dt max"]["data"].append(up_slope)
                    self.OfflineManager.fitting_dictionary["dv/dt min"]["data"].append(down_slope)

                    # check if multiple peaks are there, add and appropiate threshold for the peaks
                    if peaks_width_half:
                        print("found peak with half_width")
                        self.OfflineManager.fitting_dictionary["half_width"]["data"].append(peaks_width_half[0][0])
                        ax.hlines(*peaks_width_half[1:], color="red")
                        ax.plot(peaks, i[3][peaks],"x", color = "blue")
                    if peaks_width_eight:
                        self.OfflineManager.fitting_dictionary["80% width"]["data"].append(peaks_width_eight[0][0])
                        ax.hlines(*peaks_width_eight[1:], color = "black")
                   
                    self.OfflineManager.fitting_dictionary["event number"]["data"].append(event_number)
                    
               
                    #draw the lines for the half width
                    
                    

        print(self.OfflineManager.fitting_dictionary)
        ax.scatter(x = self.OfflineManager.fitting_dictionary["onset"]["index"],
                   y = self.OfflineManager.fitting_dictionary["onset"]["data"],
                   color = "green",
                   marker = "x")

        ax.scatter(x = self.OfflineManager.fitting_dictionary["repolarizing_value"]["index"],
                   y =self.OfflineManager.fitting_dictionary["repolarizing_value"]["data"],
                   color = "red",
                   marker = "x", 
                   alpha = 1)

        legend_elements = [Line2D([0],[0], color = "skyblue", lw = 4, label = "Traces"),
                           Line2D([0],[0], color = "red", lw = 4, label = "Half-Width"),
                           Line2D([0],[0], color = "black", lw = 4, label = "80% Width"),
                           Line2D([0],[0], marker = "x", color = "green", label = "AP onset",
                           markerfacecolor="green", markersize = 10),
                           Line2D([0],[0], marker = "x", color = "red", label = "AP Hyperpolarization value",
                           markerfacecolor="green", markersize = 10)]

        ax.legend(handles=legend_elements, loc='upper right')
 
        self.canvas.draw_idle()
        self.write_fittings()

    def write_fittings(self):
        """ writes the fitted values into the fitting dictionary """
        for i,t,z in zip(self.entry_list_mean, self.entry_list_sem, self.OfflineManager.fitting_dictionary.keys()):
            try: 
                i.delete(0,tk.END)
                t.delete(0,tk.END)
                i.insert(0,round(statistics.mean(self.OfflineManager.fitting_dictionary[z]["data"]),5))
                t.insert(0,round(statistics.stdev(self.OfflineManager.fitting_dictionary[z]["data"]),5))
            except:
                pass

    def buttonbox(self):
       pass

    def draw_canvas(self):
        """ draws the canvas of the fitting plot """
        self.fig = Figure(figsize=(9, 6), dpi=90)
        ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.1, bottom=0.07, right=0.95, top=0.97, wspace=0.3, hspace=0.3)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().grid(column = 1, row = 1, sticky = "n")
        return ax

    def get_theme(self):
        self.theme = GuiEtools.get_appearance(appearance)






            
            
        



