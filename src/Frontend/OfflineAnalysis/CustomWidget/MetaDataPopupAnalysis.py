
from PySide6.QtWidgets import *  # type: ignore
from Frontend.OfflineAnalysis.CustomWidget.ui_metadata_analysis_popup import Ui_MetadataPopup
import pandas as pd
from Frontend.CustomWidget.Pandas_Table import PandasTable
from functools import partial

class MetadataPopupAnalysis(QDialog, Ui_MetadataPopup):

    def __init__(self, database_handler, frontend, series = False, parent=None) -> None:
        """_summary_: Initalize the MetaDataPopupModel

        Args:
            database_handler (DuckDB): the DuckDb database handler object
            frontend (Frontend): The Frontend Designer Class that holds the frontend object
            series (bool, optional): _description_. Defaults to False.
        """
        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database_handler
        self.frontend_style = frontend
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.content_model = None
        self.quit.clicked.connect(self.close)
        self.table_model = None
        self.scroll_area = QScrollArea()
        self.metadata_table = QTableView()
        self.scroll_area.setWidget(self.metadata_table)
        self.scroll_area.setWidgetResizable(True)
        self.metadata_table.setStyleSheet("border: 0.2px solid black")
        self.final_table_layout.addWidget(self.scroll_area, 0, 1)
        self.series = series
        
        if self.series:
            self.query = f'select * from series_analysis_mapping where experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})'
        else:
            self.query = f'select * from global_meta_data where experiment_name in (select experiment_name from experiment_analysis_mapping where analysis_id = {self.database_handler.analysis_id})'
            self.SearchSeries.hide()
            self.submitser.hide()
            self.label_2.hide()
        
        
    def create_table(self):
        """_summary_: This creates the MetaDataTable as Pandas Table
        """
        self.metadata_table.setSortingEnabled(True)
        self.retrieve_metadatatable_from_database()
        
    def retrieve_metadatatable_from_database(self):
        """_summary_: This retrieve the metadata table and sets the model
        """
        
        table_handling = self.database_handler.get_data_from_database(
            self.database_handler.database, self.query, fetch_mode=2
        )

        if self.series:
            table_handling  = table_handling[table_handling["analysis_id"]==self.database_handler.analysis_id]
    
        self.table_model = PandasTable(table_handling)

        
        self.submitexp.clicked.connect(partial(self.slide_search_model))
        self.submitser.clicked.connect(partial(self.slide_search_model, series = True))
        self.metadata_table.setModel(self.table_model)
        self.table_model.resize_header(self.metadata_table)
     

    def add_metadata_into_db(self,experiment:bool):
        """ This function overwrites existing metadata in the database
        """
        
        # @todo: this function overwrites the global meta data table, while the series annotation is only added to the series analysis mapping table
        # @todo: make sure that the appropriate table columns are blocked from editing
        new_df = self.table_model._data
        df = new_df
        for index, row in df.iterrows():
            if experiment:
                for c in ["experiment_label", "species", "genotype", "sex", "celltype","condition", "individuum_id"]:
                    #if row[c] != "None":
                    q = f"""update global_meta_data set {c} = \'{row[c]}\' where experiment_name = \'{row["experiment_name"]}\' """
                    self.database_handler.database.execute(q)
            else:
                # only update  the series meta data column !! 
                 q = f"""update experiment_series set series_meta_data = \'{row["series_meta_data"]}\' where experiment_name = \'{row["experiment_name"]}\' and series_identifier = \'{row["series_identifier"]}\'"""
                 self.database_handler.database.execute(q)
                 q = f"""update series_analysis_mapping set series_meta_data = \'{row["series_meta_data"]}\' where experiment_name = \'{row["experiment_name"]}\' and series_identifier = \'{row["series_identifier"]}\'"""
                 self.database_handler.database.execute(q)

        self.close()

    def slide_search_model(self, series = False):
        print(series)
        if series:
            text = self.SearchSeries.text()
            self.table_model.slice_series_data(text)
        else:
            text = self.SearchExperiment.text()
            self.table_model.slice_experiment_data(text)
        #self.metadata_table.dataChanged.connect()

  