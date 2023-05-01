from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtCore import *
from functools import partial

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup import Ui_Dialog


class Load_Data_From_Database_Popup_Handler(QDialog, Ui_Dialog):

    def __init__(self,database_handler, frontend_style, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.frontend_style = frontend_style
        self.read_label_list()
        if self.frontend_style.default_mode == 0:
            self.frontend_style.set_mpl_style_dark()
        else:
            self.frontend_style.set_mpl_style_white()
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #GlobalBlur(self.winId(), Acrylic=True)

    def read_label_list(self):

        self.available_labels = self.database_handler.get_available_experiment_label()
        self.checkbox_list = []

        cba = QCheckBox("All")
        self.checkbox_list.append(cba)
        self.label_grid.addWidget(cba, 0, 0)
        cba.stateChanged.connect(partial(self.checkbox_checked,cba,"All"))
        self.all_cb = cba

        for i in self.available_labels:
            c = QCheckBox(i[0])
            self.checkbox_list.append(c)
            self.label_grid.addWidget(c, self.available_labels.index(i)+1 , 0)
            c.stateChanged.connect(partial(self.checkbox_checked,c,i[0]))
        self.available_labels = [("All",)] + self.available_labels

    def checkbox_checked(self,checkbox,label,state):
        if state == Qt.Checked:
            for cb in self.checkbox_list:
                if cb!= checkbox:
                    cb.setChecked(False)
                else:
                    checkbox.setChecked(True)

        self.create_experiment_specific_visualization(label)

    def create_experiment_specific_visualization(self, label):

        #Create a figure

        self.figure = Figure()
        #manual_colors = ["#FD8A8A","#8b785b","#6e8b5b","#785b8b",] # "#9ca8b9", "#adb6c5", "#c0c0c0"].reverse()
        manual_colors = ["#FD8A8A", "#F1F7B5", "#A8D1D1", "#9EA1D4", "#316B83", "#6D8299", "#D5BFBF", "#8CA1A5", "#C6D57E", "#D57E7E", "#A2CDCD", "#FFE1AF", "#0b525b", "#144552", "#1b3a4b", "#212f45", "#272640", "#312244", "#3e1f47", "#4d194d"]

        # Set the figure size and create the subplots
        ax = self.figure.subplots(2, 3)


        # Create a canvas to display the figure
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setStyleSheet("background-color: rgba(1,0,0,0);")
        # in case of previous plots: clear the layout first
        for i in range(self.diagram_grid.count()):
            self.diagram_grid.itemAt(i).widget().deleteLater()

        #select the existing layout and add the canvas
        self.diagram_grid.addWidget(self.canvas)

        # get experiment meta data assigned to this experiment label from the database
        q = f'select * from global_meta_data '
        if label is not "All":
            q = q +  f' where experiment_label = \'{label}\''

        meta_data_table = self.database_handler.database.execute(q).fetchdf()

        row = 0
        column = 0

        meta_data_columns_to_plot = ["species", "genotype","sex", "celltype", "condition"] #, "individuum_id"]
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

            plot_colors = []
            expl = []
            for l in range(0, len(df[column_name].unique())):
                plot_colors.append(manual_colors[l])
                expl.append(0.1)
            ax[row, column].pie(df[column_name].value_counts(), labels=df[column_name].unique(), autopct=lambda p: '{:.0f}'.format(p * total / 100), colors=plot_colors, explode = expl)
            #ax[row, column].pie(df[column_name].value_counts(), autopct=lambda p: f'{df[column_name].unique()} \n {p:.0f}, {p * total / 100}', colors=plot_colors, explode = expl)
            ax[row, column].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax[row, column].set_title(column_name)

        # move this to series_analysis_mapping table
        q = f'select series_meta_data from experiment_series'
        df = self.database_handler.database.execute(q).fetchdf()
        plot_colors = []
        expl = []
        for l in range(0, len(df["series_meta_data"].unique())):
                plot_colors.append(manual_colors[l])
                expl.append(0.1)
        ax[1, 2].pie(df["series_meta_data"].value_counts(), labels=df["series_meta_data"].unique(), autopct=lambda p: '{:.0f}'.format(p * total / 100), colors=plot_colors, explode = expl)
        #ax[1, 2].pie(df["series_meta_data"].value_counts(), colors=plot_colors, explode = expl)

        #ax[1, 2].pie(df["series_meta_data"].value_counts(), colors=plot_colors, explode = expl)
        ax[1, 2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax[1, 2].set_title("series_meta_data")
