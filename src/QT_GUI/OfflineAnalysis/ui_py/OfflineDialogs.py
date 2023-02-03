from QT_GUI.OfflineAnalysis.CustomWidget.SubstractDialog import SubstractDialog
from QT_GUI.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp

class OfflineDialogs:
    """_summary_
    """
    def __init__(self, database_handler, offline_manager, frontend) -> None:
        """_summary_
        """
        self.database_handler = database_handler
        self.offline_manage = offline_manager
        self.frontend_style = frontend
    
    
    