import numpy as np
import pandas as pd
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *
import array
#from scikit-learn import StandardScaler
#from scikit-learn import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class SpecificAnalysisFunctions():
    
    @staticmethod
    def  boxplot_calc(result_table:tuple, database):
        """Creates the Data for the boxplot --> long table from the Result Tables

        Args:
            result_table (tuple): List of Result Table for the Analysis Id
            database (): DataBase Handler

        Returns:
            pd.DataFrame: Contains long table with values,metadata, experiment name 
        """
       
        plot_dataframe = database.database.execute(f'select * from {result_table[0]}').fetchdf()
        
        return plot_dataframe
        # no nan handling required since sweeps without an AP are not stored in the dataframe

    # Here we should also denote if we have an increment for this we would need the location of the 
    @staticmethod	
    def simple_plot_calc(result_table: list, database) -> tuple:
            
        """Calculates the data for the experiment aggregated data used in lineplots

        Args:
            result_table_list (list): List of Result Tables 
            database (_type_): DataBase Handler

        Returns:
            tuple: The plot_dataframe with as long table with experiment name, 
            values and indeces
        """
        
        sweep_table, increment= SweepWiseAnalysisTemplate.fetch_x_and_y_data(result_table, database)
       

        return sweep_table, increment
    
    
    @staticmethod
    def rheobase_calc(result_table_list:list, database):
        """Specific calculation for Rheobase Data constructed by the Rheobase Function

        Args:
            result_table_list (list): Result Table List from Rheobase ID
            database (duckDb): Database Handler

        Returns:
            pd.DataFrame: long table pd.DataFrame with Data for boxplot and lineplot plotting
        """

        for table in result_table_list:
            if "_max" not in table:
                plot_dataframe = database.database.execute(f'select * from {table}').fetchdf()
        plot_dataframe.columns = ["Result", "experiment_name","Sweep_Table_Name"]
        return plot_dataframe

    @staticmethod
    def sweep_rheobase_calc(result_table_list, database):
        """Get the max voltage per sweep for the Rheobase from the Result_Max tables

        Args:
            result_table_list (tuple): list of result table for series
            database (database_handler): datadb Class which should handle the database

        Returns:
            plot_dataframe	pd.DataFrame: Dataframe containing the data for plotting
        """
   
        for table in result_table_list:
            if "_max" in table:
                query_data_df = database.database.execute(f'select * from {table}').fetchdf()
            
        return query_data_df

    @staticmethod
    def rheoramp_calc(result_table:tuple, database):
        """Calculates the #APs per Sweep 

        Args:
            result_table_list (tuple): Result Table List Rheoramp
            database (duckDB): Database Handler

        Returns:
            _type_: DataFrame with the #APs per sweep and experiment logn table
        """
       
        return database.database.execute(f'select * from {result_table[0]}').fetchdf()
        
    @staticmethod
    def ap_calc(result_table:tuple, database):
        """
        Creates the AP propertie table frmo the AP fitting result table
        Args:
            result_table_list (tuple): Result Tables from AP fitting
            database (duckDB): database handler
        """

        plot_dataframe = database.database.execute(f'select * from {result_table[0]}').fetchdf()
        #plot_dataframe = plot_dataframe.dropna(axis = 0)
        print(plot_dataframe.columns)
        df_names_to_drop = ['Analysis_ID', 'Function_Analysis_ID', 'Sweep_Table_Name', 'Sweep_Number', 
                            'Current', 'Duration', 'Result', 'Increment', 'experiment_name',
                            'series_meta_data','analysis_id','experiment_label','species','genotype','sex','celltype','condition','individuum_id']
        
        z_df = plot_dataframe.drop(columns=[col for col in plot_dataframe.columns if col in df_names_to_drop])
       
        # Create a DataFrame with only the dropped columns
        df_dropped = plot_dataframe[[col for col in plot_dataframe.columns if col in df_names_to_drop]]

        # todo here: ap fitting/firing pattern header columns are not standardized
        # z scaling can be only done for the non z scaled parameters
        z_score = StandardScaler().fit_transform(z_df.values)
        z_score_df = pd.DataFrame(z_score, columns = z_df.columns)

        z_score_df = pd.concat([z_score_df,df_dropped],axis=1)
        #z_score_df["experiment_name"] = plot_dataframe.experiment_name
        #z_score_df["Sweep_Table_Name"] =plot_dataframe.Sweep_Table_Name

        return plot_dataframe, z_score_df

    @staticmethod
    def pca_calc(result_table:tuple, database,plot_dataframe=None):
        """Calculates the 1st and 2nd Principal Component of the queried 
        data --> e.g. Action Potential Parameters

        Args:
            result_table_list (tuple): list of result_tables generated by calculated result
            databaes (DuckDB): DuckDB Database Haendler
        """
        
        df_names_to_drop = ['Analysis_ID', 'Function_Analysis_ID', 'Sweep_Table_Name', 'Sweep_Number', 
                            'Current', 'Duration','Voltage', 'Increment', 'experiment_name',
                            'series_meta_data','analysis_id','experiment_label','species','genotype','sex','celltype','condition','individuum_id']
       
        if plot_dataframe is None:
            plot_dataframe = database.database.execute(f'select * from {result_table[0]}').fetchdf()
        #plot_dataframe = plot_dataframe.dropna(axis = 0)
        reduced_df = plot_dataframe.drop(columns=[col for col in plot_dataframe.columns if col in df_names_to_drop])
        reduced_df = reduced_df.dropna(axis = 1) # drop columns with nan values
        for col in reduced_df.columns:
            reduced_df[col] = reduced_df[col].values.astype(np.float64)
            print(reduced_df[col].values.dtype)

        scaled = StandardScaler().fit_transform(reduced_df.values)
        pca = PCA(n_components=2)
        pca_data = pca.fit_transform(scaled)
        explained_variance = pca.explained_variance_ratio_.tolist()
        pca_dataframe = pd.DataFrame(pca_data, columns = ["PC1", "PC2"])
        pca_dataframe["experiment_name"] = plot_dataframe["experiment_name"]
        pca_dataframe["Sweep_Table_Name"] = plot_dataframe["Sweep_Table_Name"]
        #pca_dataframe["meta_data"] = plot_dataframe["meta_data"]
        #plot_dataframe = plot_dataframe.dropna(axis = 0)
        
        return pca_dataframe, explained_variance
    
    @staticmethod
    def overlay_cal(result_table:list, database):
        query_data_df = database.database.execute(f'select * from {result_table[0]}').fetchdf()
        return query_data_df



