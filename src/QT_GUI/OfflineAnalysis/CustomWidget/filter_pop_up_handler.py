
from PySide6.QtWidgets import *  # type: ignore
from QT_GUI.OfflineAnalysis.CustomWidget.filter_pop_up import Ui_Dialog
from functools import partial

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from PySide6.QtCore import Slot
from PySide6.QtCore import QThreadPool
from PySide6.QtGui import QFont, QFontMetrics, QTransform
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

    
    def set_meta_data_filter_combobox_options(self, combo_box):
        '''go through all series metadata of the tree and find all common meta data information

        '''

    # deprecated MZ
    #def display_select_meta_data_group_dialog(self, meta_data_groups_in_db):
        """
        Opens a new popup and displays buttons to select an action: button 1: load meta data groups from template, button 2: assign all experiments to the same meta data group,
        button 3: read values from database
        :param meta_data_groups_in_db: true if for at least each experiment meta data groups are available in the database, false if not
        :return:
        """ 

        self.create_meta_data_template()

        """
        dialog = Select_Meta_Data_Options_Pop_Up()



        # fill the layout with a default table

        
        self.frontend_style.set_pop_up_dialog_style_sheet(dialog)

        # assign later button will close the dialog without any additional assignments
        dialog.assign_one_group_to_all.clicked.connect(partial(self.continue_open_directory, dialog))

        # Create Template button will open a new popup to assign different meta data groups
        dialog.assign_now_button.clicked.connect(partial(self.create_meta_data_template, dialog))

        # Load Template button will open a filedialog to select a template
        dialog.load_template_button.clicked.connect(partial(self.open_meta_data_template_file, dialog))

        dialog.assign_one_group_to_all.setAccessibleName("big_square")
        dialog.assign_now_button.setAccessibleName("big_square")
        dialog.load_template_button.setAccessibleName("big_square")
        dialog.select_from_database_button.setAccessibleName("big_square")

        if not meta_data_groups_in_db:
            dialog.select_from_database_button.setDisabled(True)

        dialog.exec_()
        """

        
