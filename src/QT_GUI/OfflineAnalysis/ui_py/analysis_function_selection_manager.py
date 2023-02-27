from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform
from PySide6.QtTest import QTest

from functools import partial

from Offline_Analysis.error_dialog_class import CustomErrorDialog

import pandas as pd

class AnalysisFunctionSelectionManager():

    """
    Main class to handle all set up configurations for the analysis functions.
    This includes button generation for each of the selected analysis function. 
    Additionally, cursor bounds, pgf segment selection and live plot feature 
    can be activated in a QTableWidget which is also generated and controlled 
    by this class.
    """


    def __init__(self, 
                 database_handler, 
                 plot_widget_manager, 
                 current_tab, 
                 analysis_functions, 
                 frontend):
        
        self.plot_widget_manager = plot_widget_manager
        self.database_handler = database_handler
        self.current_tab = current_tab
        self.frontend_style = frontend

        self.default_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']
        self.operands =  ["+", "-", "*", "/", "(", ")"]
         # keep grid changes within the related dataframe to avoid exhaustive iteration over the grid
        
        self.FUNC_GRID_ROW = 1
        self.LEFT_CB_GRID_ROW = 2
        self.RIGHT_CB_GRID_ROW = 3
        self.PGF_SEQ_GRID_ROW = 4
        self.LIVE_GRID_ROW = 5

        # add a button for each selected analysis function
        self.add_buttons_to_layout(analysis_functions)

    def clear_analysis_widgets(self,layout):
        """
        clears all pages and layouts from previous widgets 
        """
        # at 0 there is the "add" button which shouldn't be deleted
        for i in range(1,layout.count()):
            layout.itemAt(i).widget().deleteLater()

        
        pages = self.current_tab.analysis_stacked_widget.count()
        for i in range(pages):
            # allways delete page 0
            widget = self.current_tab.analysis_stacked_widget.widget(0)
            self.current_tab.analysis_stacked_widget.removeWidget(widget)

        # insert the default Widget for the "+" button "        
        page_widget = QWidget()
        self.current_tab.analysis_stacked_widget.insertWidget(0, page_widget)

        print("page count = ", self.current_tab.analysis_stacked_widget.count())

        self.plot_widget_manager.coursor_bound_tuple_dict = {}
        self.live_plot_info = pd.DataFrame(columns=["page", "col", "func_name", "left_cursor", "right_cursor", "live_plot", "cursor_bound"]) #, "live_plot"


    def add_buttons_to_layout(self, analysis_functions):
        """
        Add a button for each of the selected analysis functions to the layout.
        """
        layout = self.current_tab.analysis_button_grid
        self.pgf_files_amount = ["1","2","3"] #self.database_handler.get_pgf_file_selection(self.current_tab)
        self.clear_analysis_widgets(layout)

        
        row = 1
        col = 0
        
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        try:
            analysis_functions.remove([])
        except:
            print("No need to remove an empty list")


        for fct in analysis_functions:

            if len(fct)>1:
                text = ""
                for n in fct:
                    text = text +  n + " "
            else:
                try:
                    text = fct [0]
                except Exception as e:
                    print(e)
            button = QPushButton(text)


            show_cb_checkbx = QCheckBox()
            sizePolicy4.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy4)
            button.setMinimumSize(QSize(150, 150))
            button.setMaximumSize(QSize(150, 150))
            button.setAccessibleName(QCoreApplication.translate("SpecificAnalysisTab", u"analysis_grid_bt", None))

            sizePolicy4.setHeightForWidth(show_cb_checkbx.sizePolicy().hasHeightForWidth())
            show_cb_checkbx.setSizePolicy(sizePolicy4)
            #button.setMinimumSize(QSize(150, 150))
            #button.setMaximumSize(QSize(150, 150))

            layout.addWidget(button, row, col)
            layout.addWidget(show_cb_checkbx, row, col+1) 

            button_width = button.sizeHint().width()
            if button_width > 150:
                lines = text.split()
                line_width = 0
                line_text = ""
                for word in lines:
                        line_text = line_text + word + " \n "

                layout.removeWidget(button)
                layout.removeWidget(show_cb_checkbx)

                button.setText(line_text)
                button.setMaximumSize(QSize(150, 150))
                show_cb_checkbx.setMaximumSize(QSize(150, 150))
                
                layout.addWidget(button, row, col)
                layout.addWidget(show_cb_checkbx, row, col+1)

            button.clicked.connect(partial(self.show_analysis_grid, row,text, show_cb_checkbx))
            show_cb_checkbx.stateChanged.connect(partial(self.on_checkbox_state_changed,row))
            show_cb_checkbx.setEnabled(False)

            # click the buttons to make sure each analysis function gets assigned with cursor bounds
            # this eliminated the need of further checks for empty cursor bounds
            QTest.mouseClick(button, Qt.LeftButton)

            row += 1

        self.run_analysis_functions = QPushButton("Run")
        layout.addWidget(self.run_analysis_functions, row, col)
        

    def on_checkbox_state_changed(self, row, state):
        """
        Handles checkboxes next to the analysis function button.
        Enables or disables all additional drawings ( cursor bounds and live plot) 
        which are related to this analysis function
        """
        print("row = ", row)
        
        self.current_tab.analysis_stacked_widget.setCurrentIndex(row)
        table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
        #table_widget  = table_widget.layout().itemAt(0).widget()
        
        if state == 2:

            # if checked show cursor bounds and also (if checked) live plot
            for col in range(table_widget.columnCount()):

                # add cursor bounds: of not existing new ones are created, otherwise existing ones will be selected    
                self.add_coursor_bounds((row,col), self.current_tab, table_widget)

                condition = (self.live_plot_info['page'] == row) & (self.live_plot_info['col'] == col)
                filtered_df = self.live_plot_info[condition]
                
                # if cursor bounds were created, they will be added to the live plot info dataframe
                if filtered_df.empty:
                    
                    func_name = table_widget.item(self.FUNC_GRID_ROW, col).text()
                    left_cursor = table_widget.item(self.LEFT_CB_GRID_ROW, col).text()
                    right_cursor = table_widget.item(self.RIGHT_CB_GRID_ROW, col).text()
                    tmp = pd.DataFrame({"page":[row], "col":[col], "func_name":[func_name], 
                        "left_cursor":[left_cursor], "right_cursor":[right_cursor], 
                        "live_plot":[False], "cursor_bound":[True]})
                
                    self.live_plot_info = pd.concat([self.live_plot_info, tmp])
                    self.live_plot_info.reset_index(drop = True, inplace=True)
                else:
                    self.update_grid_data_frame(row,col,"cursor_bound",True)
                    
        
        else:
                # @todo improve: merge the  two for loops
                self.plot_widget_manager.remove_dragable_lines(row)

                for col in self.live_plot_info[self.live_plot_info['page'] == row]["col"].values:
                    self.update_grid_data_frame(row,col,"cursor_bound",False)
                    
        # very important: dont forget to update the plot widget manager object !
        self.plot_widget_manager.update_live_analysis_info(self.live_plot_info)
        self.reclick_tree_view_item()

    def group_box_fullsize(self):
        tmp_size = self.current_tab.analysis_button_grid.sizeHint().width() + self.current_tab.analysis_stacked_widget.sizeHint().width()
        self.resize_group_box(tmp_size)
    
    def group_box_smallsize(self):
        tmp_size = self.current_tab.analysis_button_grid.sizeHint().width() + 50
        self.resize_group_box(tmp_size)

    def resize_group_box(self,tmp_size):
        self.current_tab.subwindow_calc.setMinimumSize(QSize(tmp_size, 900))
        self.current_tab.subwindow_calc.setMaximumSize(QSize(tmp_size, 900))
    

        
    """
    def rotate_row_indexes(self,table_widget):
        print("rotation started")
        # Get the current number of rows in the table
        num_rows = table_widget.rowCount()

        # Set the row index names and rotate them by 90 degrees
        for row in range(num_rows):
            item = table_widget.verticalHeaderItem(row)
            if item is None:
                item = QTableWidgetItem("")
                table_widget.setVerticalHeaderItem(row, item)
            item.setFont(QFont('Arial', 10))
            item_text = item.text()
            item_text_width = QFontMetrics(item.font()).boundingRect(item_text).width()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            transform = QTransform().rotate(90)
            item.setData(Qt.UserRole, transform)
            table_widget.verticalHeader().resizeSection(row, item_text_width + 10)

        # Resize the columns to fit the contents
        table_widget.resizeColumnsToContents()

        # Set the row height to be equal to the column width (for square cells)
        table_widget.verticalHeader().setDefaultSectionSize(table_widget.horizontalHeader().defaultSectionSize())
        print("rotation finished")
    """

    def create_qtablewidget(self,col_cnt,row_cnt):
        # Create a new QTableWidget with 2 columns and 5 rows
        table_widget = QTableWidget(row_cnt, col_cnt)

        # Set the headers for each column
        for c in range(col_cnt):
        
            table_widget.setHorizontalHeaderItem(c, QTableWidgetItem("Column " + str(c)))
        
        row_names = ["Color", "Func", "Left", "Right", "PGF", "Live"]
        # Set the row index names and rotate them by 90 degrees
        for row in range(row_cnt):
            item = QTableWidgetItem(row_names[row])
            item.setFont(QFont('Arial', 10))
            item_text = item.text()
            item_text_width = QFontMetrics(item.font()).boundingRect(item_text).width()
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            transform = QTransform().rotate(90)
            item.setData(Qt.UserRole, transform)
            table_widget.setVerticalHeaderItem(row, item)
            table_widget.verticalHeader().resizeSection(row, item_text_width + 10)

        # Resize the columns to fit the contents
        table_widget.resizeColumnsToContents()

        # Set the row height to be equal to the column width (for square cells)
        table_widget.verticalHeader().setDefaultSectionSize(table_widget.horizontalHeader().defaultSectionSize())

        return table_widget

    def adapt_stacked_widget_width(self, table_widget: QTableWidget, stacked_widget: QStackedWidget):

        # Get the width of the table widget
        table_width = table_widget.verticalHeader().width() + table_widget.horizontalHeader().length() + table_widget.verticalScrollBar().width() + 4  # Add some extra pixels for borders and padding

        # Set the width of the stacked widget
        stacked_widget.setFixedWidth(table_width)

    def show_analysis_grid(self, row,text, show_cb_checkbx):
        
        print("stacked widget page ", row, " requested")      
        self.current_tab.analysis_stacked_widget.setCurrentIndex(row)
        print("Current Index = ", self.current_tab.analysis_stacked_widget.currentIndex())
        
        if row == self.current_tab.analysis_stacked_widget.currentIndex():

                print("i found a layout")
                # display the cursor bounds -> check if they are in the dict
                table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
                #for col in range(table_widget.columnCount()):
                #    self.add_coursor_bounds((row,col), self.current_tab, table_widget)

                self.current_tab.analysis_stacked_widget.show()
        else:

            print("page didnt exist yet")

            page_widget = QWidget()
            page_widget_layout = QVBoxLayout()
            
            
            col = 0
            if len(text.split())>1:
                for expr in text.split():
                    if expr not in self.operands:
                        col+=1
            else:
                col = 1
        
            # MUsT BE SPECIFIED DOES NOT WORK WITHOUT TAKES YOU 3 H of LIFE WHEN YOU DONT DO IT !
            analysis_table_widget =  self.create_qtablewidget(col,6)
            #analysis_table_widget.tableWidget.setColumnCount(col)
            #analysis_table_widget.tableWidget.setRowCount(6)
            #self.rotate_row_indexes(analysis_table_widget.tableWidget)


            page_widget_layout.addWidget(analysis_table_widget)

            hide_bt = QPushButton("Hide")
            hide_bt.clicked.connect(self.hide_stacked_widget)
            page_widget_layout.addWidget(hide_bt)

            page_widget.setLayout(page_widget_layout)    

            
            self.current_tab.analysis_stacked_widget.insertWidget(row, page_widget)

            

            # fill the table
            
           
            col = 0
            if len(text.split())>1:
                for expr in text.split():
                    if expr not in ["+", "-", "*", "/", "(", ")"]:
                        self.add_cell_widgets_to_analysis_grid(row,col, analysis_table_widget, expr)
                        col+=1
            else:   
                self.add_cell_widgets_to_analysis_grid(row,col, analysis_table_widget, text)

            self.adapt_stacked_widget_width(analysis_table_widget, self.current_tab.analysis_stacked_widget)
            analysis_table_widget.show()
            self.current_tab.analysis_stacked_widget.show()
            # will draw the cursor bounds             
            show_cb_checkbx.setEnabled(True)
            show_cb_checkbx.setChecked(True)
        
        self.group_box_fullsize()

    def hide_stacked_widget(self):
      self.current_tab.analysis_stacked_widget.hide()
      self.group_box_smallsize()


    def add_cell_widgets_to_analysis_grid(self, row, col, analysis_table_widget, text):
        """
        adds cell widgets for a specific column of a an analysis table widget
        """
        color_button = QPushButton("")
        color_button.setStyleSheet("background-color: " + self.default_colors[row + col])
        analysis_table_widget.setCellWidget(0, col, color_button)
        func_item = QTableWidgetItem(text)
        func_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        analysis_table_widget.setItem(self.FUNC_GRID_ROW, col, func_item)
        self.pgf_selection = QComboBox()
        self.pgf_selection.addItems(self.pgf_files_amount)
        analysis_table_widget.setCellWidget(self.PGF_SEQ_GRID_ROW,col ,self.pgf_selection)
        live_result = QCheckBox()
        analysis_table_widget.setCellWidget(self.LIVE_GRID_ROW,col ,live_result)
        # tuple 
        live_result.stateChanged.connect(partial(self.show_live_results_changed, (row,col), text))


    def show_live_results_changed(self, row_column_tuple, text, state):
        """
        Function to handle activation of an analysis function specific checkbox in the analysis table. It checks if
        cursor bounds were set correctly (if not error dialog is displayed). In the analysis function objects specified
        points used for the related analysis will be added or removed within the trace plot.
        @param row_number: row of the checkbox in the analysis function table
        @param current_tab: current tab
        @param checkbox_object: QCheckbox
        @return:
        @author: dz, 02.2023
        """

        table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
        if state == Qt.Checked:
            # check if cursor bounds are not empty otherwise print dialog and unchecke the checkbox again
            try:
                # table_widget = current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
                l_cb= float(table_widget.item(2, row_column_tuple[1]).text())
                r_cb= float(table_widget.item(3, row_column_tuple[1]).text())

                index = self.live_plot_info[(self.live_plot_info['page'] == row_column_tuple[0]) & (self.live_plot_info["col"]==row_column_tuple[1])].index[0]
                self.live_plot_info["live_plot"][index]=True
                self.live_plot_info["left_cursor"][index]=l_cb
                self.live_plot_info["right_cursor"][index]=r_cb
            except Exception as e:
                print(e)
                #dialog_message = "Please select cursor bounds first and activate live plot afterwords"
                #CustomErrorDialog().show_dialog(dialog_message)
                #checkbox_object.setCheckState(Qt.CheckState.Unchecked)
        else:
            self.update_grid_data_frame( row_column_tuple[0],  row_column_tuple[1], "live_plot", False)

        # very important: dont forget to update the plot widget manager object !
        self.plot_widget_manager.update_live_analysis_info(self.live_plot_info)
        self.reclick_tree_view_item()
        
       
    def analysis_table_cell_changed(self, item):
        print("a cell changed")
        print(item.text())

    def add_coursor_bounds(self, row_column_tuple, current_tab, table_widget):
       
        print("adding cursor bounds")

        print(self.plot_widget_manager.coursor_bound_tuple_dict.keys())

        if row_column_tuple in self.plot_widget_manager.coursor_bound_tuple_dict.keys():

            # show existing cursor bounds which are also already connected 
            self.plot_widget_manager.show_draggable_lines(row_column_tuple)

        else:

            # 1) insert dragable coursor bounds into graph
            left_val, right_val = self.plot_widget_manager.create_dragable_lines(row_column_tuple)
            
            # 2) connect to the signal that will be emitted when cursor bounds are moved by user
            self.plot_widget_manager.left_bound_changed.cursor_bound_signal.connect(
                self.update_left_common_labels)

            self.plot_widget_manager.right_bound_changed.cursor_bound_signal.connect(
                self.update_right_common_labels)

            # 3) update the function selection grid
            self.update_left_common_labels((left_val, row_column_tuple[0], row_column_tuple[1]), table_widget)

            self.update_right_common_labels((right_val, row_column_tuple[0], row_column_tuple[1]), table_widget)



    @Slot(tuple)
    def update_left_common_labels(self, tuple_in, table_widget=None):
        self.update_cursor_bound_labels(self.LEFT_CB_GRID_ROW,tuple_in, table_widget)
        try:
            self.update_grid_data_frame(tuple_in[1], tuple_in[2], "left_cursor", tuple_in[0])
            self.plot_widget_manager.update_live_analysis_info(self.live_plot_info)
            self.reclick_tree_view_item()
        except Exception as e:
            # will give an error at the beginning when no cursor bounds are added to the table widget
            print(e)

    @Slot(tuple)
    def update_right_common_labels(self, tuple_in, table_widget=None):
        # tuple in fields: [0]: cb value, [1]: row of the button, [2]: column of the function
        self.update_cursor_bound_labels(self.RIGHT_CB_GRID_ROW,tuple_in, table_widget)
        try:
            self.update_grid_data_frame(tuple_in[1], tuple_in[2], "right_cursor", tuple_in[0])
            self.plot_widget_manager.update_live_analysis_info(self.live_plot_info)
            self.reclick_tree_view_item()
        except Exception as e:
             # will give an error at the beginning when no cursor bounds are added to the table widget
            print(e)


    def update_cursor_bound_labels(self, table_row, tuple_in, table_widget):
        
        # tuple in fields: [0]: cb value, [1]: row of the button, [2]: column of the function
        if table_widget is None:
            self.current_tab.analysis_stacked_widget.setCurrentIndex(tuple_in[1])
            table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
   
        print(
            f"updating: row = {str(tuple_in[1])} column={str(tuple_in[2])} value= {str(tuple_in[0])}"
        )

        insert_item = QTableWidgetItem(str(round(tuple_in[0],2)))
        insert_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        table_widget.setItem(table_row, tuple_in[2], insert_item)

    def update_grid_data_frame(self, page:int, column:int, column_name:str, value):
        """
        update a single data frame cell value
        value can be either float, bool, str, ... 
        """
        index = self.live_plot_info[(self.live_plot_info['page'] == page) & (self.live_plot_info["col"]==column)].index[0]
        self.live_plot_info[column_name][index]=value      

    def reclick_tree_view_item(self):
        """
        reclick the last clicked treeview item to update the view
        """
        index = self.current_tab.widget.selected_tree_view.selectedIndexes()[1]
        rect = self.current_tab.widget.selected_tree_view.visualRect(index)
        # on click (handled in treeview manager) plot compartments will be evaluated
        QTest.mouseClick(self.current_tab.widget.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())

    def write_table_widget_to_database(self):
        """
         iterates through each tab of the stacked widget and writes each column as a new row to the database
        """

        initial_index = self.current_tab.analysis_stacked_widget.currentIndex()
        multiple_interval_analysis = pd.DataFrame(columns=["page", "func", "id", "function"])

        # -2 because of the add button at the beginning and the run button at the end
        max_page = int((self.current_tab.analysis_button_grid.count()-2)/2)+1

        for page in range(1,max_page):

            print("reading page " , str(page))
            self.current_tab.analysis_stacked_widget.setCurrentIndex(page)
            table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()

            for col in range(table_widget.columnCount()):
                print("writing col" , col)
                analysis_function = table_widget.item(self.FUNC_GRID_ROW, col).text()
                lower_bound = table_widget.item(self.LEFT_CB_GRID_ROW, col).text()
                upper_bound = table_widget.item(self.RIGHT_CB_GRID_ROW, col).text()

                print("hi")
                analysis_series_name = self.current_tab.objectName()
                print(analysis_series_name)

                func_name = self.current_tab.analysis_button_grid.itemAtPosition(page, 0).widget().text()

                print("func name", func_name  )
                print("starting to wrtie to db")
                print(analysis_function)
                print(analysis_series_name)
                print(lower_bound)
                print(upper_bound)
                """
                try:
                    self.database_handler.open_connection()
                except Exception as e:
                    print("opening failed with error", e)
                """
                self.database_handler.write_analysis_function_name_and_cursor_bounds_to_database(analysis_function,
                                                                                                analysis_series_name,
                                                                                               lower_bound, upper_bound)
                #self.database_handler.database.close()
                print("finished writing")
                # non single analysis types will be calculated as single interval analysis but additional calculation is needed
                # that is why we have to note down the function with its id for postprocessing
                if table_widget.columnCount()>1:
                    print("requesting id")
                    id = self.database_handler.get_last_inserted_analysis_function_id()
                    print("got id, ", id)
                    multiple_interval_analysis = pd.concat([multiple_interval_analysis, pd.DataFrame({"page": [page], "func": [func_name],"id": [id], "function_name":[analysis_function] })])

        print("returning multiple analysis ", multiple_interval_analysis)

        return multiple_interval_analysis


   
           
                