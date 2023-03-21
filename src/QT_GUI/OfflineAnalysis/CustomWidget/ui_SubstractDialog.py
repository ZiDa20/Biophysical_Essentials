# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubstractDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QWidget,QDialog)

class Ui_CreateNewSeries(QDialog):
    def setupUi(self, CreateNewSeries):
        if not CreateNewSeries.objectName():
            CreateNewSeries.setObjectName(u"CreateNewSeries")
        CreateNewSeries.resize(1159, 617)
        self.gridLayout_5 = QGridLayout(CreateNewSeries)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.WholeGrid = QGridLayout()
        self.WholeGrid.setObjectName(u"WholeGrid")
        self.plot_series = QGridLayout()
        self.plot_series.setObjectName(u"plot_series")
        self.SeriesStacked = QStackedWidget(CreateNewSeries)
        self.SeriesStacked.setObjectName(u"SeriesStacked")
        self.Series1 = QWidget()
        self.Series1.setObjectName(u"Series1")
        self.gridLayout_6 = QGridLayout(self.Series1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.PlotGrid = QGridLayout()
        self.PlotGrid.setObjectName(u"PlotGrid")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.PlotGrid.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.PlotGrid, 1, 0, 1, 1)

        self.frame = QFrame(self.Series1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TrimmSeries = QPushButton(self.frame)
        self.TrimmSeries.setObjectName(u"TrimmSeries")

        self.gridLayout_2.addWidget(self.TrimmSeries, 0, 7, 1, 1)

        self.ExperimentCombo = QComboBox(self.frame)
        self.ExperimentCombo.setObjectName(u"ExperimentCombo")

        self.gridLayout_2.addWidget(self.ExperimentCombo, 0, 1, 1, 1)

        self.CursorBound = QPushButton(self.frame)
        self.CursorBound.setObjectName(u"CursorBound")
        self.CursorBound.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_2.addWidget(self.CursorBound, 0, 8, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.PreviewSeries = QPushButton(self.frame)
        self.PreviewSeries.setObjectName(u"PreviewSeries")

        self.gridLayout_2.addWidget(self.PreviewSeries, 0, 9, 1, 1)

        self.AddMeta = QPushButton(self.frame)
        self.AddMeta.setObjectName(u"AddMeta")

        self.gridLayout_2.addWidget(self.AddMeta, 0, 6, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.SeriesStacked.addWidget(self.Series1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Operations = QComboBox(self.page_2)
        self.Operations.setObjectName(u"Operations")

        self.gridLayout_8.addWidget(self.Operations, 1, 1, 1, 1)

        self.Experiment = QComboBox(self.page_2)
        self.Experiment.setObjectName(u"Experiment")

        self.gridLayout_8.addWidget(self.Experiment, 1, 2, 1, 1)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_8.addWidget(self.label_8, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_8.addWidget(self.pushButton, 1, 3, 1, 1)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 0, 3, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.PreviewPlot = QGridLayout()
        self.PreviewPlot.setObjectName(u"PreviewPlot")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.PreviewPlot.addItem(self.verticalSpacer, 0, 0, 1, 1)


        self.gridLayout_9.addLayout(self.PreviewPlot, 1, 0, 1, 1)

        self.SeriesStacked.addWidget(self.page_2)

        self.plot_series.addWidget(self.SeriesStacked, 0, 0, 1, 1)


        self.WholeGrid.addLayout(self.plot_series, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.WholeGrid, 1, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(CreateNewSeries)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.series_2 = QComboBox(self.groupBox)
        self.series_2.setObjectName(u"series_2")

        self.gridLayout_12.addWidget(self.series_2, 0, 0, 1, 1)

        self.select_pgf_series2 = QCheckBox(self.groupBox)
        self.select_pgf_series2.setObjectName(u"select_pgf_series2")

        self.gridLayout_12.addWidget(self.select_pgf_series2, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_12, 16, 0, 1, 1)

        self.AddDataBase = QPushButton(self.groupBox)
        self.AddDataBase.setObjectName(u"AddDataBase")

        self.gridLayout.addWidget(self.AddDataBase, 23, 0, 1, 1)

        self.selectbymetadata = QRadioButton(self.groupBox)
        self.selectbymetadata.setObjectName(u"selectbymetadata")

        self.gridLayout.addWidget(self.selectbymetadata, 7, 0, 1, 1)

        self.quit = QPushButton(self.groupBox)
        self.quit.setObjectName(u"quit")

        self.gridLayout.addWidget(self.quit, 24, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 15, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 12, 0, 1, 1)

        self.divide_s = QCheckBox(self.groupBox)
        self.divide_s.setObjectName(u"divide_s")

        self.gridLayout.addWidget(self.divide_s, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 18, 0, 1, 1)

        self.add_s = QCheckBox(self.groupBox)
        self.add_s.setObjectName(u"add_s")

        self.gridLayout.addWidget(self.add_s, 2, 0, 1, 1)

        self.SeriesLength = QLabel(self.groupBox)
        self.SeriesLength.setObjectName(u"SeriesLength")

        self.gridLayout.addWidget(self.SeriesLength, 17, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.series_1 = QComboBox(self.groupBox)
        self.series_1.setObjectName(u"series_1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.series_1.sizePolicy().hasHeightForWidth())
        self.series_1.setSizePolicy(sizePolicy)
        self.series_1.setMinimumSize(QSize(50, 0))

        self.gridLayout_11.addWidget(self.series_1, 0, 0, 1, 1)

        self.select_pgf_series1 = QCheckBox(self.groupBox)
        self.select_pgf_series1.setObjectName(u"select_pgf_series1")

        self.gridLayout_11.addWidget(self.select_pgf_series1, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_11, 14, 0, 1, 1)

        self.substract_s = QCheckBox(self.groupBox)
        self.substract_s.setObjectName(u"substract_s")

        self.gridLayout.addWidget(self.substract_s, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 11, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.retranslateUi(CreateNewSeries)

        self.SeriesStacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CreateNewSeries)
    # setupUi

    def retranslateUi(self, CreateNewSeries):
        self.TrimmSeries.setText(QCoreApplication.translate("CreateNewSeries", u"Trimm Series", None))
        self.CursorBound.setText(QCoreApplication.translate("CreateNewSeries", u"Add Cursor Bounds", None))
        self.PreviewSeries.setText(QCoreApplication.translate("CreateNewSeries", u"Preview New Series", None))
        self.AddMeta.setText(QCoreApplication.translate("CreateNewSeries", u"Add Metadata", None))
        self.label_3.setText(QCoreApplication.translate("CreateNewSeries", u"Experiment Name:", None))
        self.label_8.setText(QCoreApplication.translate("CreateNewSeries", u"Experiment Name", None))
        self.label_7.setText(QCoreApplication.translate("CreateNewSeries", u"Series Operation", None))
        self.pushButton.setText(QCoreApplication.translate("CreateNewSeries", u"Go Back", None))
        self.label_9.setText(QCoreApplication.translate("CreateNewSeries", u"Go Back", None))
        self.groupBox.setTitle(QCoreApplication.translate("CreateNewSeries", u"Select Series", None))
        self.label_5.setText(QCoreApplication.translate("CreateNewSeries", u"Search By Metadata", None))
        self.select_pgf_series2.setText(QCoreApplication.translate("CreateNewSeries", u"Select PGF", None))
        self.AddDataBase.setText(QCoreApplication.translate("CreateNewSeries", u"Process", None))
        self.selectbymetadata.setText(QCoreApplication.translate("CreateNewSeries", u"Select By Metadata", None))
        self.quit.setText(QCoreApplication.translate("CreateNewSeries", u"Quit", None))
        self.label_2.setText(QCoreApplication.translate("CreateNewSeries", u"Series 2", None))
        self.label_4.setText(QCoreApplication.translate("CreateNewSeries", u"Select Series Operation:", None))
        self.label_6.setText(QCoreApplication.translate("CreateNewSeries", u"Select Series:", None))
        self.divide_s.setText(QCoreApplication.translate("CreateNewSeries", u"Divide", None))
        self.add_s.setText(QCoreApplication.translate("CreateNewSeries", u"Add", None))
        self.SeriesLength.setText(QCoreApplication.translate("CreateNewSeries", u"InfoBox", None))
        self.label.setText(QCoreApplication.translate("CreateNewSeries", u"Series 1", None))
        self.select_pgf_series1.setText(QCoreApplication.translate("CreateNewSeries", u"Select PGF", None))
        self.substract_s.setText(QCoreApplication.translate("CreateNewSeries", u"Substract", None))
    # retranslateUi

