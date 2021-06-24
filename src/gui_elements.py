import tkinter as tk
import tkinter.ttk as ttk
from helper_functions import HelperFunction
import os
from tkinter import filedialog
import pandas as pd


class ToolBar():

    def __init__(self, master = None,frame = None):

        # initialize the class
        self.master = master
        self.frame = frame
        self.note = None
        self.helper = HelperFunction()

        # hold the template path
        self._template_path = None
        self.analysis_fr = None


    def configuration_toolbar(self, command):
        """ here we can add also command to call the function for the batch communicaton """

        self.frame.pack(side = tk.LEFT, fill = "both", expand = True)
        #abs_pathname = os.path.
        start_img = self.helper.resize(os.getcwd()[:-3] + "/figures/play_sign.jpg")
        #start_img = abs_pathname+"/figures/play_sign.jpg"
        print(start_img)
        stop_img = self.helper.resize(os.getcwd()[:-3] + "/figures/stop_sign.jpg")

        self.play_button = tk.Button(self.frame, image = start_img, width = 50, height = 50, command = command, borderwidth = 0)
        self.play_button.image = start_img
        self.stop_button = tk.Button(self.frame,image = stop_img, width = 50, height = 50, borderwidth = 0)
        self.stop_button.image = stop_img
        self.play_button.pack(side = tk.LEFT, padx = 3, pady = 3)
        self.stop_button.pack(side = tk.LEFT, padx = 3, pady = 3)

    def event_handler(self, tab_liste, root):
        # click event handler, can be much cleaner i guess
        if self.note is None:  
            self.draw(tab_liste, root)
        else:
            self.note.destroy()
            self.draw(tab_liste, root)

    def draw(self, tab_liste, root):

        """Build the notebook"""
        if self.note:
            self.note.destroy()
        self.note = ttk.Notebook(root)
        self.frames = [] 
        for i,t in zip(range(len(tab_liste)), tab_liste):
                tmp_frame = ttk.Frame(style = "grey.TFrame") # construct a new frame for each individual tab
                self.frames.append(tmp_frame)
                self.note.add(self.frames[i], text = t)

        self.note.pack(expand=1, fill='both')
    
    def analysis_template(self, command = None, command_2= None):
        """ template for the analysis """

        # open a new window
        self.template = tk.Tk()
        self.template.option_add("*foreground","black")
        self.template.tk.call("source",os.getcwd()[:-3] +"/Azure_theme/azure-dark.tcl")

        # set the style of the window matching main
        s = ttk.Style(self.template)
        appearance = "azure-dark"
        s.theme_use(appearance)
        
        #two frames one for selection and one for the analysis
        self.entry_frame = ttk.Frame(self.template)
        self.entry_frame.grid()

        #construct the load template stuff
        self.entry_box = ttk.Entry(self.entry_frame)
        
        load_button = ttk.Button(self.entry_frame, text = "Load Template", style = "AccentButton", command = self.get_template) # load template as tab_delimited text fill
        show_button = ttk.Button(self.entry_frame, text = "Show Template", style = "AccentButton", command = self.show_template)
        enable = ttk.Checkbutton(self.entry_frame, text = "Enable Editing", style = "Switch", onvalue = 1, offvalue = 0)
        self.entry_box.grid(padx = 10, pady = 20, column = 1, row = 1)
        load_button.grid(padx = 10, pady = 5, column = 2, row = 1)
        show_button.grid(padx = 4, pady = 5, column = 3, row = 1)
        enable.grid(padx = 4, pady = 5, column = 4, row = 1)
        ttk.Separator(self.entry_frame, orient = tk.HORIZONTAL).grid(row=2, columnspan=5,sticky="ew")

    def open_file(self):
        file = pd.read_csv(self._template_path, delimiter = "\t")
        return file

    def get_template(self):
        """ maybe redundant """ 
        print("Setting the template")
        metadata_files = filedialog.askopenfilename(master=self.template)
        self.entry_box.insert(0,metadata_files)
        self._template_path = metadata_files

    def handler_analysis(self,frame,root):
        """check if the frame is already constructed otherwise destroy --> maybe simplify"""
        if frame is None:
            print("hallo")
            self.analysis_fr = ttk.Frame(root)
            
        else:
            frame.destroy()
            self.analysis_fr = ttk.Frame(root)
           
  
    def show_template(self):
        """ templates """

        if self._template_path:
            self.handler_analysis(self.analysis_fr, self.template)
            self.show_template_handling()
               
        else:
            print("Please set the path properly:")


    def show_template_handling(self):

        """ making the wizard for the template analysis """ 
        metafile = self.open_file()
        
        self.analysis_fr.grid()
        # save the entry 
        protocol_list = []
        upper_bound_list = []
        lower_bound_list = []

        for i,t in zip(metafile.columns, range(len(metafile.columns))):
            print(i,t)
            # make the header
            header = ttk.Entry(self.analysis_fr)
            header.insert(0, i)
            header.configure(state = "disabled")
            header.grid(column = t+1, row = 1, pady = 25)


        for name,lower,upper,col in zip(metafile["protocol"].tolist(), metafile["upper_bound"].tolist(), metafile["lower_bound"].tolist(), range(len(metafile))):
            # draw the grid 
            up = str(upper)
            low = str(lower)

            # generate entries for the number of values in template file
            file = ttk.Entry(self.analysis_fr)
            upper = ttk.Entry(self.analysis_fr)
            lower = ttk.Entry(self.analysis_fr)

            # insert the entries values
            file.insert(0,name)
            upper.insert(0,up)
            lower.insert(0, low)
            file.configure(state="disabled")
            upper.configure(state="disabled")
            lower.configure(state="disabled")
            
            #put files into the grid
            file.grid(column = 1, row = col+2, pady = 5, padx = 5,  sticky = tk.W)
            lower.grid(column = 2, row = col+2, pady = 5, padx = 5, sticky = tk.W)
            upper.grid(column = 3, row = col+2, pady = 5, padx = 5, sticky = tk.W)

            # append the entries for retrieval
            protocol_list.append(file)
            lower_bound_list.append(lower)
            upper_bound_list.append(upper)

        # add a save button
        save_button = ttk.Button(self.analysis_fr, text = "Save the file as txt", style = "AccentButton")
        save_button.grid(column = 2, row = 7, pady = 10)

        # add a quit button 
        quit_button = ttk.Button(self.analysis_fr, text = "Quit", style = "AccentButton", command = self.template.destroy)
        quit_button.grid(column = 3, row = 7, pady = 10, padx = 5)



    









