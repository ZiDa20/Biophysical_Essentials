from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview import Ui_Dialog
import numpy as np
from functools import partial

class SelectMetaDataForTreeviewDialog(QDialog, Ui_Dialog):

    def __init__(self, database_handler, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
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
            available_groups = np.unique(global_meta_data_table[s].values)
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
            else:
                grid = self.sweep_grid
                column = "sweep_meta_data"

            grid.addWidget(c, 0, 0)
            grid.addWidget(l, 0, 1)
            available_groups = self.database_handler.database.execute(
                f'select distinct {column} from experiment_series ' \
                f'where experiment_name in (select experiment_name ' \
                f'from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})').fetchdf()

            available_groups = np.unique(available_groups[column].values)
            l2 = QLabel(', '.join(map(str, available_groups)))
            grid.addWidget(l2, 0, 2)
            print(available_groups)
            name_list.append(tuple(["experiment_series", c, available_groups]))
            c.stateChanged.connect(partial(self.checkbox_state_changed, checkbox_list, name_list))

    def checkbox_state_changed(self,checkbox_list,name_list, signal):
        """
        update the selection grid
        """
        concatenated_label = []

        for i in range(self.selection_grid.count()):
            self.selection_grid.itemAt(i).widget().deleteLater()

        for i in checkbox_list:
            if i.isChecked():
                available_groups = list(name_list[checkbox_list.index(i)][2])
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