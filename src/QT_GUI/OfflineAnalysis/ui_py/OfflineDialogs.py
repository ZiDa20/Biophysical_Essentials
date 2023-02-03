from QT_GUI.OfflineAnalysis.CustomWidget.SubstractDialog import SubstractDialog
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from QT_GUI.OfflineAnalysis.CustomWidget.MetaDataPopupAnalysis import MetadataPopupAnalysis
from QT_GUI.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog
from functools import partial
class OfflineDialogs:
    """_summary_
    """
    def __init__(self, 
                 database_handler, 
                 offline_manager, 
                 frontend, 
                 blank_analysis_tree_view_manager,
                 blank_analysis_plot_manager) -> None:
        """_summary_
        """
        self.database_handler = database_handler
        self.offline_manager = offline_manager
        self.frontend_style = frontend
        self.blank_analysis_tree_view_manager = blank_analysis_tree_view_manager
        self.blank_analysis_plot_manager = blank_analysis_plot_manager
        
    def new_series_creation(self):
        series_dialog = SubstractDialog()
        series_dialog.exec()
        
    def edit_metadata_analysis_id(self):
        
        """ Popup Dialog to edit the metadata of the selected experiments 
        """
        edit_data = MetadataPopupAnalysis(self.database_handler, self.frontend_style, series = False)
        edit_data.create_table()
        edit_data.submit.clicked.connect(edit_data.add_metadata_into_db)
        edit_data.exec()

    def edit_series_meta_data_popup(self):
        """ 
            Popup Dialog to edit the metadata of the related series
        """
        edit_data = MetadataPopupAnalysis(self.database_handler, self.frontend_style, series = True)
        edit_data.create_table()
        edit_data.submit.clicked.connect(edit_data.add_metadata_into_db)
        edit_data.exec()
        
    def create_meta_data_template(self, save, open, make):
        '''
        Creates a new dialog popup to create a new meta data template. The created template can be saved or not
        :param dialog: open dialog object
        :return:
        '''
        # open a new dialog with a tree view representation of the selected directory - only on experiment and series level
        meta_data_popup = Assign_Meta_Data_PopUp(self.database_handler, self.offline_manager, self.frontend_style)
        template_table_view = meta_data_popup.map_metadata_to_database()
        meta_data_popup.save_to_template_button.clicked.connect(partial(save,
                                                                        meta_data_popup))
        
        meta_data_popup.load_template.clicked.connect(partial(open,template_table_view))
        meta_data_popup.continue_loading.clicked.connect(partial(make,meta_data_popup,template_table_view))
        meta_data_popup.exec_()
        
    def select_tree_view_meta_data(self):
        # Create the Dialog to be shown to the user: The user will be allowed to check/uncheck desired labels
        dialog = SelectMetaDataForTreeviewDialog(self.database_handler, 
                                                 self.blank_analysis_tree_view_manager, 
                                                 self.blank_analysis_plot_manager, 
                                                 frontend = self.frontend_style)
        dialog.exec()
        #dialog.finish_button.clicked.connect(
        #    partial(self.add_meta_data_to_tree_view,checkbox_list, name_list, dialog))


    
    
    