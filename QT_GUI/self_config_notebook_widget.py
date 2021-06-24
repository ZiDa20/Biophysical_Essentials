# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'self_config_notebook_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        Config_Widget.setObjectName("Config_Widget")
        Config_Widget.resize(961, 651)
        self.Notebook = QtWidgets.QTabWidget(Config_Widget)
        self.Notebook.setGeometry(QtCore.QRect(20, 0, 931, 621))
        self.Notebook.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Notebook.setObjectName("Notebook")
        self.experiment_initialization = QtWidgets.QWidget()
        self.experiment_initialization.setObjectName("experiment_initialization")
        self.Notebook.addTab(self.experiment_initialization, "")
        self.batch_communication = QtWidgets.QWidget()
        self.batch_communication.setObjectName("batch_communication")
        self.Notebook.addTab(self.batch_communication, "")
        self.camera = QtWidgets.QWidget()
        self.camera.setObjectName("camera")
        self.Notebook.addTab(self.camera, "")

        self.retranslateUi(Config_Widget)
        self.Notebook.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Config_Widget)

    def retranslateUi(self, Config_Widget):
        _translate = QtCore.QCoreApplication.translate
        Config_Widget.setWindowTitle(_translate("Config_Widget", "Form"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.experiment_initialization), _translate("Config_Widget", "Experiment Initialization"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.batch_communication), _translate("Config_Widget", "Batch Communication"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.camera), _translate("Config_Widget", "Camera"))

