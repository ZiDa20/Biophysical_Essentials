import numpy as np
import pandas as pd
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
import array
from sklearn.preprocessing import StandardScaler

class SpecificAnalysisFunctions():
    
    @staticmethod
    def  boxplot_calc(result_table_list:list, database):
        """Creates the Data for the boxplot --> long table from the Result Tables

        Args:
            result_table_list (list): List of Result Table for the Analysis Id
            database (_type_): DataBase Handler

        Returns:
            pd.DataFrame: Contains long table with values,metadata, experiment name 
        """
       
        x_list =[] # make an array for the data
        experiment_name_list = []
        
        for table in result_table_list:
            database.database.execute(f'select * from {table}')
            query_data_df = database.database.fetchdf()
            experiment_name = "_".join(table.split("_")[-3:-1])
           
            try:
                x_data = 1000* query_data_df['Result'].values.tolist() #toDO Scaling
            except Exception as e:
                print(e)
                break
            
            x_list.extend(list(set(x_data)))
            experiment_name_list.append(experiment_name*len(list(set(x_data))))
        
    
        boxplot_df = pd.DataFrame()
        boxplot_df["values"] = x_list
        boxplot_df["experiment_name"] = experiment_name_list
        return boxplot_df
        # no nan handling required since sweeps without an AP are not stored in the dataframe

    # Here we should also denote if we have an increment for this we would need the location of the 
    @staticmethod	
    def simple_plot_calc(result_table_list: list, database) -> tuple:
            
        """Calculates the data for the experiment aggregated data used in lineplots

        Args:
            result_table_list (list): List of Result Tables 
            database (_type_): DataBase Handler

        Returns:
            tuple: The plot_dataframe with as long table with experiment name, 
            values and indeces
        """
        plot_data = {"Unit": [],"values":array.array("d"), "experiment_name":[], "index":[]}
        increment_list = []

        for table in result_table_list:
                
            try:
                y_data, x_data, experiment_name, increment, sweep_table = SweepWiseAnalysisTemplate.fetch_x_and_y_data(table, database)
        
                # add data to dictionary
                plot_data["values"].extend(y_data)
                plot_data["Unit"].extend(x_data)
                plot_data["experiment_name"].extend(len(x_data) * [experiment_name])
                plot_data["index"].extend(range(len(x_data)))
                increment_list.append(increment)
                
            except Exception as e:
                print(f"The functin the error was is simple cal: {e}")
                break
        if (len(set(plot_data["Unit"])) == 1) or  (mean(increment_list)==0):
            increment = True
        else:
            increment = None

        plot_dataframe = pd.DataFrame(plot_data)
        return plot_dataframe, increment

    @staticmethod
    def rheobase_calc(result_table_list:list, database):
        """Specific calculation for Rheobase Data constructed by the Rheobase Function

        Args:
            result_table_list (list): Result Table List from Rheobase ID
            database (duckDb): Database Handler

        Returns:
            pd.DataFrame: long table pd.DataFrame with Data for boxplot and lineplot plotting
        """
        meta_data_groups = []
        first_ap = array.array("d")
        experiment_names = []

        for table in result_table_list:
            if "_max" not in table:
                database.database.execute(f'select * from {table}')
                experiment_name = "_".join(table.split("_")[-3:-1])
                query_data_df = database.database.fetchdf()

                q = f'select condition from global_meta_data where experiment_name = (select experiment_name from ' \
                    f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                    f'specific_result_table_name = \'{table}\'))'

                first_ap.extend(query_data_df["1st AP"])
                meta_data_group = database.get_data_from_database(database.database, q)[0][0]
                if meta_data_group:
                    meta_data_groups.extend([meta_data_group])
                else:
                    meta_data_groups.extend(["None"])
                experiment_names.extend([experiment_name])

        plot_dataframe = pd.DataFrame()
        plot_dataframe["AP"] = first_ap
        plot_dataframe["Meta_data"] = meta_data_groups
        plot_dataframe["experiment_name"] = experiment_name
        return plot_dataframe

    @staticmethod
    def sweep_rheobase_calc(result_table_list, database):
        """Get the max voltage per sweep for the Rheobase from the Result_Max tables

        Args:
            result_table_list (list): list of result table for series
            database (database_handler): datadb Class which should handle the database

        Returns:
            plot_dataframe	pd.DataFrame: Dataframe containing the data for plotting
        """
        meta_data_groups = []
        max_voltage = array.array("d")
        current = array.array("d")
        experiment_names = []

        for table in result_table_list:
            if "_max" in table:
                database.database.execute(f'select * from {table}')
                experiment_name = "_".join(table.split("_")[-3:-1])
                query_data_df = database.database.fetchdf()

                q = f'select condition from global_meta_data where experiment_name = (select experiment_name from ' \
                    f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                    f'specific_result_table_name = \'{table}\'))'

                max_voltage.extend(query_data_df["max_voltage"])
                current.extend(query_data_df["current"])
                meta_data_group = database.get_data_from_database(database.database, q)[0][0]
                meta_data_groups.extend(query_data_df.shape[0]*[meta_data_group])
                experiment_names.extend(query_data_df.shape[0]*[experiment_name])

        plot_dataframe = pd.DataFrame()
        plot_dataframe["voltage"] = max_voltage
        plot_dataframe["current"] = current
        plot_dataframe["Meta_data"] = meta_data_groups
        plot_dataframe["experiment_name"] = experiment_name
        return plot_dataframe

    @staticmethod
    def rheoramp_calc(result_table_list:list, database):
        """Calculates the #APs per Sweep 

        Args:
            result_table_list (list): Result Table List Rheoramp
            database (duckDB): Database Handler

        Returns:
            _type_: DataFrame with the #APs per sweep and experiment logn table
        """
        count = array.array("i")
        rheo = []
        meta_data = []
        experiment_names = []

        for table in result_table_list:
            experiment_name = "_".join(table.split("_")[-3:-1])
            database.database.execute(f'select * from {table}')
            query_data_df = database.database.fetchdf()
            q = f'select condition from global_meta_data where experiment_name = (select experiment_name from ' \
                    f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                    f'specific_result_table_name = \'{table}\'))'

            meta_data_group = database.get_data_from_database(database.database, q)[0][0]
            rheobase = 1
            for column in query_data_df:

                data = query_data_df.get(column)
                data = data.dropna(how='all')
                data = data.values.tolist()
                number = len(data)
                if number == 0:
                    count.append(0)
                else: 
                    count.append(number)
                rheo.append("Rheo_"+str(rheobase) + "x")
                rheobase += 1
                meta_data.append(meta_data_group)
                experiment_names.append(experiment_name)
        

        plot_dataframe = pd.DataFrame()
        plot_dataframe["Number AP"] = count
        plot_dataframe["Rheoramp"] = rheo
        plot_dataframe["Meta_data"] = meta_data
        plot_dataframe["experiment_name"] = experiment_names
        return plot_dataframe
        
    @staticmethod
    def ap_calc(result_table_list:list, database):
        """
        Creates the AP propertie table frmo the AP fitting result table
        Args:
            result_table_list (list): Result Tables from AP fitting
            database (duckDB): database handler
        """

        meta_data_groups = []
        dataframe = pd.DataFrame()
        experiment_names = []
        for table in result_table_list:
            experiment_name = "_".join(table.split("_")[-3:-1])
            database.database.execute(f'select * from {table}')
            query_data_df = database.database.fetchdf()
            query_data_df.set_index('Fitting Parameters', inplace =True, drop = True)

            # here we can may switch to a join might be faster than iterating database queries
            q = f'select condition from global_meta_data where experiment_name = (select experiment_name from ' \
                f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
                f'specific_result_table_name = \'{table}\'))'
            experiment_names.extend(query_data_df.shape[1]*[experiment_name])
            dataframe = pd.concat([dataframe, query_data_df], axis = 1)
            # should still be added
            meta_data_group = database.get_data_from_database(database.database, q)[0][0]
            meta_data_groups.extend(query_data_df.shape[1]*[experiment_name])	

        dataframe = dataframe.transpose()
        dataframe["Meta_data"] = meta_data_groups
        dataframe["experiment_name"] = experiment_names

        z_score = StandardScaler().fit_transform(dataframe.iloc[:,0:-2].values)
        z_score_df = pd.DataFrame(z_score, columns = dataframe.iloc[:,0:-2].columns, index = dataframe.experiment_name)

        return dataframe, z_score_df

    def pca_calc(result_table_list:list, database):
        """Calculates the 1st and 2nd Principal Component of the queried 
        data --> e.g. Action Potential Parameters

        Args:
            result_table_list (list): list of result_tables generated by calculated result
            databaes (DuckDB): DuckDB Database Haendler
        """
        
        print("needs to be implemented")
