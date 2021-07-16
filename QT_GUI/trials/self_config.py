# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self_config_notebook_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PIL import ImageQt ,Image
from backend_manager import *
import os.path
import logging
from dragable_label import *
from tkinter_camera import *
from time import sleep
import pandas as pd
from dropable_list_view import ListView
from plotting_pyqt import PlotClass
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
pg.setConfigOption('foreground', '#448aff')
from dvg_pyqtgraph_threadsafe import PlotCurve

class Ui_Config_Widget(object):

    def initialized(self):
        print("class initalized")
        self.batch_path = None
        self.backend_manager = BackendManager()
        self.pgf_file = None
        self.pro_file = None
        self.onl_file = None
        self.general_commands_list = ["GetEpcParam-1 Rseries", "GetEpcParam-1 Cfast", "GetEpcParam-1 Rcomp","GetEpcParam-1 Cslow","Setup","Seal","Whole-cell"]
        self.submission_count = 2

        self.default_mode = 1

        self.pyqt_graph = pg.PlotWidget(height = 100) # insert a plot widget
        self.pyqt_graph.setBackground("#232629")
        self.setupUi(self)
        self.check_session = None
        self.logger=logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../Logs/configuration.log')
        print(file_handler)
        formatter  = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.debug('A debug message')


    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(1613, 1023)
        self.gridLayoutWidget = QWidget(Config_Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 20, 1531, 891))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Notebook_2 = QTabWidget(self.gridLayoutWidget)
        self.Notebook_2.setObjectName(u"Notebook_2")
        self.Notebook_2.setTabShape(QTabWidget.Rounded)
        self.experiment_initialization_3 = QWidget()
        self.experiment_initialization_3.setObjectName(u"experiment_initialization_3")
        self.horizontalLayoutWidget_11 = QWidget(self.experiment_initialization_3)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(660, 10, 191, 51))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Load_meta_data_experiment_12 = QPushButton(self.horizontalLayoutWidget_11)
        self.Load_meta_data_experiment_12.setObjectName(u"Load_meta_data_experiment_12")

        self.horizontalLayout_15.addWidget(self.Load_meta_data_experiment_12)

        self.meta_data_loading_1 = QStackedWidget(self.experiment_initialization_3)
        self.meta_data_loading_1.setObjectName(u"meta_data_loading_1")
        self.meta_data_loading_1.setGeometry(QRect(-10, 80, 1521, 771))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayoutWidget_9 = QWidget(self.page)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(30, 380, 1441, 381))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_32 = QGroupBox(self.horizontalLayoutWidget_9)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.St_com1 = QComboBox(self.groupBox_32)
        self.St_com1.setObjectName(u"St_com1")
        self.St_com1.setGeometry(QRect(100, 50, 281, 41))
        self.St_com2 = QComboBox(self.groupBox_32)
        self.St_com2.setObjectName(u"St_com2")
        self.St_com2.setGeometry(QRect(100, 130, 281, 41))
        self.St_com3 = QComboBox(self.groupBox_32)
        self.St_com3.setObjectName(u"St_com3")
        self.St_com3.setGeometry(QRect(100, 210, 281, 41))
        self.label_220 = QLabel(self.groupBox_32)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(100, 90, 101, 16))
        self.label_221 = QLabel(self.groupBox_32)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(100, 170, 101, 16))
        self.label_222 = QLabel(self.groupBox_32)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(100, 250, 101, 16))

        self.gridLayout_31.addWidget(self.groupBox_32, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_31)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.groupBox_33 = QGroupBox(self.horizontalLayoutWidget_9)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.button_pgf_set_3 = QPushButton(self.groupBox_33)
        self.button_pgf_set_3.setObjectName(u"button_pgf_set_3")
        self.button_pgf_set_3.setGeometry(QRect(340, 50, 111, 41))
        self.label_61 = QLabel(self.groupBox_33)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(10, 170, 71, 16))
        self.pg_file_set_3 = QLineEdit(self.groupBox_33)
        self.pg_file_set_3.setObjectName(u"pg_file_set_3")
        self.pg_file_set_3.setGeometry(QRect(10, 50, 301, 41))
        self.protocol_file_set_3 = QLineEdit(self.groupBox_33)
        self.protocol_file_set_3.setObjectName(u"protocol_file_set_3")
        self.protocol_file_set_3.setGeometry(QRect(10, 130, 301, 41))
        self.label_60 = QLabel(self.groupBox_33)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(10, 250, 101, 16))
        self.button_protocol_set_3 = QPushButton(self.groupBox_33)
        self.button_protocol_set_3.setObjectName(u"button_protocol_set_3")
        self.button_protocol_set_3.setGeometry(QRect(340, 130, 111, 41))
        self.label_59 = QLabel(self.groupBox_33)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(10, 90, 61, 16))
        self.button_onl_analysis_set_3 = QPushButton(self.groupBox_33)
        self.button_onl_analysis_set_3.setObjectName(u"button_onl_analysis_set_3")
        self.button_onl_analysis_set_3.setGeometry(QRect(340, 210, 111, 41))
        self.online_analysis_file_set_3 = QLineEdit(self.groupBox_33)
        self.online_analysis_file_set_3.setObjectName(u"online_analysis_file_set_3")
        self.online_analysis_file_set_3.setGeometry(QRect(10, 210, 301, 41))

        self.gridLayout_32.addWidget(self.groupBox_33, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_32)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.groupBox_34 = QGroupBox(self.horizontalLayoutWidget_9)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.A_com1 = QComboBox(self.groupBox_34)
        self.A_com1.setObjectName(u"A_com1")
        self.A_com1.setGeometry(QRect(10, 50, 141, 41))
        self.A_com2 = QComboBox(self.groupBox_34)
        self.A_com2.setObjectName(u"A_com2")
        self.A_com2.setGeometry(QRect(170, 50, 141, 41))
        self.A1 = QLineEdit(self.groupBox_34)
        self.A1.setObjectName(u"A1")
        self.A1.setGeometry(QRect(330, 50, 131, 41))
        self.A_com3 = QComboBox(self.groupBox_34)
        self.A_com3.setObjectName(u"A_com3")
        self.A_com3.setGeometry(QRect(10, 130, 141, 41))
        self.A2 = QLineEdit(self.groupBox_34)
        self.A2.setObjectName(u"A2")
        self.A2.setGeometry(QRect(170, 130, 291, 41))
        self.label_227 = QLabel(self.groupBox_34)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(10, 90, 81, 16))
        self.label_228 = QLabel(self.groupBox_34)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(170, 90, 91, 16))
        self.label_229 = QLabel(self.groupBox_34)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(330, 90, 81, 16))
        self.label_230 = QLabel(self.groupBox_34)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(10, 170, 71, 16))
        self.label_231 = QLabel(self.groupBox_34)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(170, 170, 141, 16))
        self.horizontalLayoutWidget_10 = QWidget(self.groupBox_34)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(90, 290, 311, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.button_batch_7 = QPushButton(self.horizontalLayoutWidget_10)
        self.button_batch_7.setObjectName(u"button_batch_7")

        self.horizontalLayout_6.addWidget(self.button_batch_7)

        self.Batch1_4 = QLineEdit(self.groupBox_34)
        self.Batch1_4.setObjectName(u"Batch1_4")
        self.Batch1_4.setGeometry(QRect(10, 210, 451, 41))
        self.label_62 = QLabel(self.groupBox_34)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(10, 260, 111, 16))

        self.gridLayout_33.addWidget(self.groupBox_34, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_33)

        self.horizontalLayoutWidget_8 = QWidget(self.page)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(30, 20, 1441, 351))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.groupBox_22 = QGroupBox(self.horizontalLayoutWidget_8)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.So_com1 = QComboBox(self.groupBox_22)
        self.So_com1.setObjectName(u"So_com1")
        self.So_com1.setGeometry(QRect(100, 20, 281, 41))
        self.label_199 = QLabel(self.groupBox_22)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(110, 60, 71, 16))
        self.So_com2 = QComboBox(self.groupBox_22)
        self.So_com2.setObjectName(u"So_com2")
        self.So_com2.setGeometry(QRect(100, 90, 281, 41))
        self.label_200 = QLabel(self.groupBox_22)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(110, 130, 71, 16))
        self.S1 = QLineEdit(self.groupBox_22)
        self.S1.setObjectName(u"S1")
        self.S1.setGeometry(QRect(110, 160, 131, 41))
        self.S2 = QLineEdit(self.groupBox_22)
        self.S2.setObjectName(u"S2")
        self.S2.setGeometry(QRect(250, 160, 131, 41))
        self.label_201 = QLabel(self.groupBox_22)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(110, 200, 71, 16))
        self.label_202 = QLabel(self.groupBox_22)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(250, 200, 71, 16))
        self.S3 = QLineEdit(self.groupBox_22)
        self.S3.setObjectName(u"S3")
        self.S3.setGeometry(QRect(110, 230, 61, 41))
        self.S4 = QLineEdit(self.groupBox_22)
        self.S4.setObjectName(u"S4")
        self.S4.setGeometry(QRect(180, 230, 61, 41))
        self.S5 = QLineEdit(self.groupBox_22)
        self.S5.setObjectName(u"S5")
        self.S5.setGeometry(QRect(250, 230, 61, 41))
        self.S6 = QLineEdit(self.groupBox_22)
        self.S6.setObjectName(u"S6")
        self.S6.setGeometry(QRect(320, 230, 61, 41))
        self.label_203 = QLabel(self.groupBox_22)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(110, 270, 71, 16))
        self.label_204 = QLabel(self.groupBox_22)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(180, 270, 71, 16))
        self.label_205 = QLabel(self.groupBox_22)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(250, 270, 71, 16))
        self.label_206 = QLabel(self.groupBox_22)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(320, 270, 71, 16))

        self.gridLayout_28.addWidget(self.groupBox_22, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_28)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.groupBox_30 = QGroupBox(self.horizontalLayoutWidget_8)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.Ce_com1 = QComboBox(self.groupBox_30)
        self.Ce_com1.setObjectName(u"Ce_com1")
        self.Ce_com1.setGeometry(QRect(110, 20, 281, 41))
        self.Ce_com2 = QComboBox(self.groupBox_30)
        self.Ce_com2.setObjectName(u"Ce_com2")
        self.Ce_com2.setGeometry(QRect(110, 90, 281, 41))
        self.Ce1 = QLineEdit(self.groupBox_30)
        self.Ce1.setObjectName(u"Ce1")
        self.Ce1.setGeometry(QRect(110, 160, 131, 41))
        self.label_207 = QLabel(self.groupBox_30)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(120, 60, 71, 16))
        self.label_208 = QLabel(self.groupBox_30)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(120, 130, 71, 16))
        self.label_209 = QLabel(self.groupBox_30)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(110, 200, 71, 16))

        self.gridLayout_29.addWidget(self.groupBox_30, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_29)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_31 = QGroupBox(self.horizontalLayoutWidget_8)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.C1 = QLineEdit(self.groupBox_31)
        self.C1.setObjectName(u"C1")
        self.C1.setGeometry(QRect(90, 20, 81, 41))
        self.C2 = QLineEdit(self.groupBox_31)
        self.C2.setObjectName(u"C2")
        self.C2.setGeometry(QRect(200, 20, 81, 41))
        self.Co_com1 = QComboBox(self.groupBox_31)
        self.Co_com1.setObjectName(u"Co_com1")
        self.Co_com1.setGeometry(QRect(300, 20, 91, 41))
        self.C3 = QLineEdit(self.groupBox_31)
        self.C3.setObjectName(u"C3")
        self.C3.setGeometry(QRect(90, 90, 81, 41))
        self.C4 = QLineEdit(self.groupBox_31)
        self.C4.setObjectName(u"C4")
        self.C4.setGeometry(QRect(200, 90, 81, 41))
        self.C5 = QLineEdit(self.groupBox_31)
        self.C5.setObjectName(u"C5")
        self.C5.setGeometry(QRect(90, 160, 81, 41))
        self.C6 = QLineEdit(self.groupBox_31)
        self.C6.setObjectName(u"C6")
        self.C6.setGeometry(QRect(200, 160, 81, 41))
        self.C8 = QLineEdit(self.groupBox_31)
        self.C8.setObjectName(u"C8")
        self.C8.setGeometry(QRect(90, 230, 131, 41))
        self.C9 = QLineEdit(self.groupBox_31)
        self.C9.setObjectName(u"C9")
        self.C9.setGeometry(QRect(270, 230, 131, 41))
        self.label_210 = QLabel(self.groupBox_31)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(90, 60, 81, 16))
        self.label_211 = QLabel(self.groupBox_31)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(200, 60, 71, 16))
        self.label_212 = QLabel(self.groupBox_31)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(310, 60, 71, 16))
        self.label_213 = QLabel(self.groupBox_31)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(90, 130, 71, 16))
        self.label_214 = QLabel(self.groupBox_31)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(200, 130, 71, 16))
        self.label_215 = QLabel(self.groupBox_31)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(90, 200, 71, 16))
        self.label_216 = QLabel(self.groupBox_31)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(200, 200, 71, 16))
        self.label_217 = QLabel(self.groupBox_31)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(90, 270, 71, 16))
        self.label_218 = QLabel(self.groupBox_31)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(270, 270, 111, 16))
        self.C6_2 = QLineEdit(self.groupBox_31)
        self.C6_2.setObjectName(u"C6_2")
        self.C6_2.setGeometry(QRect(310, 160, 81, 41))
        self.label_219 = QLabel(self.groupBox_31)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(310, 200, 71, 16))

        self.gridLayout_30.addWidget(self.groupBox_31, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_30)

        self.meta_data_loading_1.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.groupBox_23 = QGroupBox(self.page_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(170, 10, 571, 311))
        self.extracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.extracellular_sol_com_1.setObjectName(u"extracellular_sol_com_1")
        self.extracellular_sol_com_1.setGeometry(QRect(160, 50, 281, 41))
        self.label_243 = QLabel(self.groupBox_23)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(160, 90, 121, 16))
        self.Intracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.Intracellular_sol_com_1.setObjectName(u"Intracellular_sol_com_1")
        self.Intracellular_sol_com_1.setGeometry(QRect(160, 130, 281, 41))
        self.label_244 = QLabel(self.groupBox_23)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(160, 170, 131, 16))
        self.ent_date_prep = QLineEdit(self.groupBox_23)
        self.ent_date_prep.setObjectName(u"ent_date_prep")
        self.ent_date_prep.setGeometry(QRect(20, 210, 151, 41))
        self.S2_3 = QLineEdit(self.groupBox_23)
        self.S2_3.setObjectName(u"S2_3")
        self.S2_3.setGeometry(QRect(210, 210, 151, 41))
        self.label_245 = QLabel(self.groupBox_23)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(20, 250, 111, 16))
        self.ent_ph_set = QLabel(self.groupBox_23)
        self.ent_ph_set.setObjectName(u"ent_ph_set")
        self.ent_ph_set.setGeometry(QRect(210, 250, 131, 16))
        self.ent_ph_int_set = QLineEdit(self.groupBox_23)
        self.ent_ph_int_set.setObjectName(u"ent_ph_int_set")
        self.ent_ph_int_set.setGeometry(QRect(400, 210, 151, 41))
        self.label_247 = QLabel(self.groupBox_23)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(400, 250, 121, 16))
        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(760, 10, 611, 311))
        self.pg_file_set = QLineEdit(self.groupBox_4)
        self.pg_file_set.setObjectName(u"pg_file_set")
        self.pg_file_set.setGeometry(QRect(90, 50, 331, 41))
        self.protocol_file_set = QLineEdit(self.groupBox_4)
        self.protocol_file_set.setObjectName(u"protocol_file_set")
        self.protocol_file_set.setGeometry(QRect(90, 130, 331, 41))
        self.online_analysis_file_set = QLineEdit(self.groupBox_4)
        self.online_analysis_file_set.setObjectName(u"online_analysis_file_set")
        self.online_analysis_file_set.setGeometry(QRect(90, 210, 331, 41))
        self.button_pgf_set = QPushButton(self.groupBox_4)
        self.button_pgf_set.setObjectName(u"button_pgf_set")
        self.button_pgf_set.setGeometry(QRect(460, 50, 111, 41))
        self.button_protocol_set = QPushButton(self.groupBox_4)
        self.button_protocol_set.setObjectName(u"button_protocol_set")
        self.button_protocol_set.setGeometry(QRect(460, 130, 111, 41))
        self.button_onl_analysis_set = QPushButton(self.groupBox_4)
        self.button_onl_analysis_set.setObjectName(u"button_onl_analysis_set")
        self.button_onl_analysis_set.setGeometry(QRect(460, 210, 111, 41))
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 90, 61, 16))
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 170, 71, 16))
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 250, 101, 16))
        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(170, 340, 571, 361))
        self.experiment_type_desc = QLineEdit(self.groupBox_6)
        self.experiment_type_desc.setObjectName(u"experiment_type_desc")
        self.experiment_type_desc.setGeometry(QRect(130, 60, 331, 41))
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 100, 111, 16))
        self.cell_type_desc = QLineEdit(self.groupBox_6)
        self.cell_type_desc.setObjectName(u"cell_type_desc")
        self.cell_type_desc.setGeometry(QRect(130, 140, 331, 41))
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 180, 111, 16))
        self.min_number_cells = QLineEdit(self.groupBox_6)
        self.min_number_cells.setObjectName(u"min_number_cells")
        self.min_number_cells.setGeometry(QRect(40, 220, 121, 41))
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 260, 111, 16))
        self.patched_cells = QLineEdit(self.groupBox_6)
        self.patched_cells.setObjectName(u"patched_cells")
        self.patched_cells.setGeometry(QRect(200, 220, 111, 41))
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 260, 111, 16))
        self.database_save = QPushButton(self.groupBox_6)
        self.database_save.setObjectName(u"database_save")
        self.database_save.setGeometry(QRect(340, 220, 201, 41))
        self.groupBox_17 = QGroupBox(self.page_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(760, 340, 611, 361))
        self.Batch1 = QLineEdit(self.groupBox_17)
        self.Batch1.setObjectName(u"Batch1")
        self.Batch1.setGeometry(QRect(80, 60, 451, 41))
        self.button_batch_1 = QPushButton(self.groupBox_17)
        self.button_batch_1.setObjectName(u"button_batch_1")
        self.button_batch_1.setGeometry(QRect(130, 140, 341, 31))
        self.label_4 = QLabel(self.groupBox_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 100, 111, 16))
        self.add_pixmap_for_green = QLabel(self.groupBox_17)
        self.add_pixmap_for_green.setObjectName(u"add_pixmap_for_green")
        self.add_pixmap_for_green.setGeometry(QRect(270, 190, 91, 16))
        self.meta_data_loading_1.addWidget(self.page_2)
        self.Notebook_2.addTab(self.experiment_initialization_3, "")
        self.batch_communication_3 = QWidget()
        self.batch_communication_3.setObjectName(u"batch_communication_3")
        self.stackedWidget = QStackedWidget(self.batch_communication_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(30, 10, 1481, 821))
        self.communication_access = QWidget()
        self.communication_access.setObjectName(u"communication_access")
        self.groupBox_21 = QGroupBox(self.communication_access)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(210, 90, 1111, 541))
        self.label_40 = QLabel(self.groupBox_21)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 40, 181, 20))
        self.label_41 = QLabel(self.groupBox_21)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(410, 40, 171, 20))
        self.receive_command1 = QTextEdit(self.groupBox_21)
        self.receive_command1.setObjectName(u"receive_command1")
        self.receive_command1.setGeometry(QRect(410, 60, 301, 411))
        self.response_command_1 = QTextEdit(self.groupBox_21)
        self.response_command_1.setObjectName(u"response_command_1")
        self.response_command_1.setGeometry(QRect(780, 60, 301, 411))
        self.label_42 = QLabel(self.groupBox_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(780, 40, 231, 20))
        self.button_submit_command = QPushButton(self.groupBox_21)
        self.button_submit_command.setObjectName(u"button_submit_command")
        self.button_submit_command.setGeometry(QRect(30, 490, 151, 31))
        self.button_clear_window = QPushButton(self.groupBox_21)
        self.button_clear_window.setObjectName(u"button_clear_window")
        self.button_clear_window.setGeometry(QRect(200, 490, 141, 31))
        self.sub_command1 = QTextEdit(self.groupBox_21)
        self.sub_command1.setObjectName(u"sub_command1")
        self.sub_command1.setGeometry(QRect(30, 60, 311, 411))
        self.button_batch_2 = QPushButton(self.communication_access)
        self.button_batch_2.setObjectName(u"button_batch_2")
        self.button_batch_2.setGeometry(QRect(560, 670, 311, 51))
        self.label_24 = QLabel(self.communication_access)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(540, 20, 481, 61))
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.stackedWidget.addWidget(self.communication_access)
        self.select_commands = QWidget()
        self.select_commands.setObjectName(u"select_commands")
        self.groupBox_19 = QGroupBox(self.select_commands)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(10, 40, 1251, 791))
        self.listWidget = ListView(self.groupBox_19)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(560, 60, 256, 641))
        self.label = QLabel(self.groupBox_19)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 40, 191, 16))
        self.label_26 = QLabel(self.groupBox_19)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(830, 40, 191, 16))
        self.label_27 = QLabel(self.groupBox_19)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 40, 191, 16))
        self.label_28 = QLabel(self.groupBox_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(280, 40, 191, 16))
        self.scrollArea = QScrollArea(self.groupBox_19)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(280, 60, 261, 701))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 259, 699))
        self.SeriesWidget = ListView(self.scrollAreaWidgetContents)
        self.SeriesWidget.setObjectName(u"SeriesWidget")
        self.SeriesWidget.setGeometry(QRect(0, 0, 261, 701))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_32 = QLabel(self.groupBox_19)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 440, 191, 16))
        self.scrollArea_2 = QScrollArea(self.groupBox_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 460, 251, 301))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 249, 299))
        self.protocol_widget = ListView(self.scrollAreaWidgetContents_2)
        self.protocol_widget.setObjectName(u"protocol_widget")
        self.protocol_widget.setGeometry(QRect(0, 0, 251, 301))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget_4 = QWidget(self.groupBox_19)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(830, 420, 401, 341))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.parameter_window = QGridLayout()
        self.parameter_window.setObjectName(u"parameter_window")
        self.groupBox_3 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 60, 47, 13))
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 47, 13))
        self.cslow_qc = QLineEdit(self.groupBox_3)
        self.cslow_qc.setObjectName(u"cslow_qc")
        self.cslow_qc.setGeometry(QRect(170, 30, 141, 31))
        self.rseries_qc = QLineEdit(self.groupBox_3)
        self.rseries_qc.setObjectName(u"rseries_qc")
        self.rseries_qc.setGeometry(QRect(10, 30, 141, 31))
        self.cfast_qc = QLineEdit(self.groupBox_3)
        self.cfast_qc.setObjectName(u"cfast_qc")
        self.cfast_qc.setGeometry(QRect(10, 90, 141, 31))
        self.cfast_qc_2 = QLineEdit(self.groupBox_3)
        self.cfast_qc_2.setObjectName(u"cfast_qc_2")
        self.cfast_qc_2.setGeometry(QRect(170, 90, 141, 31))
        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 120, 47, 13))
        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(170, 120, 47, 13))

        self.parameter_window.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalSlider = QSlider(self.groupBox_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(70, 40, 211, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(110, 20, 171, 16))
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(110, 90, 141, 16))
        self.horizontalSlider_2 = QSlider(self.groupBox_5)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(70, 110, 211, 22))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.parameter_window.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.parameter_window, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_19)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(610, 720, 141, 41))
        self.scrollArea_3 = QScrollArea(self.groupBox_19)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(10, 60, 251, 371))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 249, 369))
        self.general_commands_labels = ListView(self.scrollAreaWidgetContents_3)
        self.general_commands_labels.setObjectName(u"general_commands_labels")
        self.general_commands_labels.setGeometry(QRect(0, 0, 256, 371))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.widget = QWidget(self.groupBox_19)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(830, 60, 399, 347))
        self.pyqt_window = QGridLayout(self.widget)
        self.pyqt_window.setObjectName(u"pyqt_window")
        self.pyqt_window.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.select_commands)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1270, 100, 201, 161))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.label_16 = QLabel(self.select_commands)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(1270, 70, 151, 20))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_16.setFont(font1)
        self.stackedWidget.addWidget(self.select_commands)
        self.Notebook_2.addTab(self.batch_communication_3, "")
        self.camera_3 = QWidget()
        self.camera_3.setObjectName(u"camera_3")
        self.pushButton = QPushButton(self.camera_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 20, 191, 41))
        self.groupBox = QGroupBox(self.camera_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(80, 90, 641, 571))
        self.Camera_Live_Feed = QGraphicsView(self.groupBox)
        self.Camera_Live_Feed.setObjectName(u"Camera_Live_Feed")
        self.Camera_Live_Feed.setGeometry(QRect(40, 40, 561, 451))
        self.button_start_camera = QPushButton(self.groupBox)
        self.button_start_camera.setObjectName(u"button_start_camera")
        self.button_start_camera.setGeometry(QRect(40, 510, 182, 21))
        self.button_stop_camera = QPushButton(self.groupBox)
        self.button_stop_camera.setObjectName(u"button_stop_camera")
        self.button_stop_camera.setGeometry(QRect(228, 510, 183, 23))
        self.button_take_snapshot = QPushButton(self.groupBox)
        self.button_take_snapshot.setObjectName(u"button_take_snapshot")
        self.button_take_snapshot.setGeometry(QRect(417, 510, 182, 23))
        self.groupBox_2 = QGroupBox(self.camera_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(780, 90, 641, 571))
        self.Taken_Snapshot = QGraphicsView(self.groupBox_2)
        self.Taken_Snapshot.setObjectName(u"Taken_Snapshot")
        self.Taken_Snapshot.setGeometry(QRect(40, 40, 561, 451))
        self.button_transfer_to_labbook = QPushButton(self.groupBox_2)
        self.button_transfer_to_labbook.setObjectName(u"button_transfer_to_labbook")
        self.button_transfer_to_labbook.setGeometry(QRect(420, 510, 182, 23))
        self.button_discard_snapshot = QPushButton(self.groupBox_2)
        self.button_discard_snapshot.setObjectName(u"button_discard_snapshot")
        self.button_discard_snapshot.setGeometry(QRect(43, 510, 182, 23))
        self.button_save_snapshot = QPushButton(self.groupBox_2)
        self.button_save_snapshot.setObjectName(u"button_save_snapshot")
        self.button_save_snapshot.setGeometry(QRect(231, 510, 183, 23))
        self.frame = QFrame(self.camera_3)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 710, 1341, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-20, 0, 1361, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.camera_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(80, 690, 131, 16))
        self.Notebook_2.addTab(self.camera_3, "")

        self.gridLayout_2.addWidget(self.Notebook_2, 0, 1, 1, 1)


        self.retranslateUi(Config_Widget)

        self.Notebook_2.setCurrentIndex(0)
        self.meta_data_loading_1.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.Load_meta_data_experiment_12.setText(QCoreApplication.translate("Config_Widget", u"Load Metadata", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("Config_Widget", u"Staff", None))
        self.label_220.setText(QCoreApplication.translate("Config_Widget", u"Study director", None))
        self.label_221.setText(QCoreApplication.translate("Config_Widget", u"Technician", None))
        self.label_222.setText(QCoreApplication.translate("Config_Widget", u"Laboratory Code", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Protocol", None))
        self.button_pgf_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_61.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.label_60.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.button_protocol_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_59.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.button_onl_analysis_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("Config_Widget", u"Archiving", None))
        self.label_227.setText(QCoreApplication.translate("Config_Widget", u"Model Code", None))
        self.label_228.setText(QCoreApplication.translate("Config_Widget", u"Project Code", None))
        self.label_229.setText(QCoreApplication.translate("Config_Widget", u"Study Code", None))
        self.label_230.setText(QCoreApplication.translate("Config_Widget", u"Data path", None))
        self.label_231.setText(QCoreApplication.translate("Config_Widget", u"File name template", None))
        self.button_batch_7.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication and open Communication Test Tool", None))
        self.label_62.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Config_Widget", u"Solutions", None))
        self.label_199.setText(QCoreApplication.translate("Config_Widget", u"EC Type", None))
        self.label_200.setText(QCoreApplication.translate("Config_Widget", u"IC  Type", None))
        self.S1.setText("")
        self.label_201.setText(QCoreApplication.translate("Config_Widget", u"EC Lot #", None))
        self.label_202.setText(QCoreApplication.translate("Config_Widget", u"IC lot #", None))
        self.label_203.setText(QCoreApplication.translate("Config_Widget", u"T [\u00b0C]", None))
        self.label_204.setText(QCoreApplication.translate("Config_Widget", u"F [ml/min]", None))
        self.label_205.setText(QCoreApplication.translate("Config_Widget", u"I [nm]", None))
        self.label_206.setText(QCoreApplication.translate("Config_Widget", u"e", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("Config_Widget", u"Cells", None))
        self.label_207.setText(QCoreApplication.translate("Config_Widget", u"License ID", None))
        self.label_208.setText(QCoreApplication.translate("Config_Widget", u"Cell line", None))
        self.label_209.setText(QCoreApplication.translate("Config_Widget", u"Passage #", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("Config_Widget", u"Compound", None))
        self.label_210.setText(QCoreApplication.translate("Config_Widget", u"Sample Code", None))
        self.label_211.setText(QCoreApplication.translate("Config_Widget", u"Lot #", None))
        self.label_212.setText(QCoreApplication.translate("Config_Widget", u"Salt Code", None))
        self.label_213.setText(QCoreApplication.translate("Config_Widget", u"Sample Id", None))
        self.label_214.setText(QCoreApplication.translate("Config_Widget", u"MW [Da]", None))
        self.label_215.setText(QCoreApplication.translate("Config_Widget", u"Weight [mg]", None))
        self.label_216.setText(QCoreApplication.translate("Config_Widget", u"Solvent", None))
        self.label_217.setText(QCoreApplication.translate("Config_Widget", u"Stocks [mM]", None))
        self.label_218.setText(QCoreApplication.translate("Config_Widget", u"Concentration [\u00b5M]", None))
        self.label_219.setText(QCoreApplication.translate("Config_Widget", u"Volumn [\u00b5L]", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Config_Widget", u"Extracelullar and intracellular solutions", None))
        self.label_243.setText(QCoreApplication.translate("Config_Widget", u"Extracellular Solution", None))
        self.label_244.setText(QCoreApplication.translate("Config_Widget", u"Intracellular solution", None))
        self.ent_date_prep.setText("")
        self.label_245.setText(QCoreApplication.translate("Config_Widget", u"Date of Preparation ", None))
        self.ent_ph_set.setText(QCoreApplication.translate("Config_Widget", u"pH of External Solution", None))
        self.label_247.setText(QCoreApplication.translate("Config_Widget", u"Ph of internal solution", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Config_Widget", u"Patchmaster Setup Files", None))
        self.button_pgf_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_protocol_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_onl_analysis_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.label_3.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.label_5.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Metadata", None))
        self.label_6.setText(QCoreApplication.translate("Config_Widget", u"Experiment Type", None))
        self.label_7.setText(QCoreApplication.translate("Config_Widget", u"Cell Type", None))
        self.label_8.setText(QCoreApplication.translate("Config_Widget", u"Min # of Cells", None))
        self.label_9.setText(QCoreApplication.translate("Config_Widget", u" # of Cells patched", None))
        self.database_save.setText(QCoreApplication.translate("Config_Widget", u"Save to Database", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Config_Widget", u"Set Batch Communication Settings", None))
        self.button_batch_1.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication and open Communication Test Tool", None))
        self.label_4.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.add_pixmap_for_green.setText(QCoreApplication.translate("Config_Widget", u"Connected...", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.experiment_initialization_3), QCoreApplication.translate("Config_Widget", u"Experiment Initialization", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Config_Widget", u"Test the Connection to the Patchmaster", None))
        self.label_40.setText(QCoreApplication.translate("Config_Widget", u"Submit your Commands", None))
        self.label_41.setText(QCoreApplication.translate("Config_Widget", u"Control File received", None))
        self.label_42.setText(QCoreApplication.translate("Config_Widget", u"Batch Communication Response", None))
        self.button_submit_command.setText(QCoreApplication.translate("Config_Widget", u"Submit", None))
        self.button_clear_window.setText(QCoreApplication.translate("Config_Widget", u"Clear Windows", None))
        self.button_batch_2.setText(QCoreApplication.translate("Config_Widget", u"Setup Experiment", None))
        self.label_24.setText(QCoreApplication.translate("Config_Widget", u"Test Patchmaster Batch Communication", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Config_Widget", u"Protocol Editor", None))
        self.label.setText(QCoreApplication.translate("Config_Widget", u"Final Patch Clamping Sequence:", None))
        self.label_26.setText(QCoreApplication.translate("Config_Widget", u"Notebook Online Analysis:", None))
        self.label_27.setText(QCoreApplication.translate("Config_Widget", u"Dragable Labels", None))
        self.label_28.setText(QCoreApplication.translate("Config_Widget", u"Dragable Executable Series", None))
        self.label_32.setText(QCoreApplication.translate("Config_Widget", u"Dragable Protocols", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Config_Widget", u"Get Parameter", None))
        self.label_10.setText(QCoreApplication.translate("Config_Widget", u"Cslow", None))
        self.label_12.setText(QCoreApplication.translate("Config_Widget", u"Rseries", None))
        self.label_13.setText(QCoreApplication.translate("Config_Widget", u"Cfast", None))
        self.label_14.setText(QCoreApplication.translate("Config_Widget", u"Cell", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Config_Widget", u"Set Filtering", None))
        self.label_11.setText(QCoreApplication.translate("Config_Widget", u"Rseries Change in % allowed", None))
        self.label_15.setText(QCoreApplication.translate("Config_Widget", u"Cslow Changein % allowed", None))
        self.pushButton_10.setText(QCoreApplication.translate("Config_Widget", u"Clear Sequences", None))
        self.pushButton_3.setText(QCoreApplication.translate("Config_Widget", u"Start Experiment", None))
        self.pushButton_4.setText(QCoreApplication.translate("Config_Widget", u"Stop Experiment", None))
        self.pushButton_2.setText(QCoreApplication.translate("Config_Widget", u"Save Plot", None))
        self.label_16.setText(QCoreApplication.translate("Config_Widget", u"Execution of Experiment:", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.batch_communication_3), QCoreApplication.translate("Config_Widget", u"Batch Communication", None))
        self.pushButton.setText(QCoreApplication.translate("Config_Widget", u"Initalize Camera", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config_Widget", u"Live Camera Feed", None))
        self.button_start_camera.setText(QCoreApplication.translate("Config_Widget", u"Start Camera", None))
        self.button_stop_camera.setText(QCoreApplication.translate("Config_Widget", u"Stop Camera", None))
        self.button_take_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Take Snapshot", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config_Widget", u"Snapshot Overview", None))
        self.button_transfer_to_labbook.setText(QCoreApplication.translate("Config_Widget", u"Transfer to Labbook", None))
        self.button_discard_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Discard Snapshot", None))
        self.button_save_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Save Snapshot", None))
        self.label_31.setText(QCoreApplication.translate("Config_Widget", u"Image Galery", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.camera_3), QCoreApplication.translate("Config_Widget", u"Camera", None))
    # retranslateUi
        self.set_buttons_beginning()

    def set_buttons_beginning(self):
        """ set the button state of a view buttons inactivate at the beginning"""
        self.button_batch_2.setEnabled(False)
        self.add_pixmap_for_green.setStyleSheet("color: red")

    def meta_open_directory(self):
        '''opens a filedialog where a user can select a desired directory. Once the directory has been choosen,
        it's data will be loaded immediately into the databse'''
        # open the directory
        dir_path = QFileDialog.getOpenFileName()
        dir_path = str(dir_path[0]).replace("/","\\")
        # save the path in the manager class
        return dir_path

    def set_pgf_file(self):
        """set the pgf file that is used for the patchmaster"""
        logging.info("Setted PGF File")
        self.pgf_file = self.meta_open_directory()
    
        self.pg_file_set.setText(self.pgf_file)

    def set_protocol_file(self):
        """set the .pro file that is used for the patchmaster"""
        logging.info("Setted Protocol File")
        self.pro_file = self.meta_open_directory()
        self.protocol_file_set.setText(self.pro_file)

    def set_online_file(self):
        """set the online_analysis_file that is used for the patchmaster"""
        logging.info("Setted online analysis file")
        self.onl_file = self.meta_open_directory()
        self.online_analysis_file_set.setText(self.onl_file)

    def open_batch_path(self):
        """ choose the path were the batch communication file should
        be located
        --> checks for the exisitence of the file
        --> check control file button should indicate if file is already 
        there
         """
        batch_path = self.backend_manager.set_batch_path()
        if batch_path:
            self.Batch1.setText(batch_path)
            self.batch_path = batch_path
            file_existence = self.backend_manager.check_input_file_existence()
            self.backend_manager.create_ascii_file_from_template()
            self.button_batch_2.setStyleSheet("background-color: green")
            self.button_batch_2.setEnabled(True)
            self.submit_patchmaster_files()
            self.Notebook_2.setCurrentIndex(1)
            self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "SendOnlineAnalysis notebook" +"\n")
            self.increment_count()
                           
        else:
            self.Batch1.setText("please select a Path for the Patch File")

    def initialize_camera(self):
        """ Basler camera initalizing  
        ToDO: Error handling"""

        print("stuff worked")
        self.camera = BayerCamera()
        #initialize the camera 
        camera_status = self.camera.init_camera()
        self.scence_trial = QGraphicsScene(self) # generate a graphics scence in which the image can be putted
        if camera_status is None: # initialization of the camera and error response if not correctly initialized
            self.scence_trial.addText("is not working")
            self.Camera_Live_Feed.setScene(self.scence_trial)
            self.button_start_camera.setEnabled(False)
            self.button_stop_camera.setEnabled(False)
            self.button_take_snapshot.setEnabled(False)

        else:
            print("Camera is connected")
            self.scence_trial.addText("Please start the Camera via the Start Camera Button")
            self.Camera_Live_Feed.setScene(self.scence_trial)

    def start_camera_timer(self):
        """ added the asnychronous Qtimer for the Camera initalizion"""
        self.start_cam = QTimer() # camera timer 
        self.start_cam.timeout.connect(self.start_camera)   # connected to camera methond
        self.start_cam.start(222)  # (333,self.start_camera)

    def start_camera(self):
        """ grab the current picture one by one with 50 FPS """
        camera_image = self.camera.grab_video() # grab video retrieved np.array image
        imgs = Image.fromarray(camera_image) # conversion
        image = imgs.resize((561,451), Image.ANTIALIAS) # resizing to be of appropriate size for the window
        imgqt = ImageQt.ImageQt(image) # convert to qt image
        self.trial_figure = QPixmap.fromImage(imgqt)
        self.scence_trial.clear()
        self.scence_trial.addPixmap(self.trial_figure)
        print(camera_image)

    def stop_camera(self):
        """ stop the camera timer """
        print("yeah I m here for the camera")
        self.start_cam.stop() # here the camera Qtimer is stopped

    def show_snapshot(self):
        """ does transfer the current snapshot to the galery view """

        self.check_list_lenght(self.image_stacke) # self.image_stacke is der stack der images generiert
        self.image_stacke.insert(0,self.trial_figure) # neues image wird an stelle 1 gepusht
        self.snapshot_scence = QGraphicsScene(self)
        self.Taken_Snapshot.setScene(self.snapshot_scence)
        self.snapshot_scence.addPixmap(self.trial_figure)
        self.draw_snapshots_on_galery() # draw into the galery

    def check_list_lenght(self, image_liste):
        """Here we check the lenght of the  to avoid overcrowding in the image galery
        its set to 5 images"""
        try:
            if len(image_liste) > 4:
                image_liste.pop()
                print("Expected List Length reached")
        except Exception as e:
            print(repr(f"This is the Error: {e}"))


    def draw_snapshots_on_galery(self):
        # function to draw the taken snapshot into the image galery
        for i in reversed(range(self.horizontalLayout.count())): 
            self.horizontalLayout.itemAt(i).widget().setParent(None)
        if len(self.image_stacke) > 0: #looping through the image stack
            for i,t in enumerate(self.image_stacke):
                label = QLabel()
                label.setPixmap(t)
                self.horizontalLayout.addWidget(label) # add to the layout 


    def get_commands_from_textinput(self):
        """ retrieves the command send to the patchmaster and the response from the Batch.out file """
        print("get commands")
        self.res = self.sub_command1.toPlainText()
        self.logger.debug(f'Batch communication input: {self.res}')
        self.sub_command1.clear()
        
        print(self.res)
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + self.res + "\n")
        self.submission_count += 1
        if self.check_session:
            print("still checking commands")
        else:
            self.check_session = QTimer() # timer added for regular checking 
            self.check_session.timeout.connect(self.update_page)
            self.check_session.start(1000)
        #return self.res

    def update_page(self):
        """ asynchronouse updating of the textArea with the control file and the response file
        Connected to the Qtimter """
        response_file = self.backend_manager.update_response_file_content() # response file update
        input_file = self.backend_manager.update_control_file_content() # control file update
        self.receive_command1.clear()# clearing of the last commands entered
        self.response_command_1.clear() # clearing of the response
        self.receive_command1.insertPlainText(input_file)
        self.response_command_1.insertPlainText(response_file)

    def end_communication_control(self):
        """ stop the batch communication and clear all fields """
        print("communication end")
        if self.check_session:
            self.check_session.stop() # stops the timer
            self.check_session = None
            self.receive_command1.clear()
            self.response_command_1.clear()
            self.sub_command1.clear()

    def show_analysis_window(self):
        """add Docstring"""
        # Get Input from the Sequences and the Protocols
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListSequences\n") # get the potential Series that can be started
        sleep(0.2) # sleep is inserted because of laggy writing to the response file from the patchmaster
        sequences = self.backend_manager.update_response_file_content()
        self.increment_count()
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ListProtocols\n") # get the protocols that can be started
        sleep(0.2)
        protocol_responses = self.backend_manager.update_response_file_content() # get the protocol responses 
        self.increment_count() # always increment the batch communication count 

        # Plotting
        
        self.tscurve_1 = PlotCurve(
            linked_curve=self.pyqt_graph.plot(pen=pg.mkPen('r')),
        ) # use this package to make drawing from another thread Threadsafe
     # setting of the background put to global
        self.pyqt_window.addWidget(self.pyqt_graph)
        #self.plot_qt(self.pyqt_graph.plotWidget)

        # Preprocessing
        series = self.preprocess_series_protocols(sequences) # get the listed series from batch.out response
        protocols = self.preprocess_series_protocols(protocol_responses) # get the listed protocols from batch.out response
        self.style_list_view()

        #Make List Labels
        self.make_sequence_labels(series, self.SeriesWidget) # enter items of sequences into drag and dropbable listview
        self.make_sequence_labels(protocols, self.protocol_widget) # enter items of protcols into drag and dropable listview
        self.make_general_commands() # add general commands to the general command listview
        self.stackedWidget.setCurrentIndex(1) # set the index to the testing Area

    def preprocess_series_protocols(self, sequences_reponses):
        """get the list of protocols,get rid of the submission code"""
        patch_sequences = sequences_reponses[31: ].split(",")
        patch_sequences = [i.replace('"', "") for i in patch_sequences]
        patch_sequences = [i.replace("\n", "")for i in patch_sequences]
        return patch_sequences
        
    def style_list_view(self):
        """ styling of the ListWidget make it blue to popup more"""
        self.listWidget.setStyleSheet(f"border: 2px; border-color: white")
        self.SeriesWidget.setStyleSheet("background: #448aff;")
        self.general_commands_labels.setStyleSheet("background: #448aff")
        self.protocol_widget.setStyleSheet("background: #448aff")

    def make_sequence_labels(self, list_of_sequences,widget):
        """ same as protocols"""
        for i in list_of_sequences:
            item = QStandardItem(i)
            widget.model().appendRow(item)

    def make_general_commands(self):
        #insert items into general command list
        for i in self.general_commands_list:
            item = QStandardItem(i)
            self.general_commands_labels.model().appendRow(item)

    def submit_patchmaster_files(self):
        """ Submission of the loaded pgf, prot and onl file to the patchmaster and setting them"""
        logging.info("Configuration Files setted up:....")
        for file, command in zip([self.pgf_file, self.pro_file, self.onl_file],["OpenPgfFile","OpenProtFile","OpenOnlineFile"]):
            if file:
                self.backend_manager.send_text_input("+"+f'{self.submission_count}\n' + command + f" {file}\n") # send the file lcoation and name to the patchmaster
                sleep(0.5)
                self.submission_count += 1
            else:
                logging.info("not all configuration files set:")

    def make_threading(self):
        # generate a threadpool inherted from the runnable class and connect it to the workerclass
        self.threadpool = QThreadPool()
        self.worker = Worker(self.start_experiment_patch)
        self.threadpool.start(self.worker)

    def stop_threading(self):
        # Here we need to find a way to stop the threading if an error occur !
        self.threadpool.stop(self.worker)

    def start_experiment_patch(self):
        """ get the ListView entries and send them off via the backend manager"""
        # this should be exposed to threading!
        view_list = self.listWidget.model()
        self.sequence_experiment_dictionary = {} # all derived online analyiss data will be stored here in a "Series":Data fashion
        self.increment_count()
        final_notebook_dataframe = pd.DataFrame() # initialize an empty dataframe which can be appended to
        
        for index in range(view_list.rowCount()):
            item = view_list.item(index).text() # get the name of the stacked protocols/series/programs
            self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""GetParameters Param-2,Param-3,Param-4,Param-12\n") # always check the parameters after each protocol
            #ToDO Define Cancel Options like Filters
            sleep(0.2)
            params_response = self.backend_manager.get_parameters() # return the paramters and write them into the entry boxes
            self.increment_count()
            self.rseries_qc.setText(params_response[3])
            self.cslow_qc.setText(params_response[1])
            self.cfast_qc.setText(params_response[0])
            self.cfast_qc_2.setText(params_response[2])

            if self.SeriesWidget.model().findItems(item):
                """ check if item is in series list"""
                logging.info(f"Series {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ExecuteSequence " + f'"{item}"' +"\n")
                self.increment_count()
                self.trial_setup(final_notebook_dataframe, item)

            elif "GetEpc" in item:
                #check if item is a paramter check
                logging.info(f"Parameter Command {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + f'"{item}"' +"\n")
                print("GetParameters if necessary")
            
            elif self.protocol_widget.model().findItems(item):
                #Check if item is a protcol
                logging.info(f"Protocol {item} will be executed")
                self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "ExecuteProtocol " + f'"{item}"' +"\n")
                self.increment_count()
                analyzed = self.trial_setup(final_notebook_dataframe, item)

            else:
                #check if item is a general command
                logging.info(f"General Command {item} will be executed")
                self.basic_configuration_protcols(item)


    def increment_count(self):
        #increment count to renew submission code for the patchmaster
        self.submission_count += 1

    def trial_setup(self, notebook, item):
        """gets the data and draws it into the fast analysis window
        ToDO:"""
        sleep(0.2)
        item = item 
        final_notebook_dataframe = notebook
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n" + "Query\n") # Query to get the state of the amplifier
        self.increment_count()

        query_status = self.backend_manager.get_query_status()
        query_status = query_status.replace(" ", "")
        print(f"this is the query status: {query_status}")

        if "Query_Idle" in query_status:
            # Check for different states
            try: 
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook
            except:
                final_notebook = self.get_final_notebook(final_notebook_dataframe)
                self.sequence_experiment_dictionary[item] = final_notebook
                return True
    
        elif ("Query_Acquiring" or "Query_Executing") in query_status:
            #Check if the query is still acquiring
            try:
                dataframe = self.backend_manager.return_dataframe_from_notebook()
                final_notebook_dataframe = final_notebook_dataframe.append(dataframe)
                print(final_notebook_dataframe)
                print(final_notebook_dataframe.iloc[1:,:][4].values)
                self.tscurve_1.setData([float(i) for i in final_notebook_dataframe.iloc[1:,:][4].values],[float(i) for i in final_notebook_dataframe.iloc[1:,:][7].values])
                self.tscurve_1.update()
                self.trial_setup(final_notebook_dataframe,item)
            except Exception as e:
                print(repr(e))
                self.trial_setup(final_notebook_dataframe,item)
        
        else:
            print("Connection Lost")
            return None
        

    def get_final_notebook(self, notebook):
        """ Dataframe has multiple commas therefore columsn will be shifted to adjust for this"""
        columns = notebook.iloc[0].tolist()
        columns.pop(0)
        columns = columns + ["NAN"]
        columns = [str(i).replace('"',"") for i in columns]
        final_notebook = notebook[1:]
        final_notebook.columns = columns
        final_notebook = final_notebook.iloc[:,4:]
        final_notebook = final_notebook.drop("NAN", axis = 1)
        
        print(final_notebook)
        return True

    def basic_configuration_protcols(self, item):
        print("yes i entered this file")
        function_dictionary = {"Setup": self.execute_setup, "Seal": self.execute_seal, "Whole-cell": self.execute_whole_cell}
        func = function_dictionary.get(item,lambda :'Invalid')
        func()

    def execute_setup(self):
        # setup protocol execturio command
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SETUP\n")
        self.increment_count()
    
    def execute_seal(self):
        # seal protocol exectuion command
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol SEAL\n")
        self.increment_count()
        print()

    def execute_whole_cell(self):
        #whole_cell exection command 
        self.backend_manager.send_text_input("+"+f'{self.submission_count}' + "\n""ExecuteProtocol WHOLE-CELL\n")
        self.increment_count()
        print(9)
        
    def clear_list(self):
        # connect to the button 
        self.listWidget.model().clear()
        
    def set_darkmode(self, default_mode):
        self.default_mode = default_mode
   
    def get_darkmode(self):
        "returns the darkmode state"
        print(f"this is the current mode: {self.default_mode}")
        return self.default_mode

    def setting_appearance(self):
        default_mode = self.get_darkmode()
        if default_mode == 0:
            print("light_mode")
            self.pyqt_graph.setBackground("#f5f5f5")

        else:
            print("dark_mode")
            self.pyqt_graph.setBackground("#232629")

class Config_Widget(QWidget,Ui_Config_Widget):
    """ promotion of the self configuration widget"""
    def __init__(self,parent = None):
        QWidget.__init__(self,parent)
        self.initialized()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()  # QtCore.Slot
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)




