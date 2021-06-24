import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import heka_reader as h_r


class MultipleSeriesInAFileDialog(tkinter.simpledialog.Dialog):

    def __init__(self, parent):
        self.decission = 0
        tkinter.simpledialog.Dialog.__init__(self, parent)
        #self.master = parent

    def body(self, master):
        message = ttk.Label(master, text ="Multiple series of the same type were found within one file. \n Please select a way how to proceed:")
        message.grid(column=1,row=1,columnspan = 3, padx = 50)

        b1 = ttk.Button(master, text="Continue with duplicates", command = self.b1)
        b1.grid(column=1,row=2, pady = 40, padx = 20)
        b2 = ttk.Button(master, text="Select a fix number")
        b2.grid(column=2,row=2, pady = 40, padx = 20)
        b3 = ttk.Button(master, text="Deselect manually")
        b3.grid(column=3, row=2, pady = 40, padx = 20)

    def buttonbox(self):
        pass

    def b1(self):
        self.decission = 0
        self.ok()

    def b2(self):
        self.decission = 1
        quit()

    def b3(self):
        self.decission =2
        quit()

