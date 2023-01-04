from pickle import FALSE
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtCore import * 
from functools import partial

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import pandas as pd
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup import Ui_Dialog

class Load_Data_From_Database_Popup_Handler(QDialog, Ui_Dialog):

    def __init__(self,database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.read_label_list()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #GlobalBlur(self.winId(), Acrylic=True)

    def read_label_list(self):

        self.available_labels = self.database_handler.get_available_experiment_label()
        self.checkbox_list = []

        c = QCheckBox("All")
        self.checkbox_list.append(c)
        self.label_grid.addWidget(c, 0, 0)
        c.stateChanged.connect(partial(self.checkbox_checked,c,"All"))

        for i in self.available_labels:
            c = QCheckBox(i[0])
            self.checkbox_list.append(c)
            self.label_grid.addWidget(c, self.available_labels.index(i)+1 , 0)
            c.stateChanged.connect(partial(self.checkbox_checked,c,i[0]))
        self.available_labels = [("All",)] + self.available_labels

    def checkbox_checked(self,checkbox,label,state):
        if state == Qt.Checked:
            for cb in self.checkbox_list:
                cb.setChecked(False)
            checkbox.setChecked(True)
        
        if label=="All":
            print("descriptive statistic of entire db")
        else:
            self.create_experiment_specific_visualization(label)

    def create_experiment_specific_visualization(self, label):
        
        #Create a figure
        self.figure = Figure()
       
        # Set the figure size and create the subplots
        ax = self.figure.subplots(2, 3)


        # Create a canvas to display the figure
        self.canvas = FigureCanvas(self.figure)
        
        # in case of previous plots: clear the layout first
        for i in range(self.diagram_grid.count()): 
            self.diagram_grid.itemAt(i).widget().deleteLater()

        #select the existing layout and add the canvas
        self.diagram_grid.addWidget(self.canvas)

        # get experiment meta data assigned to this experiment label from the database
        q = f'select * from global_meta_data where experiment_label = \'{label}\''
        meta_data_table = self.database_handler.database.execute(q).fetchdf()

        row = 0
        column = 0
        meta_data_columns_to_plot = ["species", "genotype","sex", "celltype", "condition", "individuum_id"]
        for column_name in meta_data_columns_to_plot:
            
            cnt = meta_data_columns_to_plot.index(column_name)
            if cnt>=1:
                if cnt%3==0:
                    column = 0
                    row = row +1 
                else:
                    column = column +1
            
            df = meta_data_table
            total = df[column_name].value_counts().sum()
            print("row=", row, " column= ", column)
            ax[row, column].pie(df[column_name].value_counts(), labels=df[column_name].unique(), autopct=lambda p: '{:.0f}'.format(p * total / 100))
            ax[row, column].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax[row, column].set_title(column_name)
        

