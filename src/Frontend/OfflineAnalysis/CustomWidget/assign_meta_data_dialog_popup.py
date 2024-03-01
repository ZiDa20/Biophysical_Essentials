
from PySide6.QtWidgets import *  # type: ignore
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_group_dialog import Ui_assign_meta_data_group
import pandas as pd
from Frontend.CustomWidget.Pandas_Table import PandasTable
from Frontend.CustomWidget.error_dialog_class import CustomErrorDialog
import csv
from PySide6.QtCore import QTimer
from PySide6.QtCore import QSize
class Assign_Meta_Data_PopUp(QDialog, Ui_assign_meta_data_group):

    def __init__(self, database_handler, offline_manager, frontend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.offline_manager = offline_manager
        self.frontend_style = frontend
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.content_model = None
        self.column_names = ["Experiment_name", "Experiment_label", "Species", "Genotype", "Sex", "Celltype","Condition",
                        "Individuum_id"]
        self.pushButton_2.clicked.connect(self.change_multiple_cell_values)
        self.pushButton_3.clicked.connect(self.reset_meta_data)
        #self.saving_template = QPushButton("Save Template")
        self.save_to_template_button.clicked.connect(self.save_template_only)
        
        #self.gridLayout.addWidget(self.saving_template, 5, 4, 1, 1)
        
        # dict that is needed to rename experiments with whitespaces or whatever
        self.experiment_name_dict = {}

    def reset_meta_data(self):
        """
        reset_meta_data: overrides all the given meta data with the value "None"
        """
        for column in self.column_names[1:len(self.column_names)]:
            self.template_dataframe[column] = ["None"]*len(self.template_dataframe[column])
        self.content_model.update_data(self.template_dataframe)

    def change_multiple_cell_values(self):
        """
        change_multiple_cell_values:
         replaces all cell values in the selected colum which was selected in the combo box by the text entered into the line edit 
         new text and  
        """
        column = self.comboBox.currentText()
        text = self.lineEdit.text()

        self.template_dataframe[column] = [text]*len(self.template_dataframe[column])
        self.content_model.update_data(self.template_dataframe)

    def map_metadata_to_database(self):
        """
        map_metadata_to_database: Writes the metadata into the database and visualizes them to the user
        if the user wants to make changes, they can be entered into the gui table

        Returns:
            _type_: _description_
        """
        
        directory = self.offline_manager._directory_path
        
        self.comboBox.addItems(self.column_names[1:len(self.column_names)])
        if self.frontend_style.default_mode == 1: # white mode
            self.comboBox.setStyleSheet(""" QComboBox::item { color: black; }    """)
        else:
            self.comboBox.setStyleSheet(""" QComboBox::item { color: white; }    """)
            
        
        self.template_dataframe = pd.DataFrame(columns=self.column_names)
        print(self.offline_manager.package_list(directory))

        for dat_file in self.offline_manager.package_list(directory):
            
            if isinstance(dat_file, list):
                splitted_name = "_".join(dat_file[0].split("_")[:2])
                self.database_handler.add_experiment_to_experiment_table(splitted_name)
            else:
                splitted_name = dat_file.split(".")
                self.database_handler.add_experiment_to_experiment_table(splitted_name[0])
            
            if isinstance(dat_file, list):
                new_experiment_name = splitted_name
            else:
                new_experiment_name = splitted_name[0]
            

            # we have to check for whitespaces in the name or other characters which are not allowed in the database
            if " " in new_experiment_name:
                 new_name= new_experiment_name.replace(" ", "_")
                 self.experiment_name_dict[new_experiment_name] = new_name
                 new_experiment_name = new_name

            # Create a DataFrame with the new data
            new_data = pd.DataFrame({"Experiment_name": [new_experiment_name],
                                        "Experiment_label": ["None"],
                                        "Species": ["None"],
                                        "Genotype": ["None"],
                                        "Sex": ["None"],
                                        "Celltype": ["None"],
                                        "Condition": ["None"],
                                        "Individuum_id": ["None"]})
                #self.template_dataframe = self.template_dataframe.append({"Experiment_name":splitted_name,"Experiment_label":"None","Species":"None",
                #                        "Genotype":"None","Sex":"None","Celltype":"None","Condition":"None","Individuum_id":"None"}, ignore_index=True)
            self.template_dataframe = pd.concat([self.template_dataframe, new_data], ignore_index=True)
           
            #    self.template_dataframe = self.template_dataframe.append({"Experiment_name":splitted_name[0],"Experiment_label":"None","Species":"None",
            #                            "Genotype":"None","Sex":"None","Celltype":"None","Condition":"None","Individuum_id":"None"}, ignore_index=True)

        return self.create_table()

    def create_table(self):
        """Create a table view."""
        template_table_view = QTableView()
        template_table_view.setObjectName("meta_data_template")
        template_table_view.setMinimumHeight(300)
        template_table_view.horizontalHeader().setSectionsClickable(True)

        # Create models for the table view and data visualizations
        self.content_model = PandasTable(self.template_dataframe,[0])
        template_table_view.setModel(self.content_model)

        # Set horizontal header resize mode
        template_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # or QHeaderView.ResizeToContents

        #def resize_popup():
        #    table_size = template_table_view.size() + QSize(100, 0)  # Adjust as needed
        #    self.resize(table_size)

        # Use a QTimer to delay resizing until the table view is fully populated
        #QTimer.singleShot(100, resize_popup)
        # Assuming self is an instance of Ui_assign_meta_data_group
        # Resize the popup to match the size of the table
        #self.resize(table_size)

        self.meta_data_template_layout.addWidget(template_table_view)
        #template_table_view.setGeometry(20, 20, 900, 581)
        template_table_view.show()
        return template_table_view



    def open_meta_data_template_file(self,template_table_view):
        meta_data_assignments = []
        file_name = QFileDialog.getOpenFileName(self, 'OpenFile', "", "*.csv")[0]

        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            meta_data_assignments = list(reader)

        if len(meta_data_assignments[0]) <= 7:
            CustomErrorDialog().show_dialog("The template needs at least 8 columns which were not found in the specified template.")

        else:
            df = pd.DataFrame(meta_data_assignments[1:], columns=meta_data_assignments[0])
            # create two models one for the table show and a second for the data visualizations
            content_model = PandasTable(df)
            template_table_view.setModel(content_model)
            template_table_view.show()
        #self.data_base_content.clicked.connect(self.retrieve_column)
        
    
    def save_template_only(self):
        """
        save the created template as csv file
        """
        data = self.content_model._data
        filename_path = QFileDialog.getSaveFileName(None, "Save As CSV", "", "CSV Files (*.csv)")[0]
        if not filename_path.endswith(".csv"):
                filename_path += ".csv"
        data.to_csv(filename_path, index=False)
        