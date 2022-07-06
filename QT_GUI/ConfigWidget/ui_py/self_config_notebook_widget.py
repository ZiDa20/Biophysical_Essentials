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

from groupbox_resizing_class import GroupBoxSize
from dropable_list_view import ListView


class Ui_Config_Widget(object):
    def setupUi(self, Config_Widget):
        if not Config_Widget.objectName():
            Config_Widget.setObjectName(u"Config_Widget")
        Config_Widget.resize(1212, 848)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Config_Widget.sizePolicy().hasHeightForWidth())
        Config_Widget.setSizePolicy(sizePolicy)
        Config_Widget.setLayoutDirection(Qt.LeftToRight)
        Config_Widget.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(Config_Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Config_Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)

        self.gridLayout_37.addWidget(self.label_11, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_20, 2, 0, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_22, 0, 0, 1, 1)

        self.self_configuration_notebook = QTabWidget(Config_Widget)
        self.self_configuration_notebook.setObjectName(u"self_configuration_notebook")
        self.self_configuration_notebook.setTabShape(QTabWidget.Rounded)
        self.experiment_initialization_3 = QWidget()
        self.experiment_initialization_3.setObjectName(u"experiment_initialization_3")
        self.gridLayout_3 = QGridLayout(self.experiment_initialization_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_41, 2, 0, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_42, 3, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_52, 0, 0, 1, 1)

        self.meta_data_loading_1 = QStackedWidget(self.experiment_initialization_3)
        self.meta_data_loading_1.setObjectName(u"meta_data_loading_1")
        sizePolicy.setHeightForWidth(self.meta_data_loading_1.sizePolicy().hasHeightForWidth())
        self.meta_data_loading_1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        self.meta_data_loading_1.setFont(font1)
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


        self.gridLayout_17.addWidget(self.groupBox_30, 0, 2, 1, 1)

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


        self.gridLayout_17.addWidget(self.groupBox_31, 0, 4, 1, 1)

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


        self.gridLayout_17.addWidget(self.groupBox_33, 1, 2, 1, 1)

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


        self.gridLayout_17.addWidget(self.groupBox_34, 1, 4, 1, 1)

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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

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


        self.gridLayout.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.page_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        self.groupBox_23.setFont(font2)
        self.gridLayout_5 = QGridLayout(self.groupBox_23)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_243 = QLabel(self.groupBox_23)
        self.label_243.setObjectName(u"label_243")
        sizePolicy1.setHeightForWidth(self.label_243.sizePolicy().hasHeightForWidth())
        self.label_243.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_243, 2, 1, 1, 2)

        self.ent_ph_int_set = QLineEdit(self.groupBox_23)
        self.ent_ph_int_set.setObjectName(u"ent_ph_int_set")

        self.gridLayout_5.addWidget(self.ent_ph_int_set, 7, 3, 1, 1)

        self.S2_3 = QLineEdit(self.groupBox_23)
        self.S2_3.setObjectName(u"S2_3")

        self.gridLayout_5.addWidget(self.S2_3, 7, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 9, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 6, 1, 1, 1)

        self.label_245 = QLabel(self.groupBox_23)
        self.label_245.setObjectName(u"label_245")
        sizePolicy1.setHeightForWidth(self.label_245.sizePolicy().hasHeightForWidth())
        self.label_245.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_245, 8, 0, 1, 1)

        self.ent_ph_set = QLabel(self.groupBox_23)
        self.ent_ph_set.setObjectName(u"ent_ph_set")
        sizePolicy1.setHeightForWidth(self.ent_ph_set.sizePolicy().hasHeightForWidth())
        self.ent_ph_set.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.ent_ph_set, 8, 2, 1, 1)

        self.label_244 = QLabel(self.groupBox_23)
        self.label_244.setObjectName(u"label_244")
        sizePolicy1.setHeightForWidth(self.label_244.sizePolicy().hasHeightForWidth())
        self.label_244.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_244, 5, 1, 1, 2)

        self.ent_date_prep = QLineEdit(self.groupBox_23)
        self.ent_date_prep.setObjectName(u"ent_date_prep")

        self.gridLayout_5.addWidget(self.ent_date_prep, 7, 0, 1, 2)

        self.label_247 = QLabel(self.groupBox_23)
        self.label_247.setObjectName(u"label_247")
        sizePolicy1.setHeightForWidth(self.label_247.sizePolicy().hasHeightForWidth())
        self.label_247.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_247, 8, 3, 1, 1)

        self.Intracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.Intracellular_sol_com_1.setObjectName(u"Intracellular_sol_com_1")
        self.Intracellular_sol_com_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.Intracellular_sol_com_1, 4, 1, 1, 3)

        self.extracellular_sol_com_1 = QComboBox(self.groupBox_23)
        self.extracellular_sol_com_1.setObjectName(u"extracellular_sol_com_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.extracellular_sol_com_1.sizePolicy().hasHeightForWidth())
        self.extracellular_sol_com_1.setSizePolicy(sizePolicy3)
        self.extracellular_sol_com_1.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_5.addWidget(self.extracellular_sol_com_1, 1, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_23, 0, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.page_2)
        self.groupBox_17.setObjectName(u"groupBox_17")
        sizePolicy.setHeightForWidth(self.groupBox_17.sizePolicy().hasHeightForWidth())
        self.groupBox_17.setSizePolicy(sizePolicy)
        self.gridLayout_8 = QGridLayout(self.groupBox_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.Batch1 = QLineEdit(self.groupBox_17)
        self.Batch1.setObjectName(u"Batch1")
        self.Batch1.setMinimumSize(QSize(300, 0))
        self.Batch1.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_8.addWidget(self.Batch1, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_17)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_11, 7, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.button_batch_1 = QPushButton(self.groupBox_17)
        self.button_batch_1.setObjectName(u"button_batch_1")
        self.button_batch_1.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_8.addWidget(self.button_batch_1, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_17, 2, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 3, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QSize(250, 16777215))
        self.groupBox_7.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.groupBox_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.metadata_table = QPushButton(self.groupBox_7)
        self.metadata_table.setObjectName(u"metadata_table")
        sizePolicy.setHeightForWidth(self.metadata_table.sizePolicy().hasHeightForWidth())
        self.metadata_table.setSizePolicy(sizePolicy)
        self.metadata_table.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_9.addWidget(self.metadata_table, 5, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 6, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_12, 9, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color:black")

        self.gridLayout_9.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_24 = QLabel(self.groupBox_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color:black")

        self.gridLayout_9.addWidget(self.label_24, 7, 0, 1, 1)

        self.check_connection = QTextEdit(self.groupBox_7)
        self.check_connection.setObjectName(u"check_connection")

        self.gridLayout_9.addWidget(self.check_connection, 11, 0, 1, 1)

        self.database_save_2 = QPushButton(self.groupBox_7)
        self.database_save_2.setObjectName(u"database_save_2")
        sizePolicy.setHeightForWidth(self.database_save_2.sizePolicy().hasHeightForWidth())
        self.database_save_2.setSizePolicy(sizePolicy)
        self.database_save_2.setMinimumSize(QSize(100, 0))
        self.database_save_2.setMaximumSize(QSize(300, 30))

        self.gridLayout_9.addWidget(self.database_save_2, 2, 0, 1, 1)

        self.establish_connection_button = QPushButton(self.groupBox_7)
        self.establish_connection_button.setObjectName(u"establish_connection_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.establish_connection_button.sizePolicy().hasHeightForWidth())
        self.establish_connection_button.setSizePolicy(sizePolicy4)
        self.establish_connection_button.setMaximumSize(QSize(300, 30))

        self.gridLayout_9.addWidget(self.establish_connection_button, 8, 0, 1, 1)

        self.Load_meta_data_experiment_12 = QPushButton(self.groupBox_7)
        self.Load_meta_data_experiment_12.setObjectName(u"Load_meta_data_experiment_12")
        sizePolicy.setHeightForWidth(self.Load_meta_data_experiment_12.sizePolicy().hasHeightForWidth())
        self.Load_meta_data_experiment_12.setSizePolicy(sizePolicy)
        self.Load_meta_data_experiment_12.setMinimumSize(QSize(50, 0))
        self.Load_meta_data_experiment_12.setMaximumSize(QSize(300, 30))

        self.gridLayout_9.addWidget(self.Load_meta_data_experiment_12, 1, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color:black")

        self.gridLayout_9.addWidget(self.label_22, 10, 0, 1, 1)

        self.label_25 = QLabel(self.groupBox_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color:black")

        self.gridLayout_9.addWidget(self.label_25, 4, 0, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_18, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 0, 4, 3, 1)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 4, 0, 1, 1)

        self.protocol_file_set = QLineEdit(self.groupBox_4)
        self.protocol_file_set.setObjectName(u"protocol_file_set")
        self.protocol_file_set.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_6.addWidget(self.protocol_file_set, 3, 0, 1, 1)

        self.pg_file_set = QLineEdit(self.groupBox_4)
        self.pg_file_set.setObjectName(u"pg_file_set")
        self.pg_file_set.setMinimumSize(QSize(300, 0))
        self.pg_file_set.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_6.addWidget(self.pg_file_set, 1, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 7, 0, 1, 1)

        self.button_onl_analysis_set = QPushButton(self.groupBox_4)
        self.button_onl_analysis_set.setObjectName(u"button_onl_analysis_set")

        self.gridLayout_6.addWidget(self.button_onl_analysis_set, 5, 1, 1, 1)

        self.button_pgf_set = QPushButton(self.groupBox_4)
        self.button_pgf_set.setObjectName(u"button_pgf_set")
        self.button_pgf_set.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_6.addWidget(self.button_pgf_set, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.online_analysis_file_set = QLineEdit(self.groupBox_4)
        self.online_analysis_file_set.setObjectName(u"online_analysis_file_set")
        self.online_analysis_file_set.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_6.addWidget(self.online_analysis_file_set, 5, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 6, 0, 1, 1)

        self.button_protocol_set = QPushButton(self.groupBox_4)
        self.button_protocol_set.setObjectName(u"button_protocol_set")

        self.gridLayout_6.addWidget(self.button_protocol_set, 3, 1, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_39, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_47, 1, 0, 1, 1)

        self.meta_data_loading_1.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.meta_data_loading_1, 1, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.experiment_initialization_3, "")
        self.batch_communication_3 = QWidget()
        self.batch_communication_3.setObjectName(u"batch_communication_3")
        self.gridLayout_23 = QGridLayout(self.batch_communication_3)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_44, 0, 0, 1, 1)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_45, 3, 0, 1, 1)

        self.gridLayout_42 = QGridLayout()
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.ProtocolBox = QGroupBox(self.batch_communication_3)
        self.ProtocolBox.setObjectName(u"ProtocolBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ProtocolBox.sizePolicy().hasHeightForWidth())
        self.ProtocolBox.setSizePolicy(sizePolicy5)
        self.ProtocolBox.setMinimumSize(QSize(500, 0))
        self.ProtocolBox.setMaximumSize(QSize(800, 16777215))
        self.ProtocolBox.setFont(font2)
        self.gridLayout_10 = QGridLayout(self.ProtocolBox)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setSizeConstraint(QLayout.SetNoConstraint)
        self.QcDrag = QGridLayout()
        self.QcDrag.setObjectName(u"QcDrag")
        self.scrollArea_4 = QScrollArea(self.ProtocolBox)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy)
        self.scrollArea_4.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 120, 213))
        self.gridLayout_29 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.SeriesWidget_2 = ListView(self.scrollAreaWidgetContents_4)
        self.SeriesWidget_2.setObjectName(u"SeriesWidget_2")

        self.gridLayout_29.addWidget(self.SeriesWidget_2, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.QcDrag.addWidget(self.scrollArea_4, 1, 0, 1, 1)

        self.label_29 = QLabel(self.ProtocolBox)
        self.label_29.setObjectName(u"label_29")

        self.QcDrag.addWidget(self.label_29, 0, 0, 1, 1)


        self.gridLayout_39.addLayout(self.QcDrag, 4, 2, 1, 1)

        self.gridLayout_35 = QGridLayout()
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.scrollArea_5 = QScrollArea(self.ProtocolBox)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMinimumSize(QSize(0, 0))
        self.scrollArea_5.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 141, 318))
        self.gridLayout_16 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.listWidget = ListView(self.scrollAreaWidgetContents_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_16.addWidget(self.listWidget, 0, 1, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_35.addWidget(self.scrollArea_5, 1, 0, 1, 1)

        self.label = QLabel(self.ProtocolBox)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))

        self.gridLayout_35.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayout_35.setRowMinimumHeight(0, 2)

        self.gridLayout_39.addLayout(self.gridLayout_35, 0, 4, 1, 1)

        self.SeriesDrag = QGridLayout()
        self.SeriesDrag.setObjectName(u"SeriesDrag")
        self.scrollArea = QScrollArea(self.ProtocolBox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(300, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 141, 213))
        self.gridLayout_27 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.SeriesWidget = ListView(self.scrollAreaWidgetContents)
        self.SeriesWidget.setObjectName(u"SeriesWidget")

        self.gridLayout_27.addWidget(self.SeriesWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.SeriesDrag.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.label_28 = QLabel(self.ProtocolBox)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)

        self.SeriesDrag.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_39.addLayout(self.SeriesDrag, 4, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_39.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_39.addItem(self.verticalSpacer_6, 0, 3, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_20 = QLabel(self.ProtocolBox)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_3.addWidget(self.label_20)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_21)

        self.start_experiment_button = QPushButton(self.ProtocolBox)
        self.start_experiment_button.setObjectName(u"start_experiment_button")
        sizePolicy1.setHeightForWidth(self.start_experiment_button.sizePolicy().hasHeightForWidth())
        self.start_experiment_button.setSizePolicy(sizePolicy1)
        self.start_experiment_button.setMinimumSize(QSize(150, 30))
        self.start_experiment_button.setMaximumSize(QSize(300, 20))

        self.verticalLayout_3.addWidget(self.start_experiment_button)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_15)

        self.stop_experiment_button = QPushButton(self.ProtocolBox)
        self.stop_experiment_button.setObjectName(u"stop_experiment_button")
        sizePolicy1.setHeightForWidth(self.stop_experiment_button.sizePolicy().hasHeightForWidth())
        self.stop_experiment_button.setSizePolicy(sizePolicy1)
        self.stop_experiment_button.setMinimumSize(QSize(150, 30))
        self.stop_experiment_button.setMaximumSize(QSize(300, 20))

        self.verticalLayout_3.addWidget(self.stop_experiment_button)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_14)

        self.pushButton_10 = QPushButton(self.ProtocolBox)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setMinimumSize(QSize(150, 30))
        self.pushButton_10.setMaximumSize(QSize(300, 16777215))
        self.pushButton_10.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)


        self.gridLayout_39.addLayout(self.verticalLayout_3, 4, 4, 1, 1)

        self.LabelsDrag = QGridLayout()
        self.LabelsDrag.setObjectName(u"LabelsDrag")
        self.scrollArea_3 = QScrollArea(self.ProtocolBox)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setMinimumSize(QSize(0, 250))
        self.scrollArea_3.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 120, 318))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.general_commands_labels = ListView(self.scrollAreaWidgetContents_3)
        self.general_commands_labels.setObjectName(u"general_commands_labels")
        self.general_commands_labels.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_26.addWidget(self.general_commands_labels, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.LabelsDrag.addWidget(self.scrollArea_3, 1, 0, 1, 1)

        self.label_27 = QLabel(self.ProtocolBox)
        self.label_27.setObjectName(u"label_27")
        sizePolicy1.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy1)

        self.LabelsDrag.addWidget(self.label_27, 0, 0, 1, 1)


        self.gridLayout_39.addLayout(self.LabelsDrag, 0, 2, 1, 1)

        self.ProtocolsDrag = QGridLayout()
        self.ProtocolsDrag.setObjectName(u"ProtocolsDrag")
        self.scrollArea_2 = QScrollArea(self.ProtocolBox)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QSize(0, 320))
        self.scrollArea_2.setMaximumSize(QSize(300, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 141, 318))
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.protocol_widget = ListView(self.scrollAreaWidgetContents_2)
        self.protocol_widget.setObjectName(u"protocol_widget")
        self.protocol_widget.setMinimumSize(QSize(0, 0))

        self.gridLayout_28.addWidget(self.protocol_widget, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.ProtocolsDrag.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.label_32 = QLabel(self.ProtocolBox)
        self.label_32.setObjectName(u"label_32")
        sizePolicy1.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy1)

        self.ProtocolsDrag.addWidget(self.label_32, 0, 0, 1, 1)


        self.gridLayout_39.addLayout(self.ProtocolsDrag, 0, 0, 1, 1)

        self.gridLayout_39.setRowMinimumHeight(0, 2)

        self.gridLayout_10.addLayout(self.gridLayout_39, 1, 1, 4, 1)


        self.gridLayout_24.addWidget(self.ProtocolBox, 0, 0, 1, 1)

        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_30 = QGridLayout()
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_34 = QGridLayout()
        self.gridLayout_34.setObjectName(u"gridLayout_34")

        self.gridLayout_30.addLayout(self.gridLayout_34, 0, 0, 1, 1)


        self.gridLayout_43.addLayout(self.gridLayout_30, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.batch_communication_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy6)
        self.groupBox_3.setMinimumSize(QSize(0, 250))
        self.groupBox_3.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_31 = QGridLayout()
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(0)
        self.gridLayout_31.setVerticalSpacing(5)
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_46, 1, 0, 1, 1)

        self.rseries = QLabel(self.groupBox_3)
        self.rseries.setObjectName(u"rseries")
        sizePolicy1.setHeightForWidth(self.rseries.sizePolicy().hasHeightForWidth())
        self.rseries.setSizePolicy(sizePolicy1)
        self.rseries.setStyleSheet(u"")

        self.gridLayout_31.addWidget(self.rseries, 4, 0, 1, 1)

        self.quality = QLabel(self.groupBox_3)
        self.quality.setObjectName(u"quality")
        sizePolicy1.setHeightForWidth(self.quality.sizePolicy().hasHeightForWidth())
        self.quality.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(12)
        self.quality.setFont(font3)
        self.quality.setStyleSheet(u"")

        self.gridLayout_31.addWidget(self.quality, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.cfast_qc = QLineEdit(self.groupBox_3)
        self.cfast_qc.setObjectName(u"cfast_qc")
        sizePolicy1.setHeightForWidth(self.cfast_qc.sizePolicy().hasHeightForWidth())
        self.cfast_qc.setSizePolicy(sizePolicy1)
        self.cfast_qc.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc, 9, 0, 1, 1)

        self.cfast = QLabel(self.groupBox_3)
        self.cfast.setObjectName(u"cfast")
        sizePolicy1.setHeightForWidth(self.cfast.sizePolicy().hasHeightForWidth())
        self.cfast.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.cfast, 8, 0, 1, 1)

        self.cslow = QLabel(self.groupBox_3)
        self.cslow.setObjectName(u"cslow")
        sizePolicy1.setHeightForWidth(self.cslow.sizePolicy().hasHeightForWidth())
        self.cslow.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.cslow, 6, 0, 1, 1)

        self.rseries_qc = QLineEdit(self.groupBox_3)
        self.rseries_qc.setObjectName(u"rseries_qc")
        sizePolicy1.setHeightForWidth(self.rseries_qc.sizePolicy().hasHeightForWidth())
        self.rseries_qc.setSizePolicy(sizePolicy1)
        self.rseries_qc.setMinimumSize(QSize(150, 0))
        self.rseries_qc.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_31.addWidget(self.rseries_qc, 2, 0, 1, 1, Qt.AlignLeft)

        self.cfast_qc_2 = QLineEdit(self.groupBox_3)
        self.cfast_qc_2.setObjectName(u"cfast_qc_2")
        sizePolicy1.setHeightForWidth(self.cfast_qc_2.sizePolicy().hasHeightForWidth())
        self.cfast_qc_2.setSizePolicy(sizePolicy1)
        self.cfast_qc_2.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_31.addWidget(self.cfast_qc_2, 7, 0, 1, 1)

        self.cslow_qc = QLineEdit(self.groupBox_3)
        self.cslow_qc.setObjectName(u"cslow_qc")
        self.cslow_qc.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_31.addWidget(self.cslow_qc, 5, 0, 1, 1)

        self.capacitance = QLabel(self.groupBox_3)
        self.capacitance.setObjectName(u"capacitance")
        sizePolicy1.setHeightForWidth(self.capacitance.sizePolicy().hasHeightForWidth())
        self.capacitance.setSizePolicy(sizePolicy1)

        self.gridLayout_31.addWidget(self.capacitance, 10, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_31)

        self.NotebookTable = QTableView(self.groupBox_3)
        self.NotebookTable.setObjectName(u"NotebookTable")

        self.horizontalLayout_4.addWidget(self.NotebookTable)


        self.gridLayout_43.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.groupBox_8 = GroupBoxSize(self.batch_communication_3)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy7)
        self.groupBox_8.setMinimumSize(QSize(0, 250))
        self.groupBox_8.setFont(font2)
        self.gridLayout_40 = QGridLayout(self.groupBox_8)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_26 = QLabel(self.groupBox_8)
        self.label_26.setObjectName(u"label_26")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy8)

        self.gridLayout_36.addWidget(self.label_26, 0, 0, 1, 1)

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
        sizePolicy6.setHeightForWidth(self.select_commands.sizePolicy().hasHeightForWidth())
        self.select_commands.setSizePolicy(sizePolicy6)
        self.select_commands.setMinimumSize(QSize(0, 200))
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


        self.gridLayout_40.addLayout(self.gridLayout_36, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.groupBox_8, 0, 0, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_43, 0, 1, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_24, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.batch_communication_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy9)
        self.groupBox_2.setMinimumSize(QSize(220, 0))
        self.groupBox_2.setFont(font2)
        self.gridLayout_61 = QGridLayout(self.groupBox_2)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.transfer_to_online_analysis_button = QPushButton(self.groupBox_2)
        self.transfer_to_online_analysis_button.setObjectName(u"transfer_to_online_analysis_button")
        sizePolicy1.setHeightForWidth(self.transfer_to_online_analysis_button.sizePolicy().hasHeightForWidth())
        self.transfer_to_online_analysis_button.setSizePolicy(sizePolicy1)
        self.transfer_to_online_analysis_button.setMinimumSize(QSize(150, 30))
        self.transfer_to_online_analysis_button.setMaximumSize(QSize(100, 300))
        self.transfer_to_online_analysis_button.setStyleSheet(u"width: 100;\n"
"height:100")

        self.gridLayout_61.addWidget(self.transfer_to_online_analysis_button, 5, 0, 1, 1, Qt.AlignHCenter)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_61.addItem(self.horizontalSpacer_26, 1, 0, 1, 1)

        self.switch_to_testing = QPushButton(self.groupBox_2)
        self.switch_to_testing.setObjectName(u"switch_to_testing")
        sizePolicy1.setHeightForWidth(self.switch_to_testing.sizePolicy().hasHeightForWidth())
        self.switch_to_testing.setSizePolicy(sizePolicy1)
        self.switch_to_testing.setMinimumSize(QSize(150, 30))
        self.switch_to_testing.setMaximumSize(QSize(150, 20))

        self.gridLayout_61.addWidget(self.switch_to_testing, 0, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_61.addWidget(self.pushButton, 2, 0, 1, 1, Qt.AlignHCenter)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy9.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy9)
        font4 = QFont()
        font4.setPointSize(8)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"")

        self.gridLayout_61.addWidget(self.label_19, 4, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_61.addItem(self.verticalSpacer_19, 3, 0, 1, 1)


        self.gridLayout_42.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.gridLayout_23.addLayout(self.gridLayout_42, 2, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.batch_communication_3, "")
        self.camera_3 = QWidget()
        self.camera_3.setObjectName(u"camera_3")
        sizePolicy8.setHeightForWidth(self.camera_3.sizePolicy().hasHeightForWidth())
        self.camera_3.setSizePolicy(sizePolicy8)
        self.gridLayout_44 = QGridLayout(self.camera_3)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_10 = QLabel(self.camera_3)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setPointSize(14)
        self.label_10.setFont(font5)

        self.gridLayout_44.addWidget(self.label_10, 0, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.CameraMDI = QMdiArea(self.camera_3)
        self.CameraMDI.setObjectName(u"CameraMDI")
        self.CameraWindow = QMainWindow()
        self.CameraWindow.setObjectName(u"CameraWindow")
        sizePolicy.setHeightForWidth(self.CameraWindow.sizePolicy().hasHeightForWidth())
        self.CameraWindow.setSizePolicy(sizePolicy)
        self.CameraWindow.setMinimumSize(QSize(700, 300))
        self.gridLayout_13 = QGridLayout(self.CameraWindow)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.CameraDock = QDockWidget(self.CameraWindow)
        self.CameraDock.setObjectName(u"CameraDock")
        sizePolicy.setHeightForWidth(self.CameraDock.sizePolicy().hasHeightForWidth())
        self.CameraDock.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_25 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupBox = GroupBoxSize(self.dockWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(350, 0))
        self.groupBox.setMaximumSize(QSize(800, 16777215))
        self.gridLayout_14 = QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.Camera_Live_Feed = QGraphicsView(self.groupBox)
        self.Camera_Live_Feed.setObjectName(u"Camera_Live_Feed")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.Camera_Live_Feed.sizePolicy().hasHeightForWidth())
        self.Camera_Live_Feed.setSizePolicy(sizePolicy10)
        self.Camera_Live_Feed.setMinimumSize(QSize(250, 200))
        self.Camera_Live_Feed.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_47.addWidget(self.Camera_Live_Feed, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_start_camera = QPushButton(self.groupBox)
        self.button_start_camera.setObjectName(u"button_start_camera")

        self.verticalLayout_2.addWidget(self.button_start_camera)

        self.button_take_snapshot = QPushButton(self.groupBox)
        self.button_take_snapshot.setObjectName(u"button_take_snapshot")

        self.verticalLayout_2.addWidget(self.button_take_snapshot)

        self.button_stop_camera = QPushButton(self.groupBox)
        self.button_stop_camera.setObjectName(u"button_stop_camera")

        self.verticalLayout_2.addWidget(self.button_stop_camera)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_16)


        self.gridLayout_47.addLayout(self.verticalLayout_2, 0, 1, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_47, 1, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox, 1, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.dockWidgetContents)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setMinimumSize(QSize(350, 0))
        self.gridLayout_62 = QGridLayout(self.groupBox_10)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_49 = QGridLayout()
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.Taken_Snapshot = QGraphicsView(self.groupBox_10)
        self.Taken_Snapshot.setObjectName(u"Taken_Snapshot")
        sizePolicy10.setHeightForWidth(self.Taken_Snapshot.sizePolicy().hasHeightForWidth())
        self.Taken_Snapshot.setSizePolicy(sizePolicy10)
        self.Taken_Snapshot.setMinimumSize(QSize(250, 200))
        self.Taken_Snapshot.setMaximumSize(QSize(16777215, 500))

        self.gridLayout_49.addWidget(self.Taken_Snapshot, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_discard_snapshot = QPushButton(self.groupBox_10)
        self.button_discard_snapshot.setObjectName(u"button_discard_snapshot")

        self.verticalLayout_4.addWidget(self.button_discard_snapshot)

        self.button_save_snapshot = QPushButton(self.groupBox_10)
        self.button_save_snapshot.setObjectName(u"button_save_snapshot")

        self.verticalLayout_4.addWidget(self.button_save_snapshot)

        self.button_transfer_to_labbook = QPushButton(self.groupBox_10)
        self.button_transfer_to_labbook.setObjectName(u"button_transfer_to_labbook")

        self.verticalLayout_4.addWidget(self.button_transfer_to_labbook)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)


        self.gridLayout_49.addLayout(self.verticalLayout_4, 0, 1, 1, 1)


        self.gridLayout_62.addLayout(self.gridLayout_49, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupBox_10, 1, 2, 1, 1)

        self.CameraDock.setWidget(self.dockWidgetContents)

        self.gridLayout_13.addWidget(self.CameraDock, 0, 0, 1, 1)

        self.CameraMDI.addSubWindow(self.CameraWindow)

        self.gridLayout_15.addWidget(self.CameraMDI, 1, 0, 1, 1)


        self.gridLayout_44.addLayout(self.gridLayout_15, 1, 0, 1, 1)

        self.camera_snapshot = QWidget(self.camera_3)
        self.camera_snapshot.setObjectName(u"camera_snapshot")
        sizePolicy2.setHeightForWidth(self.camera_snapshot.sizePolicy().hasHeightForWidth())
        self.camera_snapshot.setSizePolicy(sizePolicy2)
        self.camera_snapshot.setMinimumSize(QSize(100, 200))
        self.camera_snapshot.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_2 = QHBoxLayout(self.camera_snapshot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.camera_horizontal = QHBoxLayout()
        self.camera_horizontal.setObjectName(u"camera_horizontal")

        self.horizontalLayout_2.addLayout(self.camera_horizontal)


        self.gridLayout_44.addWidget(self.camera_snapshot, 3, 0, 1, 1)

        self.label_12 = QLabel(self.camera_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.gridLayout_44.addWidget(self.label_12, 2, 0, 1, 1)

        self.self_configuration_notebook.addTab(self.camera_3, "")

        self.gridLayout_2.addWidget(self.self_configuration_notebook, 3, 0, 1, 1)


        self.retranslateUi(Config_Widget)

        self.self_configuration_notebook.setCurrentIndex(2)
        self.meta_data_loading_1.setCurrentIndex(1)
        self.visualization_stacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Config_Widget)
    # setupUi

    def retranslateUi(self, Config_Widget):
        Config_Widget.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("Config_Widget", u"Patchmaster Connection", None))
#if QT_CONFIG(tooltip)
        self.self_configuration_notebook.setToolTip(QCoreApplication.translate("Config_Widget", u"<html><head/><body><p>Perform the Batch Communication Experiment, via direct communication with the Patch Master.</p><p>Only available with HEKA Patchmaster Systems</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
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
        self.groupBox_32.setTitle(QCoreApplication.translate("Config_Widget", u"Staff", None))
        self.label_220.setText(QCoreApplication.translate("Config_Widget", u"Study director", None))
        self.label_221.setText(QCoreApplication.translate("Config_Widget", u"Technician", None))
        self.label_222.setText(QCoreApplication.translate("Config_Widget", u"Laboratory Code", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("Config_Widget", u"Experiment Protocol", None))
        self.label_60.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.button_onl_analysis_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_pgf_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_59.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.button_protocol_set_3.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_61.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
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
        self.label_245.setText(QCoreApplication.translate("Config_Widget", u"Date of Preparation ", None))
        self.ent_ph_set.setText(QCoreApplication.translate("Config_Widget", u"pH of External Solution", None))
        self.label_244.setText(QCoreApplication.translate("Config_Widget", u"Intracellular solution", None))
        self.ent_date_prep.setText("")
        self.label_247.setText(QCoreApplication.translate("Config_Widget", u"Ph of internal solution", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Config_Widget", u"Set Batch Communication Settings", None))
        self.label_4.setText(QCoreApplication.translate("Config_Widget", u"Control File Path", None))
        self.button_batch_1.setText(QCoreApplication.translate("Config_Widget", u"Setup File Path", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Config_Widget", u"Button ToolBar", None))
        self.metadata_table.setText(QCoreApplication.translate("Config_Widget", u"Show Metadata Table", None))
        self.label_23.setText(QCoreApplication.translate("Config_Widget", u"Load Metadata Form", None))
        self.label_24.setText(QCoreApplication.translate("Config_Widget", u"Establish Connection", None))
        self.database_save_2.setText(QCoreApplication.translate("Config_Widget", u"Delete Form", None))
        self.establish_connection_button.setText(QCoreApplication.translate("Config_Widget", u"Establish Connection", None))
        self.Load_meta_data_experiment_12.setText(QCoreApplication.translate("Config_Widget", u"Load Form", None))
        self.label_22.setText(QCoreApplication.translate("Config_Widget", u"Connection Overview", None))
        self.label_25.setText(QCoreApplication.translate("Config_Widget", u"View Metadata Table", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Config_Widget", u"Patchmaster Setup Files", None))
        self.label_3.setText(QCoreApplication.translate("Config_Widget", u"Protocol File", None))
        self.button_onl_analysis_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.button_pgf_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("Config_Widget", u"PGF File", None))
        self.label_5.setText(QCoreApplication.translate("Config_Widget", u"Online Analysis File", None))
        self.button_protocol_set.setText(QCoreApplication.translate("Config_Widget", u"Set", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.experiment_initialization_3), QCoreApplication.translate("Config_Widget", u"Experiment Initialization", None))
        self.ProtocolBox.setTitle(QCoreApplication.translate("Config_Widget", u"Protocol Sequence Generator", None))
        self.label_29.setText(QCoreApplication.translate("Config_Widget", u"Dragable QC-Checks:", None))
        self.label.setText(QCoreApplication.translate("Config_Widget", u"Patch Sequence", None))
        self.label_28.setText(QCoreApplication.translate("Config_Widget", u"Dragable Executable Series:", None))
        self.label_20.setText(QCoreApplication.translate("Config_Widget", u"Execute Experiment: ", None))
        self.start_experiment_button.setText(QCoreApplication.translate("Config_Widget", u"Start Experiment", None))
        self.stop_experiment_button.setText(QCoreApplication.translate("Config_Widget", u"Stop Experiment", None))
        self.pushButton_10.setText(QCoreApplication.translate("Config_Widget", u"Clear Sequences", None))
        self.label_27.setText(QCoreApplication.translate("Config_Widget", u"Dragable Labels:", None))
        self.label_32.setText(QCoreApplication.translate("Config_Widget", u"Dragable Protocols:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Config_Widget", u"Recording Quality", None))
        self.rseries.setText(QCoreApplication.translate("Config_Widget", u"Rseries:", None))
        self.quality.setText(QCoreApplication.translate("Config_Widget", u"Quality Metrics:", None))
        self.cfast.setText(QCoreApplication.translate("Config_Widget", u"Cfast:", None))
        self.cslow.setText(QCoreApplication.translate("Config_Widget", u"Cslow:", None))
        self.capacitance.setText(QCoreApplication.translate("Config_Widget", u"Cell:", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Config_Widget", u"Analysis", None))
        self.label_26.setText(QCoreApplication.translate("Config_Widget", u"Notebook Online Analysis:", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Config_Widget", u"Test the Connection to the Patchmaster", None))
        self.button_submit_command.setText(QCoreApplication.translate("Config_Widget", u"Submit Command", None))
        self.button_clear_window.setText(QCoreApplication.translate("Config_Widget", u"Stop Submitting", None))
        self.label_42.setText(QCoreApplication.translate("Config_Widget", u"Batch Communication Response", None))
        self.label_40.setText(QCoreApplication.translate("Config_Widget", u"Submit your Commands", None))
        self.label_41.setText(QCoreApplication.translate("Config_Widget", u"Control File received", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config_Widget", u"Control Panel", None))
        self.transfer_to_online_analysis_button.setText(QCoreApplication.translate("Config_Widget", u"Transfer to Online Analysis", None))
        self.switch_to_testing.setText(QCoreApplication.translate("Config_Widget", u"Switch to testing", None))
        self.pushButton.setText(QCoreApplication.translate("Config_Widget", u"Download Notebook", None))
        self.label_19.setText(QCoreApplication.translate("Config_Widget", u"Connect to Online Analysis:", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.batch_communication_3), QCoreApplication.translate("Config_Widget", u"Batch Communication", None))
        self.label_10.setText(QCoreApplication.translate("Config_Widget", u"Camera Window ", None))
        self.CameraWindow.setWindowTitle(QCoreApplication.translate("Config_Widget", u"Subwindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config_Widget", u"Live Camera Feed", None))
        self.button_start_camera.setText(QCoreApplication.translate("Config_Widget", u"Start Camera", None))
        self.button_take_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Take Snapshot", None))
        self.button_stop_camera.setText(QCoreApplication.translate("Config_Widget", u"Stop Camera", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Config_Widget", u"Snapshot Feed", None))
        self.button_discard_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Discard Snapshot", None))
        self.button_save_snapshot.setText(QCoreApplication.translate("Config_Widget", u"Save Snapshot", None))
        self.button_transfer_to_labbook.setText(QCoreApplication.translate("Config_Widget", u"Transfer to Labbook", None))
        self.label_12.setText(QCoreApplication.translate("Config_Widget", u"Snapshot Galery", None))
        self.self_configuration_notebook.setTabText(self.self_configuration_notebook.indexOf(self.camera_3), QCoreApplication.translate("Config_Widget", u"Camera", None))
    # retranslateUi

