from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtCore import *
from functools import partial

from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvas
from QT_GUI.OfflineAnalysis.CustomWidget.load_data_from_database_popup import Ui_Dialog
from Offline_Analysis.error_dialog_class import CustomErrorDialog

from CustomWidget.Pandas_Table import PandasTable
import copy

class Load_Data_From_Database_Popup_Handler(QDialog, Ui_Dialog):

    def __init__(self,database_handler, frontend_style, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.frontend_style = frontend_style
        
        if self.frontend_style.default_mode == 0:
            self.frontend_style.set_mpl_style_dark()
        else:
            self.frontend_style.set_mpl_style_white()
     
        self.show_default()
        self.switch_to_manual.clicked.connect(self.show_manual)
        self.switch_to_auto.clicked.connect(self.show_default)
        self.execute_query.clicked.connect(self.request_data_from_query)
        self.default_categories = ["experiment_label", "species", "genotype","sex", "celltype", "condition"]
        
        self.category.currentTextChanged.connect(self.combo_box_change)
        self.category.addItems(self.default_categories)
    
    
    def combo_box_change(self):
        self.read_label_list()
        self.checkbox_list[0].setChecked(True)

    def show_default(self):
        # show the default page 0
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    def show_manual(self):
        # show the page for manual queries
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)

    def request_data_from_query(self):
        # read the manual query, process it and display the status and the result
        query = self.query_input.toPlainText()
        try:
            self.table_data = self.database_handler.database.execute(query).fetchdf()
            model = PandasTable(self.table_data)
            
            # Creating a QTableView
            table_view = QTableView()
            table_view.setModel(model)
            model.resize_header(table_view)

            # before adding, remove the old tablez:
            self.clear_layout(self.gridLayout_11)
            
            self.gridLayout_11.addWidget(table_view)
            table_view.show()
            if "experiment_name" in self.table_data.columns:
                self.query_output.setText("Query Succeeded")
            else:
                self.query_output.setText("Query Succeeded but column experiment_name is required to continue")

        except Exception as e:
            self.query_output.setText(e)

    def read_label_list(self):
        
        """Read the available lable list for the current text category"""
        self.clear_layout(self.label_grid)
        self.clear_layout(self.diagram_grid)
        
        self.available_labels = self.database_handler.get_available_category_groups(self.category.currentText())
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

    def clear_layout(self, layout):
        """
        clear a layout from all previous shown widgets and items
        """
        for l in range(layout.count()):
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                layout.removeItem(item)

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
            q = q +  f' where ' + self.category.currentText() + f' = \'{label}\''

        meta_data_table = self.database_handler.database.execute(q).fetchdf()

        row = 0
        column = 0

        meta_data_columns_to_plot = copy.deepcopy(self.default_categories)
        print(meta_data_columns_to_plot)
        print(self.category.currentText())
        meta_data_columns_to_plot.remove(self.category.currentText())
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

    def get_experiment_names(self):
        """
        return a list of experiment names to be linked with a new analysis ID
        either from the auto combo box menu or the self generated sql query
        """
        print(self.stackedWidget.currentIndex())
        if self.stackedWidget.currentIndex()==0:
            for cb in self.checkbox_list:
                if cb.isChecked():
                    pos = self.checkbox_list.index(cb)
                    value = self.available_labels[pos][0]
                    if value == "All":
                        q = 'select experiment_name from global_meta_data'
                    else:
                        q = f'select experiment_name from global_meta_data where {self.category.currentText()} = \'{value}\' '
                    return self.database_handler.database.execute(q).fetchdf()["experiment_name"].values
        else:
            try:
                return self.table_data["experiment_name"].values
            except Exception as e:
                CustomErrorDialog("Your table MUST contain the column experiment_name", self.frontend_style)

                