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
from dropable_list_view import *


class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(1729, 1035)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Config_Widget.sizePolicy().hasHeightForWidth())
        Config_Widget.setSizePolicy(sizePolicy)
        self.Notebook_2 = QTabWidget(Config_Widget)
        self.Notebook_2.setObjectName(u"Notebook_2")
        self.Notebook_2.setGeometry(QRect(9, 9, 1651, 840))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Notebook_2.sizePolicy().hasHeightForWidth())
        self.Notebook_2.setSizePolicy(sizePolicy1)
        self.Notebook_2.setTabShape(QTabWidget.Rounded)
        self.experiment_initialization_3 = QWidget()
        self.experiment_initialization_3.setObjectName(u"experiment_initialization_3")
        self.gridLayout = QGridLayout(self.experiment_initialization_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.meta_data_loading_1 = QStackedWidget(self.experiment_initialization_3)
        self.meta_data_loading_1.setObjectName(u"meta_data_loading_1")
        sizePolicy.setHeightForWidth(self.meta_data_loading_1.sizePolicy().hasHeightForWidth())
        self.meta_data_loading_1.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.groupBox_22 = QGroupBox(self.page)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.gridLayout_18 = QGridLayout(self.groupBox_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.S5 = QLineEdit(self.groupBox_22)
        self.S5.setObjectName(u"S5")

        self.gridLayout_18.addWidget(self.S5, 12, 2, 1, 1)

        self.S6 = QLineEdit(self.groupBox_22)
        self.S6.setObjectName(u"S6")

        self.gridLayout_18.addWidget(self.S6, 12, 3, 1, 1)

        self.So_com1 = QComboBox(self.groupBox_22)
        self.So_com1.setObjectName(u"So_com1")

        self.gridLayout_18.addWidget(self.So_com1, 1, 0, 1, 4)

        self.S2 = QLineEdit(self.groupBox_22)
        self.S2.setObjectName(u"S2")

        self.gridLayout_18.addWidget(self.S2, 9, 2, 1, 2)

        self.S4 = QLineEdit(self.groupBox_22)
        self.S4.setObjectName(u"S4")

        self.gridLayout_18.addWidget(self.S4, 12, 1, 1, 1)

        self.S3 = QLineEdit(self.groupBox_22)
        self.S3.setObjectName(u"S3")

        self.gridLayout_18.addWidget(self.S3, 12, 0, 1, 1)

        self.label_199 = QLabel(self.groupBox_22)
        self.label_199.setObjectName(u"label_199")
        sizePolicy1.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_199, 2, 0, 1, 1)

        self.label_200 = QLabel(self.groupBox_22)
        self.label_200.setObjectName(u"label_200")
        sizePolicy1.setHeightForWidth(self.label_200.sizePolicy().hasHeightForWidth())
        self.label_200.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_200, 6, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer, 14, 0, 1, 1)

        self.So_com2 = QComboBox(self.groupBox_22)
        self.So_com2.setObjectName(u"So_com2")

        self.gridLayout_18.addWidget(self.So_com2, 5, 0, 1, 4)

        self.S1 = QLineEdit(self.groupBox_22)
        self.S1.setObjectName(u"S1")

        self.gridLayout_18.addWidget(self.S1, 9, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 8, 0, 1, 1)

        self.label_203 = QLabel(self.groupBox_22)
        self.label_203.setObjectName(u"label_203")
        sizePolicy1.setHeightForWidth(self.label_203.sizePolicy().hasHeightForWidth())
        self.label_203.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_203, 13, 0, 1, 1)

        self.label_202 = QLabel(self.groupBox_22)
        self.label_202.setObjectName(u"label_202")
        sizePolicy1.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_202, 10, 2, 1, 1)

        self.label_206 = QLabel(self.groupBox_22)
        self.label_206.setObjectName(u"label_206")
        sizePolicy1.setHeightForWidth(self.label_206.sizePolicy().hasHeightForWidth())
        self.label_206.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_206, 13, 3, 1, 1)

        self.label_205 = QLabel(self.groupBox_22)
        self.label_205.setObjectName(u"label_205")
        sizePolicy1.setHeightForWidth(self.label_205.sizePolicy().hasHeightForWidth())
        self.label_205.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_205, 13, 2, 1, 1)

        self.label_201 = QLabel(self.groupBox_22)
        self.label_201.setObjectName(u"label_201")
        sizePolicy1.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_201, 10, 0, 1, 1)

        self.label_204 = QLabel(self.groupBox_22)
        self.label_204.setObjectName(u"label_204")
        sizePolicy1.setHeightForWidth(self.label_204.sizePolicy().hasHeightForWidth())
        self.label_204.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.label_204, 13, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_5, 11, 0, 1, 1)


        self.gridLayout_28.addWidget(self.groupBox_22, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_28)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.groupBox_30 = QGroupBox(self.page)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_20 = QGridLayout(self.groupBox_30)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_7, 9, 0, 1, 1)

        self.label_208 = QLabel(self.groupBox_30)
        self.label_208.setObjectName(u"label_208")
        sizePolicy1.setHeightForWidth(self.label_208.sizePolicy().hasHeightForWidth())
        self.label_208.setSizePolicy(sizePolicy1)

        self.gridLayout_20.addWidget(self.label_208, 5, 0, 1, 1)

        self.label_209 = QLabel(self.groupBox_30)
        self.label_209.setObjectName(u"label_209")
        sizePolicy1.setHeightForWidth(self.label_209.sizePolicy().hasHeightForWidth())
        self.label_209.setSizePolicy(sizePolicy1)

        self.gridLayout_20.addWidget(self.label_209, 8, 0, 1, 1)

        self.label_207 = QLabel(self.groupBox_30)
        self.label_207.setObjectName(u"label_207")
        sizePolicy1.setHeightForWidth(self.label_207.sizePolicy().hasHeightForWidth())
        self.label_207.setSizePolicy(sizePolicy1)

        self.gridLayout_20.addWidget(self.label_207, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_8, 6, 0, 1, 1)

        self.Ce_com1 = QComboBox(self.groupBox_30)
        self.Ce_com1.setObjectName(u"Ce_com1")

        self.gridLayout_20.addWidget(self.Ce_com1, 1, 0, 1, 1)

        self.Ce1 = QLineEdit(self.groupBox_30)
        self.Ce1.setObjectName(u"Ce1")

        self.gridLayout_20.addWidget(self.Ce1, 7, 0, 1, 1)

        self.Ce_com2 = QComboBox(self.groupBox_30)
        self.Ce_com2.setObjectName(u"Ce_com2")

        self.gridLayout_20.addWidget(self.Ce_com2, 4, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_9, 3, 0, 1, 1)


        self.gridLayout_29.addWidget(self.groupBox_30, 0, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_29)

        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.groupBox_31 = QGroupBox(self.page)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.gridLayout_19 = QGridLayout(self.groupBox_31)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_13, 6, 0, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_12, 3, 0, 1, 1)

        self.label_214 = QLabel(self.groupBox_31)
        self.label_214.setObjectName(u"label_214")
        sizePolicy1.setHeightForWidth(self.label_214.sizePolicy().hasHeightForWidth())
        self.label_214.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_214, 5, 1, 1, 1)

        self.label_213 = QLabel(self.groupBox_31)
        self.label_213.setObjectName(u"label_213")
        sizePolicy1.setHeightForWidth(self.label_213.sizePolicy().hasHeightForWidth())
        self.label_213.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_213, 5, 0, 1, 1)

        self.label_215 = QLabel(self.groupBox_31)
        self.label_215.setObjectName(u"label_215")
        sizePolicy1.setHeightForWidth(self.label_215.sizePolicy().hasHeightForWidth())
        self.label_215.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_215, 8, 0, 1, 1)

        self.label_219 = QLabel(self.groupBox_31)
        self.label_219.setObjectName(u"label_219")
        sizePolicy1.setHeightForWidth(self.label_219.sizePolicy().hasHeightForWidth())
        self.label_219.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_219, 8, 3, 1, 1)

        self.label_211 = QLabel(self.groupBox_31)
        self.label_211.setObjectName(u"label_211")
        sizePolicy1.setHeightForWidth(self.label_211.sizePolicy().hasHeightForWidth())
        self.label_211.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_211, 2, 1, 1, 1)

        self.label_216 = QLabel(self.groupBox_31)
        self.label_216.setObjectName(u"label_216")
        sizePolicy1.setHeightForWidth(self.label_216.sizePolicy().hasHeightForWidth())
        self.label_216.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_216, 8, 1, 1, 1)

        self.label_212 = QLabel(self.groupBox_31)
        self.label_212.setObjectName(u"label_212")
        sizePolicy1.setHeightForWidth(self.label_212.sizePolicy().hasHeightForWidth())
        self.label_212.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_212, 2, 3, 1, 1)

        self.label_210 = QLabel(self.groupBox_31)
        self.label_210.setObjectName(u"label_210")
        sizePolicy1.setHeightForWidth(self.label_210.sizePolicy().hasHeightForWidth())
        self.label_210.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_210, 2, 0, 1, 1)

        self.C4 = QLineEdit(self.groupBox_31)
        self.C4.setObjectName(u"C4")

        self.gridLayout_19.addWidget(self.C4, 4, 1, 1, 2)

        self.C2 = QLineEdit(self.groupBox_31)
        self.C2.setObjectName(u"C2")

        self.gridLayout_19.addWidget(self.C2, 1, 1, 1, 2)

        self.Co_com1 = QComboBox(self.groupBox_31)
        self.Co_com1.setObjectName(u"Co_com1")

        self.gridLayout_19.addWidget(self.Co_com1, 1, 3, 1, 1)

        self.C1 = QLineEdit(self.groupBox_31)
        self.C1.setObjectName(u"C1")

        self.gridLayout_19.addWidget(self.C1, 1, 0, 1, 1)

        self.C3 = QLineEdit(self.groupBox_31)
        self.C3.setObjectName(u"C3")

        self.gridLayout_19.addWidget(self.C3, 4, 0, 1, 1)

        self.C6_2 = QLineEdit(self.groupBox_31)
        self.C6_2.setObjectName(u"C6_2")

        self.gridLayout_19.addWidget(self.C6_2, 7, 3, 1, 1)

        self.C5 = QLineEdit(self.groupBox_31)
        self.C5.setObjectName(u"C5")

        self.gridLayout_19.addWidget(self.C5, 7, 0, 1, 1)

        self.C6 = QLineEdit(self.groupBox_31)
        self.C6.setObjectName(u"C6")

        self.gridLayout_19.addWidget(self.C6, 7, 1, 1, 2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_14, 9, 0, 1, 1)

        self.C8 = QLineEdit(self.groupBox_31)
        self.C8.setObjectName(u"C8")

        self.gridLayout_19.addWidget(self.C8, 10, 0, 1, 1)

        self.label_217 = QLabel(self.groupBox_31)
        self.label_217.setObjectName(u"label_217")

        self.gridLayout_19.addWidget(self.label_217, 11, 0, 1, 1)

        self.C9 = QLineEdit(self.groupBox_31)
        self.C9.setObjectName(u"C9")

        self.gridLayout_19.addWidget(self.C9, 10, 1, 1, 1)

        self.label_218 = QLabel(self.groupBox_31)
        self.label_218.setObjectName(u"label_218")
        sizePolicy1.setHeightForWidth(self.label_218.sizePolicy().hasHeightForWidth())
        self.label_218.setSizePolicy(sizePolicy1)

        self.gridLayout_19.addWidget(self.label_218, 11, 1, 1, 1)


        self.gridLayout_30.addWidget(self.groupBox_31, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_30.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_30)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.groupBox_32 = QGroupBox(self.page)
        self.groupBox_32.setObjectName(u"groupBox_32")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_32.sizePolicy().hasHeightForWidth())
        self.groupBox_32.setSizePolicy(sizePolicy2)
        self.gridLayout_21 = QGridLayout(self.groupBox_32)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_220 = QLabel(self.groupBox_32)
        self.label_220.setObjectName(u"label_220")

        self.gridLayout_21.addWidget(self.label_220, 3, 0, 1, 1)

        self.label_222 = QLabel(self.groupBox_32)
        self.label_222.setObjectName(u"label_222")

        self.gridLayout_21.addWidget(self.label_222, 9, 0, 1, 1)

        self.label_221 = QLabel(self.groupBox_32)
        self.label_221.setObjectName(u"label_221")

        self.gridLayout_21.addWidget(self.label_221, 6, 0, 1, 1)

        self.St_com1 = QComboBox(self.groupBox_32)
        self.St_com1.setObjectName(u"St_com1")

        self.gridLayout_21.addWidget(self.St_com1, 2, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_19, 4, 0, 1, 1)

        self.St_com2 = QComboBox(self.groupBox_32)
        self.St_com2.setObjectName(u"St_com2")

        self.gridLayout_21.addWidget(self.St_com2, 5, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_15, 0, 0, 1, 1)

        self.St_com3 = QComboBox(self.groupBox_32)
        self.St_com3.setObjectName(u"St_com3")

        self.gridLayout_21.addWidget(self.St_com3, 8, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_16, 11, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_17, 10, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_18, 1, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_20, 7, 0, 1, 1)


        self.gridLayout_31.addWidget(self.groupBox_32, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_31)

        self.gridLayout_32 = QGridLayout()
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.groupBox_33 = QGroupBox(self.page)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.gridLayout_22 = QGridLayout(self.groupBox_33)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_25, 4, 0, 1, 1)

        self.protocol_file_set_3 = QLineEdit(self.groupBox_33)
        self.protocol_file_set_3.setObjectName(u"protocol_file_set_3")

        self.gridLayout_22.addWidget(self.protocol_file_set_3, 5, 0, 1, 1)

        self.button_pgf_set_3 = QPushButton(self.groupBox_33)
        self.button_pgf_set_3.setObjectName(u"button_pgf_set_3")

        self.gridLayout_22.addWidget(self.button_pgf_set_3, 2, 1, 1, 1)

        self.button_protocol_set_3 = QPushButton(self.groupBox_33)
        self.button_protocol_set_3.setObjectName(u"button_protocol_set_3")

        self.gridLayout_22.addWidget(self.button_protocol_set_3, 5, 1, 1, 1)

        self.pg_file_set_3 = QLineEdit(self.groupBox_33)
        self.pg_file_set_3.setObjectName(u"pg_file_set_3")

        self.gridLayout_22.addWidget(self.pg_file_set_3, 2, 0, 1, 1)

        self.button_onl_analysis_set_3 = QPushButton(self.groupBox_33)
        self.button_onl_analysis_set_3.setObjectName(u"button_onl_analysis_set_3")

        self.gridLayout_22.addWidget(self.button_onl_analysis_set_3, 8, 1, 1, 1)

        self.label_59 = QLabel(self.groupBox_33)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_22.addWidget(self.label_59, 3, 0, 1, 1)

        self.online_analysis_file_set_3 = QLineEdit(self.groupBox_33)
        self.online_analysis_file_set_3.setObjectName(u"online_analysis_file_set_3")

        self.gridLayout_22.addWidget(self.online_analysis_file_set_3, 8, 0, 1, 1)

        self.label_61 = QLabel(self.groupBox_33)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_22.addWidget(self.label_61, 6, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_33)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_22.addWidget(self.label_60, 9, 0, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_21, 0, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_22, 11, 0, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_24, 1, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_23, 10, 0, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_26, 7, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_33, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_32)

        self.gridLayout_33 = QGridLayout()
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.groupBox_34 = QGroupBox(self.page)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.gridLayout_23 = QGridLayout(self.groupBox_34)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_29, 3, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_30, 6, 0, 1, 1)

        self.A_com1 = QComboBox(self.groupBox_34)
        self.A_com1.setObjectName(u"A_com1")

        self.gridLayout_23.addWidget(self.A_com1, 1, 0, 1, 2)

        self.A1 = QLineEdit(self.groupBox_34)
        self.A1.setObjectName(u"A1")

        self.gridLayout_23.addWidget(self.A1, 1, 3, 1, 1)

        self.label_227 = QLabel(self.groupBox_34)
        self.label_227.setObjectName(u"label_227")

        self.gridLayout_23.addWidget(self.label_227, 2, 0, 1, 1)

        self.label_230 = QLabel(self.groupBox_34)
        self.label_230.setObjectName(u"label_230")

        self.gridLayout_23.addWidget(self.label_230, 5, 0, 1, 1)

        self.label_231 = QLabel(self.groupBox_34)
        self.label_231.setObjectName(u"label_231")

        self.gridLayout_23.addWidget(self.label_231, 5, 2, 1, 1)

        self.Batch1_4 = QLineEdit(self.groupBox_34)
        self.Batch1_4.setObjectName(u"Batch1_4")

        self.gridLayout_23.addWidget(self.Batch1_4, 7, 0, 1, 4)

        self.A_com3 = QComboBox(self.groupBox_34)
        self.A_com3.setObjectName(u"A_com3")

        self.gridLayout_23.addWidget(self.A_com3, 4, 0, 1, 2)

        self.A_com2 = QComboBox(self.groupBox_34)
        self.A_com2.setObjectName(u"A_com2")

        self.gridLayout_23.addWidget(self.A_com2, 1, 2, 1, 1)

        self.label_229 = QLabel(self.groupBox_34)
        self.label_229.setObjectName(u"label_229")

        self.gridLayout_23.addWidget(self.label_229, 2, 3, 1, 1)

        self.A2 = QLineEdit(self.groupBox_34)
        self.A2.setObjectName(u"A2")

        self.gridLayout_23.addWidget(self.A2, 4, 2, 1, 2)

        self.label_228 = QLabel(self.groupBox_34)
        self.label_228.setObjectName(u"label_228")

        self.gridLayout_23.addWidget(self.label_228, 2, 2, 1, 1)

        self.label_62 = QLabel(self.groupBox_34)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_23.addWidget(self.label_62, 8, 0, 1, 2)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_31, 9, 0, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_28, 10, 1, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_27, 0, 0, 1, 1)

        self.button_batch_7 = QPushButton(self.groupBox_34)
        self.button_batch_7.setObjectName(u"button_batch_7")

        self.gridLayout_23.addWidget(self.button_batch_7, 9, 1, 1, 2)


        self.gridLayout_33.addWidget(self.groupBox_34, 0, 0, 1, 1)


        self.horizontalLayout_14.addLayout(self.gridLayout_33)


        self.gridLayout_3.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)

        self.meta_data_loading_1.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_9 = QGridLayout(self.page_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_17 = QGroupBox(self.page_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.gridLayout_17 = QGridLayout(self.groupBox_17)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.Batch1 = QLineEdit(self.groupBox_17)
        self.Batch1.setObjectName(u"Batch1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Batch1.sizePolicy().hasHeightForWidth())
        self.Batch1.setSizePolicy(sizePolicy3)

        self.gridLayout_17.addWidget(self.Batch1, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_17)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_53, 4, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_52, 8, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_7, 7, 1, 1, 1)

        self.button_batch_1 = QPushButton(self.groupBox_17)
        self.button_batch_1.setObjectName(u"button_batch_1")
        sizePolicy1.setHeightForWidth(self.button_batch_1.sizePolicy().hasHeightForWidth())
        self.button_batch_1.setSizePolicy(sizePolicy1)

        self.gridLayout_17.addWidget(self.button_batch_1, 8, 1, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_54, 1, 0, 1, 1)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_55, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_17, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_11 = QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_46, 9, 0, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_47, 0, 0, 1, 1)

        self.pg_file_set = QLineEdit(self.groupBox_4)
        self.pg_file_set.setObjectName(u"pg_file_set")

        self.gridLayout_11.addWidget(self.pg_file_set, 1, 0, 1, 1)

        self.button_pgf_set = QPushButton(self.groupBox_4)
        self.button_pgf_set.setObjectName(u"button_pgf_set")

        self.gridLayout_11.addWidget(self.button_pgf_set, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.label_2, 2, 0, 1, 1)

        self.button_protocol_set = QPushButton(self.groupBox_4)
        self.button_protocol_set.setObjectName(u"button_protocol_set")

        self.gridLayout_11.addWidget(self.button_protocol_set, 4, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.label_3, 5, 0, 1, 1)

        self.protocol_file_set = QLineEdit(self.groupBox_4)
        self.protocol_file_set.setObjectName(u"protocol_file_set")

        self.gridLayout_11.addWidget(self.protocol_file_set, 4, 0, 1, 1)

        self.online_analysis_file_set = QLineEdit(self.groupBox_4)
        self.online_analysis_file_set.setObjectName(u"online_analysis_file_set")

        self.gridLayout_11.addWidget(self.online_analysis_file_set, 7, 0, 1, 1)

        self.button_onl_analysis_set = QPushButton(self.groupBox_4)
        self.button_onl_analysis_set.setObjectName(u"button_onl_analysis_set")

        self.gridLayout_11.addWidget(self.button_onl_analysis_set, 7, 1, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_48, 3, 0, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_49, 6, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_23 = QGroupBox(self.page_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        self.gridLayout_13 = QGridLayout(self.groupBox_23)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_42, 9, 2, 1, 1)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_43, 0, 1, 1, 1)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_44, 3, 1, 1, 1)

        self.label_247 = QLabel(self.groupBox_23)
        self.label_247.setObjectName(u"label_247")
        sizePolicy1.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.label_247, 8, 3, 1, 1)

        self.label_245 = QLabel(self.groupBox_23)
        self.label_245.setObjectName(u"label_245")
        sizePolicy1.setHeightForWidth(self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.label_245, 8, 0, 1, 1)

        self.S2_3 = QLineEdit(self.groupBox_23)
        self.S2_3.setObjectName(u"S2_3")

        self.gridLayout_13.addWidget(self.S2_3, 7, 2, 1, 1)

        self.ent_ph_set = QLabel(self.groupBox_23)
        self.ent_ph_set.setObjectName(u"ent_ph_set")
        sizePolicy1.setHeightForWidth(self.ent_ph_set.sizePolicy().hasHeightForWidth())
        self.ent_ph_set.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.ent_ph_set, 8, 2, 1, 1)

        self.ent_ph_int_set = QLineEdit(self.groupBox_23)
        self.ent_ph_int_set.setObjectName(u"ent_ph_int_set")

        self.gridLayout_13.addWidget(self.ent_ph_int_set, 7, 3, 1, 1)

        self.extracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.extracellular_sol_com_1.setObjectName(u"extracellular_sol_com_1")

        self.gridLayout_13.addWidget(self.extracellular_sol_com_1, 1, 1, 1, 3)

        self.label_243 = QLabel(self.groupBox_23)
        self.label_243.setObjectName(u"label_243")
        sizePolicy1.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.label_243, 2, 1, 1, 2)

        self.Intracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.Intracellular_sol_com_1.setObjectName(u"Intracellular_sol_com_1")

        self.gridLayout_13.addWidget(self.Intracellular_sol_com_1, 4, 1, 1, 3)

        self.label_244 = QLabel(self.groupBox_23)
        self.label_244.setObjectName(u"label_244")
        sizePolicy1.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy1)

        self.gridLayout_13.addWidget(self.label_244, 5, 1, 1, 2)

        self.ent_date_prep = QLineEdit(self.groupBox_23)
        self.ent_date_prep.setObjectName(u"ent_date_prep")

        self.gridLayout_13.addWidget(self.ent_date_prep, 7, 0, 1, 2)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_45, 6, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_23, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.gridLayout_12 = QGridLayout(self.groupBox_6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.experiment_type_desc = QLineEdit(self.groupBox_6)
        self.experiment_type_desc.setObjectName(u"experiment_type_desc")

        self.gridLayout_12.addWidget(self.experiment_type_desc, 1, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_12.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_12.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_12.addWidget(self.label_9, 6, 1, 1, 1)

        self.patched_cells = QLineEdit(self.groupBox_6)
        self.patched_cells.setObjectName(u"patched_cells")

        self.gridLayout_12.addWidget(self.patched_cells, 5, 1, 1, 1)

        self.min_number_cells = QLineEdit(self.groupBox_6)
        self.min_number_cells.setObjectName(u"min_number_cells")

        self.gridLayout_12.addWidget(self.min_number_cells, 5, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_12.addWidget(self.label_8, 6, 0, 1, 1)

        self.cell_type_desc = QLineEdit(self.groupBox_6)
        self.cell_type_desc.setObjectName(u"cell_type_desc")

        self.gridLayout_12.addWidget(self.cell_type_desc, 3, 0, 1, 2)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_50, 0, 0, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_51, 7, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_6, 1, 0, 1, 1)

        self.meta_data_loading_1.addWidget(self.page_2)

        self.gridLayout.addWidget(self.meta_data_loading_1, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.experiment_initialization_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setMinimumSize(QSize(200, 0))
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(9, 9, -1, -1)
        self.Load_meta_data_experiment_12 = QPushButton(self.groupBox_7)
        self.Load_meta_data_experiment_12.setObjectName(u"Load_meta_data_experiment_12")
        sizePolicy.setHeightForWidth(self.Load_meta_data_experiment_12.sizePolicy().hasHeightForWidth())
        self.Load_meta_data_experiment_12.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.Load_meta_data_experiment_12, 0, 0, 1, 1)

        self.database_save = QPushButton(self.groupBox_7)
        self.database_save.setObjectName(u"database_save")
        sizePolicy.setHeightForWidth(self.database_save.sizePolicy().hasHeightForWidth())
        self.database_save.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.database_save, 1, 0, 1, 1)

        self.database_save_2 = QPushButton(self.groupBox_7)
        self.database_save_2.setObjectName(u"database_save_2")
        sizePolicy.setHeightForWidth(self.database_save_2.sizePolicy().hasHeightForWidth())
        self.database_save_2.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.database_save_2, 2, 0, 1, 1)

        self.add_pixmap_for_green = QLabel(self.groupBox_7)
        self.add_pixmap_for_green.setObjectName(u"add_pixmap_for_green")

        self.gridLayout_10.addWidget(self.add_pixmap_for_green, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 0, 2, 1, 1)

        self.Notebook_2.addTab(self.experiment_initialization_3, "")
        self.batch_communication_3 = QWidget()
        self.batch_communication_3.setObjectName(u"batch_communication_3")
        self.gridLayout_2 = QGridLayout(self.batch_communication_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.batch_communication_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.communication_access = QWidget()
        self.communication_access.setObjectName(u"communication_access")
        self.gridLayout_4 = QGridLayout(self.communication_access)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_24 = QLabel(self.communication_access)
        self.label_24.setObjectName(u"label_24")
        sizePolicy1.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"HoloLens MDL2 Assets"])
        font.setPointSize(13)
        self.label_24.setFont(font)

        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.communication_access)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.groupBox_21)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.button_submit_command = QPushButton(self.groupBox_21)
        self.button_submit_command.setObjectName(u"button_submit_command")
        sizePolicy1.setHeightForWidth(self.button_submit_command.sizePolicy().hasHeightForWidth())
        self.button_submit_command.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.button_submit_command, 2, 3, 1, 1)

        self.button_clear_window = QPushButton(self.groupBox_21)
        self.button_clear_window.setObjectName(u"button_clear_window")
        sizePolicy1.setHeightForWidth(self.button_clear_window.sizePolicy().hasHeightForWidth())
        self.button_clear_window.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.button_clear_window, 3, 3, 1, 1)

        self.response_command_1 = QTextEdit(self.groupBox_21)
        self.response_command_1.setObjectName(u"response_command_1")
        sizePolicy.setHeightForWidth(self.response_command_1.sizePolicy().hasHeightForWidth())
        self.response_command_1.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.response_command_1, 1, 13, 1, 1)

        self.label_41 = QLabel(self.groupBox_21)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_8.addWidget(self.label_41, 0, 9, 1, 1)

        self.label_42 = QLabel(self.groupBox_21)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_8.addWidget(self.label_42, 0, 13, 1, 1)

        self.label_40 = QLabel(self.groupBox_21)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_8.addWidget(self.label_40, 0, 3, 1, 1)

        self.receive_command1 = QTextEdit(self.groupBox_21)
        self.receive_command1.setObjectName(u"receive_command1")
        sizePolicy.setHeightForWidth(self.receive_command1.sizePolicy().hasHeightForWidth())
        self.receive_command1.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.receive_command1, 1, 9, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 1, 6, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 1, 10, 1, 1)

        self.sub_command1 = QTextEdit(self.groupBox_21)
        self.sub_command1.setObjectName(u"sub_command1")
        sizePolicy.setHeightForWidth(self.sub_command1.sizePolicy().hasHeightForWidth())
        self.sub_command1.setSizePolicy(sizePolicy)

        self.gridLayout_8.addWidget(self.sub_command1, 1, 3, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 1, 12, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 1, 11, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 7, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.button_batch_2 = QPushButton(self.communication_access)
        self.button_batch_2.setObjectName(u"button_batch_2")
        sizePolicy1.setHeightForWidth(self.button_batch_2.sizePolicy().hasHeightForWidth())
        self.button_batch_2.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.button_batch_2, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.communication_access)
        self.select_commands = QWidget()
        self.select_commands.setObjectName(u"select_commands")
        self.gridLayout_15 = QGridLayout(self.select_commands)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_11 = QLabel(self.select_commands)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_15.addWidget(self.label_11, 2, 2, 1, 1)

        self.groupBox_19 = QGroupBox(self.select_commands)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.gridLayout_14 = QGridLayout(self.groupBox_19)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_16 = QLabel(self.groupBox_19)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.label_16.setFont(font1)

        self.verticalLayout.addWidget(self.label_16)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_34)

        self.pushButton_3 = QPushButton(self.groupBox_19)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_40)

        self.pushButton_4 = QPushButton(self.groupBox_19)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_41)

        self.pushButton_2 = QPushButton(self.groupBox_19)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_35)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_37)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_38)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_39)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_36)


        self.gridLayout_14.addLayout(self.verticalLayout, 1, 6, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_19)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_14.addWidget(self.pushButton_10, 8, 2, 1, 1)

        self.pyqt_window = QGridLayout()
        self.pyqt_window.setObjectName(u"pyqt_window")

        self.gridLayout_14.addLayout(self.pyqt_window, 1, 3, 1, 3)

        self.cfast_qc_2 = QLineEdit(self.groupBox_19)
        self.cfast_qc_2.setObjectName(u"cfast_qc_2")

        self.gridLayout_14.addWidget(self.cfast_qc_2, 3, 6, 1, 1)

        self.label_12 = QLabel(self.groupBox_19)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_12, 4, 3, 1, 1)

        self.cslow_qc = QLineEdit(self.groupBox_19)
        self.cslow_qc.setObjectName(u"cslow_qc")

        self.gridLayout_14.addWidget(self.cslow_qc, 3, 5, 1, 1)

        self.rseries_qc = QLineEdit(self.groupBox_19)
        self.rseries_qc.setObjectName(u"rseries_qc")

        self.gridLayout_14.addWidget(self.rseries_qc, 3, 3, 1, 1)

        self.scrollArea = QScrollArea(self.groupBox_19)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(240, 350))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 238, 348))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.SeriesWidget = ListView(self.scrollAreaWidgetContents)
        self.SeriesWidget.setObjectName(u"SeriesWidget")
        self.SeriesWidget.setGeometry(QRect(0, 0, 241, 601))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_14.addWidget(self.scrollArea, 1, 1, 1, 1)

        self.listWidget = ListView(self.groupBox_19)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_14.addWidget(self.listWidget, 1, 2, 7, 1)

        self.label = QLabel(self.groupBox_19)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label, 0, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_19)
        self.label_26.setObjectName(u"label_26")
        sizePolicy1.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_26, 0, 3, 1, 3)

        self.label_28 = QLabel(self.groupBox_19)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_28, 0, 1, 1, 1)

        self.scrollArea_3 = QScrollArea(self.groupBox_19)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy1.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy1)
        self.scrollArea_3.setMinimumSize(QSize(240, 350))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 238, 348))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy)
        self.general_commands_labels = ListView(self.scrollAreaWidgetContents_3)
        self.general_commands_labels.setObjectName(u"general_commands_labels")
        self.general_commands_labels.setGeometry(QRect(0, 0, 240, 351))
        sizePolicy1.setHeightForWidth(self.general_commands_labels.sizePolicy().hasHeightForWidth())
        self.general_commands_labels.setSizePolicy(sizePolicy1)
        self.general_commands_labels.setMinimumSize(QSize(240, 300))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_14.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_19)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_19)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_19)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_14.addWidget(self.label_15, 2, 3, 1, 1)

        self.scrollArea_2 = QScrollArea(self.groupBox_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setMinimumSize(QSize(240, 350))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 238, 348))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.protocol_widget = ListView(self.scrollAreaWidgetContents_2)
        self.protocol_widget.setObjectName(u"protocol_widget")
        self.protocol_widget.setGeometry(QRect(0, 0, 241, 641))
        sizePolicy.setHeightForWidth(self.protocol_widget.sizePolicy().hasHeightForWidth())
        self.protocol_widget.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_14.addWidget(self.scrollArea_2, 3, 0, 6, 1)

        self.label_29 = QLabel(self.groupBox_19)
        self.label_29.setObjectName(u"label_29")
        sizePolicy1.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_29, 2, 1, 1, 1)

        self.scrollArea_4 = QScrollArea(self.groupBox_19)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy1.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy1)
        self.scrollArea_4.setMinimumSize(QSize(240, 350))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 238, 348))
        self.SeriesWidget_2 = ListView(self.scrollAreaWidgetContents_4)
        self.SeriesWidget_2.setObjectName(u"SeriesWidget_2")
        self.SeriesWidget_2.setGeometry(QRect(0, 0, 241, 641))
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_14.addWidget(self.scrollArea_4, 3, 1, 6, 1)

        self.cfast_qc = QLineEdit(self.groupBox_19)
        self.cfast_qc.setObjectName(u"cfast_qc")

        self.gridLayout_14.addWidget(self.cfast_qc, 3, 4, 1, 1)

        self.label_10 = QLabel(self.groupBox_19)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_10, 4, 4, 1, 1)

        self.label_13 = QLabel(self.groupBox_19)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_13, 4, 5, 1, 1)

        self.label_14 = QLabel(self.groupBox_19)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)

        self.gridLayout_14.addWidget(self.label_14, 4, 6, 1, 1)


        self.gridLayout_15.addWidget(self.groupBox_19, 0, 0, 3, 1)

        self.stackedWidget.addWidget(self.select_commands)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.Notebook_2.addTab(self.batch_communication_3, "")
        self.camera_3 = QWidget()
        self.camera_3.setObjectName(u"camera_3")
        self.gridLayout_5 = QGridLayout(self.camera_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.camera_3)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Camera_Live_Feed = QGraphicsView(self.groupBox)
        self.Camera_Live_Feed.setObjectName(u"Camera_Live_Feed")

        self.gridLayout_6.addWidget(self.Camera_Live_Feed, 0, 0, 1, 3)

        self.button_start_camera = QPushButton(self.groupBox)
        self.button_start_camera.setObjectName(u"button_start_camera")

        self.gridLayout_6.addWidget(self.button_start_camera, 1, 0, 1, 1)

        self.button_stop_camera = QPushButton(self.groupBox)
        self.button_stop_camera.setObjectName(u"button_stop_camera")

        self.gridLayout_6.addWidget(self.button_stop_camera, 1, 1, 1, 1)

        self.button_take_snapshot = QPushButton(self.groupBox)
        self.button_take_snapshot.setObjectName(u"button_take_snapshot")

        self.gridLayout_6.addWidget(self.button_take_snapshot, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.camera_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(1780, 200))
        self.frame.setMaximumSize(QSize(16777215, 400))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: \"#232629\";\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout_5.addLayout(self.horizontalLayout, 5, 0, 1, 3)

        self.groupBox_2 = QGroupBox(self.camera_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Taken_Snapshot = QGraphicsView(self.groupBox_2)
        self.Taken_Snapshot.setObjectName(u"Taken_Snapshot")

        self.gridLayout_7.addWidget(self.Taken_Snapshot, 0, 0, 1, 3)

        self.button_discard_snapshot = QPushButton(self.groupBox_2)
        self.button_discard_snapshot.setObjectName(u"button_discard_snapshot")

        self.gridLayout_7.addWidget(self.button_discard_snapshot, 1, 0, 1, 1)

        self.button_save_snapshot = QPushButton(self.groupBox_2)
        self.button_save_snapshot.setObjectName(u"button_save_snapshot")

        self.gridLayout_7.addWidget(self.button_save_snapshot, 1, 1, 1, 1)

        self.button_transfer_to_labbook = QPushButton(self.groupBox_2)
        self.button_transfer_to_labbook.setObjectName(u"button_transfer_to_labbook")

        self.gridLayout_7.addWidget(self.button_transfer_to_labbook, 1, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.label_18 = QLabel(self.camera_3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(13)
        self.label_18.setFont(font2)

        self.gridLayout_5.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_31 = QLabel(self.camera_3)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_31, 4, 0, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_32, 2, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_33, 3, 0, 1, 1)

        self.Notebook_2.addTab(self.camera_3, "")

        self.retranslateUi(Config_Widget)

        self.Notebook_2.setCurrentIndex(2)
        self.meta_data_loading_1.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Config_Widget", u"Solutions", None))
        self.label_199.setText(QCoreApplication.translate("Config_Widget", u"EC Type", None))
        self.label_200.setText(QCoreApplication.translate("Config_Widget", u"IC  Type", None))
        self.S1.setText("")
        self.label_203.setText(QCoreApplication.translate("Config_Widget", u"T [\u00b0C]", None))
        self.label_202.setText(QCoreApplication.translate("Config_Widget", u"IC lot #", None))
        self.label_206.setText(QCoreApplication.translate("Config_Widget", u"e", None))
        self.label_205.setText(QCoreApplication.translate("Config_Widget", u"I [nm]", None))
        self.label_201.setText(QCoreApplication.translate("Config_Widget", u"EC Lot #", None))
        self.label_204.setText(QCoreApplication.translate("Config_Widget", u"F [ml/min]", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("Config_Widget", u"Cells", None))
        self.label_208.setText(QCoreApplication.translate("Config_Widget", u"Cell line", None))
        self.label_209.setText(QCoreApplication.translate("Config_Widget", u"Passage #", None))
        self.label_207.setText(QCoreApplication.translate("Config_Widget", u"License ID", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("Config_Widget", u"Compound", None))
        self.label_214.setText(QCoreApplication.translate("Config_Widget", u"MW [Da]", None))
        self.label_213.setText(QCoreApplication.translate("Config_Widget", u"Sample Id", None))
        self.label_215.setText(QCoreApplication.translate("Config_Widget", u"Weight [mg]", None))
        self.label_219.setText(QCoreApplication.translate("Config_Widget", u"Volumn [\u00b5L]", None))
        self.label_211.setText(QCoreApplication.translate("Config_Widget", u"Lot #", None))
        self.label_216.setText(QCoreApplication.translate("Config_Widget", u"Solvent", None))
        self.label_212.setText(QCoreApplication.translate("Config_Widget", u"Salt Code", None))
        self.label_210.setText(QCoreApplication.translate("Config_Widget", u"Sample Code", None))
        self.label_217.setText(QCoreApplication.translate("Config_Widget", u"Stocks [mM]", None))
        self.label_218.setText(QCoreApplication.translate("Config_Widget", u"Concentration [\u00b5M]", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("Config_Widget", u"Staff", None))
        self.label_220.setText(QCoreApplication.translate("Config_Widget", u"Study director", None))
        self.label_222.setText(QCoreApplication.translate("Config_Widget", u"Laboratory Code", None))
        self.label_221.setText(QCoreApplication.translate("Config_Widget", u"Technician", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Protocol", None))
        self.button_pgf_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_protocol_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_onl_analysis_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_59.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.label_61.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.label_60.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("Config_Widget", u"Archiving", None))
        self.label_227.setText(QCoreApplication.translate("Config_Widget", u"Model Code", None))
        self.label_230.setText(QCoreApplication.translate("Config_Widget", u"Data path", None))
        self.label_231.setText(QCoreApplication.translate("Config_Widget", u"File name template", None))
        self.label_229.setText(QCoreApplication.translate("Config_Widget", u"Study Code", None))
        self.label_228.setText(QCoreApplication.translate("Config_Widget", u"Project Code", None))
        self.label_62.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.button_batch_7.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication and open Communication Test Tool", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Config_Widget", u"Set Batch Communication Settings", None))
        self.label_4.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.button_batch_1.setText(QCoreApplication.translate("Config_Widget", u"Setup Communication and open Communication Test Tool", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Config_Widget", u"Patchmaster Setup Files", None))
        self.button_pgf_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.button_protocol_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_5.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.label_3.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.button_onl_analysis_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Config_Widget", u"Extracelullar and intracellular solutions", None))
        self.label_247.setText(QCoreApplication.translate("Config_Widget", u"Ph of internal solution", None))
        self.label_245.setText(QCoreApplication.translate("Config_Widget", u"Date of Preparation ", None))
        self.ent_ph_set.setText(QCoreApplication.translate("Config_Widget", u"pH of External Solution", None))
        self.label_243.setText(QCoreApplication.translate("Config_Widget", u"Extracellular Solution", None))
        self.label_244.setText(QCoreApplication.translate("Config_Widget", u"Intracellular solution", None))
        self.ent_date_prep.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Metadata", None))
        self.label_6.setText(QCoreApplication.translate("Config_Widget", u"Experiment Type", None))
        self.label_7.setText(QCoreApplication.translate("Config_Widget", u"Cell Type", None))
        self.label_9.setText(QCoreApplication.translate("Config_Widget", u" # of Cells patched", None))
        self.label_8.setText(QCoreApplication.translate("Config_Widget", u"Min # of Cells", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Config_Widget", u"Button ToolBar", None))
        self.Load_meta_data_experiment_12.setText(QCoreApplication.translate("Config_Widget", u"Load Form", None))
        self.database_save.setText(QCoreApplication.translate("Config_Widget", u"Save to Database", None))
        self.database_save_2.setText(QCoreApplication.translate("Config_Widget", u"Delete Form", None))
        self.add_pixmap_for_green.setText(QCoreApplication.translate("Config_Widget", u"Connected...", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.experiment_initialization_3), QCoreApplication.translate("Config_Widget", u"Experiment Initialization", None))
        self.label_24.setText(QCoreApplication.translate("Config_Widget", u"Test Patchmaster Batch Communication", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Config_Widget", u"Test the Connection to the Patchmaster", None))
        self.button_submit_command.setText(QCoreApplication.translate("Config_Widget", u"Submit Command", None))
        self.button_clear_window.setText(QCoreApplication.translate("Config_Widget", u"Stop Submitting", None))
        self.label_41.setText(QCoreApplication.translate("Config_Widget", u"Control File received", None))
        self.label_42.setText(QCoreApplication.translate("Config_Widget", u"Batch Communication Response", None))
        self.label_40.setText(QCoreApplication.translate("Config_Widget", u"Submit your Commands", None))
        self.button_batch_2.setText(QCoreApplication.translate("Config_Widget", u"Setup Experiment", None))
        self.label_11.setText("")
        self.groupBox_19.setTitle(QCoreApplication.translate("Config_Widget", u"Protocol Editor", None))
        self.label_16.setText(QCoreApplication.translate("Config_Widget", u"Execution of Experiment:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Config_Widget", u"Start Experiment", None))
        self.pushButton_4.setText(QCoreApplication.translate("Config_Widget", u"Stop Experiment", None))
        self.pushButton_2.setText(QCoreApplication.translate("Config_Widget", u"Save Plot", None))
        self.pushButton_10.setText(QCoreApplication.translate("Config_Widget", u"Clear Sequences", None))
        self.label_12.setText(QCoreApplication.translate("Config_Widget", u"Rseries", None))
        self.label.setText(QCoreApplication.translate("Config_Widget", u"Final Patch Clamping Sequence:", None))
        self.label_26.setText(QCoreApplication.translate("Config_Widget", u"Notebook Online Analysis:", None))
        self.label_28.setText(QCoreApplication.translate("Config_Widget", u"Dragable Executable Series", None))
        self.label_27.setText(QCoreApplication.translate("Config_Widget", u"Dragable Labels", None))
        self.label_32.setText(QCoreApplication.translate("Config_Widget", u"Dragable Protocols", None))
        self.label_15.setText(QCoreApplication.translate("Config_Widget", u"Quality Metrics", None))
        self.label_29.setText(QCoreApplication.translate("Config_Widget", u"Dragable QC-Checks", None))
        self.label_10.setText(QCoreApplication.translate("Config_Widget", u"Cslow", None))
        self.label_13.setText(QCoreApplication.translate("Config_Widget", u"Cfast", None))
        self.label_14.setText(QCoreApplication.translate("Config_Widget", u"Cell", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.batch_communication_3), QCoreApplication.translate("Config_Widget", u"Batch Communication", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config_Widget", u"Live Camera Feed", None))
        self.button_start_camera.setText(QCoreApplication.translate("Config_Widget", u"Start Camera", None))
        self.button_stop_camera.setText(QCoreApplication.translate("Config_Widget", u"Stop Camera", None))
        self.button_take_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Take Snapshot", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config_Widget", u"Snapshot Overview", None))
        self.button_discard_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Discard Snapshot", None))
        self.button_save_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Save Snapshot", None))
        self.button_transfer_to_labbook.setText(QCoreApplication.translate("Config_Widget", u"Transfer to Labbook", None))
        self.label_18.setText(QCoreApplication.translate("Config_Widget", u"Camera Module for Image Integration", None))
        self.label_31.setText(QCoreApplication.translate("Config_Widget", u"Image Galery:", None))
        self.Notebook_2.setTabText(self.Notebook_2.indexOf(self.camera_3), QCoreApplication.translate("Config_Widget", u"Camera", None))
    # retranslateUi

