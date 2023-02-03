import pandas as pd
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview import Ui_Dialog
import numpy as np
from functools import partial
import duckdb

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

class SelectMetaDataForTreeviewDialog(QDialog, Ui_Dialog):

    def __init__(self, 
                 database_handler,
                 treeview_manager = None, 
                 plot_widget_manager = None,
                 parent=None, 
                 update_treeview = True, 
                 update_plot = None,
                 analysis_function_id = -1,
                 frontend = None):
        
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.treeview_manager = treeview_manager
        self.plot_widget_manager = plot_widget_manager
        self.update_treeview = update_treeview
        self.update_plot = update_plot
        self.analysis_function_id = analysis_function_id
        self.frontend_style = frontend
        self.cancel_button.clicked.connect(self.close)
        self.setWindowTitle("Available Meta Data Label")
        self.setWindowModality(Qt.ApplicationModal)
        if self.frontend_style:
            self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.load_content()
        

    def load_content(self):
        """
               Allows the user to add new meta data parents into the treeview
               @return:
        """

        # get available meta data label for specific experiments linked with this specific analysis
        q = f'select * from global_meta_data where experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})'
        global_meta_data_table = self.database_handler.database.execute(q).fetchdf()
        meta_data_list = global_meta_data_table.columns.values.tolist()
        meta_data_list = meta_data_list[2:len(meta_data_list)]

        # checkboxes are stored in a list to identify checked
        checkbox_list = []
        name_list = []
        for s in meta_data_list:
            c = QCheckBox()

            l1 = QLabel(s)
            available_groups = list(np.unique(global_meta_data_table[s].values))
            l2 = QLabel(', '.join(map(str, available_groups)))

            self.experiment_grid.addWidget(c, meta_data_list.index(s), 0)
            self.experiment_grid.addWidget(l1, meta_data_list.index(s), 1)
            self.experiment_grid.addWidget(l2, meta_data_list.index(s), 2)

            checkbox_list.append(c)
            name_list.append(tuple(["global_meta_data", s, available_groups]))
            c.stateChanged.connect(partial(self.checkbox_state_changed, checkbox_list, name_list))

        for n in ["Series", "Sweeps"]:
            c = QCheckBox()
            l = QLabel("condition")
            checkbox_list.append(c)

            if n == "Series":
                grid = self.series_grid
                column = "series_meta_data"
                table = "experiment_series"
            else:
                grid = self.sweep_grid
                column = "meta_data"
                table = "sweep_meta_data"

            available_groups = self.database_handler.database.execute(
                f'select distinct {column} from {table} ' \
                f'where experiment_name in (select experiment_name ' \
                f'from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})').fetchdf()

            grid.addWidget(c, 0, 0)
            grid.addWidget(l, 0, 1)


            available_groups = list(np.unique(available_groups[column].values))
            l2 = QLabel(', '.join(map(str, available_groups)))
            grid.addWidget(l2, 0, 2)
            print(available_groups)
            name_list.append(tuple([table, column, available_groups]))
            c.stateChanged.connect(partial(self.checkbox_state_changed, checkbox_list, name_list))

        self.finish_button.clicked.connect(partial(self.finish_dialog,checkbox_list,name_list))


    def checkbox_state_changed(self,checkbox_list,name_list, signal):
        """
        update the selection grid
        """
        concatenated_label = []
        for i in range(self.selection_grid.count()):
            self.selection_grid.itemAt(i).widget().deleteLater()

        for i in checkbox_list:
            if i.isChecked():
                available_groups =  name_list[checkbox_list.index(i)][2]
                new_list = []
                if concatenated_label == [] :
                    for a in available_groups:
                        c = QCheckBox()
                        l = QLabel(a)
                        c.setChecked(True)
                        self.selection_grid.addWidget(c, available_groups.index(a), 0)
                        self.selection_grid.addWidget(l, available_groups.index(a), 1)
                    concatenated_label = available_groups
                else:
                    for a in concatenated_label:
                        for b in available_groups:
                            new_string = a + " - " + b
                            new_list.append(new_string)
                            c = QCheckBox()
                            l = QLabel(new_string)
                            self.selection_grid.addWidget(c, len(new_list)-1, 0)
                            self.selection_grid.addWidget(l, len(new_list)-1, 1)
                            c.setChecked(True)
                            print("new_string" , new_string)
                    concatenated_label = new_list
        # create new labels and checkboxes in the selection grid

    def finish_dialog(self,checkbox_list,name_list):
        print("have to close ")
        print(name_list) 
        meta_data_df = pd.DataFrame(columns=["table", "column", "values", "analysis_function_id", "offline_analysis_id"])

        if self.analysis_function_id == -1:
            # use case: meta data get selected for tree views
            for cb in checkbox_list:
                    if cb.isChecked():
                        dt = name_list[checkbox_list.index(cb)]
                        meta_data_df = pd.concat( [meta_data_df, pd.DataFrame({"table":dt[0], "column":dt[1], "values":[dt[2]], "analysis_function_id": self.analysis_function_id}) ] )

            meta_data_df["offline_analysis_id"] = self.database_handler.analysis_id
            self.database_handler.database.register("meta_data_df", meta_data_df)
            self.database_handler.database.execute(f'INSERT INTO selected_meta_data SELECT * FROM meta_data_df')
            self.close()
        else:
            # use case: meta data get selected for specific plots
            for function_id in self.analysis_function_id: # if the tuple is bigger
                for cb in checkbox_list:
                    if cb.isChecked():
                        dt = name_list[checkbox_list.index(cb)]
                        meta_data_df = pd.concat( [meta_data_df, pd.DataFrame({"table":dt[0], "column":dt[1], "values":[dt[2]], "analysis_function_id": function_id}) ] )

            meta_data_df["offline_analysis_id"] = self.database_handler.analysis_id# here still an error ocurrs
            self.close()

            # in case of re-click on the dialog and new meta data selection the table will already exist.
            try:
                self.database_handler.database.register("meta_data_df", meta_data_df)
                selected_meta_data_table = self.database_handler.database.execute(f'Select * from selected_meta_data').fetchdf()
                already_registered = [i for i in self.analysis_function_id if i in selected_meta_data_table["analysis_function_id"].tolist()]
                if already_registered: # checks if the analysis_function id is already in the table if not 
                    self.database_handler.database.execute(f'DELETE FROM selected_meta_data WHERE analysis_function_id in {tuple(already_registered)}')
                    self.database_handler.database.register("meta_data_df", meta_data_df)
                self.database_handler.database.execute(f'INSERT INTO selected_meta_data SELECT * FROM meta_data_df')
                    
                                    
            except duckdb.CatalogException as e:
                print(f"TreeHandler {e}")
                #self.database_handler.database.execute(f'DROP TABLE {table_name}')
                #self.database_handler.database.execute(f'CREATE TABLE {table_name} AS SELECT * FROM meta_data_df')
                # no need to update again

        if self.update_treeview:
            self.treeview_manager.update_treeviews(self.plot_widget_manager)