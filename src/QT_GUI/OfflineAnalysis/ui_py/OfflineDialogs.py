from QT_GUI.OfflineAnalysis.CustomWidget.SubstractDialog import SubstractDialog
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from QT_GUI.OfflineAnalysis.CustomWidget.MetaDataPopupAnalysis import MetadataPopupAnalysis
class OfflineDialogs:
    """_summary_
    """
    def __init__(self, database_handler, offline_manager, frontend) -> None:
        """_summary_
        """
        self.database_handler = database_handler
        self.offline_manage = offline_manager
        self.frontend_style = frontend
        
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
    
    
    