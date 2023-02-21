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


    def __init__(self, database_handler, plot_widget_manager, current_tab, analysis_functions):
        
        self.plot_widget_manager = plot_widget_manager
        self.database_handler = database_handler
        self.current_tab = current_tab

        self.default_colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']
        
        # add a button for each selected analysis function
        self.add_buttons_to_layout(analysis_functions)

        self.FUNC_GRID_ROW = 1
        self.LEFT_CB_GRID_ROW = 2
        self.RIGHT_CB_GRID_ROW = 3
        self.PGF_SEQ_GRID_ROW = 4
        self.LIVE_SEQ_GRID_ROW = 5


    def add_buttons_to_layout(self, analysis_functions):
        """
        Add a button for each of the selected analysis functions to the layout.
        """

        layout = self.current_tab.analysis_button_grid

        # at 0 there is the "add" button which shouldn't be deleted
        for i in range(1,layout.count()):
            layout.itemAt(i).widget().deleteLater()

        row = 1
        col = 0
        
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)

        for fct in analysis_functions:
            if len(fct)>1:
                text = ""
                for n in fct:
                    text = text +  n + " "
            else:
                text = fct [0]

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
        
        print("row = ", row)
        
        self.current_tab.analysis_stacked_widget.setCurrentIndex(row)
        table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
        #table_widget  = table_widget.layout().itemAt(0).widget()
        
        if state == Qt.Checked:
            # show cursor bounds
            for col in range(table_widget.columnCount()):
                self.add_coursor_bounds((row,col), self.current_tab, table_widget)
        else:
                self.remove_existing_dragable_lines(row)

            #remove cursor bounds

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

        try:
            self.current_tab.analysis_stacked_widget.setCurrentIndex(row)
        except Exception as e:
            print("I got here", e)
        
        if self.current_tab.analysis_stacked_widget.currentWidget().layout():
            print("i found a layout")
            # display the cursor bounds -> check if they are in the dict
            table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
            #for col in range(table_widget.columnCount()):
            #    self.add_coursor_bounds((row,col), self.current_tab, table_widget)

            self.current_tab.analysis_stacked_widget.show()
        else:
            print("no layout found ")

            page_widget = QWidget()
            page_widget_layout = QVBoxLayout()
            
            
            col = 0
            if len(text.split())>1:
                for expr in text.split():
                    if expr not in ["+", "-", "*", "/", "(", ")"]:
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
            hide_bt.clicked.connect(self.current_tab.analysis_stacked_widget.hide)
            page_widget_layout.addWidget(hide_bt)

            page_widget.setLayout(page_widget_layout)    

            
            self.current_tab.analysis_stacked_widget.insertWidget(row, page_widget)

            

            # fill the table
            
           
            col = 0
            if len(text.split())>1:
                for expr in text.split():
                    if expr not in ["+", "-", "*", "/", "(", ")"]:
                        func_item = QTableWidgetItem(expr)
                        func_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        analysis_table_widget.setItem(1, col, func_item)
                        color_button = QPushButton("")
                        color_button.setStyleSheet("background-color: " + self.default_colors[row + col])
                        analysis_table_widget.setCellWidget(0, col, color_button)
                        self.pgf_selection = QComboBox()
                        self.get_pgf_file_selection()
                        analysis_table_widget.setCellWidget(4,col ,self.pgf_selection)
                        self.live_result = QCheckBox()
                        analysis_table_widget.setCellWidget(5,col ,self.live_result)
                        col+=1
            else:   
                color_button = QPushButton("")
                color_button.setStyleSheet("background-color: " + self.default_colors[row + col])
                analysis_table_widget.setCellWidget(0, col, color_button)
                func_item = QTableWidgetItem(text)
                func_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                analysis_table_widget.setItem(1, col, func_item)
                self.pgf_selection = QComboBox()
                self.get_pgf_file_selection()
                analysis_table_widget.setCellWidget(4,col ,self.pgf_selection)
                self.live_result = QCheckBox()
                analysis_table_widget.setCellWidget(5,col ,self.live_result)
                # tuple 
                self.live_result.clicked.connect(partial(self.show_live_results_changed, (row,0), self.current_tab, self.live_result))
            """
            analysis_table_widget.horizontalHeader().setVisible(False)
            #analysis_table_widget.tableWidget.verticalHeader().setRotation(45)
            analysis_table_widget.verticalHeader().setDefaultSectionSize(60)
            analysis_table_widget.show()

            current_tab.analysis_stacked_widget.setCurrentIndex(row)
            current_tab.analysis_stacked_widget.show()

            """
            self.adapt_stacked_widget_width(analysis_table_widget, self.current_tab.analysis_stacked_widget)
            analysis_table_widget.show()
            self.current_tab.analysis_stacked_widget.show()
            # will draw the cursor bounds             
            show_cb_checkbx.setEnabled(True)
            show_cb_checkbx.setChecked(True)

    def get_pgf_file_selection(self):
        """Should retrieve the pgf_files for all the files in the current analysis id
        This should further retrieve each individual segment"""
        analysis_id = self.database_handler.analysis_id
        series_name = self.current_tab.objectName()
        experiment_name = self.database_handler.database.execute(f"SELECT experiment_name FROM experiment_analysis_mapping WHERE analysis_id = {analysis_id};").fetchall()
        pgf_file_dict = {}
        for experiment in experiment_name:
            try:
                q = """select pgf_data_table_name from experiment_series where experiment_name = (?) and series_name = (?)"""
                pgf_sections = self.database_handler.get_data_from_database(self.database_handler.database, q, [experiment[0], series_name])[0][0]
                pgf_table = self.database_handler.database.execute(f"SELECT * FROM {pgf_sections}").fetchdf()
                print(pgf_table.info)
                pgf_table = pgf_table[pgf_table["selected_channel"] == "1"] # this should be change to an input from the user if necessary
                pgf_file_dict[experiment[0]] = (pgf_table, pgf_table.shape[0])

            except IndexError:
                print(f"The error is at the experiment: {experiment[0]}")
                continue

        pgf_files_amount = {pgf_index[1] for pgf_index in pgf_file_dict.values()}
        if len(pgf_files_amount) <= 1:
            for i in range(1, int(list(pgf_files_amount)[0])+1):
                self.pgf_selection.addItem(f"Segment {i}")

        else:
            CustomErrorDialog("The number of segments is not the same for all experiments. Please check your data.")

        print(pgf_file_dict)


    def show_live_results_changed(self, row_column_tuple, checkbox_object: QCheckBox):
        """
        Function to handle activation of an analysis function specific checkbox in the analysis table. It checks if
        cursor bounds were set correctly (if not error dialog is displayed). In the analysis function objects specified
        points used for the related analysis will be added or removed within the trace plot.
        @param row_number: row of the checkbox in the analysis function table
        @param current_tab: current tab
        @param checkbox_object: QCheckbox
        @return:
        @author: dz, 01.10.2022
        """

        table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
        if checkbox_object.isChecked():
            # check if cursor bounds are not empty otherwise print dialog and unchecke the checkbox again
            try:
                # table_widget = current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
                l_cb= float(table_widget.item(2, row_column_tuple[1]).text())
                r_cb= float(table_widget.item(3, row_column_tuple[1]).text())
                #self.plot_widget_manager.
            except Exception as e:
                dialog_message = "Please select cursor bounds first and activate live plot afterwords"
                CustomErrorDialog().show_dialog(dialog_message)
                checkbox_object.setCheckState(Qt.CheckState.Unchecked)

        print("I have to make the liveplot")
        index = self.current_tab.widget.selected_tree_view.selectedIndexes()[1]
        rect = self.current_tab.widget.selected_tree_view.visualRect(index)
        QTest.mouseClick(self.current_tab.widget.selected_tree_view.viewport(), Qt.LeftButton, pos=rect.center())
       
    def analysis_table_cell_changed(self, item):
        print("a cell changed")
        print(item.text())

    def remove_existing_dragable_lines(self, row_number):
        self.plot_widget_manager.remove_dragable_lines(row_number)

    def add_coursor_bounds(self, row_column_tuple, current_tab, table_widget):
        """
        This function will add 2 dragable lines to the plot which will be provided by the global plot manager object
        :return:
        """

        #self.current_tab_visualization[self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)].remove_dragable_lines(
        #    row_number)
        
        """
        try:
            print("read")
            left_cb_val = round(
                float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 3).text()), 2)
            right_cb_val = round(
                float(current_tab.analysis_table_widget.analysis_table_widget.item(row_number, 4).text()), 2)

            # 1) insert dragable coursor bounds into pyqt graph
            left_val, right_val = self.current_tab_visualization[
                self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)].show_draggable_lines(row_number,
                                                                                          (left_cb_val, right_cb_val))
        """

        #if row_column_tuple not in self.current_tab_visualization[
        #        self.offline_tree.SeriesItems.currentItem().data(7, Qt.UserRole)].coursor_bound_tuple_dict.keys():
                
        if table_widget.item(2, row_column_tuple[1]) is None:

                    # check if already left and right row values were selected -> than recreate with these values - otherwise use default

                    #except Exception as e:
                        #print(e)
                    # 1) insert dragable coursor bounds into pyqt graph
                    left_val, right_val = self.plot_widget_manager.show_draggable_lines(row_column_tuple)

                    
                    # 2) connect to the signal that will be emitted when cursor bounds are moved by user
                    self.plot_widget_manager.left_bound_changed.cursor_bound_signal.connect(
                        self.update_left_common_labels)

                    self.plot_widget_manager.right_bound_changed.cursor_bound_signal.connect(
                        self.update_right_common_labels)

                    # 3) update the function selection grid
                    self.update_left_common_labels((left_val, row_column_tuple[0], row_column_tuple[1]), table_widget)

                    self.update_right_common_labels((right_val, row_column_tuple[0], row_column_tuple[1]), table_widget)
                
        else:
                    l_cb= float(table_widget.item(2, row_column_tuple[1]).text())
                    r_cb= float(table_widget.item(3, row_column_tuple[1]).text())
                    left_val, right_val = self.plot_widget_manager.show_draggable_lines(row_column_tuple, (l_cb,r_cb))
        

                #self.check_ready_for_analysis(current_tab)
        """
       

        current_tab.analysis_table_widget.analysis_table_widget.removeCellWidget(row_number, 1)
        self.b = QPushButton("Change")
        current_tab.analysis_table_widget.analysis_table_widget.setCellWidget(row_number, 1, self.b)
        self.b.clicked.connect(partial(self.add_coursor_bounds, row_number, current_tab))
        current_tab.checkbox_list[0].setEnabled(True)
        """

    @Slot(tuple)
    def update_left_common_labels(self, tuple_in, table_widget=None):
        left_cursor_row = 2
        self.update_cursor_bound_labels(left_cursor_row,tuple_in, table_widget)

    @Slot(tuple)
    def update_right_common_labels(self, tuple_in, table_widget=None):
        right_cursor_row = 3
        self.update_cursor_bound_labels(right_cursor_row,tuple_in, table_widget)

    def update_cursor_bound_labels(self, table_row, tuple_in, table_widget):
        
        # tuple in has: [0]: cb value, [1]: row of the button, [2]: column of the function
        if table_widget is None:
            self.current_tab.analysis_stacked_widget.setCurrentIndex(tuple_in[1])
            table_widget = self.current_tab.analysis_stacked_widget.currentWidget().layout().itemAt(0).widget()
   
        print(
            f"updating: row = {str(tuple_in[1])} column={str(tuple_in[2])} value= {str(tuple_in[0])}"
        )

        insert_item = QTableWidgetItem(str(round(tuple_in[0],2)))
        insert_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        table_widget.setItem(table_row, tuple_in[2], insert_item)


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
                analysis_series_name = self.current_tab.objectName()

                func_name = self.current_tab.analysis_button_grid.itemAtPosition(page, 0).widget().text()


                self.database_handler.write_analysis_function_name_and_cursor_bounds_to_database(analysis_function,
                                                                                                analysis_series_name,
                                                                                                lower_bound, upper_bound)

                # non single analysis types will be calculated as single interval analysis but additional calculation is needed
                # that is why we have to note down the function with its id for postprocessing
                if table_widget.columnCount()>1:
                    print("requesting id")
                    id = self.database_handler.get_last_inserted_analysis_function_id()
                    print("got id, ", id)
                    multiple_interval_analysis = pd.concat([multiple_interval_analysis, pd.DataFrame({"page": [page], "func": [func_name],"id": [id], "function_name":[analysis_function] })])

        return multiple_interval_analysis


   
           
                