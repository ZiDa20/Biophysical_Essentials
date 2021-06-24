# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online_anlysis_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Online_Analysis(object):
    def setupUi(self, Online_Analysis):
        Online_Analysis.setObjectName("Online_Analysis")
        Online_Analysis.resize(961, 651)
        self.Notebook = QtWidgets.QTabWidget(Online_Analysis)
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

        self.retranslateUi(Online_Analysis)
        self.Notebook.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Online_Analysis)

    def retranslateUi(self, Online_Analysis):
        _translate = QtCore.QCoreApplication.translate
        Online_Analysis.setWindowTitle(_translate("Online_Analysis", "Form"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.experiment_initialization), _translate("Online_Analysis", "onlinonlineasdasdasd"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.batch_communication), _translate("Online_Analysis", "Batch Communication"))
        self.Notebook.setTabText(self.Notebook.indexOf(self.camera), _translate("Online_Analysis", "Camera"))


class Online_Analysis(QtWidgets.QWidget,Ui_Online_Analysis):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
