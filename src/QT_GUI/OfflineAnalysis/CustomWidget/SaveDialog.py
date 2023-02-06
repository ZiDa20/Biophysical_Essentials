from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class SaveDialog(QDialog):
    def __init__(self, label, frontend, parent=None):
        super().__init__(parent)
        self.frontend_style = frontend
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(label)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)