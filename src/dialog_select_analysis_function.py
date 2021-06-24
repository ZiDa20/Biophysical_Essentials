import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import heka_reader as h_r


class DialogSelectAnalysisFunction(tkinter.simpledialog.Dialog):

    def __init__(self, parent, series_list,data_list):
        '''
        @input series_list: string list of series names
               data_list= list of quadruples (group,series name, series identifier, data array)
        '''
        self.decission = 0
        self.series = series_list
        self.data_list = data_list
        tkinter.simpledialog.Dialog.__init__(self, parent)
        #self.master = parent

    def body(self, master):
        message = ttk.Label(master, text ="Configure your analysis setup:")
        message.grid(column=1,row=1,columnspan = 3, padx = 50)

        series_frame = ttk.LabelFrame(master, text="Series selection")
        series_frame_combobox = ttk.Combobox(series_frame,values=self.series)

        series_frame.grid(column=1, row=2)
        series_frame_combobox.pack()
        series_frame_combobox.current(0)

        series_frame_combobox.bind("<<ComboboxSelected>>", self.series_changed)

        tmp_series = series_frame_combobox.get() # string name ?

        debug  =1



        # step 1 select series if multiple series have been selected
        # step 2 select : show series plot (per default this will be the first element, but there should be an option to change)
        # -> show analysis function according to recording mode
        # step 3 select : set coursor bounds or load from template


    def series_changed(self):
        print("implemented yet")
    def buttonbox(self):
        pass

    '''
    def b1(self):
        self.decission = 0
        self.ok()

    def b2(self):
        self.decission = 1
        quit()

    def b3(self):
        self.decission =2
        quit()

    '''