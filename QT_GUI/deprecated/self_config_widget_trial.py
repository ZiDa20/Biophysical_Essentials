# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self_config_widget_trial.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(1428, 748)
        self.gridLayout_23 = QGridLayout(Config_Widget)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.self_configuration_notebook = QTabWidget(Config_Widget)
        self.self_configuration_notebook.setObjectName(u"self_configuration_notebook")
        self.experiment_initialization_3 = QWidget()
        self.experiment_initialization_3.setObjectName(u"experiment_initialization_3")
        self.gridLayout_2 = QGridLayout(self.experiment_initialization_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.meta_data_loading_1 = QStackedWidget(self.experiment_initialization_3)
        self.meta_data_loading_1.setObjectName(u"meta_data_loading_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meta_data_loading_1.sizePolicy().hasHeightForWidth())
        self.meta_data_loading_1.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_17 = QGridLayout(self.page)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_30 = QGroupBox(self.page)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_19 = QGridLayout(self.groupBox_30)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.Ce_com1 = QComboBox(self.groupBox_30)
        self.Ce_com1.setObjectName(u"Ce_com1")
        self.Ce_com1.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_19.addWidget(self.Ce_com1, 1, 0, 1, 1)

        self.label_207 = QLabel(self.groupBox_30)
        self.label_207.setObjectName(u"label_207")

        self.gridLayout_19.addWidget(self.label_207, 2, 0, 1, 1)

        self.Ce_com2 = QComboBox(self.groupBox_30)
        self.Ce_com2.setObjectName(u"Ce_com2")
        self.Ce_com2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_19.addWidget(self.Ce_com2, 3, 0, 1, 1)

        self.Ce1 = QLineEdit(self.groupBox_30)
        self.Ce1.setObjectName(u"Ce1")
        self.Ce1.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_19.addWidget(self.Ce1, 5, 0, 1, 1)

        self.label_209 = QLabel(self.groupBox_30)
        self.label_209.setObjectName(u"label_209")

        self.gridLayout_19.addWidget(self.label_209, 6, 0, 1, 1)

        self.label_208 = QLabel(self.groupBox_30)
        self.label_208.setObjectName(u"label_208")

        self.gridLayout_19.addWidget(self.label_208, 4, 0, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_31, 7, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_30, 0, 1, 1, 1)

        self.groupBox_31 = QGroupBox(self.page)
        self.groupBox_31.setObjectName(u"groupBox_31")
        sizePolicy.setHeightForWidth(self.groupBox_31.sizePolicy().hasHeightForWidth())
        self.groupBox_31.setSizePolicy(sizePolicy)
        self.gridLayout_20 = QGridLayout(self.groupBox_31)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.C1 = QLineEdit(self.groupBox_31)
        self.C1.setObjectName(u"C1")

        self.gridLayout_20.addWidget(self.C1, 0, 0, 1, 2)

        self.C2 = QLineEdit(self.groupBox_31)
        self.C2.setObjectName(u"C2")

        self.gridLayout_20.addWidget(self.C2, 0, 2, 1, 2)

        self.Co_com1 = QComboBox(self.groupBox_31)
        self.Co_com1.setObjectName(u"Co_com1")

        self.gridLayout_20.addWidget(self.Co_com1, 0, 4, 1, 1)

        self.label_210 = QLabel(self.groupBox_31)
        self.label_210.setObjectName(u"label_210")

        self.gridLayout_20.addWidget(self.label_210, 1, 0, 1, 1)

        self.label_211 = QLabel(self.groupBox_31)
        self.label_211.setObjectName(u"label_211")

        self.gridLayout_20.addWidget(self.label_211, 1, 2, 1, 1)

        self.label_212 = QLabel(self.groupBox_31)
        self.label_212.setObjectName(u"label_212")

        self.gridLayout_20.addWidget(self.label_212, 1, 4, 1, 1)

        self.C3 = QLineEdit(self.groupBox_31)
        self.C3.setObjectName(u"C3")

        self.gridLayout_20.addWidget(self.C3, 2, 0, 1, 2)

        self.C4 = QLineEdit(self.groupBox_31)
        self.C4.setObjectName(u"C4")

        self.gridLayout_20.addWidget(self.C4, 2, 2, 1, 2)

        self.label_213 = QLabel(self.groupBox_31)
        self.label_213.setObjectName(u"label_213")

        self.gridLayout_20.addWidget(self.label_213, 3, 0, 1, 1)

        self.label_214 = QLabel(self.groupBox_31)
        self.label_214.setObjectName(u"label_214")

        self.gridLayout_20.addWidget(self.label_214, 3, 2, 1, 1)

        self.C5 = QLineEdit(self.groupBox_31)
        self.C5.setObjectName(u"C5")

        self.gridLayout_20.addWidget(self.C5, 5, 0, 1, 2)

        self.C6 = QLineEdit(self.groupBox_31)
        self.C6.setObjectName(u"C6")

        self.gridLayout_20.addWidget(self.C6, 5, 2, 1, 2)

        self.C6_2 = QLineEdit(self.groupBox_31)
        self.C6_2.setObjectName(u"C6_2")

        self.gridLayout_20.addWidget(self.C6_2, 5, 4, 1, 1)

        self.label_215 = QLabel(self.groupBox_31)
        self.label_215.setObjectName(u"label_215")

        self.gridLayout_20.addWidget(self.label_215, 6, 0, 1, 1)

        self.label_216 = QLabel(self.groupBox_31)
        self.label_216.setObjectName(u"label_216")

        self.gridLayout_20.addWidget(self.label_216, 6, 2, 1, 1)

        self.label_219 = QLabel(self.groupBox_31)
        self.label_219.setObjectName(u"label_219")

        self.gridLayout_20.addWidget(self.label_219, 6, 4, 1, 1)

        self.C8 = QLineEdit(self.groupBox_31)
        self.C8.setObjectName(u"C8")

        self.gridLayout_20.addWidget(self.C8, 7, 0, 1, 2)

        self.C9 = QLineEdit(self.groupBox_31)
        self.C9.setObjectName(u"C9")

        self.gridLayout_20.addWidget(self.C9, 7, 3, 1, 2)

        self.label_218 = QLabel(self.groupBox_31)
        self.label_218.setObjectName(u"label_218")

        self.gridLayout_20.addWidget(self.label_218, 8, 3, 1, 2)

        self.label_217 = QLabel(self.groupBox_31)
        self.label_217.setObjectName(u"label_217")

        self.gridLayout_20.addWidget(self.label_217, 8, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_31, 0, 2, 1, 1)

        self.groupBox_33 = QGroupBox(self.page)
        self.groupBox_33.setObjectName(u"groupBox_33")
        sizePolicy.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy)
        self.gridLayout_22 = QGridLayout(self.groupBox_33)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_32, 0, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_33)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_22.addWidget(self.label_60, 7, 0, 1, 1)

        self.button_onl_analysis_set_3 = QPushButton(self.groupBox_33)
        self.button_onl_analysis_set_3.setObjectName(u"button_onl_analysis_set_3")

        self.gridLayout_22.addWidget(self.button_onl_analysis_set_3, 6, 1, 1, 1)

        self.pg_file_set_3 = QLineEdit(self.groupBox_33)
        self.pg_file_set_3.setObjectName(u"pg_file_set_3")
        self.pg_file_set_3.setMaximumSize(QSize(300, 200))

        self.gridLayout_22.addWidget(self.pg_file_set_3, 2, 0, 1, 1)

        self.button_pgf_set_3 = QPushButton(self.groupBox_33)
        self.button_pgf_set_3.setObjectName(u"button_pgf_set_3")

        self.gridLayout_22.addWidget(self.button_pgf_set_3, 2, 1, 1, 1)

        self.label_59 = QLabel(self.groupBox_33)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_22.addWidget(self.label_59, 3, 0, 1, 1)

        self.button_protocol_set_3 = QPushButton(self.groupBox_33)
        self.button_protocol_set_3.setObjectName(u"button_protocol_set_3")

        self.gridLayout_22.addWidget(self.button_protocol_set_3, 4, 1, 1, 1)

        self.protocol_file_set_3 = QLineEdit(self.groupBox_33)
        self.protocol_file_set_3.setObjectName(u"protocol_file_set_3")
        self.protocol_file_set_3.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_22.addWidget(self.protocol_file_set_3, 4, 0, 1, 1)

        self.label_61 = QLabel(self.groupBox_33)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_22.addWidget(self.label_61, 5, 0, 1, 1)

        self.online_analysis_file_set_3 = QLineEdit(self.groupBox_33)
        self.online_analysis_file_set_3.setObjectName(u"online_analysis_file_set_3")
        self.online_analysis_file_set_3.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_22.addWidget(self.online_analysis_file_set_3, 6, 0, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_38, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_33, 1, 1, 1, 1)

        self.groupBox_32 = QGroupBox(self.page)
        self.groupBox_32.setObjectName(u"groupBox_32")
        sizePolicy.setHeightForWidth(self.groupBox_32.sizePolicy().hasHeightForWidth())
        self.groupBox_32.setSizePolicy(sizePolicy)
        self.gridLayout_21 = QGridLayout(self.groupBox_32)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_220 = QLabel(self.groupBox_32)
        self.label_220.setObjectName(u"label_220")

        self.gridLayout_21.addWidget(self.label_220, 2, 0, 1, 1)

        self.St_com2 = QComboBox(self.groupBox_32)
        self.St_com2.setObjectName(u"St_com2")
        self.St_com2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_21.addWidget(self.St_com2, 3, 0, 1, 1)

        self.St_com1 = QComboBox(self.groupBox_32)
        self.St_com1.setObjectName(u"St_com1")
        self.St_com1.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_21.addWidget(self.St_com1, 1, 0, 1, 1)

        self.label_221 = QLabel(self.groupBox_32)
        self.label_221.setObjectName(u"label_221")

        self.gridLayout_21.addWidget(self.label_221, 4, 0, 1, 1)

        self.label_222 = QLabel(self.groupBox_32)
        self.label_222.setObjectName(u"label_222")

        self.gridLayout_21.addWidget(self.label_222, 6, 0, 1, 1)

        self.St_com3 = QComboBox(self.groupBox_32)
        self.St_com3.setObjectName(u"St_com3")
        self.St_com3.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_21.addWidget(self.St_com3, 5, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_33, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_32, 1, 0, 1, 1)

        self.groupBox_34 = QGroupBox(self.page)
        self.groupBox_34.setObjectName(u"groupBox_34")
        sizePolicy.setHeightForWidth(self.groupBox_34.sizePolicy().hasHeightForWidth())
        self.groupBox_34.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.groupBox_34)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_37, 0, 0, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_34, 1, 0, 1, 1)

        self.A_com1 = QComboBox(self.groupBox_34)
        self.A_com1.setObjectName(u"A_com1")

        self.gridLayout_4.addWidget(self.A_com1, 2, 0, 1, 1)

        self.A_com2 = QComboBox(self.groupBox_34)
        self.A_com2.setObjectName(u"A_com2")

        self.gridLayout_4.addWidget(self.A_com2, 2, 1, 1, 1)

        self.A1 = QLineEdit(self.groupBox_34)
        self.A1.setObjectName(u"A1")

        self.gridLayout_4.addWidget(self.A1, 2, 2, 1, 1)

        self.label_227 = QLabel(self.groupBox_34)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_4.addWidget(self.label_227, 3, 0, 1, 1)

        self.label_228 = QLabel(self.groupBox_34)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_4.addWidget(self.label_228, 3, 1, 1, 1)

        self.label_229 = QLabel(self.groupBox_34)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_4.addWidget(self.label_229, 3, 2, 1, 1)

        self.A_com3 = QComboBox(self.groupBox_34)
        self.A_com3.setObjectName(u"A_com3")

        self.gridLayout_4.addWidget(self.A_com3, 4, 0, 1, 1)

        self.A2 = QLineEdit(self.groupBox_34)
        self.A2.setObjectName(u"A2")

        self.gridLayout_4.addWidget(self.A2, 4, 1, 1, 2)

        self.label_230 = QLabel(self.groupBox_34)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_4.addWidget(self.label_230, 5, 0, 1, 1)

        self.label_231 = QLabel(self.groupBox_34)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_4.addWidget(self.label_231, 5, 1, 1, 1)

        self.Batch1_4 = QLineEdit(self.groupBox_34)
        self.Batch1_4.setObjectName(u"Batch1_4")

        self.gridLayout_4.addWidget(self.Batch1_4, 6, 0, 1, 2)

        self.label_62 = QLabel(self.groupBox_34)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_4.addWidget(self.label_62, 7, 0, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_35, 8, 0, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_36, 9, 0, 1, 1)

        self.button_batch_7 = QPushButton(self.groupBox_34)
        self.button_batch_7.setObjectName(u"button_batch_7")

        self.gridLayout_4.addWidget(self.button_batch_7, 10, 1, 1, 2)


        self.gridLayout_17.addWidget(self.groupBox_34, 1, 2, 1, 1)

        self.groupBox_22 = QGroupBox(self.page)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_18 = QGridLayout(self.groupBox_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_201 = QLabel(self.groupBox_22)
        self.label_201.setObjectName(u"label_201")

        self.gridLayout_18.addWidget(self.label_201, 6, 0, 1, 1)

        self.So_com1 = QComboBox(self.groupBox_22)
        self.So_com1.setObjectName(u"So_com1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.So_com1.sizePolicy().hasHeightForWidth())
        self.So_com1.setSizePolicy(sizePolicy1)
        self.So_com1.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_18.addWidget(self.So_com1, 1, 0, 1, 1)

        self.S1 = QLineEdit(self.groupBox_22)
        self.S1.setObjectName(u"S1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.S1.sizePolicy().hasHeightForWidth())
        self.S1.setSizePolicy(sizePolicy2)
        self.S1.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_18.addWidget(self.S1, 5, 0, 1, 1)

        self.label_199 = QLabel(self.groupBox_22)
        self.label_199.setObjectName(u"label_199")

        self.gridLayout_18.addWidget(self.label_199, 2, 0, 1, 1)

        self.So_com2 = QComboBox(self.groupBox_22)
        self.So_com2.setObjectName(u"So_com2")
        sizePolicy1.setHeightForWidth(self.So_com2.sizePolicy().hasHeightForWidth())
        self.So_com2.setSizePolicy(sizePolicy1)
        self.So_com2.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_18.addWidget(self.So_com2, 1, 1, 1, 1)

        self.label_200 = QLabel(self.groupBox_22)
        self.label_200.setObjectName(u"label_200")

        self.gridLayout_18.addWidget(self.label_200, 2, 1, 1, 1)

        self.label_204 = QLabel(self.groupBox_22)
        self.label_204.setObjectName(u"label_204")

        self.gridLayout_18.addWidget(self.label_204, 8, 2, 1, 1)

        self.S6 = QLineEdit(self.groupBox_22)
        self.S6.setObjectName(u"S6")
        sizePolicy2.setHeightForWidth(self.S6.sizePolicy().hasHeightForWidth())
        self.S6.setSizePolicy(sizePolicy2)

        self.gridLayout_18.addWidget(self.S6, 7, 1, 1, 1)

        self.S5 = QLineEdit(self.groupBox_22)
        self.S5.setObjectName(u"S5")
        sizePolicy2.setHeightForWidth(self.S5.sizePolicy().hasHeightForWidth())
        self.S5.setSizePolicy(sizePolicy2)

        self.gridLayout_18.addWidget(self.S5, 7, 0, 1, 1)

        self.label_205 = QLabel(self.groupBox_22)
        self.label_205.setObjectName(u"label_205")

        self.gridLayout_18.addWidget(self.label_205, 8, 0, 1, 1)

        self.label_206 = QLabel(self.groupBox_22)
        self.label_206.setObjectName(u"label_206")

        self.gridLayout_18.addWidget(self.label_206, 8, 1, 1, 1)

        self.S2 = QLineEdit(self.groupBox_22)
        self.S2.setObjectName(u"S2")
        sizePolicy2.setHeightForWidth(self.S2.sizePolicy().hasHeightForWidth())
        self.S2.setSizePolicy(sizePolicy2)
        self.S2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_18.addWidget(self.S2, 5, 1, 1, 1)

        self.S3 = QLineEdit(self.groupBox_22)
        self.S3.setObjectName(u"S3")
        sizePolicy2.setHeightForWidth(self.S3.sizePolicy().hasHeightForWidth())
        self.S3.setSizePolicy(sizePolicy2)

        self.gridLayout_18.addWidget(self.S3, 5, 2, 1, 1)

        self.label_202 = QLabel(self.groupBox_22)
        self.label_202.setObjectName(u"label_202")

        self.gridLayout_18.addWidget(self.label_202, 6, 1, 1, 1)

        self.label_203 = QLabel(self.groupBox_22)
        self.label_203.setObjectName(u"label_203")

        self.gridLayout_18.addWidget(self.label_203, 6, 2, 1, 1)

        self.S4 = QLineEdit(self.groupBox_22)
        self.S4.setObjectName(u"S4")
        sizePolicy2.setHeightForWidth(self.S4.sizePolicy().hasHeightForWidth())
        self.S4.setSizePolicy(sizePolicy2)

        self.gridLayout_18.addWidget(self.S4, 7, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_30, 0, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_28, 0, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_29, 0, 2, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.meta_data_loading_1.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 9, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_9, 6, 0, 1, 1)

        self.experiment_type_desc = QLineEdit(self.groupBox_6)
        self.experiment_type_desc.setObjectName(u"experiment_type_desc")
        self.experiment_type_desc.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_7.addWidget(self.experiment_type_desc, 1, 0, 1, 2)

        self.cell_type_desc = QLineEdit(self.groupBox_6)
        self.cell_type_desc.setObjectName(u"cell_type_desc")
        self.cell_type_desc.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_7.addWidget(self.cell_type_desc, 4, 0, 1, 2)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 8, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_8, 8, 0, 1, 1)

        self.min_number_cells = QLineEdit(self.groupBox_6)
        self.min_number_cells.setObjectName(u"min_number_cells")

        self.gridLayout_7.addWidget(self.min_number_cells, 7, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)

        self.patched_cells = QLineEdit(self.groupBox_6)
        self.patched_cells.setObjectName(u"patched_cells")

        self.gridLayout_7.addWidget(self.patched_cells, 7, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.label_7, 5, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.page_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_23)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 9, 0, 1, 1)

        self.extracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.extracellular_sol_com_1.setObjectName(u"extracellular_sol_com_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.extracellular_sol_com_1.sizePolicy().hasHeightForWidth())
        self.extracellular_sol_com_1.setSizePolicy(sizePolicy3)
        self.extracellular_sol_com_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.extracellular_sol_com_1, 1, 1, 1, 3)

        self.label_243 = QLabel(self.groupBox_23)
        self.label_243.setObjectName(u"label_243")
        sizePolicy1.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_243, 2, 1, 1, 2)

        self.ent_ph_set = QLabel(self.groupBox_23)
        self.ent_ph_set.setObjectName(u"ent_ph_set")
        sizePolicy1.setHeightForWidth(self.ent_ph_set.sizePolicy().hasHeightForWidth())
        self.ent_ph_set.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ent_ph_set, 8, 2, 1, 1)

        self.label_247 = QLabel(self.groupBox_23)
        self.label_247.setObjectName(u"label_247")
        sizePolicy1.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_247, 8, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 6, 1, 1, 1)

        self.label_244 = QLabel(self.groupBox_23)
        self.label_244.setObjectName(u"label_244")
        sizePolicy1.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_244, 5, 1, 1, 2)

        self.ent_ph_int_set = QLineEdit(self.groupBox_23)
        self.ent_ph_int_set.setObjectName(u"ent_ph_int_set")

        self.gridLayout_5.addWidget(self.ent_ph_int_set, 7, 3, 1, 1)

        self.S2_3 = QLineEdit(self.groupBox_23)
        self.S2_3.setObjectName(u"S2_3")

        self.gridLayout_5.addWidget(self.S2_3, 7, 2, 1, 1)

        self.label_245 = QLabel(self.groupBox_23)
        self.label_245.setObjectName(u"label_245")
        sizePolicy1.setHeightForWidth(self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_245, 8, 0, 1, 1)

        self.ent_date_prep = QLineEdit(self.groupBox_23)
        self.ent_date_prep.setObjectName(u"ent_date_prep")

        self.gridLayout_5.addWidget(self.ent_date_prep, 7, 0, 1, 2)

        self.Intracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.Intracellular_sol_com_1.setObjectName(u"Intracellular_sol_com_1")
        self.Intracellular_sol_com_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.Intracellular_sol_com_1, 4, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_23, 2, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.page_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.groupBox_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 6, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.Batch1 = QLineEdit(self.groupBox_17)
        self.Batch1.setObjectName(u"Batch1")
        self.Batch1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_8.addWidget(self.Batch1, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_17)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)

        self.button_batch_1 = QPushButton(self.groupBox_17)
        self.button_batch_1.setObjectName(u"button_batch_1")
        self.button_batch_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_8.addWidget(self.button_batch_1, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_17, 3, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.online_analysis_file_set = QLineEdit(self.groupBox_4)
        self.online_analysis_file_set.setObjectName(u"online_analysis_file_set")
        self.online_analysis_file_set.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.online_analysis_file_set, 5, 0, 1, 1)

        self.button_onl_analysis_set = QPushButton(self.groupBox_4)
        self.button_onl_analysis_set.setObjectName(u"button_onl_analysis_set")

        self.gridLayout_6.addWidget(self.button_onl_analysis_set, 5, 1, 1, 1)

        self.protocol_file_set = QLineEdit(self.groupBox_4)
        self.protocol_file_set.setObjectName(u"protocol_file_set")
        self.protocol_file_set.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.protocol_file_set, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 4, 0, 1, 1)

        self.button_protocol_set = QPushButton(self.groupBox_4)
        self.button_protocol_set.setObjectName(u"button_protocol_set")

        self.gridLayout_6.addWidget(self.button_protocol_set, 3, 1, 1, 1)

        self.button_pgf_set = QPushButton(self.groupBox_4)
        self.button_pgf_set.setObjectName(u"button_pgf_set")
        self.button_pgf_set.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.button_pgf_set, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 6, 0, 1, 1)

        self.pg_file_set = QLineEdit(self.groupBox_4)
        self.pg_file_set.setObjectName(u"pg_file_set")
        self.pg_file_set.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_6.addWidget(self.pg_file_set, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(250, 16777215))
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_14, 16, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_24, 9, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_25, 8, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_23, 4, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_21, 10, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_22, 2, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 15, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 14, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_26, 7, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_19, 12, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_18, 13, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_20, 11, 0, 1, 1)

        self.database_save = QPushButton(self.groupBox_7)
        self.database_save.setObjectName(u"database_save")
        sizePolicy.setHeightForWidth(self.database_save.sizePolicy().hasHeightForWidth())
        self.database_save.setSizePolicy(sizePolicy)
        self.database_save.setMaximumSize(QSize(200, 30))

        self.gridLayout_9.addWidget(self.database_save, 3, 0, 1, 1)

        self.database_save_2 = QPushButton(self.groupBox_7)
        self.database_save_2.setObjectName(u"database_save_2")
        sizePolicy.setHeightForWidth(self.database_save_2.sizePolicy().hasHeightForWidth())
        self.database_save_2.setSizePolicy(sizePolicy)
        self.database_save_2.setMaximumSize(QSize(200, 30))

        self.gridLayout_9.addWidget(self.database_save_2, 5, 0, 1, 1)

        self.add_pixmap_for_green = QLabel(self.groupBox_7)
        self.add_pixmap_for_green.setObjectName(u"add_pixmap_for_green")
        sizePolicy1.setHeightForWidth(self.add_pixmap_for_green.sizePolicy().hasHeightForWidth())
        self.add_pixmap_for_green.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.add_pixmap_for_green, 17, 0, 1, 1)

        self.Load_meta_data_experiment_12 = QPushButton(self.groupBox_7)
        self.Load_meta_data_experiment_12.setObjectName(u"Load_meta_data_experiment_12")
        sizePolicy.setHeightForWidth(self.Load_meta_data_experiment_12.sizePolicy().hasHeightForWidth())
        self.Load_meta_data_experiment_12.setSizePolicy(sizePolicy)
        self.Load_meta_data_experiment_12.setMaximumSize(QSize(200, 30))

        self.gridLayout_9.addWidget(self.Load_meta_data_experiment_12, 1, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_27, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 2, 2, 2, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_39, 0, 0, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_40, 1, 0, 1, 1)

        self.meta_data_loading_1.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.meta_data_loading_1, 0, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.experiment_initialization_3, "")
        self.batch_communication_3 = QWidget()
        self.batch_communication_3.setObjectName(u"batch_communication_3")
        self.gridLayout_3 = QGridLayout(self.batch_communication_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.batch_communication_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.communication_access = QWidget()
        self.communication_access.setObjectName(u"communication_access")
        self.gridLayout_12 = QGridLayout(self.communication_access)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_24 = QLabel(self.communication_access)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(13)
        self.label_24.setFont(font)

        self.gridLayout_12.addWidget(self.label_24, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.communication_access)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.groupBox_21)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_40 = QLabel(self.groupBox_21)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_11.addWidget(self.label_40, 0, 0, 1, 2)

        self.label_41 = QLabel(self.groupBox_21)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_11.addWidget(self.label_41, 0, 2, 1, 1)

        self.label_42 = QLabel(self.groupBox_21)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_11.addWidget(self.label_42, 0, 3, 1, 1)

        self.sub_command1 = QTextEdit(self.groupBox_21)
        self.sub_command1.setObjectName(u"sub_command1")

        self.gridLayout_11.addWidget(self.sub_command1, 1, 0, 1, 2)

        self.receive_command1 = QTextEdit(self.groupBox_21)
        self.receive_command1.setObjectName(u"receive_command1")

        self.gridLayout_11.addWidget(self.receive_command1, 1, 2, 1, 1)

        self.response_command_1 = QTextEdit(self.groupBox_21)
        self.response_command_1.setObjectName(u"response_command_1")

        self.gridLayout_11.addWidget(self.response_command_1, 1, 3, 1, 1)

        self.button_submit_command = QPushButton(self.groupBox_21)
        self.button_submit_command.setObjectName(u"button_submit_command")
        sizePolicy.setHeightForWidth(self.button_submit_command.sizePolicy().hasHeightForWidth())
        self.button_submit_command.setSizePolicy(sizePolicy)
        self.button_submit_command.setMaximumSize(QSize(200, 20))

        self.gridLayout_11.addWidget(self.button_submit_command, 2, 0, 1, 1)

        self.button_clear_window = QPushButton(self.groupBox_21)
        self.button_clear_window.setObjectName(u"button_clear_window")
        sizePolicy.setHeightForWidth(self.button_clear_window.sizePolicy().hasHeightForWidth())
        self.button_clear_window.setSizePolicy(sizePolicy)
        self.button_clear_window.setMaximumSize(QSize(200, 20))

        self.gridLayout_11.addWidget(self.button_clear_window, 2, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.button_batch_2 = QPushButton(self.communication_access)
        self.button_batch_2.setObjectName(u"button_batch_2")
        sizePolicy.setHeightForWidth(self.button_batch_2.sizePolicy().hasHeightForWidth())
        self.button_batch_2.setSizePolicy(sizePolicy)
        self.button_batch_2.setMaximumSize(QSize(200, 20))

        self.gridLayout_12.addWidget(self.button_batch_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.communication_access)
        self.select_commands = QWidget()
        self.select_commands.setObjectName(u"select_commands")
        self.label_11 = QLabel(self.select_commands)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1280, 100, 47, 13))
        self.gridLayout_25 = QGridLayout(self.select_commands)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_19 = QGroupBox(self.select_commands)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_24 = QGridLayout(self.groupBox_19)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.scrollArea = QScrollArea(self.groupBox_19)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(250, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 248, 348))
        self.gridLayout_27 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.SeriesWidget = QListWidget(self.scrollAreaWidgetContents)
        self.SeriesWidget.setObjectName(u"SeriesWidget")

        self.gridLayout_27.addWidget(self.SeriesWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_24.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_19)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_24.addWidget(self.label_29, 2, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_19)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)

        self.gridLayout_24.addWidget(self.label_27, 0, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.groupBox_19)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(250, 350))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 248, 348))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.general_commands_labels = QListWidget(self.scrollAreaWidgetContents_3)
        self.general_commands_labels.setObjectName(u"general_commands_labels")

        self.gridLayout_26.addWidget(self.general_commands_labels, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_24.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_19)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)

        self.gridLayout_24.addWidget(self.label_28, 0, 1, 1, 1)

        self.label_32 = QLabel(self.groupBox_19)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.gridLayout_24.addWidget(self.label_32, 2, 0, 1, 1)

        self.scrollArea_4 = QScrollArea(self.groupBox_19)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(250, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 248, 237))
        self.gridLayout_29 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.SeriesWidget_2 = QListWidget(self.scrollAreaWidgetContents_4)
        self.SeriesWidget_2.setObjectName(u"SeriesWidget_2")

        self.gridLayout_29.addWidget(self.SeriesWidget_2, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_24.addWidget(self.scrollArea_4, 3, 1, 3, 1)

        self.scrollArea_2 = QScrollArea(self.groupBox_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(250, 450))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 248, 237))
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.protocol_widget = QListWidget(self.scrollAreaWidgetContents_2)
        self.protocol_widget.setObjectName(u"protocol_widget")

        self.gridLayout_28.addWidget(self.protocol_widget, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_24.addWidget(self.scrollArea_2, 3, 0, 3, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_19)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMaximumSize(QSize(16777215, 2000))
        self.gridLayout_30 = QGridLayout(self.groupBox_3)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setSizeConstraint(QLayout.SetNoConstraint)
        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_30.addWidget(self.label_26, 0, 2, 1, 1)

        self.listWidget = QListWidget(self.groupBox_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_30.addWidget(self.listWidget, 1, 0, 1, 1)

        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.label_12, 2, 0, 1, 1)

        self.cslow_qc = QLineEdit(self.groupBox_3)
        self.cslow_qc.setObjectName(u"cslow_qc")
        self.cslow_qc.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_31.addWidget(self.cslow_qc, 3, 0, 1, 1)

        self.rseries_qc = QLineEdit(self.groupBox_3)
        self.rseries_qc.setObjectName(u"rseries_qc")
        self.rseries_qc.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_31.addWidget(self.rseries_qc, 1, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.label_15, 0, 0, 1, 1)

        self.cfast_qc_2 = QLineEdit(self.groupBox_3)
        self.cfast_qc_2.setObjectName(u"cfast_qc_2")
        self.cfast_qc_2.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc_2, 5, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.label_13, 6, 0, 1, 1)

        self.cfast_qc = QLineEdit(self.groupBox_3)
        self.cfast_qc.setObjectName(u"cfast_qc")
        self.cfast_qc.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc, 7, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.label_14, 8, 0, 1, 1)


        self.gridLayout_30.addLayout(self.gridLayout_31, 2, 2, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_30.addWidget(self.label, 0, 0, 1, 1)

        self.pyqt_window = QGridLayout()
        self.pyqt_window.setObjectName(u"pyqt_window")

        self.gridLayout_30.addLayout(self.pyqt_window, 1, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_30.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.gridLayout_30.setRowStretch(0, 5)

        self.gridLayout_24.addWidget(self.groupBox_3, 0, 2, 6, 1)


        self.verticalLayout.addWidget(self.groupBox_19)


        self.gridLayout_25.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.select_commands)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.batch_communication_3, "")
        self.camera_3 = QWidget()
        self.camera_3.setObjectName(u"camera_3")
        self.gridLayout_10 = QGridLayout(self.camera_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox = QGroupBox(self.camera_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy5)
        self.groupBox.setMaximumSize(QSize(16777215, 450))
        self.gridLayout_14 = QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Camera_Live_Feed = QGraphicsView(self.groupBox)
        self.Camera_Live_Feed.setObjectName(u"Camera_Live_Feed")

        self.gridLayout_14.addWidget(self.Camera_Live_Feed, 0, 0, 1, 3)

        self.button_start_camera = QPushButton(self.groupBox)
        self.button_start_camera.setObjectName(u"button_start_camera")

        self.gridLayout_14.addWidget(self.button_start_camera, 1, 0, 1, 1)

        self.button_stop_camera = QPushButton(self.groupBox)
        self.button_stop_camera.setObjectName(u"button_stop_camera")

        self.gridLayout_14.addWidget(self.button_stop_camera, 1, 1, 1, 1)

        self.button_take_snapshot = QPushButton(self.groupBox)
        self.button_take_snapshot.setObjectName(u"button_take_snapshot")

        self.gridLayout_14.addWidget(self.button_take_snapshot, 1, 2, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.camera_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 450))
        self.gridLayout_15 = QGridLayout(self.groupBox_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.Taken_Snapshot = QGraphicsView(self.groupBox_2)
        self.Taken_Snapshot.setObjectName(u"Taken_Snapshot")

        self.gridLayout_15.addWidget(self.Taken_Snapshot, 0, 0, 1, 3)

        self.button_discard_snapshot = QPushButton(self.groupBox_2)
        self.button_discard_snapshot.setObjectName(u"button_discard_snapshot")

        self.gridLayout_15.addWidget(self.button_discard_snapshot, 1, 0, 1, 1)

        self.button_save_snapshot = QPushButton(self.groupBox_2)
        self.button_save_snapshot.setObjectName(u"button_save_snapshot")

        self.gridLayout_15.addWidget(self.button_save_snapshot, 1, 1, 1, 1)

        self.button_transfer_to_labbook = QPushButton(self.groupBox_2)
        self.button_transfer_to_labbook.setObjectName(u"button_transfer_to_labbook")

        self.gridLayout_15.addWidget(self.button_transfer_to_labbook, 1, 2, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.frame = QFrame(self.camera_3)
        self.frame.setObjectName(u"frame")
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setMinimumSize(QSize(0, 200))
        self.frame.setMaximumSize(QSize(16777215, 400))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: \"#232629\";\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_10.addWidget(self.frame, 1, 0, 2, 2)

        self.label_31 = QLabel(self.camera_3)
        self.label_31.setObjectName(u"label_31")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_31.setFont(font1)

        self.gridLayout_10.addWidget(self.label_31, 3, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.camera_3, "")

        self.gridLayout_23.addWidget(self.self_configuration_notebook, 0, 0, 1, 1)


        self.retranslateUi(Config_Widget)

        self.self_configuration_notebook.setCurrentIndex(0)
        self.meta_data_loading_1.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("Config_Widget", u"Cells", None))
        self.label_207.setText(QCoreApplication.translate("Config_Widget", u"License ID", None))
        self.label_209.setText(QCoreApplication.translate("Config_Widget", u"Passage #", None))
        self.label_208.setText(QCoreApplication.translate("Config_Widget", u"Cell line", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("Config_Widget", u"Compound", None))
        self.label_210.setText(QCoreApplication.translate("Config_Widget", u"Sample Code", None))
        self.label_211.setText(QCoreApplication.translate("Config_Widget", u"Lot #", None))
        self.label_212.setText(QCoreApplication.translate("Config_Widget", u"Salt Code", None))
        self.label_213.setText(QCoreApplication.translate("Config_Widget", u"Sample Id", None))
        self.label_214.setText(QCoreApplication.translate("Config_Widget", u"MW [Da]", None))
        self.label_215.setText(QCoreApplication.translate("Config_Widget", u"Weight [mg]", None))
        self.label_216.setText(QCoreApplication.translate("Config_Widget", u"Solvent", None))
        self.label_219.setText(QCoreApplication.translate("Config_Widget", u"Volumn [\u00b5L]", None))
        self.label_218.setText(QCoreApplication.translate("Config_Widget", u"Concentration [\u00b5M]", None))
        self.label_217.setText(QCoreApplication.translate("Config_Widget", u"Stocks [mM]", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Protocol", None))
        self.label_60.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.button_onl_analysis_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_pgf_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_59.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.button_protocol_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_61.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("Config_Widget", u"Staff", None))
        self.label_220.setText(QCoreApplication.translate("Config_Widget", u"Study director", None))
        self.label_221.setText(QCoreApplication.translate("Config_Widget", u"Technician", None))
        self.label_222.setText(QCoreApplication.translate("Config_Widget", u"Laboratory Code", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("Config_Widget", u"Archiving", None))
        self.label_227.setText(QCoreApplication.translate("Config_Widget", u"Model Code", None))
        self.label_228.setText(QCoreApplication.translate("Config_Widget", u"Project Code", None))
        self.label_229.setText(QCoreApplication.translate("Config_Widget", u"Study Code", None))
        self.label_230.setText(QCoreApplication.translate("Config_Widget", u"Data path", None))
        self.label_231.setText(QCoreApplication.translate("Config_Widget", u"File name template", None))
        self.label_62.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.button_batch_7.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication and open Communication Test Tool", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Config_Widget", u"Solutions", None))
        self.label_201.setText(QCoreApplication.translate("Config_Widget", u"EC Lot #", None))
        self.S1.setText("")
        self.label_199.setText(QCoreApplication.translate("Config_Widget", u"EC Type", None))
        self.label_200.setText(QCoreApplication.translate("Config_Widget", u"IC  Type", None))
        self.label_204.setText(QCoreApplication.translate("Config_Widget", u"F [ml/min]", None))
        self.label_205.setText(QCoreApplication.translate("Config_Widget", u"I [nm]", None))
        self.label_206.setText(QCoreApplication.translate("Config_Widget", u"e", None))
        self.label_202.setText(QCoreApplication.translate("Config_Widget", u"IC lot #", None))
        self.label_203.setText(QCoreApplication.translate("Config_Widget", u"T [\u00b0C]", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Metadata", None))
        self.label_9.setText(QCoreApplication.translate("Config_Widget", u" # of Cells patched", None))
        self.label_8.setText(QCoreApplication.translate("Config_Widget", u"Min # of Cells", None))
        self.label_6.setText(QCoreApplication.translate("Config_Widget", u"Experiment Type", None))
        self.label_7.setText(QCoreApplication.translate("Config_Widget", u"Cell Type", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Config_Widget", u"Extracelullar and intracellular solutions", None))
        self.label_243.setText(QCoreApplication.translate("Config_Widget", u"Extracellular Solution", None))
        self.ent_ph_set.setText(QCoreApplication.translate("Config_Widget", u"pH of External Solution", None))
        self.label_247.setText(QCoreApplication.translate("Config_Widget", u"Ph of internal solution", None))
        self.label_244.setText(QCoreApplication.translate("Config_Widget", u"Intracellular solution", None))
        self.label_245.setText(QCoreApplication.translate("Config_Widget", u"Date of Preparation ", None))
        self.ent_date_prep.setText("")
        self.groupBox_17.setTitle(QCoreApplication.translate("Config_Widget", u"Set Batch Communication Settings", None))
        self.label_4.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.button_batch_1.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Config_Widget", u"Patchmaster Setup Files", None))
        self.button_onl_analysis_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_3.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.button_protocol_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_pgf_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_5.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.label_2.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Config_Widget", u"Button ToolBar", None))
        self.database_save.setText(QCoreApplication.translate("Config_Widget", u"Save to Database", None))
        self.database_save_2.setText(QCoreApplication.translate("Config_Widget", u"Delete Form", None))
        self.add_pixmap_for_green.setText(QCoreApplication.translate("Config_Widget", u"Connected...", None))
        self.Load_meta_data_experiment_12.setText(QCoreApplication.translate("Config_Widget", u"Load Form", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.experiment_initialization_3), QCoreApplication.translate("Config_Widget", u"Tab 1", None))
        self.label_24.setText(QCoreApplication.translate("Config_Widget", u"Test Patchmaster Batch Communication", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Config_Widget", u"Test the Connection to the Patchmaster", None))
        self.label_40.setText(QCoreApplication.translate("Config_Widget", u"Submit your Commands", None))
        self.label_41.setText(QCoreApplication.translate("Config_Widget", u"Control File received", None))
        self.label_42.setText(QCoreApplication.translate("Config_Widget", u"Batch Communication Response", None))
        self.button_submit_command.setText(QCoreApplication.translate("Config_Widget", u"Submit Command", None))
        self.button_clear_window.setText(QCoreApplication.translate("Config_Widget", u"Stop Submitting", None))
        self.button_batch_2.setText(QCoreApplication.translate("Config_Widget", u"Setup Experiment", None))
        self.label_11.setText("")
        self.groupBox_19.setTitle(QCoreApplication.translate("Config_Widget", u"Protocol Editor", None))
        self.label_29.setText(QCoreApplication.translate("Config_Widget", u"Dragable QC-Checks", None))
        self.label_27.setText(QCoreApplication.translate("Config_Widget", u"Dragable Labels", None))
        self.label_28.setText(QCoreApplication.translate("Config_Widget", u"Dragable Executable Series", None))
        self.label_32.setText(QCoreApplication.translate("Config_Widget", u"Dragable Protocols", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Config_Widget", u"Final Sequence", None))
        self.label_26.setText(QCoreApplication.translate("Config_Widget", u"Notebook Online Analysis:", None))
        self.label_12.setText(QCoreApplication.translate("Config_Widget", u"Rseries", None))
        self.label_15.setText(QCoreApplication.translate("Config_Widget", u"Quality Metrics", None))
        self.label_13.setText(QCoreApplication.translate("Config_Widget", u"Cfast", None))
        self.label_10.setText(QCoreApplication.translate("Config_Widget", u"Cslow", None))
        self.label_14.setText(QCoreApplication.translate("Config_Widget", u"Cell", None))
        self.label.setText(QCoreApplication.translate("Config_Widget", u"Final Patch Clamping Sequence:", None))
        self.pushButton_10.setText(QCoreApplication.translate("Config_Widget", u"Clear Sequences", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.batch_communication_3), QCoreApplication.translate("Config_Widget", u"Tab 2", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config_Widget", u"Live Camera Feed", None))
        self.button_start_camera.setText(QCoreApplication.translate("Config_Widget", u"Start Camera", None))
        self.button_stop_camera.setText(QCoreApplication.translate("Config_Widget", u"Stop Camera", None))
        self.button_take_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Take Snapshot", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config_Widget", u"Snapshot Overview", None))
        self.button_discard_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Discard Snapshot", None))
        self.button_save_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Save Snapshot", None))
        self.button_transfer_to_labbook.setText(QCoreApplication.translate("Config_Widget", u"Transfer to Labbook", None))
        self.label_31.setText(QCoreApplication.translate("Config_Widget", u"Image Galery:", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.camera_3), QCoreApplication.translate("Config_Widget", u"Seite", None))
    # retranslateUi

