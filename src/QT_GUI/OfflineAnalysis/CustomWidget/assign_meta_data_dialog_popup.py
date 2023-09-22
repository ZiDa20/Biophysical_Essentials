
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_group_dialog import Ui_assign_meta_data_group
import pandas as pd
from CustomWidget.Pandas_Table import PandasTable
from Offline_Analysis.error_dialog_class import CustomErrorDialog
import csv
class Assign_Meta_Data_PopUp(QDialog, Ui_assign_meta_data_group):

    def __init__(self, database_handler, offline_manager, frontend, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.offline_manager = offline_manager
        self.frontend_style = frontend
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.content_model = None
        self.saving_template = QPushButton("Save Template")
        self.saving_template.clicked.connect(self.save_template_only)
        self.gridLayout.addWidget(self.saving_template, 5, 4, 1, 1)
        
    def map_metadata_to_database(self):
        """_summary_
        """
        directory = self.offline_manager._directory_path
        column_names = ["Experiment_name", "Experiment_label", "Species", "Genotype", "Sex", "Celltype","Condition",
                        "Individuum_id"]
        self.template_dataframe = pd.DataFrame(columns=column_names)
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
        """_summary_
        """
        template_table_view = QTableView()
        template_table_view.setObjectName("meta_data_template")
        template_table_view.setMinimumHeight(300)
        template_table_view.horizontalHeader().setSectionsClickable(True)

        # create two models one for the table show and a second for the data visualizations
        self.content_model = PandasTable(self.template_dataframe)
        template_table_view.setModel(self.content_model)

        # self.data_base_content.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        template_table_view.horizontalHeader().resizeSections(QHeaderView.ResizeToContents)
        self.meta_data_template_layout.addWidget(template_table_view)
        template_table_view.setGeometry(20, 20, 691, 581)
        # show and retrieve the selected columns
        template_table_view.show()
        return template_table_view
        #self.data_base_content.clicked.connect(self.retrieve_column)


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
        data = self.content_model._data
        data.to_csv("template_creator.csv")
        