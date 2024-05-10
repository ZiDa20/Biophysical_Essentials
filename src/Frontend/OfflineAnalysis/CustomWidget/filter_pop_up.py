# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_popup_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(979, 547)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(150, 0))
        self.groupBox_3.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.and_checkbox = QCheckBox(self.groupBox_3)
        self.and_checkbox.setObjectName(u"and_checkbox")
        self.and_checkbox.setChecked(True)

        self.gridLayout_8.addWidget(self.and_checkbox, 0, 0, 1, 1)

        self.or_checkbox = QCheckBox(self.groupBox_3)
        self.or_checkbox.setObjectName(u"or_checkbox")

        self.gridLayout_8.addWidget(self.or_checkbox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.contains_series_grid = QGridLayout()
        self.contains_series_grid.setObjectName(u"contains_series_grid")

        self.gridLayout_4.addLayout(self.contains_series_grid, 1, 0, 2, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 3, 1)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.contains_checkbox = QCheckBox(self.groupBox_4)
        self.contains_checkbox.setObjectName(u"contains_checkbox")
        self.contains_checkbox.setChecked(True)

        self.gridLayout_7.addWidget(self.contains_checkbox, 0, 0, 1, 1)

        self.contains_not_checkbox = QCheckBox(self.groupBox_4)
        self.contains_not_checkbox.setObjectName(u"contains_not_checkbox")

        self.gridLayout_7.addWidget(self.contains_not_checkbox, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 1, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_11 = QGridLayout(self.tab_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_7 = QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.slider_upper_threshold_2 = QSlider(self.groupBox_7)
        self.slider_upper_threshold_2.setObjectName(u"slider_upper_threshold_2")
        self.slider_upper_threshold_2.setValue(50)
        self.slider_upper_threshold_2.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.slider_upper_threshold_2, 2, 2, 1, 2)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_9.addWidget(self.label_5, 1, 3, 1, 1)

        self.filter_parameter_combobox = QComboBox(self.groupBox_7)
        self.filter_parameter_combobox.addItem("")
        self.filter_parameter_combobox.addItem("")
        self.filter_parameter_combobox.setObjectName(u"filter_parameter_combobox")

        self.gridLayout_9.addWidget(self.filter_parameter_combobox, 0, 0, 1, 4)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_8, 1, 0, 1, 1)

        self.filter_plot_widget = QGridLayout()
        self.filter_plot_widget.setObjectName(u"filter_plot_widget")

        self.gridLayout_9.addLayout(self.filter_plot_widget, 3, 0, 1, 4)

        self.slider_lower_threshold_2 = QSlider(self.groupBox_7)
        self.slider_lower_threshold_2.setObjectName(u"slider_lower_threshold_2")
        self.slider_lower_threshold_2.setValue(50)
        self.slider_lower_threshold_2.setOrientation(Qt.Horizontal)

        self.gridLayout_9.addWidget(self.slider_lower_threshold_2, 2, 0, 1, 2)


        self.gridLayout_11.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_8 = QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_14 = QGridLayout(self.groupBox_8)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.show_data_distribution = QCheckBox(self.groupBox_8)
        self.show_data_distribution.setObjectName(u"show_data_distribution")

        self.horizontalLayout_2.addWidget(self.show_data_distribution)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_14.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_10 = QGridLayout(self.groupBox_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.comboBox = QComboBox(self.groupBox_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_10.addWidget(self.comboBox, 0, 0, 1, 4)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")

        self.gridLayout_2.addLayout(self.gridLayout_12, 3, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_13 = QGridLayout(self.page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_9 = QGroupBox(self.page)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_15 = QGridLayout(self.groupBox_9)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_3 = QLabel(self.groupBox_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_3, 0, 0, 1, 1)

        self.left_signal_threshold_slider = QSlider(self.groupBox_9)
        self.left_signal_threshold_slider.setObjectName(u"left_signal_threshold_slider")
        self.left_signal_threshold_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.left_signal_threshold_slider, 1, 0, 1, 1)

        self.right_signal_threshold_slider = QSlider(self.groupBox_9)
        self.right_signal_threshold_slider.setObjectName(u"right_signal_threshold_slider")
        self.right_signal_threshold_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_15.addWidget(self.right_signal_threshold_slider, 1, 2, 1, 1)

        self.left_signal_threshold_label = QLabel(self.groupBox_9)
        self.left_signal_threshold_label.setObjectName(u"left_signal_threshold_label")

        self.gridLayout_15.addWidget(self.left_signal_threshold_label, 1, 1, 1, 1)

        self.right_signal_threshold_label = QLabel(self.groupBox_9)
        self.right_signal_threshold_label.setObjectName(u"right_signal_threshold_label")

        self.gridLayout_15.addWidget(self.right_signal_threshold_label, 1, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_2, 0, 2, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_16 = QGridLayout(self.page_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_17 = QGridLayout(self.groupBox_6)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.update_peak_filter = QPushButton(self.groupBox_6)
        self.update_peak_filter.setObjectName(u"update_peak_filter")

        self.gridLayout_17.addWidget(self.update_peak_filter, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_17.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_17.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_17.addWidget(self.label_10, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_17.addWidget(self.lineEdit_3, 2, 1, 1, 3)

        self.lineEdit_2 = QLineEdit(self.groupBox_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_17.addWidget(self.lineEdit_2, 1, 1, 1, 3)

        self.lineEdit = QLineEdit(self.groupBox_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_17.addWidget(self.lineEdit, 0, 1, 1, 3)


        self.gridLayout_16.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_5 = QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.contains_meta_data_grid = QGridLayout()
        self.contains_meta_data_grid.setObjectName(u"contains_meta_data_grid")

        self.gridLayout_6.addLayout(self.contains_meta_data_grid, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.apply_filter_button = QPushButton(Dialog)
        self.apply_filter_button.setObjectName(u"apply_filter_button")

        self.gridLayout.addWidget(self.apply_filter_button, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_3.setTitle("")
        self.and_checkbox.setText(QCoreApplication.translate("Dialog", u"AND", None))
        self.or_checkbox.setText(QCoreApplication.translate("Dialog", u"OR", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Contains Series", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filter for Experiments that contain/do not contain a specific series protocoll. For mutliple selection, you can choose between OR/AND.", None))
        self.groupBox_4.setTitle("")
        self.contains_checkbox.setText(QCoreApplication.translate("Dialog", u"Contains", None))
        self.contains_not_checkbox.setText(QCoreApplication.translate("Dialog", u"Contains Not", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Series Filter", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Parameter Value", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"50", None))
        self.filter_parameter_combobox.setItemText(0, QCoreApplication.translate("Dialog", u"CSlow", None))
        self.filter_parameter_combobox.setItemText(1, QCoreApplication.translate("Dialog", u"RSeries", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"50", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Upper Threshold: ", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Lower Threshold: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Parameter Filter", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"2. Activate the plot checkbox below to scan the data for the selected criteria.", None))
        self.show_data_distribution.setText(QCoreApplication.translate("Dialog", u"Show Data Distribution Plot", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"1. Choose a criteria to select and discard data", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Minimum", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Maximum", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Number of Peaks", None))

        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"3. Adapt the thresholds using the sliders", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Lower Threshold", None))
        self.left_signal_threshold_label.setText("")
        self.right_signal_threshold_label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Upper Threshold", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"3. Enter the thresholds ", None))
        self.update_peak_filter.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Enter the minimum amount of peaks per sweep:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Enter the minimum distance between two peaks:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Enter the minimum amplitude of each peak:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Dialog", u"min peak height", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"min distance", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"peak number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Signal Thresholds", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Contains Meta Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Meta Data Filter", None))
        self.apply_filter_button.setText(QCoreApplication.translate("Dialog", u"Apply Filter", None))
    # retranslateUi

