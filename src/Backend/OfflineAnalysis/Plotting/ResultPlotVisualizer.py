from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from Frontend.CustomWidget.groupbox_resizing_class import *
from matplotlib.backends.backend_qtagg import FigureCanvas
from functools import partial
from Frontend.OfflineAnalysis.CustomWidget.specific_visualization_plot import Ui_result_plot_visualizer


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
        self.export_data_frame = None
        self.holded_dataframe = None
        self.is_splitter_moving = False
        self.first_resize = True
        self.parameter_label.hide()
        self.parameter_combobox.hide()

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


    def add_labels_to_plot(self, plot_type_list: list, visualization_func: callable) -> None:
        """This function adds the labels to the plot in the combobox to select
        the appropiate visualization function to be run in the offline plot

        Args:
            plot_type_list (list): Option List of Visualization Functions
        """
        if self.plot_type_combo_box.currentText() not in plot_type_list:
            self.plot_type_combo_box.addItems(plot_type_list)
            self.plot_type_combo_box.currentTextChanged.connect(
                partial(self.plot_type_changed, visualization_func))


    def plot_type_changed(self, func, new_text):
        """
        Will change the plot type whenever the combo box selected item is changed by the user
        @param parent_widget: custom widget class ResultPlotVisualizer
        @param new_text: item text of the new displayed item in the combo boc
        @author dz, 13.07.2022
        """
        func(self,new_text, switch = True)

