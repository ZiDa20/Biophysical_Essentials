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
        ax = self.figure.add_subplot(111)

        # Create a canvas to display the figure
        self.canvas = FigureCanvas(self.figure)

        # Create a layout to contain the canvas
        self.diagram_grid.addWidget(self.canvas)

        q = f'select * from global_meta_data where experiment_label = \'{label}\''
        meta_data_table = self.database_handler.database.execute(q).fetchdf()
        print("Welcome to create_experiment_specific_visualization")
        df = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Amount': [10, 20, 30]})
        total = df['Amount'].sum()
        ax.pie(df['Amount'], labels=df['Category'], autopct=lambda p: '{:.0f}'.format(p * total / 100))
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.set_title("Category Breakdown")

        #for column_name in meta_data_table.columns:
        #    meta_data_table[

