
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up import Ui_Dialog
from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform


from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import mplcursors
import numpy as np
class Filter_Settings(QDialog, Ui_Dialog):

    def __init__(self,frontend, database_handler, parent=None):
        super().__init__(parent)
        self.frontend_style = frontend
        self.setupUi(self)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.database_handler = database_handler
        self.contains_series_list = []
        self.read_available_series_names()
        self.DISCARD_DATA = 0
    
        #self.filter_checkbox_remove.stateChanged.connect(self.handle_filter_options)

        self.SeriesItems = None
        self.current_tab_visualization = None
        self.current_tab_tree_view_manager = None

        self.and_checkbox.stateChanged.connect(self.and_or_checkbox_handling)
        self.or_checkbox.stateChanged.connect(self.and_or_checkbox_handling)
        self.contains_checkbox.stateChanged.connect(self.contains_checkbox_handling)
        self.contains_not_checkbox.stateChanged.connect(self.contains_checkbox_handling)

    def contains_checkbox_handling(self):	
        self.checkbox_handler(self.contains_checkbox,self.contains_not_checkbox)

    def and_or_checkbox_handling(self):
        self.checkbox_handler(self.and_checkbox,self.or_checkbox)
    
    def checkbox_handler(self,c1,c2):
        sender = self.sender()
        if sender.isChecked():
            if sender == c1:
                c2.setChecked(False)
            elif sender == c2:
                c1.setChecked(False)
        else: # make sure that at least one is always checked
            if not c1.isChecked() and not c2.isChecked():
                sender.setChecked(True)

    def read_available_series_names(self):

        series_names_string_list =self.database_handler.get_distinct_non_discarded_series_names()
        # series_names_string_list = ["Block Pulse", "IV"]
        
        for s in series_names_string_list:
            c = QCheckBox()
            c.setText(s[0])
            self.contains_series_grid.addWidget(c)    
            c.stateChanged.connect(partial(self.checkbox_state_changed,c,self.contains_series_list))


    def checkbox_state_changed(self,checkbox,list_name,state):
        if checkbox.checkState() == 2:
           list_name.append(checkbox.text())
        else:
            list_name.remove(checkbox.text())


    def handle_filter_options(self,state):
        if state == 2:
            self.DISCARD_DATA =1
        else:
            self.DISCARD_DATA =0

    
    def make_cslow_plot(self):
        """
        
        """
        # df with columns item_name, parent, type, level, identifier
        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        plot_widget_manager  = self.current_tab_visualization[current_index]
        tree_manager = self.current_tab_tree_view_manager[current_index]

        df = tree_manager.selected_tree_view_data_table
        experiment_cslow_param = {}
        for identifier in df[df['type'] == 'Series']["identifier"].values:
            identifier = identifier.split("::")

            q = f'select sweep_table_name from experiment_series where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
            name = self.database_handler.database.execute(q).fetchall()[0][0]
            cslow =  self.database_handler.get_cslow_value_for_sweep_table(name)
            experiment_cslow_param[identifier[0]]=cslow

        self.fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasQTAgg(self.fig)        
        self.filter_plot_widget.addWidget(canvas)

        self.ax = self.fig.add_subplot(111)

        # adjust axis to pico farad 
        vals =  [float(i)* 1e12   for i in experiment_cslow_param.values()] # 
    

        points = self.ax.plot(vals,'o')
        labels = list(experiment_cslow_param.keys())
        m = np.mean(vals)
        mad = np.median(np.absolute(vals - np.median(vals)))
        self.ax.axhline(y = m, color = 'b', linestyle = ':', label = "mean")
        self.ax.axhline(y = m+mad, color = 'b', linestyle = ':', label = "mean + MAD")
        self.ax.axhline(y = m-mad, color = 'b', linestyle = ':', label = "mean - MAD")
        
        # Add annotations to the points using mplcursors
        cursor = mplcursors.cursor(points, hover = True)
        self.ax.set_ylabel("CSlow in pF")
        canvas.draw()

        @cursor.connect("add")
        def on_add(sel):
            idx = sel.target.index
            label = labels[idx]
            sel.annotation.set_text(label)
            sel.annotation.get_bbox_patch().set(fc = "white")
        
        self.lower_slider_threshold_line = None
        self.upper_slider_threshold_line = None
        # Connect the slider valueChanged signals to update_label
        self.slider_lower_threshold_2.valueChanged.connect(lambda value, line=0, label=self.label_6: self.update_label(value, line,label))
        self.slider_upper_threshold_2.valueChanged.connect(lambda value, line=1, label=self.label_5:  self.update_label(value, line, label))

        self.slider_lower_threshold_2.setMinimum(min(vals))
        self.slider_lower_threshold_2.setMaximum(m) 
        self.slider_lower_threshold_2.setValue(m-mad/2)  

        self.slider_upper_threshold_2.setMinimum(m)
        self.slider_upper_threshold_2.setMaximum(max(vals)) 
        self.slider_upper_threshold_2.setValue(m+mad/2)  

        self.ax.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
        

    def update_label(self, value, line, label):
        label.setText(f"{value} pF")

        if line == 0:
            if  self.lower_slider_threshold_line:
                self.lower_slider_threshold_line.remove()   
            # Draw horizontal lines on the matplotlib figure
            self.lower_slider_threshold_line = self.ax.axhline(y=value, color='r', linestyle='--', label="lower threshold")
        else:
            if self.upper_slider_threshold_line:
                self.upper_slider_threshold_line.remove()   
            # Draw horizontal lines on the matplotlib figure
            self.upper_slider_threshold_line = self.ax.axhline(y=value, color='r', linestyle='--', label="upper threshold")

        self.fig.canvas.draw()
        


    def contains_series_filter(self):
        """evaluate the filter selection to remove experiments that do not containa a specific series 
        """
        if len(self.contains_series_list) > 0:
          
            

            # only keep experiment_names with 2 and more counts
            q = f'select experiment_name from experiment_analysis_mapping where analysis_id == {self.database_handler.analysis_id}'
            list_of_all_experiments = self.database_handler.database.execute(q).fetchall()
            list_of_all_experiments = self.extract_first_elements(list_of_all_experiments)


            # prepare the sql expression:
            q1 = ""

            for pos in range(len(self.contains_series_list)):

                    if self.contains_not_checkbox.isChecked():
                        q1 = q1 + f' renamed_series_name != \'{self.contains_series_list[pos]}\' '
                    else:
                        q1 = q1 + f' renamed_series_name == \'{self.contains_series_list[pos]}\' '

                    if pos < len(self.contains_series_list) - 1:
                        q1 += " or "

            # renamed_series_name
            # analysis_discarded
            
            for experiment_name in list_of_all_experiments:
                    q = f' select series_identifier,renamed_series_name from series_analysis_mapping where experiment_name == \'{experiment_name}\' and analysis_discarded = False and analysis_id == {self.database_handler.analysis_id} and ({q1})'
                    occurency_cnts = self.database_handler.database.execute(q).fetchall()
                    cnt_series = len(self.extract_first_elements(occurency_cnts))

                    # and condition requires all series names to be in the experiment
                    and_condition_failed = False  
                    if self.and_checkbox.isChecked():
                        unqiue_series_names = []
                        for tup in occurency_cnts:
                            unqiue_series_names.append(tup[1])
                     
                        if self.contains_series_list != list(set(unqiue_series_names)):
                            and_condition_failed = True
                    #    print(occurency_cnts
                    #          )
                    if cnt_series <1 or and_condition_failed:

                        # discard
                        q = f"update series_analysis_mapping set analysis_discarded = 1 where experiment_name == \'{experiment_name}\' and analysis_id =={self.database_handler.analysis_id}"
                        self.database_handler.database.execute(q).fetchall()

    def filter_parameter_value(self):
        # get the parameter name
        parameter = self.filter_parameter_combobox.currentText()

        # get the user defined thresholds
        m1 = self.slider_lower_threshold_2.value() *  1e-12
        m2  = self.slider_upper_threshold_2.value()  * 1e-12

        current_index = self.SeriesItems.currentItem().data(7, Qt.UserRole)
        tree_manager = self.current_tab_tree_view_manager[current_index]

        df = tree_manager.selected_tree_view_data_table
        
        for identifier in df[df['type'] == 'Series']["identifier"].values:
            identifier = identifier.split("::")

            q = f'select sweep_table_name from experiment_series where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
            name = self.database_handler.database.execute(q).fetchall()[0][0]
            cslow =  self.database_handler.get_cslow_value_for_sweep_table(name)
            
            if cslow < m1 or cslow > m2:
                q = f'update series_analysis_mapping set analysis_discarded = 1 where experiment_name == \'{identifier[0]}\' and series_identifier == \'{identifier[1]}\' and analysis_id =={self.database_handler.analysis_id}'
                print("outfiltered" + identifier[0] + " " + identifier[0])
        

    def apply_filters(self):
        if self.tabWidget.currentIndex() == 0:
            self.contains_series_filter()
        
        if self.tabWidget.currentIndex() == 1:
            self.filter_parameter_value()

    def extract_first_elements(self,lst):
        return [t[0] for t in lst]