# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'solutions_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_SolutionsDialog(object):
    def setupUi(self, SolutionsDialog):
        if not SolutionsDialog.objectName():
            SolutionsDialog.setObjectName(u"SolutionsDialog")
        SolutionsDialog.resize(431, 344)
        self.gridLayout_2 = QGridLayout(SolutionsDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line = QFrame(SolutionsDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 1)

        self.line_2 = QFrame(SolutionsDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.solution_type = QComboBox(SolutionsDialog)
        self.solution_type.setObjectName(u"solution_type")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.solution_type.sizePolicy().hasHeightForWidth())
        self.solution_type.setSizePolicy(sizePolicy)
        self.solution_type.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.solution_type, 1, 2, 1, 1)

        self.solutions_name = QLineEdit(SolutionsDialog)
        self.solutions_name.setObjectName(u"solutions_name")

        self.gridLayout.addWidget(self.solutions_name, 1, 1, 1, 1)

        self.label = QLabel(SolutionsDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_4 = QLabel(SolutionsDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.database_save = QPushButton(SolutionsDialog)
        self.database_save.setObjectName(u"database_save")

        self.gridLayout_2.addWidget(self.database_save, 10, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(SolutionsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 11, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(SolutionsDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(SolutionsDialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 3, 1, 1)

        self.label_2 = QLabel(SolutionsDialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignTop)

        self.label_3 = QLabel(SolutionsDialog)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label_3, 0, 3, 1, 1, Qt.AlignTop)


        self.gridLayout_2.addLayout(self.gridLayout_3, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 8, 0, 1, 1)

        self.add_ions = QPushButton(SolutionsDialog)
        self.add_ions.setObjectName(u"add_ions")

        self.gridLayout_2.addWidget(self.add_ions, 5, 0, 1, 1)


        self.retranslateUi(SolutionsDialog)
        self.buttonBox.accepted.connect(SolutionsDialog.accept)
        self.buttonBox.rejected.connect(SolutionsDialog.reject)

        QMetaObject.connectSlotsByName(SolutionsDialog)
    # setupUi

    def retranslateUi(self, SolutionsDialog):
        SolutionsDialog.setWindowTitle(QCoreApplication.translate("SolutionsDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SolutionsDialog", u"Solution Name:", None))
        self.label_4.setText(QCoreApplication.translate("SolutionsDialog", u"Solution Type", None))
        self.database_save.setText(QCoreApplication.translate("SolutionsDialog", u"Save to Database", None))
        self.label_2.setText(QCoreApplication.translate("SolutionsDialog", u"Ion:", None))
        self.label_3.setText(QCoreApplication.translate("SolutionsDialog", u"Concentration:", None))
        self.add_ions.setText(QCoreApplication.translate("SolutionsDialog", u"Add", None))
    # retranslateUi

