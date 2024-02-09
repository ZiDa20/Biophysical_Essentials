# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self_config_notebook_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListWidgetItem, QMdiArea, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableView, QTextEdit, QVBoxLayout, QWidget, QMainWindow)

from Frontend.CustomWidget.groupbox_resizing_class import GroupBoxSize
from Frontend.CustomWidget.dropable_list_view import ListView

class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(1478, 1222)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Config_Widget.sizePolicy().hasHeightForWidth())
        Config_Widget.setSizePolicy(sizePolicy)
        Config_Widget.setLayoutDirection(Qt.LeftToRight)
        Config_Widget.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(Config_Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(10)
        self.frame_2 = QFrame(Config_Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_2)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.groupBox_11 = QGroupBox(self.frame_2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_51 = QGridLayout(self.groupBox_11)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_50 = QGridLayout()
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.metadata_table = QPushButton(self.groupBox_11)
        self.metadata_table.setObjectName(u"metadata_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.metadata_table.sizePolicy().hasHeightForWidth())
        self.metadata_table.setSizePolicy(sizePolicy1)
        self.metadata_table.setMinimumSize(QSize(30, 30))
        self.metadata_table.setMaximumSize(QSize(30, 30))

        self.gridLayout_50.addWidget(self.metadata_table, 0, 0, 1, 1)

        self.change_solutions = QPushButton(self.groupBox_11)
        self.change_solutions.setObjectName(u"change_solutions")
        self.change_solutions.setMinimumSize(QSize(30, 30))
        self.change_solutions.setMaximumSize(QSize(30, 30))

        self.gridLayout_50.addWidget(self.change_solutions, 0, 1, 1, 1)


        self.gridLayout_51.addLayout(self.gridLayout_50, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_11, 0, 3, 1, 1)

        self.groupBox_13 = QGroupBox(self.frame_2)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.gridLayout_55 = QGridLayout(self.groupBox_13)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setHorizontalSpacing(0)
        self.go_to_online = QPushButton(self.groupBox_13)
        self.go_to_online.setObjectName(u"go_to_online")
        sizePolicy1.setHeightForWidth(self.go_to_online.sizePolicy().hasHeightForWidth())
        self.go_to_online.setSizePolicy(sizePolicy1)
        self.go_to_online.setMinimumSize(QSize(30, 30))
        self.go_to_online.setMaximumSize(QSize(30, 30))

        self.gridLayout_19.addWidget(self.go_to_online, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_15 = QLabel(self.groupBox_13)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_19.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_55.addLayout(self.gridLayout_19, 1, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_13, 0, 1, 1, 1)

        self.groupBox_16 = QGroupBox(self.frame_2)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_59 = QGridLayout(self.groupBox_16)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.gridLayout_59.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.transfer_to_online_analysis_button = QPushButton(self.groupBox_16)
        self.transfer_to_online_analysis_button.setObjectName(u"transfer_to_online_analysis_button")
        sizePolicy1.setHeightForWidth(self.transfer_to_online_analysis_button.sizePolicy().hasHeightForWidth())
        self.transfer_to_online_analysis_button.setSizePolicy(sizePolicy1)
        self.transfer_to_online_analysis_button.setMinimumSize(QSize(30, 30))
        self.transfer_to_online_analysis_button.setMaximumSize(QSize(30, 30))
        self.transfer_to_online_analysis_button.setStyleSheet(u"")

        self.gridLayout_23.addWidget(self.transfer_to_online_analysis_button, 0, 0, 1, 1)


        self.gridLayout_59.addLayout(self.gridLayout_23, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_16, 0, 8, 1, 1)

        self.groupBox_15 = QGroupBox(self.frame_2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_57 = QGridLayout(self.groupBox_15)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.start_analysis = QPushButton(self.groupBox_15)
        self.start_analysis.setObjectName(u"start_analysis")
        sizePolicy1.setHeightForWidth(self.start_analysis.sizePolicy().hasHeightForWidth())
        self.start_analysis.setSizePolicy(sizePolicy1)
        self.start_analysis.setMinimumSize(QSize(30, 30))
        self.start_analysis.setMaximumSize(QSize(30, 30))

        self.gridLayout_39.addWidget(self.start_analysis, 0, 0, 1, 1)

        self.clear_sequence = QPushButton(self.groupBox_15)
        self.clear_sequence.setObjectName(u"clear_sequence")
        self.clear_sequence.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.clear_sequence.sizePolicy().hasHeightForWidth())
        self.clear_sequence.setSizePolicy(sizePolicy1)
        self.clear_sequence.setMinimumSize(QSize(30, 30))
        self.clear_sequence.setMaximumSize(QSize(30, 30))
        self.clear_sequence.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_39.addWidget(self.clear_sequence, 0, 2, 1, 1)

        self.stop_experiment_button = QPushButton(self.groupBox_15)
        self.stop_experiment_button.setObjectName(u"stop_experiment_button")
        sizePolicy1.setHeightForWidth(self.stop_experiment_button.sizePolicy().hasHeightForWidth())
        self.stop_experiment_button.setSizePolicy(sizePolicy1)
        self.stop_experiment_button.setMinimumSize(QSize(30, 30))
        self.stop_experiment_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_39.addWidget(self.stop_experiment_button, 0, 1, 1, 1)


        self.gridLayout_57.addLayout(self.gridLayout_39, 0, 1, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_15, 0, 7, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_58 = QGridLayout(self.groupBox_5)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_45 = QGridLayout()
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setHorizontalSpacing(8)
        self.go_back_button = QPushButton(self.groupBox_5)
        self.go_back_button.setObjectName(u"go_back_button")
        self.go_back_button.setMinimumSize(QSize(30, 30))
        self.go_back_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_45.addWidget(self.go_back_button, 0, 2, 1, 1)

        self.go_home = QPushButton(self.groupBox_5)
        self.go_home.setObjectName(u"go_home")
        self.go_home.setMinimumSize(QSize(30, 30))
        self.go_home.setMaximumSize(QSize(30, 30))

        self.gridLayout_45.addWidget(self.go_home, 0, 0, 1, 1)

        self.fo_forward_button = QPushButton(self.groupBox_5)
        self.fo_forward_button.setObjectName(u"fo_forward_button")
        self.fo_forward_button.setMinimumSize(QSize(30, 30))
        self.fo_forward_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_45.addWidget(self.fo_forward_button, 0, 3, 1, 1)

        self.line = QFrame(self.groupBox_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_45.addWidget(self.line, 0, 1, 1, 1)


        self.gridLayout_58.addLayout(self.gridLayout_45, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.frame_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_56 = QGridLayout(self.groupBox_14)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.switch_to_testing = QPushButton(self.groupBox_14)
        self.switch_to_testing.setObjectName(u"switch_to_testing")
        sizePolicy1.setHeightForWidth(self.switch_to_testing.sizePolicy().hasHeightForWidth())
        self.switch_to_testing.setSizePolicy(sizePolicy1)
        self.switch_to_testing.setMinimumSize(QSize(30, 30))
        self.switch_to_testing.setMaximumSize(QSize(30, 30))

        self.gridLayout_37.addWidget(self.switch_to_testing, 0, 0, 1, 1)

        self.download_notebook = QPushButton(self.groupBox_14)
        self.download_notebook.setObjectName(u"download_notebook")
        sizePolicy1.setHeightForWidth(self.download_notebook.sizePolicy().hasHeightForWidth())
        self.download_notebook.setSizePolicy(sizePolicy1)
        self.download_notebook.setMinimumSize(QSize(30, 30))
        self.download_notebook.setMaximumSize(QSize(30, 30))

        self.gridLayout_37.addWidget(self.download_notebook, 0, 1, 1, 1)


        self.gridLayout_56.addLayout(self.gridLayout_37, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_14, 0, 6, 1, 1)

        self.groupBox_12 = QGroupBox(self.frame_2)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_54 = QGridLayout(self.groupBox_12)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.gridLayout_54.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.establish_connection_button = QPushButton(self.groupBox_12)
        self.establish_connection_button.setObjectName(u"establish_connection_button")
        sizePolicy1.setHeightForWidth(self.establish_connection_button.sizePolicy().hasHeightForWidth())
        self.establish_connection_button.setSizePolicy(sizePolicy1)
        self.establish_connection_button.setMinimumSize(QSize(30, 30))
        self.establish_connection_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_53.addWidget(self.establish_connection_button, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_23 = QLabel(self.groupBox_12)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_53.addWidget(self.label_23, 0, 0, 1, 1, Qt.AlignHCenter)


        self.gridLayout_54.addLayout(self.gridLayout_53, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_12, 0, 5, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_48 = QGridLayout(self.groupBox_9)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_46 = QGridLayout()
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.add_metadata_button = QPushButton(self.groupBox_9)
        self.add_metadata_button.setObjectName(u"add_metadata_button")
        sizePolicy1.setHeightForWidth(self.add_metadata_button.sizePolicy().hasHeightForWidth())
        self.add_metadata_button.setSizePolicy(sizePolicy1)
        self.add_metadata_button.setMinimumSize(QSize(30, 0))
        self.add_metadata_button.setMaximumSize(QSize(30, 30))

        self.gridLayout_46.addWidget(self.add_metadata_button, 0, 0, 1, 1)

        self.database_save_2 = QPushButton(self.groupBox_9)
        self.database_save_2.setObjectName(u"database_save_2")
        sizePolicy1.setHeightForWidth(self.database_save_2.sizePolicy().hasHeightForWidth())
        self.database_save_2.setSizePolicy(sizePolicy1)
        self.database_save_2.setMinimumSize(QSize(30, 30))
        self.database_save_2.setMaximumSize(QSize(30, 30))

        self.gridLayout_46.addWidget(self.database_save_2, 0, 1, 1, 1)


        self.gridLayout_48.addLayout(self.gridLayout_46, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_9, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_21 = QGridLayout(self.groupBox_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 1, 0, -1)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.save_plot_online = QPushButton(self.groupBox_2)
        self.save_plot_online.setObjectName(u"save_plot_online")
        self.save_plot_online.setMinimumSize(QSize(30, 30))
        self.save_plot_online.setMaximumSize(QSize(30, 30))

        self.gridLayout_20.addWidget(self.save_plot_online, 0, 0, 1, 1)

        self.plot_home = QPushButton(self.groupBox_2)
        self.plot_home.setObjectName(u"plot_home")
        self.plot_home.setMinimumSize(QSize(30, 30))
        self.plot_home.setMaximumSize(QSize(30, 30))

        self.gridLayout_20.addWidget(self.plot_home, 0, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 0, 1, 1)


        self.gridLayout_38.addWidget(self.groupBox_2, 0, 4, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 1)

        self.experiment_control_stacked = QStackedWidget(Config_Widget)
        self.experiment_control_stacked.setObjectName(u"experiment_control_stacked")
        self.start_experiment = QWidget()
        self.start_experiment.setObjectName(u"start_experiment")
        self.gridLayout_44 = QGridLayout(self.start_experiment)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_63 = QGridLayout()
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.groupBox_23 = QGroupBox(self.start_experiment)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.groupBox_23.setFont(font)
        self.gridLayout_5 = QGridLayout(self.groupBox_23)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(20)
        self.label_243 = QLabel(self.groupBox_23)
        self.label_243.setObjectName(u"label_243")
        sizePolicy1.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_243, 0, 0, 1, 1)

        self.label_244 = QLabel(self.groupBox_23)
        self.label_244.setObjectName(u"label_244")
        sizePolicy1.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_244, 0, 1, 1, 1)

        self.extracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.extracellular_sol_com_1.setObjectName(u"extracellular_sol_com_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.extracellular_sol_com_1.sizePolicy().hasHeightForWidth())
        self.extracellular_sol_com_1.setSizePolicy(sizePolicy2)
        self.extracellular_sol_com_1.setMinimumSize(QSize(0, 30))
        self.extracellular_sol_com_1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.extracellular_sol_com_1, 1, 0, 1, 1)

        self.Intracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.Intracellular_sol_com_1.setObjectName(u"Intracellular_sol_com_1")
        self.Intracellular_sol_com_1.setMinimumSize(QSize(0, 30))
        self.Intracellular_sol_com_1.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.Intracellular_sol_com_1, 1, 1, 1, 1)

        self.S2_3 = QLineEdit(self.groupBox_23)
        self.S2_3.setObjectName(u"S2_3")
        self.S2_3.setMinimumSize(QSize(0, 30))
        self.S2_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.S2_3, 3, 0, 1, 1)

        self.ent_ph_int_set = QLineEdit(self.groupBox_23)
        self.ent_ph_int_set.setObjectName(u"ent_ph_int_set")
        self.ent_ph_int_set.setMinimumSize(QSize(0, 30))
        self.ent_ph_int_set.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_17.addWidget(self.ent_ph_int_set, 3, 1, 1, 1)

        self.ent_ph_set = QLabel(self.groupBox_23)
        self.ent_ph_set.setObjectName(u"ent_ph_set")
        sizePolicy1.setHeightForWidth(self.ent_ph_set.sizePolicy().hasHeightForWidth())
        self.ent_ph_set.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.ent_ph_set, 2, 0, 1, 1)

        self.label_247 = QLabel(self.groupBox_23)
        self.label_247.setObjectName(u"label_247")
        sizePolicy1.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_247, 2, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_17, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 3, 1, 1, 1)


        self.gridLayout_63.addWidget(self.groupBox_23, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.start_experiment)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(20)
        self.online_analysis_file_set = QLineEdit(self.groupBox_4)
        self.online_analysis_file_set.setObjectName(u"online_analysis_file_set")
        self.online_analysis_file_set.setMinimumSize(QSize(0, 30))
        self.online_analysis_file_set.setMaximumSize(QSize(400, 30))

        self.gridLayout_3.addWidget(self.online_analysis_file_set, 5, 1, 1, 1)

        self.button_pgf_set = QPushButton(self.groupBox_4)
        self.button_pgf_set.setObjectName(u"button_pgf_set")
        self.button_pgf_set.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_3.addWidget(self.button_pgf_set, 1, 3, 1, 1)

        self.button_protocol_set = QPushButton(self.groupBox_4)
        self.button_protocol_set.setObjectName(u"button_protocol_set")

        self.gridLayout_3.addWidget(self.button_protocol_set, 3, 3, 1, 1)

        self.protocol_file_set = QLineEdit(self.groupBox_4)
        self.protocol_file_set.setObjectName(u"protocol_file_set")
        self.protocol_file_set.setMinimumSize(QSize(0, 30))
        self.protocol_file_set.setMaximumSize(QSize(400, 30))

        self.gridLayout_3.addWidget(self.protocol_file_set, 3, 1, 1, 1)

        self.button_batch_1 = QPushButton(self.groupBox_4)
        self.button_batch_1.setObjectName(u"button_batch_1")
        self.button_batch_1.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.button_batch_1, 7, 3, 1, 1)

        self.button_onl_analysis_set = QPushButton(self.groupBox_4)
        self.button_onl_analysis_set.setObjectName(u"button_onl_analysis_set")

        self.gridLayout_3.addWidget(self.button_onl_analysis_set, 5, 3, 1, 1)

        self.Batch1 = QLineEdit(self.groupBox_4)
        self.Batch1.setObjectName(u"Batch1")
        self.Batch1.setMinimumSize(QSize(300, 30))
        self.Batch1.setMaximumSize(QSize(400, 30))

        self.gridLayout_3.addWidget(self.Batch1, 7, 1, 1, 1, Qt.AlignTop)

        self.pg_file_set = QLineEdit(self.groupBox_4)
        self.pg_file_set.setObjectName(u"pg_file_set")
        self.pg_file_set.setMinimumSize(QSize(300, 30))
        self.pg_file_set.setMaximumSize(QSize(400, 30))

        self.gridLayout_3.addWidget(self.pg_file_set, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignRight)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1, Qt.AlignRight)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1, Qt.AlignRight)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1, Qt.AlignRight)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_63.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_17 = QGroupBox(self.start_experiment)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.groupBox_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(20)
        self.lineEdit_5 = QLineEdit(self.groupBox_17)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_5, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_17)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_17)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_19, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.groupBox_17)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_6, 5, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_17)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_17)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_17)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_17)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_17)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_17)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_4.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_17)
        self.label_20.setObjectName(u"label_20")
        sizePolicy3.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_20, 4, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_17)
        self.label_21.setObjectName(u"label_21")
        sizePolicy3.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.label_21, 4, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 1, 0, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)


        self.gridLayout_63.addWidget(self.groupBox_17, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.start_experiment)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setVerticalSpacing(20)
        self.patched_cells = QLineEdit(self.groupBox_6)
        self.patched_cells.setObjectName(u"patched_cells")
        self.patched_cells.setMinimumSize(QSize(0, 30))
        self.patched_cells.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.patched_cells, 5, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_18.addWidget(self.label_9, 4, 1, 1, 1)

        self.cell_type_desc = QLineEdit(self.groupBox_6)
        self.cell_type_desc.setObjectName(u"cell_type_desc")
        self.cell_type_desc.setMinimumSize(QSize(0, 30))
        self.cell_type_desc.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.cell_type_desc, 3, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_18.addWidget(self.label_22, 2, 0, 1, 1)

        self.ent_date_prep = QLineEdit(self.groupBox_6)
        self.ent_date_prep.setObjectName(u"ent_date_prep")
        self.ent_date_prep.setMinimumSize(QSize(0, 30))
        self.ent_date_prep.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.ent_date_prep, 3, 0, 1, 1)

        self.min_number_cells = QLineEdit(self.groupBox_6)
        self.min_number_cells.setObjectName(u"min_number_cells")
        self.min_number_cells.setMinimumSize(QSize(0, 30))
        self.min_number_cells.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.min_number_cells, 5, 0, 1, 1)

        self.experiment_type_desc = QLineEdit(self.groupBox_6)
        self.experiment_type_desc.setObjectName(u"experiment_type_desc")
        self.experiment_type_desc.setMinimumSize(QSize(0, 30))
        self.experiment_type_desc.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_18.addWidget(self.experiment_type_desc, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_6, 0, 1, 1, 1)

        self.experiment_label = QLineEdit(self.groupBox_6)
        self.experiment_label.setObjectName(u"experiment_label")

        self.gridLayout_18.addWidget(self.experiment_label, 1, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_18.addWidget(self.label_24, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_18, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_63.addWidget(self.groupBox_6, 1, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_63, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.start_experiment)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(16777215, 150))
        self.groupBox_7.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.check_connection = QTextEdit(self.groupBox_7)
        self.check_connection.setObjectName(u"check_connection")

        self.gridLayout_9.addWidget(self.check_connection, 5, 0, 1, 1)


        self.gridLayout_44.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.experiment_control_stacked.addWidget(self.start_experiment)
        self.experiment_init = QWidget()
        self.experiment_init.setObjectName(u"experiment_init")
        self.gridLayout_64 = QGridLayout(self.experiment_init)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.ProtocolBox = QGroupBox(self.experiment_init)
        self.ProtocolBox.setObjectName(u"ProtocolBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ProtocolBox.sizePolicy().hasHeightForWidth())
        self.ProtocolBox.setSizePolicy(sizePolicy4)
        self.ProtocolBox.setMinimumSize(QSize(600, 0))
        self.ProtocolBox.setMaximumSize(QSize(800, 16777215))
        self.ProtocolBox.setFont(font)
        self.gridLayout_10 = QGridLayout(self.ProtocolBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.scrollArea_5 = QScrollArea(self.ProtocolBox)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMinimumSize(QSize(0, 0))
        self.scrollArea_5.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 225, 1055))
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.listWidget = ListView(self.scrollAreaWidgetContents_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_16.addWidget(self.listWidget, 1, 1, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_16.addWidget(self.label_10, 0, 1, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_10.addWidget(self.scrollArea_5, 0, 2, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.exp_stacked = QStackedWidget(self.ProtocolBox)
        self.exp_stacked.setObjectName(u"exp_stacked")
        self.series_page = QWidget()
        self.series_page.setObjectName(u"series_page")
        self.gridLayout_49 = QGridLayout(self.series_page)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.scrollArea = QScrollArea(self.series_page)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 232, 1040))
        self.gridLayout_27 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.SeriesWidget = ListView(self.scrollAreaWidgetContents)
        self.SeriesWidget.setObjectName(u"SeriesWidget")

        self.gridLayout_27.addWidget(self.SeriesWidget, 1, 0, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_27.addWidget(self.label_11, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_49.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.exp_stacked.addWidget(self.series_page)
        self.modi_page = QWidget()
        self.modi_page.setObjectName(u"modi_page")
        self.gridLayout_61 = QGridLayout(self.modi_page)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.scrollArea_3 = QScrollArea(self.modi_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(0, 250))
        self.scrollArea_3.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 232, 1040))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.general_commands_labels = ListView(self.scrollAreaWidgetContents_3)
        self.general_commands_labels.setObjectName(u"general_commands_labels")
        self.general_commands_labels.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_26.addWidget(self.general_commands_labels, 1, 0, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_26.addWidget(self.label_12, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_61.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.exp_stacked.addWidget(self.modi_page)
        self.label_page = QWidget()
        self.label_page.setObjectName(u"label_page")
        self.gridLayout_62 = QGridLayout(self.label_page)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.scrollArea_4 = QScrollArea(self.label_page)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 232, 1040))
        self.gridLayout_29 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.SeriesWidget_2 = ListView(self.scrollAreaWidgetContents_4)
        self.SeriesWidget_2.setObjectName(u"SeriesWidget_2")

        self.gridLayout_29.addWidget(self.SeriesWidget_2, 1, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_29.addWidget(self.label_13, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_62.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.exp_stacked.addWidget(self.label_page)
        self.protocol_page = QWidget()
        self.protocol_page.setObjectName(u"protocol_page")
        self.gridLayout_60 = QGridLayout(self.protocol_page)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.scrollArea_2 = QScrollArea(self.protocol_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QSize(0, 320))
        self.scrollArea_2.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 225, 1041))
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.protocol_widget = ListView(self.scrollAreaWidgetContents_2)
        self.protocol_widget.setObjectName(u"protocol_widget")
        self.protocol_widget.setMinimumSize(QSize(0, 0))

        self.gridLayout_28.addWidget(self.protocol_widget, 1, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_28.addWidget(self.label_14, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_60.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.exp_stacked.addWidget(self.protocol_page)

        self.gridLayout_25.addWidget(self.exp_stacked, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_25, 0, 1, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(15)
        self.series_select = QPushButton(self.ProtocolBox)
        self.series_select.setObjectName(u"series_select")

        self.gridLayout_15.addWidget(self.series_select, 1, 0, 1, 1)

        self.protocols_select = QPushButton(self.ProtocolBox)
        self.protocols_select.setObjectName(u"protocols_select")

        self.gridLayout_15.addWidget(self.protocols_select, 2, 0, 1, 1)

        self.label = QLabel(self.ProtocolBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_15.addWidget(self.label, 0, 0, 1, 1)

        self.modi_select = QPushButton(self.ProtocolBox)
        self.modi_select.setObjectName(u"modi_select")

        self.gridLayout_15.addWidget(self.modi_select, 4, 0, 1, 1)

        self.labels_select = QPushButton(self.ProtocolBox)
        self.labels_select.setObjectName(u"labels_select")

        self.gridLayout_15.addWidget(self.labels_select, 3, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 5, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.ProtocolBox, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = GroupBoxSize(self.experiment_init)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(500, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_14 = QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.camera_snapshot_2 = QWidget(self.groupBox)
        self.camera_snapshot_2.setObjectName(u"camera_snapshot_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.camera_snapshot_2.sizePolicy().hasHeightForWidth())
        self.camera_snapshot_2.setSizePolicy(sizePolicy5)
        self.camera_snapshot_2.setMinimumSize(QSize(125, 0))
        self.camera_snapshot_2.setMaximumSize(QSize(150, 16777215))
        self.gridLayout_13 = QGridLayout(self.camera_snapshot_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.camera_horizontal = QVBoxLayout()
        self.camera_horizontal.setObjectName(u"camera_horizontal")

        self.gridLayout_13.addLayout(self.camera_horizontal, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.camera_snapshot_2, 1, 3, 1, 1)

        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.Camera_Live_Feed = QGraphicsView(self.groupBox)
        self.Camera_Live_Feed.setObjectName(u"Camera_Live_Feed")
        sizePolicy.setHeightForWidth(self.Camera_Live_Feed.sizePolicy().hasHeightForWidth())
        self.Camera_Live_Feed.setSizePolicy(sizePolicy)
        self.Camera_Live_Feed.setMinimumSize(QSize(16777215, 200))
        self.Camera_Live_Feed.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_47.addWidget(self.Camera_Live_Feed, 0, 2, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(0)
        self.gridLayout_31.setVerticalSpacing(5)
        self.quality = QLabel(self.groupBox)
        self.quality.setObjectName(u"quality")
        sizePolicy1.setHeightForWidth(self.quality.sizePolicy().hasHeightForWidth())
        self.quality.setSizePolicy(sizePolicy1)
        self.quality.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.quality.setFont(font1)
        self.quality.setStyleSheet(u"")

        self.gridLayout_31.addWidget(self.quality, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_5, 12, 0, 1, 1)

        self.cfast_qc = QLineEdit(self.groupBox)
        self.cfast_qc.setObjectName(u"cfast_qc")
        sizePolicy1.setHeightForWidth(self.cfast_qc.sizePolicy().hasHeightForWidth())
        self.cfast_qc.setSizePolicy(sizePolicy1)
        self.cfast_qc.setMinimumSize(QSize(70, 30))
        self.cfast_qc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc, 10, 0, 1, 1)

        self.cfast_qc_2 = QLineEdit(self.groupBox)
        self.cfast_qc_2.setObjectName(u"cfast_qc_2")
        sizePolicy1.setHeightForWidth(self.cfast_qc_2.sizePolicy().hasHeightForWidth())
        self.cfast_qc_2.setSizePolicy(sizePolicy1)
        self.cfast_qc_2.setMinimumSize(QSize(70, 30))
        self.cfast_qc_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc_2, 8, 0, 1, 1)

        self.rseries = QLabel(self.groupBox)
        self.rseries.setObjectName(u"rseries")
        sizePolicy1.setHeightForWidth(self.rseries.sizePolicy().hasHeightForWidth())
        self.rseries.setSizePolicy(sizePolicy1)
        self.rseries.setMaximumSize(QSize(100, 16777215))
        self.rseries.setStyleSheet(u"")

        self.gridLayout_31.addWidget(self.rseries, 5, 0, 1, 1)

        self.rseries_qc = QLineEdit(self.groupBox)
        self.rseries_qc.setObjectName(u"rseries_qc")
        sizePolicy1.setHeightForWidth(self.rseries_qc.sizePolicy().hasHeightForWidth())
        self.rseries_qc.setSizePolicy(sizePolicy1)
        self.rseries_qc.setMinimumSize(QSize(70, 30))
        self.rseries_qc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.rseries_qc, 3, 0, 1, 1, Qt.AlignLeft)

        self.cslow = QLabel(self.groupBox)
        self.cslow.setObjectName(u"cslow")
        sizePolicy1.setHeightForWidth(self.cslow.sizePolicy().hasHeightForWidth())
        self.cslow.setSizePolicy(sizePolicy1)
        self.cslow.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.cslow, 7, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_15, 2, 0, 1, 1)

        self.cfast = QLabel(self.groupBox)
        self.cfast.setObjectName(u"cfast")
        sizePolicy1.setHeightForWidth(self.cfast.sizePolicy().hasHeightForWidth())
        self.cfast.setSizePolicy(sizePolicy1)
        self.cfast.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.cfast, 9, 0, 1, 1)

        self.cslow_qc = QLineEdit(self.groupBox)
        self.cslow_qc.setObjectName(u"cslow_qc")
        sizePolicy1.setHeightForWidth(self.cslow_qc.sizePolicy().hasHeightForWidth())
        self.cslow_qc.setSizePolicy(sizePolicy1)
        self.cslow_qc.setMinimumSize(QSize(70, 30))
        self.cslow_qc.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.cslow_qc, 6, 0, 1, 1)

        self.capacitance = QLabel(self.groupBox)
        self.capacitance.setObjectName(u"capacitance")
        sizePolicy1.setHeightForWidth(self.capacitance.sizePolicy().hasHeightForWidth())
        self.capacitance.setSizePolicy(sizePolicy1)
        self.capacitance.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_31.addWidget(self.capacitance, 11, 0, 1, 1)


        self.gridLayout_47.addLayout(self.gridLayout_31, 0, 0, 1, 1)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_47.addWidget(self.line_2, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_47, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_start_camera = QPushButton(self.groupBox)
        self.button_start_camera.setObjectName(u"button_start_camera")
        self.button_start_camera.setMinimumSize(QSize(30, 30))
        self.button_start_camera.setMaximumSize(QSize(30, 30))
        self.button_start_camera.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_start_camera)

        self.button_stop_camera = QPushButton(self.groupBox)
        self.button_stop_camera.setObjectName(u"button_stop_camera")
        self.button_stop_camera.setMinimumSize(QSize(30, 30))
        self.button_stop_camera.setMaximumSize(QSize(30, 30))
        self.button_stop_camera.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_stop_camera)

        self.button_take_snapshot = QPushButton(self.groupBox)
        self.button_take_snapshot.setObjectName(u"button_take_snapshot")
        self.button_take_snapshot.setMinimumSize(QSize(30, 30))
        self.button_take_snapshot.setMaximumSize(QSize(30, 30))
        self.button_take_snapshot.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_take_snapshot)

        self.transfer_snapshot = QPushButton(self.groupBox)
        self.transfer_snapshot.setObjectName(u"transfer_snapshot")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(30)
        sizePolicy6.setVerticalStretch(30)
        sizePolicy6.setHeightForWidth(self.transfer_snapshot.sizePolicy().hasHeightForWidth())
        self.transfer_snapshot.setSizePolicy(sizePolicy6)
        self.transfer_snapshot.setMinimumSize(QSize(30, 30))
        self.transfer_snapshot.setMaximumSize(QSize(30, 30))
        self.transfer_snapshot.setStyleSheet(u"QPushButton{\n"
"background-repeat:None;\n"
"background-color: transparent;\n"
"background-position:None;\n"
"border:None;\n"
"border-radius: 5px;\n"
"background-position:center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: \"#54545a\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"  color: skyblue;\n"
"  text-transform: scale(1.5);\n"
"}")

        self.verticalLayout_2.addWidget(self.transfer_snapshot)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_16)


        self.gridLayout_14.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_14.addWidget(self.line_3, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_8 = GroupBoxSize(self.experiment_init)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setFont(font)
        self.gridLayout_40 = QGridLayout(self.groupBox_8)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.pyqt_window_grid = QGridLayout()
        self.pyqt_window_grid.setObjectName(u"pyqt_window_grid")
        self.pyqt_window_grid.setHorizontalSpacing(4)
        self.visualization_stacked = QStackedWidget(self.groupBox_8)
        self.visualization_stacked.setObjectName(u"visualization_stacked")
        sizePolicy.setHeightForWidth(self.visualization_stacked.sizePolicy().hasHeightForWidth())
        self.visualization_stacked.setSizePolicy(sizePolicy)
        self.visualization_stacked.setMinimumSize(QSize(400, 250))
        self.visualization_stacked.setAutoFillBackground(True)
        self.communication_access = QWidget()
        self.communication_access.setObjectName(u"communication_access")
        self.gridLayout_12 = QGridLayout(self.communication_access)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_21 = QGroupBox(self.communication_access)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.groupBox_21)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.button_submit_command = QPushButton(self.groupBox_21)
        self.button_submit_command.setObjectName(u"button_submit_command")
        sizePolicy1.setHeightForWidth(self.button_submit_command.sizePolicy().hasHeightForWidth())
        self.button_submit_command.setSizePolicy(sizePolicy1)
        self.button_submit_command.setMinimumSize(QSize(80, 0))
        self.button_submit_command.setMaximumSize(QSize(200, 40))

        self.gridLayout_33.addWidget(self.button_submit_command, 0, 0, 1, 1)

        self.button_clear_window = QPushButton(self.groupBox_21)
        self.button_clear_window.setObjectName(u"button_clear_window")
        sizePolicy1.setHeightForWidth(self.button_clear_window.sizePolicy().hasHeightForWidth())
        self.button_clear_window.setSizePolicy(sizePolicy1)
        self.button_clear_window.setMinimumSize(QSize(80, 0))
        self.button_clear_window.setMaximumSize(QSize(200, 40))

        self.gridLayout_33.addWidget(self.button_clear_window, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_33, 1, 0, 1, 1)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.receive_command1 = QTextEdit(self.groupBox_21)
        self.receive_command1.setObjectName(u"receive_command1")
        self.receive_command1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_32.addWidget(self.receive_command1, 1, 2, 1, 1)

        self.label_42 = QLabel(self.groupBox_21)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_32.addWidget(self.label_42, 0, 4, 1, 1)

        self.label_40 = QLabel(self.groupBox_21)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_32.addWidget(self.label_40, 0, 0, 1, 1)

        self.sub_command1 = QTextEdit(self.groupBox_21)
        self.sub_command1.setObjectName(u"sub_command1")
        self.sub_command1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_32.addWidget(self.sub_command1, 1, 0, 1, 1)

        self.response_command_1 = QTextEdit(self.groupBox_21)
        self.response_command_1.setObjectName(u"response_command_1")
        self.response_command_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_32.addWidget(self.response_command_1, 1, 4, 1, 1)

        self.label_41 = QLabel(self.groupBox_21)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_32.addWidget(self.label_41, 0, 2, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_32, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_21, 0, 0, 1, 1)

        self.visualization_stacked.addWidget(self.communication_access)
        self.select_commands = QWidget()
        self.select_commands.setObjectName(u"select_commands")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.select_commands.sizePolicy().hasHeightForWidth())
        self.select_commands.setSizePolicy(sizePolicy7)
        self.select_commands.setMinimumSize(QSize(0, 0))
        self.gridLayout_41 = QGridLayout(self.select_commands)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(-1, 5, -1, 5)
        self.pyqt_window = QGridLayout()
        self.pyqt_window.setObjectName(u"pyqt_window")
        self.pyqt_window.setSizeConstraint(QLayout.SetNoConstraint)

        self.gridLayout_41.addLayout(self.pyqt_window, 0, 0, 1, 1)

        self.visualization_stacked.addWidget(self.select_commands)

        self.pyqt_window_grid.addWidget(self.visualization_stacked, 0, 0, 1, 1)


        self.gridLayout_36.addLayout(self.pyqt_window_grid, 2, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_8)
        self.label_26.setObjectName(u"label_26")
        sizePolicy3.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy3)

        self.gridLayout_36.addWidget(self.label_26, 0, 0, 1, 1)


        self.gridLayout_40.addLayout(self.gridLayout_36, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_8, 0, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.gridLayout_64.addLayout(self.gridLayout_24, 0, 0, 1, 1)

        self.experiment_control_stacked.addWidget(self.experiment_init)

        self.gridLayout_2.addWidget(self.experiment_control_stacked, 3, 0, 1, 1)


        self.retranslateUi(Config_Widget)

        self.experiment_control_stacked.setCurrentIndex(0)
        self.exp_stacked.setCurrentIndex(3)
        self.visualization_stacked.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Config_Widget", u"Meta Data", None))
#if QT_CONFIG(tooltip)
        self.metadata_table.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>Opens Global Meta Data Table in the database to have view what was done previously</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.metadata_table.setText("")
#if QT_CONFIG(tooltip)
        self.change_solutions.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>Here you can add additional internal and external solutions to the database for selection</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.change_solutions.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("Config_Widget", u"Go To", None))
        self.go_to_online.setText("")
        self.label_15.setText(QCoreApplication.translate("Config_Widget", u"Go To Online Analysis", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Config_Widget", u"Transfer Options", None))
#if QT_CONFIG(tooltip)
        self.transfer_to_online_analysis_button.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>This button finalizes the experiment, by completly sending it to the online analysis for further review and creating a new experiment .dat file for the next experiment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.transfer_to_online_analysis_button.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Control", None))
#if QT_CONFIG(tooltip)
        self.start_analysis.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>This starts the experiment whenever everything is setup</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.start_analysis.setText("")
#if QT_CONFIG(tooltip)
        self.clear_sequence.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>This resets the patch sequence that you have entered below in the sequence panel for the experiment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.clear_sequence.setText("")
#if QT_CONFIG(tooltip)
        self.stop_experiment_button.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>Stops the experiment by sending a terminate command to the patchmaster</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stop_experiment_button.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("Config_Widget", u"Home", None))
        self.go_back_button.setText("")
        self.go_home.setText("")
        self.fo_forward_button.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("Config_Widget", u"Batch Communication", None))
        self.switch_to_testing.setText("")
        self.download_notebook.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("Config_Widget", u"Connection", None))
#if QT_CONFIG(tooltip)
        self.establish_connection_button.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>Whenever all the files e.g. pgf, protocol and online analysis files are set as well as the batch communication path where the batch.out is located then this establishes a connection between Biophysical Essentials and the Patchmaster</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.establish_connection_button.setText("")
        self.label_23.setText(QCoreApplication.translate("Config_Widget", u"Establish Connection:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Config_Widget", u"Edit and Save Form", None))
        self.add_metadata_button.setText("")
        self.database_save_2.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Config_Widget", u"Plot Options", None))
        self.save_plot_online.setText("")
        self.plot_home.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("Config_Widget", u"Extracelullar and intracellular solutions", None))
        self.label_243.setText(QCoreApplication.translate("Config_Widget", u"Extracellular Solution", None))
        self.label_244.setText(QCoreApplication.translate("Config_Widget", u"Intracellular solution", None))
        self.ent_ph_set.setText(QCoreApplication.translate("Config_Widget", u"pH of External Solution", None))
        self.label_247.setText(QCoreApplication.translate("Config_Widget", u"Ph of internal solution", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Config_Widget", u"Patchmaster Setup Files", None))
        self.button_pgf_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_protocol_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_batch_1.setText(QCoreApplication.translate("Config_Widget", u"Setup File Path", None))
        self.button_onl_analysis_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.label_3.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.label_5.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.label_4.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Config_Widget", u"Set Metadata", None))
        self.label_19.setText(QCoreApplication.translate("Config_Widget", u"Genotype", None))
        self.label_17.setText(QCoreApplication.translate("Config_Widget", u"Condition", None))
        self.label_16.setText(QCoreApplication.translate("Config_Widget", u"Species", None))
        self.label_18.setText(QCoreApplication.translate("Config_Widget", u"Species", None))
        self.label_20.setText(QCoreApplication.translate("Config_Widget", u"Celltype", None))
        self.label_21.setText(QCoreApplication.translate("Config_Widget", u"Individium ID", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Metadata", None))
        self.label_7.setText(QCoreApplication.translate("Config_Widget", u"Cell Type", None))
        self.label_9.setText(QCoreApplication.translate("Config_Widget", u" # of Cells patched", None))
        self.label_8.setText(QCoreApplication.translate("Config_Widget", u"Min # of Cells", None))
        self.label_22.setText(QCoreApplication.translate("Config_Widget", u"Date of Preparation", None))
        self.ent_date_prep.setText("")
        self.label_6.setText(QCoreApplication.translate("Config_Widget", u"Experiment Name", None))
        self.label_24.setText(QCoreApplication.translate("Config_Widget", u"Experiment Label", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Config_Widget", u"Connection Overview", None))
        self.ProtocolBox.setTitle(QCoreApplication.translate("Config_Widget", u"Protocol Sequence Generator", None))
        self.label_10.setText(QCoreApplication.translate("Config_Widget", u"Patch Sequence", None))
        self.label_11.setText(QCoreApplication.translate("Config_Widget", u"Select Series:", None))
        self.label_12.setText(QCoreApplication.translate("Config_Widget", u"Select Patch Mode:", None))
        self.label_13.setText(QCoreApplication.translate("Config_Widget", u"Select Label", None))
        self.label_14.setText(QCoreApplication.translate("Config_Widget", u"Select Protocol", None))
#if QT_CONFIG(accessibility)
        self.series_select.setAccessibleName(QCoreApplication.translate("Config_Widget", u"experiment_button", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.series_select.setAccessibleDescription(QCoreApplication.translate("Config_Widget", u"experiment_button", None))
#endif // QT_CONFIG(accessibility)
        self.series_select.setText(QCoreApplication.translate("Config_Widget", u"Series", None))
#if QT_CONFIG(accessibility)
        self.protocols_select.setAccessibleDescription(QCoreApplication.translate("Config_Widget", u"experiment_button", None))
#endif // QT_CONFIG(accessibility)
        self.protocols_select.setText(QCoreApplication.translate("Config_Widget", u"Protocols", None))
        self.label.setText(QCoreApplication.translate("Config_Widget", u"Add Experiment", None))
        self.modi_select.setText(QCoreApplication.translate("Config_Widget", u"Modi", None))
#if QT_CONFIG(accessibility)
        self.labels_select.setAccessibleDescription(QCoreApplication.translate("Config_Widget", u"experiment_button", None))
#endif // QT_CONFIG(accessibility)
        self.labels_select.setText(QCoreApplication.translate("Config_Widget", u"Labels", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Metrics and Camera", None))
        self.quality.setText(QCoreApplication.translate("Config_Widget", u"Quality:", None))
        self.rseries.setText(QCoreApplication.translate("Config_Widget", u"Rseries:", None))
        self.cslow.setText(QCoreApplication.translate("Config_Widget", u"Cslow:", None))
        self.cfast.setText(QCoreApplication.translate("Config_Widget", u"Cfast:", None))
        self.capacitance.setText(QCoreApplication.translate("Config_Widget", u"Cell:", None))
#if QT_CONFIG(accessibility)
        self.button_start_camera.setAccessibleName(QCoreApplication.translate("Config_Widget", u"camera_buttons", None))
#endif // QT_CONFIG(accessibility)
        self.button_start_camera.setText("")
#if QT_CONFIG(accessibility)
        self.button_stop_camera.setAccessibleName(QCoreApplication.translate("Config_Widget", u"camera_buttons", None))
#endif // QT_CONFIG(accessibility)
        self.button_stop_camera.setText("")
#if QT_CONFIG(accessibility)
        self.button_take_snapshot.setAccessibleName(QCoreApplication.translate("Config_Widget", u"camera_buttons", None))
#endif // QT_CONFIG(accessibility)
        self.button_take_snapshot.setText("")
#if QT_CONFIG(accessibility)
        self.transfer_snapshot.setAccessibleName(QCoreApplication.translate("Config_Widget", u"camera_buttons", None))
#endif // QT_CONFIG(accessibility)
        self.transfer_snapshot.setText("")
        self.groupBox_8.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Overview", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Config_Widget", u"Test the Connection to the Patchmaster", None))
        self.button_submit_command.setText(QCoreApplication.translate("Config_Widget", u"Submit Command", None))
        self.button_clear_window.setText(QCoreApplication.translate("Config_Widget", u"Stop Submitting", None))
        self.label_42.setText(QCoreApplication.translate("Config_Widget", u"Batch Communication Response", None))
        self.label_40.setText(QCoreApplication.translate("Config_Widget", u"Submit your Commands", None))
        self.label_41.setText(QCoreApplication.translate("Config_Widget", u"Control File received", None))
        self.label_26.setText(QCoreApplication.translate("Config_Widget", u"Notebook Online Analysis:", None))
    # retranslateUi

