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
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

class Ui_CreateNewSeries(object):
    def setupUi(self, CreateNewSeries):
        if not CreateNewSeries.objectName():
            CreateNewSeries.setObjectName(u"CreateNewSeries")
        CreateNewSeries.resize(1149, 617)
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
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 7, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 0, 6, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 200))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 4, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.SeriesStacked.addWidget(self.Series1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")

        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

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
        self.substract_s = QCheckBox(self.groupBox)
        self.substract_s.setObjectName(u"substract_s")

        self.gridLayout.addWidget(self.substract_s, 4, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.add_s = QCheckBox(self.groupBox)
        self.add_s.setObjectName(u"add_s")

        self.gridLayout.addWidget(self.add_s, 6, 0, 1, 1)

        self.divide_s = QCheckBox(self.groupBox)
        self.divide_s.setObjectName(u"divide_s")

        self.gridLayout.addWidget(self.divide_s, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.series_1 = QComboBox(self.groupBox)
        self.series_1.setObjectName(u"series_1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.series_1.sizePolicy().hasHeightForWidth())
        self.series_1.setSizePolicy(sizePolicy)
        self.series_1.setMinimumSize(QSize(50, 0))

        self.gridLayout.addWidget(self.series_1, 1, 0, 1, 1)

        self.series_2 = QComboBox(self.groupBox)
        self.series_2.setObjectName(u"series_2")

        self.gridLayout.addWidget(self.series_2, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 9, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.retranslateUi(CreateNewSeries)

        self.SeriesStacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CreateNewSeries)
    # setupUi

    def retranslateUi(self, CreateNewSeries):
        CreateNewSeries.setWindowTitle(QCoreApplication.translate("CreateNewSeries", u"GroupBox", None))
        CreateNewSeries.setTitle(QCoreApplication.translate("CreateNewSeries", u"GroupBox", None))
        self.pushButton_3.setText(QCoreApplication.translate("CreateNewSeries", u"Preview New Series", None))
        self.pushButton_4.setText(QCoreApplication.translate("CreateNewSeries", u"Add Metadata", None))
        self.pushButton_2.setText(QCoreApplication.translate("CreateNewSeries", u"Add Cursor Bounds", None))
        self.label_3.setText(QCoreApplication.translate("CreateNewSeries", u"Experiment Name:", None))
        self.groupBox.setTitle(QCoreApplication.translate("CreateNewSeries", u"Select Series", None))
        self.substract_s.setText(QCoreApplication.translate("CreateNewSeries", u"Substract", None))
        self.label.setText(QCoreApplication.translate("CreateNewSeries", u"Series 1", None))
        self.add_s.setText(QCoreApplication.translate("CreateNewSeries", u"Add", None))
        self.divide_s.setText(QCoreApplication.translate("CreateNewSeries", u"Divide", None))
        self.label_2.setText(QCoreApplication.translate("CreateNewSeries", u"Series 2", None))
        self.pushButton.setText(QCoreApplication.translate("CreateNewSeries", u"Process", None))
        self.pushButton_5.setText(QCoreApplication.translate("CreateNewSeries", u"Quit", None))
    # retranslateUi

