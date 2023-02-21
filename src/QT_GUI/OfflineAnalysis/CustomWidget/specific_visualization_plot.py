# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'specific_visualization_plot.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from CustomWidget.groupbox_resizing_class import *
from matplotlib.backends.backend_qtagg import FigureCanvas

class Ui_result_plot_visualizer(object):
    def setupUi(self, result_plot_visualizer):
        if not result_plot_visualizer.objectName():
            result_plot_visualizer.setObjectName(u"result_plot_visualizer")
        result_plot_visualizer.resize(757, 588)
        self.gridLayout = QGridLayout(result_plot_visualizer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.specific_plot_box = QGroupBox(result_plot_visualizer)
        self.specific_plot_box.setObjectName(u"specific_plot_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specific_plot_box.sizePolicy().hasHeightForWidth())
        self.specific_plot_box.setSizePolicy(sizePolicy)
        self.specific_plot_box.setMaximumSize(QSize(16777215, 600))
        self.gridLayout_2 = QGridLayout(self.specific_plot_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.save_plot_button = QPushButton(self.specific_plot_box)
        self.save_plot_button.setObjectName(u"save_plot_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.save_plot_button.sizePolicy().hasHeightForWidth())
        self.save_plot_button.setSizePolicy(sizePolicy1)
        self.save_plot_button.setMinimumSize(QSize(150, 50))
        font = QFont()
        font.setPointSize(12)
        self.save_plot_button.setFont(font)
        self.save_plot_button.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"background-repeat:None;\n"
"border: 1px #fff5cc;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.save_plot_button, 0, 1, 1, 1)

        self.export_data_button = QPushButton(self.specific_plot_box)
        self.export_data_button.setObjectName(u"export_data_button")
        sizePolicy1.setHeightForWidth(self.export_data_button.sizePolicy().hasHeightForWidth())
        self.export_data_button.setSizePolicy(sizePolicy1)
        self.export_data_button.setMinimumSize(QSize(150, 50))
        self.export_data_button.setMaximumSize(QSize(25, 16777215))
        self.export_data_button.setFont(font)
        self.export_data_button.setStyleSheet(u"\n"
"background-color: rgba(255,255,255,0);\n"
"background-repeat:None;\n"
"border: 1px #fff5cc;\n"
"padding: 5px 10px;\n"
"background-position: left;\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.export_data_button, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.widget = QWidget(self.specific_plot_box)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMinimumSize(QSize(0, 400))
        self.widget.setStyleSheet(u"border-radius: 5px;")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plot_layout = QVBoxLayout()
        self.plot_layout.setObjectName(u"plot_layout")

        self.gridLayout_3.addLayout(self.plot_layout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plot_type = QLabel(self.specific_plot_box)
        self.plot_type.setObjectName(u"plot_type")

        self.gridLayout_5.addWidget(self.plot_type, 0, 0, 1, 1)

        self.plot_type_combo_box = QComboBox(self.specific_plot_box)
        self.plot_type_combo_box.setObjectName(u"plot_type_combo_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plot_type_combo_box.sizePolicy().hasHeightForWidth())
        self.plot_type_combo_box.setSizePolicy(sizePolicy3)
        self.plot_type_combo_box.setMinimumSize(QSize(150, 0))
        self.plot_type_combo_box.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_5.addWidget(self.plot_type_combo_box, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.line = QFrame(self.specific_plot_box)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.line_2 = QFrame(self.specific_plot_box)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.specific_plot_box, 0, 1, 1, 1)


        self.retranslateUi(result_plot_visualizer)

        QMetaObject.connectSlotsByName(result_plot_visualizer)
    # setupUi

    def retranslateUi(self, result_plot_visualizer):
        result_plot_visualizer.setWindowTitle(QCoreApplication.translate("result_plot_visualizer", u"Form", None))
        self.specific_plot_box.setTitle(QCoreApplication.translate("result_plot_visualizer", u"GroupBox", None))
        self.save_plot_button.setText(QCoreApplication.translate("result_plot_visualizer", u"Save Plot", None))
        self.export_data_button.setText(QCoreApplication.translate("result_plot_visualizer", u"Save Table", None))
        self.plot_type.setText(QCoreApplication.translate("result_plot_visualizer", u"Plot Type:", None))
    # retranslateUi


class ResultPlotVisualizer(QWidget, Ui_result_plot_visualizer):
    def __init__(self, offline_tree, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        ## manually added
        self.offline_tree = offline_tree
        self.analysis_id = None
        self.analysis_function_id = None
        self.analysis_name = None
        self.series_name = None
        # object where plot data will be stored to be exported easily
        self.export_data_frame = None
        self.holded_dataframe = None
        self.is_splitter_moving = False
        self.first_resize = True
                    
    def on_click(self, event, annot):
        """Event Detection in the Matplotlib Plot
        
        Args:
            event (mpl_connect_event): Event Connection via hovering motion notify
            annot (ax.annotate): Annotations of the axis
        
        """
        for line in self.ax.lines:
            #check if the selected line is drawn
            if line.contains(event)[0]:
                cont, ind = line.contains(event)
                line.set_linewidth(4)
                self.update_annot(ind,annot,line)
                annot.set_visible(True)
            else:
                line.set_linewidth(1)

            self.canvas.draw_idle()
    
    def update_annot(self, ind: tuple, annot, line):
        """Annotation Update for visualization of the lineplot name
        when hovering

        Args:
            ind (tuple): _description_
            annot (_type_): _description_
            line (_type_): _description_
        """
        x,y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        index_line = line.axes.get_lines().index(line)
        name = line.axes.get_legend().texts[index_line].get_text()
        text = f'{" ".join(list(map(str, ind["ind"])))}, {" ".join([name for _ in ind["ind"]])}'
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.4)
        
    def connect_hover(self, plot):
        """Function to connect the plot with the on_click function

        Args:
            plot (seaborn plot): seaborn plot (g) which should be connected
        """
        self.ax.legend().set_visible(False)
        
        annot = self.ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        
        self.canvas.mpl_connect("motion_notify_event", 
                                    lambda event: self.on_click(event, 
                                                                annot
                                                                ))
        self.canvas.mpl_connect("button_press_event",self.on_pick)

    def on_pick(self, event):
        """Event Detection in the Matplotlib Plot to retrieve the Experiment from the TreeView
        
        Args:
            event (mpl_connect_event): Event Connection via button pressing"""
        for line in self.ax.lines:
            if line.contains(event)[0]:
                index_line = line.axes.get_lines().index(line)
                name = line.axes.get_legend().texts[index_line].get_text()
                print(self.offline_tree.SeriesItems.selectedItems())
                self.offline_tree.SeriesItems.setCurrentItem(self.offline_tree.SeriesItems.selectedItems()[0].parent().child(0))
                self.offline_tree.offline_analysis_result_tree_item_clicked()
                self.offline_tree.click_top_level_tree_item(name)

       

