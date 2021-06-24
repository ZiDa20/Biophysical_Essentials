import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk
import heka_reader as h_r


class MetaDataDialog(tkinter.simpledialog.Dialog):

    def body(self, master):

        self.fields = [
            ('Mark', 'i'),
            ('Label', '32s'),
            ('TraceCount', 'i'),
            ('Data', 'i'),
            ('DataPoints', 'i'),
            ('InternalSolution', 'i'),
            ('AverageCount', 'i'),
            ('LeakCount', 'i'),
            ('LeakTraces', 'i'),
            ('DataKind', 'h'),
            ('Filler1', 'h', None),
            ('RecordingMode', 'c'),
            ('AmplIndex', 'c'),
            ('DataFormat', 'c'),
            ('DataAbscissa', 'c'),
            ('DataScaler', 'd'),
            ('TimeOffset', 'd'),
            ('ZeroData', 'd'),
            ('YUnit', '8s'),
            ('XInterval', 'd'),
            ('XStart', 'd'),
            ('XUnit', '8s'),
            ('YRange', 'd'),
            ('YOffset', 'd'),
            ('Bandwidth', 'd'),
            ('PipetteResistance', 'd'),
            ('CellPotential', 'd'),
            ('SealResistance', 'd'),
            ('CSlow', 'd'),
            ('GSeries', 'd'),
            ('RsValue', 'd'),
            ('GLeak', 'd'),
            ('MConductance', 'd'),
            ('LinkDAChannel', 'i'),
            ('ValidYrange', 'c'),
            ('AdcMode', 'c'),
            ('AdcChannel', 'h'),
            ('Ymin', 'd'),
            ('Ymax', 'd'),
            ('SourceChannel', 'i'),
            ('ExternalSolution', 'i'),
            ('CM', 'd'),
            ('GM', 'd'),
            ('Phase', 'd'),
            ('DataCRC', 'i'),
            ('CRC', 'i'),
            ('GS', 'd'),
            ('SelfChannel', 'i'),
            ('Filler2', 'i', None),
        ]

        self.variable_fields = self.fields[:]

        instructions = ttk.Label(master, text="Choose meta data to add")
        instructions.grid(row=0)


        self.answerreturn_list = []
        incr = 0

        for elem in range(len(self.fields)):

           single_field_text = self.fields[elem][0]

           if (elem+1) % 10 == 0:
               incr=incr+2

           text = ttk.Label(master, text=single_field_text)
           text.grid(row=(elem+1) % 10,column=0+incr)
           self.variable_fields[elem] = tk.Variable()
           l = ttk.Checkbutton(master,variable=self.variable_fields[elem])
           l.grid(row=(elem+1) % 10, column=1+incr)


    def apply(self):
        self.identifier_list =[]
        print("eval")
        for i in range(len(self.fields)):
            if self.variable_fields[i].get() =="1":
                self.identifier_list.append(str(self.fields[i][0]))

        #print(self.identifier_list)