
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
    
        self.filter_checkbox_remove.stateChanged.connect(self.handle_filter_options)

        self.SeriesItems = None
        self.current_tab_visualization = None
        self.current_tab_tree_view_manager = None

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

        fig = Figure(figsize=(5, 4), dpi=100)
        canvas = FigureCanvasQTAgg(fig)        
        self.filter_plot_widget.addWidget(canvas)

        ax = fig.add_subplot(111)
        points = ax.plot(experiment_cslow_param.values(),'o')
        labels = list(experiment_cslow_param.keys())

        # Add annotations to the points using mplcursors
        cursor = mplcursors.cursor(points)

        canvas.draw()
        @cursor.connect("add")
        def on_add(sel):
            idx = sel.target.index
            label = labels[idx]
            sel.annotation.set_text(label)
   

        
