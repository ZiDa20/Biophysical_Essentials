
from PySide6.QtWidgets import QDialog, QDialogButtonBox  # type: ignore
from QT_GUI.OnlineAnalysis.ui_py.ui_RedundantDialog import Ui_RedundantDialog
from PySide6.QtCore import Qt

class RedundantDialog(QDialog, Ui_RedundantDialog):
    def __init__(self, offline_database, treeview_name, logger, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.offline_database = offline_database
        self._treeview_name = treeview_name
        self._new_treeview_name = None
        self.logger = logger
        self.checkName.clicked.connect(self.check_analysis_in_database)
        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.checkBox.setEnabled(False)
        self.checkBox.stateChanged.connect(self.set_discarded_state)
        self.ok_button.setEnabled(False)

    @property
    def treeview_name(self):
        return self._treeview_name
    
    @property
    def new_treeview_name(self):
        return self._new_treeview_name
    
    @new_treeview_name.setter
    def new_treeview_name(self, value):
        self._new_treeview_name = value

    def check_analysis_in_database(self) -> None:
        """"""
        name = self.lineEdit.text() + f"_{self.treeview_name}"
        q = "select * from experiments where experiment_name = $1"
        df = self.offline_database.database.execute(q, [name]).fetchdf()
        if df.empty:
            self.ok_button.setEnabled(True)
            self.checkName.setStyleSheet("background: green;")
            self.new_treeview_name = name
            self.checkBox.setEnabled(True)
        else:
            self.checkName.setStyleSheet("background: red;")

    def set_discarded_state(self, state) -> None:
        """ """
        print(state)
        if state == 2:
            self.offline_database.database.execute("""UPDATE experiment_series
                                                        SET discarded = True
                                                        WHERE experiment_name = (?)
                                                    """, [self.treeview_name])
            self.logger.info("Successfully replaced the discarded state by True in Redundant Dialog")
        
        elif state == 0:
            self.offline_database.database.execute("""UPDATE experiment_series
                                                        SET discarded = False
                                                        WHERE experiment_name = (?)
                                                    """, [self.treeview_name])
            self.logger.info("Successfully replaced the discarded state by False in Redundant Dialog")




