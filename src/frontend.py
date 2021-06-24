import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import logging as lg
from gui_elements import ToolBar
from pandastable import Table, TableModel
import pandas as pd
from main import patch_structure
import os
from backend_manager import *
from backend_elements import *
from online_analysis_manager import *
from online_analysis_elements import *
import pandastable
from matplotlib.widgets import RectangleSelector
from tkinter_camera import *
from offline_analysis_elements import OfflineElements
from offline_analysis_manager import OfflineManager
import welcome_page_elements

import sys



plt.style.use('dark_background')
mpl.use('TkAgg')
plt.rcParams['axes.facecolor']='#333333'
plt.rcParams['figure.facecolor'] ='#333333'
mpl.rc('axes',edgecolor='black')

from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('../QT_GUI/main_window.ui', self)
        self.show()

from functools import partial
current_dir = os.path.dirname(os.path.abspath(__file__))
Form, Base = uic.loadUiType(os.path.join(current_dir, '../QT_GUI/main_window.ui'))


class FrontPage(Base, Form):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        #uic.loadUi('../QT_GUI/self_config_notebook_widget.ui', self)
        self.setupUi(self)

        buttons = (self.self_configuration, self.online_analysis, self.offline_analysis, self.statistics)
        for i, button in enumerate(buttons):
            button.clicked.connect(partial(self.notebook.setCurrentIndex, i))

class GuiEtools():

    def __init__(self,master=None, appearance = None):

        if master:
            master.destroy()

        self.window = tk.Tk()
        self.window.title("Intra Cellular Recording Mode")
        self.window.geometry("1500x1000")
        self.path_set = None # second Window
    
        #Backend connection to Patchmaster
        self.bm = BackendManager()
        self.be = BackendElements()
        self.online_manager = OnlineAnalysisManager()
        self.offline = OfflineElements(appearance)
        
        # specify style
        self.s = ttk.Style(self.window)
        self.appearance = appearance
        self.ona = OnlineAnalysisElements(self.appearance)
        self.cam = BayerCamera(self.ona)
        self.themes_call()
        self.s.theme_use(self.appearance)
        self.set_darkmode()
        #apply the self maded theme


        #implement menu bar
        self.widgets_menu()
        self.stats_notebook = None
        self.tools = None
        self.figure_frame = None #frame for the Figure to hold
        self.canvas = None
        
        #Notebook implementation with class
        self.Note = ToolBar(self.window)
        self.Note.notebook = None


        # necessary for the tabs within the notebook
        self.statistics = ["Statistical tests", "Parameter", "Quality Control"]
        self.online_analysis=["Live Data","Labbook"]
        self.offline_analysis = ["Metadata","Start an Analysis","Visualization","Report"]
        self.configuration = ["Experiment Initialization","Batch Settings","Communication Log", "Camera"]

        # fetching the path for the metadata as well as the data files
        self.metadata_path = None
        self.analysis_path = None


    def widgets_menu(self):

        """ Function to add the widgets to the GUI 
        Menubar --> Load configurations, enable visualizations, statistical analysis ect
        Checkbuttons -> open Metadata, Dataframes ect.
        Input boxes -> annotate the Path
        Buttons -> induce actions such as the normalizing step and load profile for loading
        Maybe we can build configuration files?
        """


        menubar = tk.Menu(self.window) # simple Menubar 
        filemenu = tk.Menu(menubar,tearoff = 0)
        editing = tk.Menu(menubar,tearoff = 0)
        visualization = tk.Menu(menubar,tearoff = 0)
        statistics = tk.Menu(menubar, tearoff = 0)
        recording_mode = tk.Menu(menubar,tearoff = 0)

        #add the cascades topics
        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label = "Edit", menu = editing)
        menubar.add_cascade(label = "Visualizations", menu = visualization)
        menubar.add_cascade(label = "Fitting and statistics", menu = statistics)
        menubar.add_command(label="Switch Recording Mode", command = self.return_to_welcome_page)


        self.boolvar=tk.IntVar()
        self.boolvar.set(0)

        # add the entries within the cascades
        configuration = tk.Menu(self.window)
        meta_file = configuration.add_command(label = "Metadata upload", command = self.metadata_file)
        configuration.add_command(label = "Path to Analysis Files", command = self.analysis_file)

        # add a template wizard and load the template file
        template_wizard = ToolBar()
        editing.add_command(label = "Load Template", command = template_wizard.analysis_template)

        filemenu.add_command(label="Open")
        filemenu.add_cascade(label = "Configuration Files", menu = configuration)
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Exit", command = self.window.destroy)


        self.window.config(menu=menubar)


        #create a first frame that is used for the path input and for the analysis options
        self.toolbar = ttk.Frame(master = self.window)
        self.toolbar.pack(side = tk.LEFT, fill = "both")  


        # contruct the buttons
        self.button_conf = ttk.Button(self.toolbar,
                                     text = "Start configuration",
                                     command =  lambda: self.draw_analysis(self.configuration,func=1),
                                     width = "32"
                                 
                                     )

        self.button_ana = ttk.Button(self.toolbar, 
                                    text=" Online Analysis", 
                                    command = lambda: self.draw_analysis(self.online_analysis,func=2),
                                    width = "32"
                                   
                                  )

        self.button_off = ttk.Button(self.toolbar, 
                                     text="Offline Analysis",
                                     command = lambda: self.draw_analysis(self.offline_analysis, func=0),
                                     width = "32"
                                     
                                   )


        self.button_stat = ttk.Button(self.toolbar, 
                                     text="Report/Statistics",
                                     command = lambda: self.draw_analysis(self.statistics, 3),
                                     width = "32"
                                    
                                     )

        logo = Image.open("../Logo/random_trial.png")
        logo = logo.resize((200, 200), Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(logo)
        image_frame = tk.Label(self.toolbar,image=logo)
        image_frame.image = logo

        image_frame.pack(padx = 10, pady = 10, side = tk.TOP, ipady = 40)
        self.button_conf.pack(padx = 10, pady = 10, side = tk.TOP, ipady = 40)
        self.button_ana.pack(padx = 10, pady = 10, side = tk.TOP, ipady = 40)
        self.button_off.pack(padx = 10, pady = 10, side = tk.TOP, ipady = 40)
        self.button_stat.pack(padx = 10, pady = 10, side = tk.TOP, ipady = 40)
      

    def metadata_file(self,window):

        """ we need to implement both option """ 

        metadata_files = filedialog.askopenfilename(master=window)
        self.metadata_path = metadata_files
        

    def analysis_file(self,window):
        analysis_files = filedialog.askdirectory(master=window, initialdir=os.getcwd())
        self.analysis_path = analysis_files
        print(self.analysis_path)

    
    def themes_call(self):
        if self.appearance == "azure":
            self.window.tk.call("source", os.getcwd() + "/../Azure_theme/azure.tcl")
        else:
            self.window.tk.call("source",os.getcwd() +"/../Azure_theme/azure-dark.tcl")

        

    def draw_analysis(self, tab_liste, func= None):

            """ I will rework this whenever all is implemented
            """
    
            # construct the notebook
            self.Note.event_handler(tab_liste, self.window)
            # insert here test for object initializing

            # check if the buttons ect are already there
            # TODO pack forget will increase memory stack: find alternative solution
            if self.tools:
                self.tools.pack_forget()
      
            if self.canvas:
                #func=-1
                self.function_select(func)
            else:
                #func=1
                self.function_select(func)
                    

    def function_select(self, i):
        switcher = {
            0: self.drawing,
            1: self.backend_control,
            2: self.online_evaluation
        }
        func_item = switcher.get(i,lambda :'Invalid')
        print(func_item)

        func_item()
        
    def drawing(self):
        # 
        self.offline.offline_elements(self.Note)
   
    def backend_control(self):
            # find all the frontend code for backend handling in class BackendManager

            self.be.backend_notes(self.bm, self.Note, self.window, self.cam)

    def online_evaluation(self):
            self.ona.select_online_file(self.Note,self.online_manager,self.window)

    def set_darkmode(self):
        """ toDO -> destroy window and restart with new parameters """
        if self.appearance=="azure-dark":
            plt.rcParams['axes.facecolor']='#333333'
            plt.rcParams['figure.facecolor'] ='#333333'
            COLOR = 'white'
            plt.rcParams['text.color'] = COLOR
            plt.rcParams['axes.labelcolor'] = COLOR
            plt.rcParams['xtick.color'] = "black"
            plt.rcParams['ytick.color'] = "black"
            
            
        else:
            #TODO redraw the plot based on new configurations

            plt.rcParams['axes.facecolor']='#ffffff'
            plt.rcParams['figure.facecolor'] ='#ffffff'
            plt.rcParams['text.color'] = "black"
            plt.rcParams['axes.labelcolor'] = "black"
            plt.rcParams['xtick.color'] = "black"
            plt.rcParams['ytick.color'] = "black"


    def return_to_welcome_page(self):
        self.window.destroy()
        welcome_page_elements.FrontPage(self.appearance)



if __name__ == "__main__":
    #GuiEtools(appearance = "azure").window.mainloop()
    app = QtWidgets.QApplication(sys.argv)
    w = FrontPage()
    w.show()
    sys.exit(app.exec_())