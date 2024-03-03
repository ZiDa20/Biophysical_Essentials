
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
            QTableView: the table view that is actually showing the data that need to be imported
        """
        
        # in the case the user clicks the dialog close button - the initial mappings remain in the experiments table
        self.database_handler.clear_from_previous_uncomplete_mappings()
        # path that was manually assigned by the user
        directory = self.offline_manager._directory_path
        # combo box to select a column where entries for all rows should be changed
        self.comboBox.addItems(self.column_names[1:len(self.column_names)])
        if self.frontend_style.default_mode == 1: # white mode
            self.comboBox.setStyleSheet(""" QComboBox::item { color: black; }    """)
        else:
            self.comboBox.setStyleSheet(""" QComboBox::item { color: white; }    """)
            
        # pandas df for new data
        self.template_dataframe = pd.DataFrame(columns=self.column_names) 
        # pandas df for existing data - will have an additional column analysis id
        self.duplicate_dataframe = pd.DataFrame()

        # iterate over each recording in the directory
        for dat_file in self.offline_manager.package_list(directory):
            status = 1 # status of the database entry process: can be either 0,1,-1 as described in add_experiment_to_experiment_table
            new_experiment_name = ""
            if isinstance(dat_file, list):
                splitted_name = "_".join(dat_file[0].split("_")[:2])
                status = self.database_handler.add_experiment_to_experiment_table(splitted_name)
                new_experiment_name = splitted_name
            else:
                splitted_name = dat_file.split(".")
                status = self.database_handler.add_experiment_to_experiment_table(splitted_name[0])
                new_experiment_name = splitted_name[0]

            # we have to check for whitespaces in the name or other characters which are not allowed in the database
            if " " in new_experiment_name:
                 new_name= new_experiment_name.replace(" ", "_")
                 self.experiment_name_dict[new_experiment_name] = new_name
                 new_experiment_name = new_name
            
             # if status = 1: experiment name was entered into the db, if not something went wrong
            if status != 1:
                print("this needs proper debugging")
                if status ==0: # 0 is returned when the experiment name does already exist
                    exsiting_df = self.database_handler.get_experiment_meta_data(new_experiment_name)
                    if self.duplicate_dataframe.empty:
                        self.duplicate_dataframe = exsiting_df
                    else:
                        self.duplicate_dataframe = pd.concat([self.duplicate_dataframe, exsiting_df], ignore_index=True)
                else:
                    self.logger.error(f'An Error was detected for experiment {new_experiment_name}')
                    CustomErrorDialog(f'An Error was detected for experiment {new_experiment_name}', self.frontend_style)
            else:
                # Create a deault DataFrame with the new data
                new_data = pd.DataFrame({"Experiment_name": [new_experiment_name],
                                        "Experiment_label": ["None"],
                                        "Species": ["None"],
                                        "Genotype": ["None"],
                                        "Sex": ["None"],
                                        "Celltype": ["None"],
                                        "Condition": ["None"],
                                        "Individuum_id": ["None"]})
           
                self.template_dataframe = pd.concat([self.template_dataframe, new_data], ignore_index=True)
           
        # return the QTable View
        return self.prepare_user_data_visualization()

    def prepare_user_data_visualization(self):
        """
        prepare_user_data_visualization: show data that need to be imported and data which are already imported

        Returns:
           QTableView: the table view that is actually showing the data that need to be imported
        """
        if self.template_dataframe.empty:
            info = QLabel()
            info.setText("All of your selected recordings were already imported into the database previously, please see the table below.")
            info.setStyleSheet("padding: 15px; font-size: 14px;")           
            self.meta_data_template_layout.addWidget(info)
        self.content_model = PandasTable(self.template_dataframe,[0])
        new_data = self.create_table(self.template_dataframe,self.content_model)

        # create the meta data table for existing data
        if not self.duplicate_dataframe.empty:
            new_label = QLabel()
            new_label.setText("The following experiments do already exist in the database and do not need to be imported again. If you still want to import this file, please close the import wizard, rename the recording file and start the import wizard again.")            
            new_label.setStyleSheet("padding: 15px; font-size: 14px;")     
            self.meta_data_template_layout.addWidget(new_label)

            existing_data_model = PandasTable(self.duplicate_dataframe, [0,1,2,3,4,5,5,7])
            self.create_table(self.duplicate_dataframe, existing_data_model)
        
        # Get the current width of the dialog
        current_width = self.width()

        # Adjust the height of the dialog based on its contents
        self.adjustSize()

        # Set the width back to its original value
        self.resize(current_width, self.height())
        return new_data
    
    def create_table(self,df: pd.DataFrame,model):
        """
        create_table _summary_

        Args:
            df (_type_): pandas data frame with the data to visualize 
            model (_type_): model to be set for the 

        Returns:
            _type_: _description_
        """
        template_table_view = QTableView()

        # adjust the size 
        table_length = len(df) * 30 # 20 = empirical size
        if table_length > 250:
            table_length = 250
        template_table_view.setMinimumHeight(table_length)
        template_table_view.horizontalHeader().setSectionsClickable(True)

        # Create models for the table view and data visualizations
        template_table_view.setModel(model)

        # Set horizontal header resize mode
        template_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # or QHeaderView.ResizeToContents

        self.meta_data_template_layout.addWidget(template_table_view)
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
        