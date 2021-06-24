import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import heka_reader as h_r


class SeriesSelectionDialog(tkinter.simpledialog.Dialog):

    def __init__(self,series_list,parent):
        self.series_list = series_list
        tkinter.simpledialog.Dialog.__init__(self, parent)
        #self.master = parent

    def body(self, master):
        #self.series_list = ['Block Pulse', 'IV', 'IV-40', 'Inact', 'CClamp', 'InputRes.', 'APfastCI', 'Rheobase', '5xRheo', 'RheoRamp', '2xRheobase']
        #master = self.master
        #self.master = parameter_list[0]
        #self.series_list= parameter_list[1]

        self.variable_fields = self.series_list[:]

        instructions = ttk.Label(master, text="Available:")
        instructions.grid(row=0)


        self.answerreturn_list = []
        incr = 0

        number_of_rows = 4
        for elem in range(len(self.series_list)):

           single_field_text = self.series_list[elem]

           if (elem+1) % number_of_rows == 0:
               incr=incr+2

           text = ttk.Label(master, text=single_field_text)
           text.grid(row=(elem+1) % number_of_rows,column=0+incr)
           self.variable_fields[elem] = tk.Variable()
           l = ttk.Checkbutton(master,variable=self.variable_fields[elem])
           l.grid(row=(elem+1) % number_of_rows, column=1+incr)



    def apply(self):

        self.identifier_list =[]
        print("eval")
        for i in range(len(self.series_list)):
            if self.variable_fields[i].get() =="1":
                self.identifier_list.append(str(self.series_list[i]))


        #return identifier_list
        #print(self.identifier_list)
