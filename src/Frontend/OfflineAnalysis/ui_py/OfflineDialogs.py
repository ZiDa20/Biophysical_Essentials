from Frontend.OfflineAnalysis.CustomWidget.SubstractDialog import SubstractDialog
from Frontend.OfflineAnalysis.CustomWidget.assign_meta_data_dialog_popup import Assign_Meta_Data_PopUp
from Frontend.OfflineAnalysis.CustomWidget.MetaDataPopupAnalysis import MetadataPopupAnalysis
from Frontend.OfflineAnalysis.CustomWidget.select_meta_data_for_treeview_handler import SelectMetaDataForTreeviewDialog
from Frontend.OfflineAnalysis.CustomWidget.ChooseSeriesDialog import SeriesDialog
from Frontend.OfflineAnalysis.CustomWidget.filter_pop_up_handler import Filter_Settings

from functools import partial

class OfflineDialogs:
    """_summary_: Class that should handle PopUps/Dialogs for the Offline Analysis
    """
    def __init__(self,
                 database_handler,
                 offline_manager,
                 frontend,
                 blank_analysis_plot_manager,
                 treeview_manager) -> None:


        self.database_handler = database_handler
        self.offline_manager = offline_manager
        self.frontend_style = frontend
        self.blank_analysis_tree_view_manager = treeview_manager
        self.series_dialog = None
        self.blank_analysis_plot_manager = blank_analysis_plot_manager
        self.final_series = []
        self.meta_data_popup = None

    def new_series_creation(self):
        """_summary_: Creates a Popup that can be used for new Series generation
        such as e.g Substraction/Addition of two equally length series
        """
        series_dialog = SubstractDialog(self.database_handler, self.frontend_style, self.edit_series_meta_data_popup, self.blank_analysis_plot_manager, self.blank_analysis_tree_view_manager)
        series_dialog.exec()

    def edit_metadata_analysis_id(self):
        """_summary_: Popup Dialog to edit the metadata of the selected experiments
        """
        # dialog needs to be global to be accessible in the unittest
        self.edit_data = MetadataPopupAnalysis(self.database_handler, self.frontend_style, series = False)
        self.edit_data.create_table()
        self.edit_data.submit.setAutoDefault(False)
        self.edit_data.quit.setAutoDefault(False)
        self.edit_data.submit.clicked.connect(partial(self.change_meta_data,True, self.edit_data))
        self.edit_data.show()

    def edit_series_meta_data_popup(self):
        """ _summary_: Popup Dialog to edit the metadata of the related series
        """
        # dialog needs to be global to be accessible in the unittest
        self.edit_data = MetadataPopupAnalysis(self.database_handler, self.frontend_style, series = True)
        self.edit_data.create_table()
        self.edit_data.submit.setAutoDefault(False)
        self. edit_data.quit.setAutoDefault(False)
        self.edit_data.submit.clicked.connect(partial(self.change_meta_data,False, self.edit_data))
        self.edit_data.show()

    def change_meta_data(self,experiment:bool, popup:MetadataPopupAnalysis):
        """_summary_: Function that will be called when the submit button is clicked in the MetaDataPopupAnalysis"""
        # write the update 
        popup.add_metadata_into_db(experiment)
        popup.close()

    def create_meta_data_template(self, save, make):
        """_summary_

        Args:
            save (function): Function that will be performed by the save button, saving the changed metadata into the database
            open (function): _description_
            make (function): _description_
            test (function): For testing purposes only
        """
        # open a new dialog with a tree view representation of the selected directory - only on experiment and series level
        meta_data_popup = Assign_Meta_Data_PopUp(self.database_handler, self.offline_manager, self.frontend_style)

        template_table_view = meta_data_popup.map_metadata_to_database()
        #meta_data_popup.save_to_template_button.clicked.connect(partial(save,
        #                                                                meta_data_popup))
        
        meta_data_popup.load_template.clicked.connect(partial(meta_data_popup.open_meta_data_template_file,template_table_view))
        meta_data_popup.continue_loading.clicked.connect(partial(make,meta_data_popup,template_table_view))
        meta_data_popup.exec_()
        
    def select_tree_view_meta_data(self, tree_view, plot_widget_manager,series_name=None):
        """_summary_
        """
        # Create the Dialog to be shown to the user: The user will be allowed to check/uncheck desired labels
        dialog = SelectMetaDataForTreeviewDialog(self.database_handler, 
                                                 tree_view, 
                                                 plot_widget_manager, 
                                                 frontend = self.frontend_style, 
                                                 series_name=series_name)
        dialog.exec()
        #dialog.finish_button.clicked.connect(
        #    partial(self.add_meta_data_to_tree_view,checkbox_list, name_list, dialog))

    def choose_series(self, selected_series_combo):
        """_summary_: Opens the PopUp Dialog for the Series selection which should be analyzed further

        Args:
            seleced_series_combo (QTCombobox): Combobox holding the individual selected series for the analysis
        """
        self.series_dialog = SeriesDialog(self.database_handler, self.frontend_style, selected_series_combo)
        
        # this would only work for a blocking dialog
        #self.final_series.extend(self.series_dialog.final_series)
        #print(self.final_series)

    def add_filter_to_offline_analysis(self):
        """_summary_: Will be called when the filter button is clicked and should open a popup to filter for certain parameters derived from the sweep metadata table
        """
        filter_dialog = Filter_Settings(self.frontend_style)
        filter_dialog.set_meta_data_filter_combobox_options(filter_dialog.meta_data_combo_box)
        filter_dialog.exec_()


