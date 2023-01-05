# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_meta_data_for_treeview.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(546, 541)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sweeps = QGroupBox(Dialog)
        self.sweeps.setObjectName(u"sweeps")
        self.gridLayout_3 = QGridLayout(self.sweeps)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.sweep_grid = QGridLayout()
        self.sweep_grid.setObjectName(u"sweep_grid")

        self.gridLayout_3.addLayout(self.sweep_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.sweeps, 4, 0, 1, 2)

        self.series = QGroupBox(Dialog)
        self.series.setObjectName(u"series")
        self.gridLayout_5 = QGridLayout(self.series)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.series_grid = QGridLayout()
        self.series_grid.setObjectName(u"series_grid")

        self.gridLayout_5.addLayout(self.series_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.series, 2, 0, 1, 2)

        self.experiments = QGroupBox(Dialog)
        self.experiments.setObjectName(u"experiments")
        self.gridLayout_4 = QGridLayout(self.experiments)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.experiment_grid = QGridLayout()
        self.experiment_grid.setObjectName(u"experiment_grid")

        self.gridLayout_4.addLayout(self.experiment_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.experiments, 0, 0, 1, 2)

        self.finish_button = QPushButton(Dialog)
        self.finish_button.setObjectName(u"finish_button")

        self.gridLayout.addWidget(self.finish_button, 8, 0, 1, 1)

        self.cancel_button = QPushButton(Dialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.gridLayout.addWidget(self.cancel_button, 8, 1, 1, 1)

        self.line_3 = QFrame(Dialog)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 2)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)

        self.line_2 = QFrame(Dialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 2)

        self.selection = QGroupBox(Dialog)
        self.selection.setObjectName(u"selection")
        self.gridLayout_6 = QGridLayout(self.selection)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.selection_grid = QGridLayout()
        self.selection_grid.setObjectName(u"selection_grid")

        self.gridLayout_6.addLayout(self.selection_grid, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.selection, 7, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sweeps.setTitle(QCoreApplication.translate("Dialog", u"Sweeps", None))
        self.series.setTitle(QCoreApplication.translate("Dialog", u"Series", None))
        self.experiments.setTitle(QCoreApplication.translate("Dialog", u"Experiments", None))
        self.finish_button.setText(QCoreApplication.translate("Dialog", u"Finish", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.selection.setTitle(QCoreApplication.translate("Dialog", u"Your Selection", None))
    # retranslateUi

