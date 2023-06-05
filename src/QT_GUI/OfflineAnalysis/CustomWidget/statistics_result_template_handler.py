from QT_GUI.OfflineAnalysis.CustomWidget.statistics_result_template import Ui_Form
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from CustomWidget.Pandas_Table import PandasTable
import pandas as pd
from functools import partial


import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from statannotations.Annotator import Annotator


class StatisticsResultTemplate(QWidget, Ui_Form):
    """ a tmeplate class that creates a widget with a lable, a qtableview and a matplotlib plot of the given result tables

    Args:
        QWidget (_type_): _description_
        Ui_Form (_type_): _description_
    """

    def __init__(self, function_name:str, test_type:str, df: pd.DataFrame, res_df:pd.DataFrame, pairs:list[tuple[str,str]], result_column_name:str, step_column_name:str= None, steps:list[float]=None ,parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        
        # for steps protocols, a combo box alloes to select which steps should be chosen to display the statistics
        if steps:
            self.set_up_combo_box(df, res_df, pairs,test_type,steps,result_column_name, step_column_name)
        else:
            self.comboBox.hide()
            self.add_canvas_to_result_widget(df, res_df, pairs,test_type,result_column_name)

        self.add_table_view(function_name, test_type, res_df)

    def add_table_view(self, function_name:str, test_type:str, res_df:pd.DataFrame):
        """
        frontend handling to show table with labels and some text

        Args:
            function_name (str): _description_
            test_type (str): _description_
            res_df (pd.DataFrame): _description_
        """
        self.label.setText("Performed Statistics:" + test_type)
        self.label.setMaximumSize(400, 50)  # Set the maximum width and height as desired
        self.label.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.statistics_table_view = QTableView()
        model = PandasTable(res_df)
        self.statistics_table_view.setModel(model)
        model.resize_header(self.statistics_table_view)
        
        # Set the section resize mode to stretch for all columns
        horizontal_header = self.statistics_table_view.horizontalHeader()
        horizontal_header.setSectionResizeMode(QHeaderView.Stretch)

        row_span = len(res_df.index)//10
        # to avoid that the plot is stretched to much for long tables
        if row_span < 2:
            row_span = 2

        self.gridLayout_2.addWidget(self.statistics_table_view,1,0,row_span,1)

        
        self.statistics_table_view.setSizeAdjustPolicy(QTableView.AdjustToContents)

        # Set the size policy of the QTableView and its parent widget to MinimumExpanding
        self.statistics_table_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #self.statistics_table_view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        self.groupBox.setTitle("Statistics of " + function_name)

    def set_up_combo_box(self,df:pd.DataFrame, res_df:pd.DataFrame, pairs:list[tuple[str,str]], test_type:str,steps_int:list[int|float], result_column_name:str, step_column_name:str,):
        """add selectable text items to the combo box and connect to the textchanged function 
        Args:
            df (pd.DataFrame): _description_
            res_df (pd.DataFrame): _description_
            pairs (list[tuple[str,str]]): _description_
            test_type (str): _description_
            steps_int (list[int | float]): _description_
        """
        self.comboBox.currentTextChanged.connect(partial(self.add_canvas_to_result_widget, df, res_df, pairs,test_type,result_column_name,step_column_name)) #result_column_name #step_column_name
        steps_str = []

        for i in steps_int:
            steps_str.append(str(i))
        self.comboBox.addItems(steps_str)
      
    def add_canvas_to_result_widget(self,df:pd.DataFrame, res_df:pd.DataFrame, pairs:list[tuple[str,str]], test_type:str, result_column_name:str, step_column_name:str=None, new_text:str=None):
        """function will be called whenever there is a change in the combo box

        Args:
            df (pd.DataFrame): _description_
            res_df (pd.DataFrame): _description_
            pairs (list[tuple[str,str]]): _description_
            test_type (str): _description_
            result_column_name (str): _description_
            step_column_name (str): _description_
            new_text (str): _description_
        """

        if step_column_name:
            canvas= self.create_result_canvas(df, pairs,test_type, result_column_name,step_column_name, float(new_text))
        else:
            canvas= self.create_result_canvas(df, pairs,test_type, result_column_name)
              
        background_widget_layout = QGridLayout()
        background_widget = QWidget()
        background_widget_layout.addWidget(canvas,0,0,1,2)
        save_plot = QPushButton("Save the Plot")
        save_plot.clicked.connect(partial(self.save_plot,canvas))
        save_table = QPushButton("Save the Table")
        save_table.clicked.connect(partial(self.save_table,res_df))
        background_widget_layout.addWidget(save_plot,1,1,1,1)
        background_widget_layout.addWidget(save_table,1,0,1,1)
        
        background_widget.setLayout(background_widget_layout)
        
        self.gridLayout_2.addWidget(background_widget,2, 1, 1, 1)
        #canvas.draw_idle()

    
    def create_result_canvas(self, df:pd.DataFrame, pairs:list[tuple[str,str]], test_type:str, y_column:str, step_column:str = None, step_value:float = None):
        """ create a plot of the data

        Args:
            df (pd.DataFrame): _description_
            pairs (list[tuple[str,str]]): _description_
            test_type (str): _description_
            y_column (str): _description_
            step_column (str, optional): _description_. Defaults to None.
            step_value (float, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        # Create a FigureCanvasQTAgg from the Figure object returned by Seaborn
        fig = plt.Figure(figsize = (6,6))   #figsize=(6,3)

        ax = fig.add_subplot(111)
        if step_column:
            df = df[df[step_column]==step_value]

        sns.boxplot(data=df,x ="meta_data" ,y = y_column, ax=ax)
        ax.grid=False
        annotator = Annotator(ax, pairs, data=df, x ="meta_data" ,y = y_column)
        test_identifier= {"Independent t-test": "t-test_ind",
                          "Welchs t-test":"t-test_welch", 
                          "Paired t-test":"test_paired",
                          "Mann-Whitney-U test":"Mann-Whitney",
                          "Wilcoxon Signed-Rank test":"Wilcoxon", 
                          "Kruskal Wallis test":"Kruskal"}
        # t-test_ind, t-test_welch, t-test_paired, Mann-Whitney, Mann-Whitney-gt, Mann-Whitney-ls, Levene, Wilcoxon, Kruskal, Brunner-Munzel.
        if test_type not in ["Kruskal Wallis test", "ANOVA"]:
            annotator.configure(test=test_identifier[test_type], text_format='star', loc='inside') #Mann-Whitney
            annotator.apply_and_annotate()
        
        # Call tight_layout to adjust the layout
        fig.tight_layout()
        canvas = FigureCanvas(fig)

        print("returning filled canvas")
        return canvas

    def save_plot(self, canvas:FigureCanvas):
        """save the dispalyed seaborn plot

        Args:
            canvas (FigureCanvas): matplotlib figure to be saved
        """
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;All Files (*)")

        if file_dialog.exec() == QFileDialog.Accepted:
            # Get selected file path
            file_path = file_dialog.selectedFiles()[0]


        buffer = canvas.print_to_buffer()
        canvas.print_figure(file_path)
        print("stored succesfully")

    def save_table(self, df:pd.DataFrame):
        """save the displayed table

        Args:
            df (pd.DataFrame): statistics result dataframe that is also displayeed within the frontend
        """
        file_dialog = QFileDialog()
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("CSV Files (*.csv);;All Files (*)")

        if file_dialog.exec() == QFileDialog.Accepted:
            # Get selected file path
            file_path = file_dialog.selectedFiles()[0]
            df.to_csv(file_path)
