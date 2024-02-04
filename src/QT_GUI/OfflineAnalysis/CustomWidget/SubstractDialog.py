from PySide6.QtWidgets import *  # type: ignore
from matplotlib.backends.backend_qtagg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from QT_GUI.OfflineAnalysis.CustomWidget.ui_SubstractDialog import Ui_CreateNewSeries
from CustomWidget.error_dialog_class import CustomErrorDialog

class SubstractDialog(Ui_CreateNewSeries):

    def __init__(self, database, frontend_style, metadata_open, plot_widget_manager, treeview_manager, parent=None):

        super().__init__(parent)
        self.setupUi(self)
        self.database_handler = database
        self.frontend_style = frontend_style
        self.plot_widget_manager = plot_widget_manager
        self.treeview_manager = treeview_manager
        self.checkbox_list = [self.add_s, self.substract_s, self.divide_s]
        if self.frontend_style.default_mode== 0:
            self.frontend_style.set_mpl_style_dark()
        else:
            self.frontend_style.set_mpl_style_white()
        self.canvas = FigureCanvas()
        self.canvas_preview = FigureCanvas()
        self.ax_preview = self.canvas_preview.figure.subplots()
        self.ax = self.canvas.figure.subplots()
        self.canvas_2 = FigureCanvas()
        self.ax_2 = self.canvas_2.figure.subplots()
        self.PlotGrid.addWidget(self.canvas)
        self.PlotGrid.addWidget(self.canvas_2)
        self.PreviewPlot.addWidget(self.canvas_preview)
        self.series_1.activated.connect(self.connected_box)
        self.series_2.activated.connect(self.connected_box_series_2)
        self.experiment_intersect_list = None
        self.fill_combobox_with_series()
        self.ExperimentCombo.activated.connect(self.retrieve_raw_data_series)
        self.PreviewSeries.clicked.connect(self.initialize_data_merge)
        self.AddMeta.clicked.connect(metadata_open)
        self.frontend_style.set_pop_up_dialog_style_sheet(self)
        self.AddDataBase.clicked.connect(self.write_into_database)
        self.AddDataBase.setEnabled(False)
        self.analysis_dictionary = {}
        self.selectbymetadata.toggled.connect(self.fill_only_metadata_options)

    def fill_only_metadata_options(self):
        """_summary_: Retrieves the initial experiments and series_names that can be identified for both series
        """
        if self.selectbymetadata.isChecked():
            self.fill_combobox_with_meta_series()
        else:
            self.fill_combobox_with_series()

    def fill_combobox_with_series(self):
        """_summary_: Retrieves the initial experiments and series_names that can be identified for both series
        as identified by the selected analysis_id which is available in the database handler
        """

        self.series_1.clear()
        analysis_id = self.database_handler.analysis_id
        unique_series_meta = self.database_handler.database.execute(f"Select series_name, series_identifier, series_meta_data from experiment_series WHERE experiment_name IN (Select experiment_name from experiment_analysis_mapping WHERE analysis_id = {analysis_id})").fetchdf()
        unique_series_meta = self.unique_series_return(unique_series_meta)
        self.series_1.addItems(unique_series_meta)
        self.connected_box()

    def unique_series_return(self, series, meta = False):
        """_summary_

        Args:
            series (pd.DataFrame): holding the series namess
            meta (bool, optional): _description_. Defaults to False.

        Returns:
            list: List of combined string of series:meta_data:series_identifier or if metadata
            then only series:meta_data
        """
        if meta:
            return list({f"{i}:{t}" for i, t in zip(series["series_name"],series["series_meta_data"]) if t not in  "None"})

        else:
            return sorted(list(
                {
                    f"{i}:{t}:{m}"
                    for i, t, m in zip(
                        series["series_name"],
                        series["series_meta_data"],
                        series["series_identifier"],
                    )
                }
            ))

    def fill_combobox_with_meta_series(self):
        """This fills the combobox only with the series and with the meta data
        Here we should add another layer, by providing evidence that this is only working if we
        have only one selected series per meta data group per experiment
        """
        self.series_1.clear()
        self.series_2.clear()
        unique_series_meta = self.database_handler.database.execute("Select series_name, series_identifier, series_meta_data from experiment_series ").fetchdf()
        unique_series_meta = self.unique_series_return(unique_series_meta, meta = True)

        if unique_series_meta:
            self.series_1.addItems(unique_series_meta)
            self.connected_box(meta = True)
        else:
            CustomErrorDialog("No Metadata found! Please first assign Metadata to each Series!", self.frontend_style)

    def select_series_to_be_analized(self):
        """
        executed after all experiment files have been loaded
        :return:
        """
        return self.database_handler.get_distinct_non_discarded_series_names()

    def connected_box_series_2(self):
        """_summary_: recheck the overlapping experiment names
        """
        experiment_names_1 = self.get_experiment_names(self.series_2)
        series_intersection = [i for i in self.experiment_intersect_list if i in experiment_names_1]
        self.ExperimentCombo.clear()
        self.ExperimentCombo.addItems(series_intersection)
        self.retrieve_raw_data_series()

    def connected_box(self, meta = False):
        """_summary_: Function that retrieves the experiment names fill the series 2 combobox
        in response to the series that are also present in the experiments where series 1 is preseent

        args:
            meta: If metadata is present or not
        """
        experiment_names_1 = self.get_experiment_names(self.series_1)
        series_name_2 = self.database_handler.database.execute(f"""Select series_name, series_identifier, series_meta_data, experiment_name from experiment_series
                                                                WHERE experiment_name IN {tuple(experiment_names_1)}""").fetchdf()

        self.experiment_intersect_list = sorted(series_name_2["experiment_name"].unique())
        if meta is True:
            #check if meta data was applied
            series_name_2 = self.unique_series_return(series_name_2.iloc[:,:-1], meta = True)
        else:
            series_name_2 = self.unique_series_return(series_name_2.iloc[:,:-1], meta = False)

        if series_name_2: # check if there is any existing series in the experiments that connects to the current sereies
            self.ExperimentCombo.clear()
            self.series_2.clear()
            self.ExperimentCombo.addItems(self.experiment_intersect_list)
            self.series_2.addItems(series_name_2)
            self.retrieve_raw_data_series()

        else:
            CustomErrorDialog("No experiments found for the second series", self.frontend_style)
            self.series_2.clear()

    def get_experiment_names(self, series):
        """_summary_: Should retrieve the experiment names either per with the meta data or with
        the series identifer, metadata only when the radiobutton is checked

        Args:
            series (QCombobox): The QCombobox holding the series names

        Returns:
            list: List of Experiments corresponding to the selected series
        """
        if self.selectbymetadata.isChecked is True:
            experiment_names_1 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id_with_meta(series.currenText().split(":")[0],series.currentText().split(":")[1])]
        else:
            experiment_names_1 = [i[0] for i in self.database_handler.get_experiments_by_series_name_and_analysis_id_with_series(series.currentText().split(":")[0],series.currentText().split(":")[2])]

        return experiment_names_1

    def retrieve_raw_data_series(self):
        """_summary: Should retrieve the Analysis Functions
        """
        sweep_tables_series_name_1 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText().split(":")[0], self.series_1.currentText().split(":")[1]) if self.ExperimentCombo.currentText() in i]
        sweep_tables_series_name_2 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_2.currentText().split(":")[0], self.series_2.currentText().split(":")[1]) if self.ExperimentCombo.currentText() in i]

        try:
            # retrieve the sweep tables
            sweep_table_1 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_1[0])
            sweep_table_2 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_2[0])
            self.draw_plots_series(sweep_table_1, self.ax, self.canvas)
            self.draw_plots_series(sweep_table_2, self.ax_2, self.canvas_2)
            return sweep_table_1, sweep_table_2
        except Exception as e:
            print(e)
            return None

    def draw_plots_series(self, sweep_table, ax, canvas):
        """_summary_: Draw Series Function

        Args:
            sweep_table (pd.DataFrame): The dataframe holding the sweep table to draw
            ax (axes): the axes to draw in
            canvas (FigureCanvas): The Figure Canvas to draw in
        """
        ax.clear()
        ax.plot(sweep_table)
        canvas.draw_idle()

    def retrieve_sweep_table_iterator(self, experiment_name):
        """_summary_ This should retrieve the sweep tables for the selected series_1 and 2

        Args:
            experiment_name (str): experiment name that is present for both selected series

        Returns:
            tuple(pd.DataFrame): Holding the Sweep Tables for series_1 and 2
        """
        sweep_tables_series_name_1 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_1.currentText().split(":")[0], self.series_1.currentText().split(":")[1]) if experiment_name in i]
        sweep_tables_series_name_2 = [i for i in self.database_handler.get_sweep_table_names_for_offline_analysis(self.series_2.currentText().split(":")[0], self.series_2.currentText().split(":")[1]) if experiment_name in i]
        sweep_table_1 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_1[0])
        sweep_table_2 = self.database_handler.get_entire_sweep_table_as_df(sweep_tables_series_name_2[0])
        return sweep_table_1, sweep_table_2

    def initialize_data_merge(self):
        """_summary_
        """
        if not any(checkbox.isChecked() for checkbox in self.checkbox_list):
            print("no function is checked yet please check a function")
            CustomErrorDialog("Please select a Series Analysis Option from the checkboxes", self.frontend_style)
            return None
        count = 1
        for i in self.checkbox_list:

            if i.isChecked():
                analysis_option = i.text()
                analysis_dictionary_temp = {}
                items = []
                for i in range(self.ExperimentCombo.count()):
                    items.append(self.ExperimentCombo.itemText(i))

                for experiment_name in items:
                    sweep_table_1, sweep_table_2 = self.retrieve_sweep_table_iterator(experiment_name)
                    #calculation
                    if sweep_table_1.shape == sweep_table_2.shape: 
                        match analysis_option:
                            case "Add":
                                new_table = sweep_table_1 + sweep_table_2
                            case "Divide":
                                new_table = sweep_table_1 / sweep_table_2
                            case "Substract":
                                new_table = sweep_table_1 - sweep_table_2
                                
                    else:
                        CustomErrorDialog("The Sweep Tables do not have the same shape, please check the data", self.frontend_style)

                    #metadata that should be written into the database
                    series_len = self.database_handler.database.execute(f"Select * from experiment_series WHERE experiment_name = '{experiment_name}'").fetchdf().shape[0]
                    series_len += count
                    series_name = f"Series{series_len}"
                    discarded = "False"

                    # get the default labels with series name and meta data name
                    series_name_1 = self.series_1.currentText().split(':')[0]
                    series_name_2 = self.series_2.currentText().split(':')[0]
                    series_meta_1 = self.series_1.currentText().split(':')[1]
                    series_meta_2 = self.series_2.currentText().split(':')[1]
                    check = self.selectbymetadata.isChecked()
             
             
                    # if only metadata where selected than we need to retrieve the series
                    if self.selectbymetadata.isChecked is True:
                        series_name_1_identifier = self.database_handler.database.execute(f"Select series_identifier from experiment_series WHERE experiment_name = '{experiment_name}' AND series_meta_data = '{series_meta_1}'").fetchall()[0][0]
                        series_name_2_identifier = self.database_handler.database.execute(f"Select series_identifier from experiment_series WHERE experiment_name = '{experiment_name}' AND series_meta_data = '{series_meta_2}'").fetchall()[0][0]
                        if series_name_1_identifier == series_name_2_identifier:
                            print("Same series choosen therefore analysis not run further!!!!")
                            CustomErrorDialog("You selected the same Series! Please use two different Series!", self.frontend_style)
                            return
                    else:
                        series_name_1_identifier = self.series_1.currentText().split(':')[2]
                        series_name_2_identifier = self.series_2.currentText().split(':')[2]

                    # retrieve the metadatatable and the pgf table
                    series_meta = self.database_handler.database.execute(f"Select meta_data_table_name, pgf_data_table_name from experiment_series WHERE experiment_name = '{experiment_name}' AND series_name = '{series_name_1}' AND series_identifier = '{series_name_1_identifier}'").fetchall()
                    series_name_table = f"{analysis_option}_{series_name_1}_{series_name_2}_{series_meta_1}_{series_meta_2}"
                    # creates a new specific table name
                    table_name = self.create_new_specific_result_table_name(experiment_name, series_name)
                    analysis_dictionary_temp[experiment_name + series_name_1 + series_name_2] = (experiment_name,series_name_table, series_name, discarded, table_name, series_meta[0][0], series_meta[0][1],"None", new_table)
                self.analysis_dictionary.update({analysis_option:analysis_dictionary_temp})

        self.AddDataBase.setEnabled(True)
        print("Succesfully substracted series")
        self.switch_to_preview()

    def switch_to_preview(self):
        """_summary_: Switched the SeriesStacked notebook to the preview page
        """
        self.SeriesStacked.setCurrentIndex(1)
        self.Operations.addItems(self.analysis_dictionary.keys())
        self.Operations.currentIndexChanged.connect(self.show_newly_created_series)
        self.show_newly_created_series()

    def show_newly_created_series(self):
        """_summary_: This should draw the newly created series for each experiment
        """
        operation = self.Operations.currentText()
        operation_dict = self.analysis_dictionary[operation]
        self.Experiment.clear()
        self.Experiment.addItems(operation_dict.keys())
        self.Experiment.activated.connect(lambda index: self.show_series_plot(operation_dict))
        self.show_series_plot(operation_dict)

    def show_series_plot(self, operation):
        """_summary_: This should show the newly created series plot
        after selection of the experiment

        Args:
            operation (dict): Dictionary holding the Substracted Series with all data necessary
            for the addition to the database under the operational key
        """
        selected_experiment = self.Experiment.currentText()
        table = operation[selected_experiment][-1]
        self.draw_plots_series(table, self.ax_preview, self.canvas_preview)

    def create_new_specific_result_table_name(self,experiment_name, series_number) -> str:
        """
        creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
        :param offline_analysis_id:
        :param data_table_name:
        :return:
        :author dz, 08.07.2022
        """
        return f"imon_signal_{experiment_name}_{series_number}"

    def write_into_database(self):
        """_summary_: Writes all the substracted data into the dataset and updates the treeview
        so that newly generated series can be used as series!!
        """
        for _, exp in self.analysis_dictionary.items():
            for _, value in exp.items():
                imon_name = value[4]
                imon_table = value[8]
                self.database_handler.database.execute(f"Create Table {imon_name} AS SELECT * FROM imon_table")
                self.database_handler.database.execute(f"Insert into experiment_series VALUES ('{value[0]}', '{value[1]}', '{value[2]}', '{value[3]}', '{value[4]}', '{value[5]}', '{value[6]}', '{value[7]}')")
                
                self.database_handler.database.execute(f"Insert into series_analysis_mapping VALUES ('{self.database_handler.analysis_id}', '{value[0]}', '{value[1]}', '{value[2]}', '{value[2]}', '{value[3]}')")

        self.treeview_manager.update_treeviews(self.plot_widget_manager)
        self.close()





