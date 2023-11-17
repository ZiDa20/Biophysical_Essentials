
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up import Ui_Dialog
from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform

from Backend.treeview_manager import TreeViewManager
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import mplcursors
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
class Filter_Settings(QDialog, Ui_Dialog):

    def __init__(self,frontend, database_handler, treeview_manager,parent=None):
        super().__init__(parent)
        self.frontend_style = frontend
        self.setupUi(self)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.database_handler = database_handler
        self.contains_series_list = []
        self.read_available_series_names()
        self.DISCARD_DATA = 0
    
        #self.filter_checkbox_remove.stateChanged.connect(self.handle_filter_options)
        if isinstance(treeview_manager,TreeViewManager):
            self.treeview_manager = treeview_manager
            self.offline_tree = None
        else:
            self.current_index = treeview_manager.SeriesItems.currentItem().data(7, Qt.UserRole)
            self.offline_tree = treeview_manager
            self.treeview_manager = treeview_manager.current_tab_tree_view_manager[self.current_index]

        self.and_checkbox.stateChanged.connect(self.and_or_checkbox_handling)
        self.or_checkbox.stateChanged.connect(self.and_or_checkbox_handling)
        self.contains_checkbox.stateChanged.connect(self.contains_checkbox_handling)
        self.contains_not_checkbox.stateChanged.connect(self.contains_checkbox_handling)
        
        self.show_data_distribution.stateChanged.connect(self.make_data_distribution_plot)
        #QTimer.singleShot(2000, lambda: self.show_data_distribution.setChecked(False))

        self.fig = None
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.update_peak_filter.clicked.connect(self.update_peak_filter_clicked)
    def tab_changed(self):
        if self.tabWidget.currentIndex() == 1:
            if self.fig is None:
                self.make_cslow_plot()

    def make_data_distribution_plot(self,state):
        """calculate the result for a select easy analysis function and plot the results series wise

        Args:
            state (_type_): _description_
        """
        # if the checkbox is checked
        if state == 2:
            # query the selected analysis function
            analysis_fct = self.comboBox.currentText()
            if analysis_fct == "Maximum":
                    self.stackedWidget.setCurrentIndex(0)
                    self.min_max_analysis(np.nanmax)
            elif analysis_fct == "Minimum":
                    self.stackedWidget.setCurrentIndex(0)
                    self.min_max_analysis(np.nanmin) 
            # @(todo) implement the peak detection
            #elif analysis_fct == "Number of Peaks":
            #        self.min_max_analysis(np.nanmax)
            #       self.stackedWidget.setCurrentIndex(1)
                    # if the checkbox was unchecked
        else:
            item = self.gridLayout_12.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            print("unchecked")
        
    def update_peak_filter_clicked(self):
        print("update peak filter")

    def min_max_analysis(self,selected_fct):
            # if the menu was opened while beeing on page 2 (series specific tree)
            # the current series with the correct selected treeview needs to be identified	 
            if self.offline_tree:
                self.current_index = self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)
                self.treeview_manager = self.offline_tree.current_tab_tree_view_manager[self.current_index]
            # only query the data frome the selected treeview
            df = self.treeview_manager.selected_tree_view_data_table
            # new df to store the calculated results and the discarded flag
            self.fct_filter_plot_df = pd.DataFrame(columns=["identifier", "val","discarded"])
            # HEKA data are between 0 and inf but the ymin and ymax values give a hint how to shift the absolute values for each sweep
            # @todo check if this is true for non-HEKA data too
            meta_data_table_name = None
            # loop through each series as, query the data, adjust to min and max values and calculate execute the user selected analysis function
            for identifier in df[df['type'] == 'Series']["identifier"].values:
                
                identifier = identifier.split("::")
                # in case of meta data were added only keep the last : Mouse::220318_02::Series9
                if len(identifier)>2:
                    identifier=identifier[len(identifier)-2:len(identifier)]
                # get the meta data table name and series sweep data table names and from that the raw data table
                q = f'select sweep_table_name, meta_data_table_name from experiment_series where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
                name = self.database_handler.database.execute(q).fetchall()[0]
                meta_data_table_name = name[1]
                name = name[0]
                q = f'select * from {name}'
                raw_data = self.database_handler.database.execute(q).fetchdf()
                # this thresh-varaible will be assinged with the smallest/greatest result from all sweeps
                result_list = []
               
                #run this brief analysis for all sweeps 
                for c in raw_data.columns:
                    y_min, y_max = self.database_handler.get_ymin_from_metadata_by_sweep_table_name(name, c)
                    data = np.interp(raw_data[c], (raw_data[c].min(), raw_data[c].max()), (y_min, y_max))
                    result_list.append(selected_fct(data))
              
                thresh = selected_fct(result_list)

                self.fct_filter_plot_df = pd.concat([self.fct_filter_plot_df,
                                                     pd.DataFrame({ "identifier":[identifier[0]+"::"+identifier[1]], "val":[thresh], "discarded":[0] })])

            q = f'select * from {meta_data_table_name}'
            meta_data_df = self.database_handler.database.execute(q).fetchdf()
            meta_data_df = meta_data_df[meta_data_df['Parameter'] == 'RecordingMode']
            unit = "A"
            
            if meta_data_df["sweep_1"].values == ['4']:
                   unit  = "V"

            # adjust the unit to the SI prefix
            si_prefix = ""
            print("adjusting the prefix")
            for prefix in ["m","u","n","p","f"]:
                print(self.fct_filter_plot_df["val"].values)

                if all(abs(i) < 1 for i in self.fct_filter_plot_df["val"].values):
                    self.fct_filter_plot_df["val"] = self.fct_filter_plot_df["val"] * 1e3
                    si_prefix = prefix        
                else:
                    break
            self.unit = si_prefix + unit

            vals =  [float(i) for i in self.fct_filter_plot_df["val"].values] # 
        
            self.make_interactive_plot(self.gridLayout_12,
                                   vals,
                                   self.fct_filter_plot_df["identifier"].values,
                                   self.left_signal_threshold_slider,
                                   self.right_signal_threshold_slider,
                                   self.left_signal_threshold_label,
                                   self.right_signal_threshold_label)
            
            self.ax.set_ylabel(self.unit)

        

    def update_fct_label(self,value,label):        
         label.setText(f"{value}")

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
            c.stateChanged.connect(partial(self.checkbox_state_changed,c))
            #c.stateChanged.connect(self.test123)

    #def test123(self):
        

    def checkbox_state_changed(self,checkbox,state):
        """_summary_

        Args:
            checkbox (_type_): _description_
            state (_type_): _description_
        """
        if state == 2:
           self.contains_series_list.append(checkbox.text())
        else:
            self.contains_series_list.remove(checkbox.text())


    def handle_filter_options(self,state):
        if state == 2:
            self.DISCARD_DATA =1
        else:
            self.DISCARD_DATA =0

    
    def make_cslow_plot(self):
        """Make a scatter plot that shows the cslow value for each series
        """

        df = self.treeview_manager.selected_tree_view_data_table
        experiment_cslow_param = {}
        for identifier in df[df['type'] == 'Series']["identifier"].values:
            identifier = identifier.split("::")

            q = f'select sweep_table_name from experiment_series where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
            name = self.database_handler.database.execute(q).fetchall()[0][0]
            cslow =  self.database_handler.get_cslow_value_for_sweep_table(name)
            experiment_cslow_param[identifier[0]]=cslow

        self.unit = "pF"
        # adjust axis to pico farad 
        vals =  [float(i)* 1e12   for i in experiment_cslow_param.values()] # 

        self.make_interactive_plot(self.filter_plot_widget,
                                   vals,
                                   list(experiment_cslow_param.keys()),
                                   self.slider_lower_threshold_2,
                                   self.slider_upper_threshold_2,
                                   self.label_6,
                                   self.label_5)
        self.ax.set_ylabel("CSlow in pF")

    def make_interactive_plot(self,plot_widget,vals:list[float],labels:list[str], lower_slider, upper_slider, lower_label, upper_label):

        self.fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasQTAgg(self.fig)        
        plot_widget.addWidget(canvas)
        self.ax = self.fig.add_subplot(111)

        points = self.ax.plot(vals,'o')
        m = np.mean(vals)
        mad = np.median(np.absolute(vals - np.median(vals)))
        self.ax.axhline(y = m, color = 'b', linestyle = ':', label = "mean")
        self.ax.axhline(y = m+mad, color = 'b', linestyle = ':', label = "mean + MAD")
        self.ax.axhline(y = m-mad, color = 'b', linestyle = ':', label = "mean - MAD")
        
        # Add annotations to the points using mplcursors
        cursor = mplcursors.cursor(points, hover = True)
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

        lower_slider.valueChanged.connect(lambda value, line=0, label=lower_label: self.update_label(value, line,label))
        upper_slider.valueChanged.connect(lambda value, line=1, label=upper_label:  self.update_label(value, line, label))
        

        lower_slider.setMinimum(min(vals)*1.2)
        lower_slider.setMaximum(m*1.2) 
        lower_slider.setValue(min(vals)*0.5)  

        upper_slider.setMinimum(m*1.2)
        upper_slider.setMaximum(max(vals)*1.2) 
        upper_slider.setValue(m*0.5)  

        self.ax.legend(bbox_to_anchor = (1.0, 1), loc = 'upper center')
    
    def update_label(self, value, line, label):
        label.setText(f"{value} "+ self.unit)

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

        

        df = self.treeview_manager.selected_tree_view_data_table
        
        for identifier in df[df['type'] == 'Series']["identifier"].values:
            identifier = identifier.split("::")

            q = f'select sweep_table_name from experiment_series where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
            name = self.database_handler.database.execute(q).fetchall()[0][0]
            cslow =  self.database_handler.get_cslow_value_for_sweep_table(name)
            
            if cslow < m1 or cslow > m2:
                q = f'update series_analysis_mapping set analysis_discarded = 1 where experiment_name == \'{identifier[0]}\' and series_identifier == \'{identifier[1]}\' and analysis_id =={self.database_handler.analysis_id}'
                self.database_handler.database.execute(q).fetchall()
                print("outfiltered" + identifier[0] + " " + identifier[1])

    def filter_fct_values(self):
        """ Apply the filters that were chosen to select series according to some minor analysis function
        """

        # read the respective values from the labels        
        left_val = float(self.left_signal_threshold_slider.value())
        right_val = float(self.right_signal_threshold_slider.value())
        
        # flage the series that are out of the threshold
        self.fct_filter_plot_df.loc[(self.fct_filter_plot_df['val'] < left_val) | 
                                        (self.fct_filter_plot_df['val'] > right_val), 'discarded'] = 1

        # Filter the DataFrame to only include rows where discarded== 1
        filtered_df = self.fct_filter_plot_df[self.fct_filter_plot_df['discarded'] == 1]

        # discard the flagged series
        for index, row in filtered_df.iterrows():
            identifier = row['identifier'].split("::")
            q = f'update series_analysis_mapping set analysis_discarded = True where experiment_name = \'{identifier[0]}\' and series_identifier = \'{identifier[1]}\''
            self.database_handler.database.execute(q)

            
    def apply_filters(self):
        if self.tabWidget.currentIndex() == 0:
            self.contains_series_filter()
        
        if self.tabWidget.currentIndex() == 1:
            self.filter_parameter_value()
        
        if self.tabWidget.currentIndex() == 2:
            self.filter_fct_values()

    def extract_first_elements(self,lst):
        return [t[0] for t in lst]