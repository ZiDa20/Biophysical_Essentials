
from PySide6.QtWidgets import QDialog, QDialogButtonBox  # type: ignore
from QT_GUI.OnlineAnalysis.ui_py.ui_RedundantDialog import Ui_RedundantDialog


class RedundantDialog(QDialog, Ui_RedundantDialog):
    def __init__(self, offline_database, treeview_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.offline_database = offline_database
        self.treeview_name = treeview_name
        self.checkName.clicked.connect(self.check_analysis_in_database)
        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)

    def check_analysis_in_database(self):
        name = self.lineEdit.text() + f"_{self.treeview_name}"
        q = "select * from experiments where experiment_name = $1"
        df = self.offline_database.database.execute(q, [name]).fetchdf()
        if df.empty:
            self.ok_button.setEnabled(True)
            self.checkName.setStyleSheet("background: green;")
            self.treeview_name = name
        else:
            self.checkName.setStyleSheet("background: red;")



