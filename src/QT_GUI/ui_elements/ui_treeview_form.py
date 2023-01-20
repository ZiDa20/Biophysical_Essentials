# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treeview_form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 544)
        self.treeview_experiment_discarded = QTreeView(Form)
        self.treeview_experiment_discarded.setObjectName(u"treeview_experiment_discarded")
        self.treeview_experiment_discarded.setGeometry(QRect(40, 310, 241, 181))
        self.discard_button = QPushButton(Form)
        self.discard_button.setObjectName(u"discard_button")
        self.discard_button.setGeometry(QRect(100, 230, 121, 31))
        self.retrieve_button = QPushButton(Form)
        self.retrieve_button.setObjectName(u"retrieve_button")
        self.retrieve_button.setGeometry(QRect(100, 270, 121, 31))
        self.treeview_experiment = QTreeView(Form)
        self.treeview_experiment.setObjectName(u"treeview_experiment")
        self.treeview_experiment.setGeometry(QRect(40, 40, 241, 181))
        self.treeview_frame_2 = QFrame(Form)
        self.treeview_frame_2.setObjectName(u"treeview_frame_2")
        self.treeview_frame_2.setGeometry(QRect(30, 40, 251, 451))
        self.treeview_frame_2.setFrameShape(QFrame.StyledPanel)
        self.treeview_frame_2.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.discard_button.setText(QCoreApplication.translate("Form", u"Discard", None))
        self.retrieve_button.setText(QCoreApplication.translate("Form", u"Retrieve", None))
    # retranslateUi

