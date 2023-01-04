import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
from sklearn.preprocessing import StandardScaler

class SweepWiseAnalysisTemplate(object):
	"""
	Parent class to handle all analysis general processing to analyze each single sweep of a series:

	"""
	def __init__(self):

		# really needed ?
		self.function_name = None
		self.analysis_function_id = None

		self.data = None
		self.voltage = None

		self.database = None  # database
		self.plot_type_options : list = ["No Split", "Split by Meta Data"]

		self.cslow_normalization = 1

		self.lower_bound = None
		self.upper_bound = None
		self.time = None
		self.data = None

		self.sliced_volt = None

		self.database = None
		self.series_name = None

	@property
	def lower_bounds(self) -> float:
		""" get the lower and upper bounds 
  		
    	"""
		print("The lower bound: ")
		return self._lower_bounds

	@property
	def upper_bounds(self) -> float:
		print("The upper bound: ")
		return self._upper_bounds

	@lower_bounds.setter
	def lower_bounds(self, lower_bound: float):
		""" set the lower and upper bound """
		if type(lower_bound) in [int, float]:
			self._lower_bounds = lower_bound
		else:
			raise TypeError("Wrong Input please specificy floats")

	@upper_bounds.setter
	def upper_bounds(self, upper_bound:float):
		""" set the lower and upper bound """
		if type(upper_bound) in [int, float]:
			self._upper_bounds = upper_bound
		else:
			raise TypeError("Wrong Input please specificy floats")

	@classmethod
	def construct_trace(self):
		""" construct the trace """
		try:
			self.trace = np.vstack((self.time, self.data)).T
		except:
			raise ValueError("Please use the same dimension, only 1-dimensional arrays should be used")

	@classmethod
	def slice_trace(self):
		""" slice the trace based on the incoming upper and lower bounds """
		if all([self.lower_bound, self.upper_bound]):
			self.sliced_trace = self.trace[
				((self.trace[:, 0] > self.lower_bound) & (self.trace[:, 0] < self.upper_bound))]
			self.sliced_volt = self.sliced_trace[:, 1]
		else:
			raise ValueError("No upper and lower bonds set yet, please sets and use the rectangular function")

	def show_configuration_options(self):
		print("not implemented")

	@classmethod
	def live_data(self,lower_bound, upper_bound, experiment_name,series_identifier, database_handler, sweep_name = None):
		"""for each sweep, find correct x and y value to be plotted as live result
		@author: dz, 29.09.2022
		"""
		print("live ")
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
		data_table_name = database_handler.get_sweep_table_name(experiment_name,series_identifier)
		self.time = database_handler.get_time_in_ms_of_by_sweep_table_name(data_table_name)
		entire_sweep_table = database_handler.get_entire_sweep_table(data_table_name)

		# @Todo
		#series_specific_recording_mode = database_handler.get_recording_mode_from_analysis_series_table(self.series_name)

		print(entire_sweep_table)

		if sweep_name:
			print(sweep_name)
			data = entire_sweep_table.get(sweep_name)
			print(data)
			return [self.live_data_for_single_sweep(data)]
		else:
			return self.live_data_for_entire_series(entire_sweep_table)

	@classmethod
	def live_data_for_entire_series(self, entire_sweep_table) -> list:
		"""
		calculates a list of tuples (x_value, y-value) to be plotted on top in the trace plot for each sweep within a series
		@param entire_sweep_table:
		@return:
		@author: dz, 29.09.2022
		"""
		plot_data = []

		for column in entire_sweep_table:
			data = entire_sweep_table.get(column)
			plot_data.append((self.live_data_for_single_sweep(data)))

		return(plot_data)

	@classmethod
	def live_data_for_single_sweep(self, data):
		"""
		takes a single sweep, slices according defined coursor bounds and calculates the related x-yvalue tuple
		@param data:
		@return:
		@author: dz, 29.09.2022
		"""
		self.data = data

		#@todo
		# if series_specific_recording_mode != "Voltage Clamp":
		# y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
		# self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

		# slice trace according to coursor bounds
		self.construct_trace()
		self.slice_trace()


		return self.live_data_calculation()

	@classmethod
	def calculate_results(self):
		"""
		iterate through each single sweep of all not discarded series in the database and save the calculated result
		to a new database table.
		:return:
		"""

		# @todo get this from the configuration window


		series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)
		"""
		try:
			if series_specific_recording_mode == "Voltage Clamp":
				cslow_normalization = 1
			else:
				cslow_normalization = 0
		except Exception as e:
			print("Error in Excecute_Single_Series_Analysis")
			print(e)
			cslow_normalization = 0
		"""

		data_table_names = []
		# get the names of all data tables to be evaluated
		data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
		# set time to non - will be set by the first data frame
		# should assure that the time and bound setting will be only exeuted once since it is the same all the time
		self.time = None
		self.upper_bounds = None
		self.lower_bounds = None

		for data_table in data_table_names:

			#
			if self.time is None:
				self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)
			# calculate the time
			# set the lower bound
			# set the upper bound

			entire_sweep_table = self.database.get_entire_sweep_table(data_table)

			# added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
			# adding the name would increase readibility of the database ut also add a lot of redundant information
			column_names = ["Analysis_ID", "Function_Analysis_ID", "Sweep_Table_Name", "Sweep_Number", "Voltage", "Result"]
			result_data_frame = pd.DataFrame(columns = column_names)

			for column in entire_sweep_table:

				self.data = entire_sweep_table.get(column)

				if series_specific_recording_mode != "Voltage Clamp":
					y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
					self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

				# slice trace according to coursor bounds
				self.construct_trace()
				self.slice_trace()

				res = self.specific_calculation()

				print("result")
				print(res)
				if self.cslow_normalization:
					cslow = self.database.get_cslow_value_for_sweep_table(data_table)
					res = res / cslow
					print("normalized")
					print(res)

				# get the sweep number
				sweep_number = column.split("_")
				sweep_number = int(sweep_number[1])

				# get the related pgf value
				#	therefore get the pgf table for this series first
				pgf_data_frame = self.database.get_entire_pgf_table(data_table)
				# 	from the coursor bounds indentify the correct segment

				duration_list = pgf_data_frame.loc[:,"duration"].values
				increment_list = pgf_data_frame.loc[:,"increment"].values
				voltage_list = pgf_data_frame.loc[:,"voltage"].values

				duration_list_float = []
				volt_val = 0

				for i in range(0,len(duration_list)):
					duration_list_float.append(float(duration_list[i])*1000)

					# should be greater all the time until the correct segment is entered
					if self.lower_bound <= sum(duration_list_float):
						volt_val = (float(voltage_list[i])*1000) + (sweep_number-1)*(float(increment_list[i])*1000)
						break

				new_df = pd.DataFrame([[self.database.analysis_id,self.analysis_function_id,data_table,sweep_number,volt_val,res]],columns = column_names)

				result_data_frame = pd.concat([result_data_frame,new_df])

			# write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table

			new_specific_result_table_name = self.create_new_specific_result_table_name(self.analysis_function_id, data_table)
			self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
																				   self.analysis_function_id,
																				   data_table,
																				   new_specific_result_table_name,
																				   result_data_frame)

			print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')

	@classmethod
	def create_new_specific_result_table_name(cls, analysis_function_id:int, data_table_name:str) -> str:
		"""
		creates a unique name combination for the specific result table name for the specific calculation of a series by a specific function
		:param offline_analysis_id:
		:param data_table_name:
		:return:
		:author dz, 08.07.2022
		"""
		return "results_analysis_function_" +str(analysis_function_id) + "_" + data_table_name

	@classmethod
	def specific_calculation(self):
		# return None
		print("specific result calculation")

	@classmethod
	def run_late_register_feature(cls):
		print("not implemented for sweep wise")

	@classmethod
	def visualize_results(self, parent_widget) -> list:
		"""Function to retrieve the list result tables for the function analysis id

		Args:
			parent_widget (OfflineResultVisualizer): Widget to put the Analysis in 

		Returns:
			list: list of funciton id related tables
		"""
		result_table_names = self.get_list_of_result_tables(parent_widget.analysis_id, parent_widget.analysis_function_id)
		return result_table_names

	@classmethod
	def fetch_x_and_y_data(self, table_name: str,database) -> tuple:

		#@todo move this function to the database class ?
		# "Sweep_Table_Name", "Sweep_Number", "Voltage", "Result"

		table_name_increment = "pgf_table_" + "_".join(table_name.split("_")[-3:])
		q = f'select Sweep_Table_Name, Sweep_Number, Voltage, Result from {table_name}'
		q_increment =f'select Increment from {table_name_increment}'
		query_data = database.get_data_from_database(database.database, q)
		query_increment = mean([float(t) for i in database.get_data_from_database(database.database, q_increment) for t in i])
		
		# query data are quadruples of ("Sweep_Table_Name", "Sweep_Number", "Voltage", "Result")
		# therefore make lists of each tuple "column"
		x_data = (list(zip(*query_data))[3])
		y_data = (list(zip(*query_data))[2])
		sweep_tables = (list(zip(*query_data))[0])

		q = """select experiment_name from experiment_series where sweep_table_name = (?)"""
		experiment_name = database.get_data_from_database(database.database, q,
														  [query_data[0][0]]) [0][0]
		return x_data, y_data, experiment_name, query_increment, sweep_tables

	@classmethod
	def get_list_of_result_tables(self, analysis_id, analysis_function_id)-> list:
		"""	
  		
    	"""
		q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
		result_list = self.database.get_data_from_database(self.database.database, q,
														  [analysis_id, analysis_function_id])

		try:
			result_list = (list(zip(*result_list))[0])
		except Exception as e:
			print(e)
			result_list = []
		return result_list


	def plot_meta_data_wise(self, canvas, result_list:list, number_of_series:int, meta_data_groups:list):
		"""
        rearrange the plot to color each trace according to it's meta data group.

        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :param meta_data_groups:
        :return:
        """
		print("metadata construction")
		number_of_sweeps = int(len(result_list) / number_of_series)
		meta_data_types = list(dict.fromkeys(meta_data_groups))

		x_data, y_data, series_names = self.fetch_x_and_y_data(result_list, number_of_sweeps)
		# analysis_specific_plot_widget.addLegend()

		ax = canvas.figure.subplots()

		# for each data trace ( = a sub list) create the plot in the correct color according to meta data group
		for a in range(len(x_data)):

			meta_data_group = meta_data_groups[a]

			for m in meta_data_types:
				if m == meta_data_group:
					pos = meta_data_types.index(m)
					ax.plot(x_data[a], y_data[a], self.default_colors[pos], label=series_names[a])
					
			ax.legend()

	@classmethod
	def boxplot_calc(self, result_table_list:list, database):
		"""Creates the Data for the boxplot --> long table from the Result Tables
  
		Args:
			result_table_list (list): List of Result Table for the Analysis Id
			database (_type_): DataBase Handler

		Returns:
			pd.DataFrame: Contains long table with values,metadata, experiment name 
		"""
		meta_data_groups = []
		meta_data_types = []
		x_list = []

		# get the chosen meta data from the database
		q = f' select * from (select selected_meta_data from offline_analysis where analysis_id = {database.analysis_id}   )'
		meta_data_table = database.database.execute(q).fetchdf()
		

		for table in result_table_list:

			database.database.execute(f'select * from {table}')
			query_data_df = database.database.fetchdf()

			#print("querried data look like this")
			#print(query_data_df)


			q = f'select * from global_meta_data where experiment_name = (select experiment_name from ' \
				f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
				f'specific_result_table_name = \'{table}\'))'

			meta_data_group = database.database.execute(q).fetchdf()
			print(meta_data_group)
			# index has the same name as the function. Will not work if the names differ.
			#TODO scaling 
			try:
				x_data = 1000* query_data_df['Result'].values.tolist()[0]
			except Exception as e:
				print(e)
				break

			print("xdata  data look like this")
			print(x_data)

			if meta_data_group in meta_data_groups:
				meta_data_types.append(meta_data_group)
				x_list.append(x_data)
			else:
				# add a new meta data group
				meta_data_groups.append(meta_data_group)
				meta_data_types.append(meta_data_group)
				x_list.append(x_data)
		
		boxplot_df = pd.DataFrame()
		boxplot_df["values"] = x_list
		boxplot_df["meta_data"] = meta_data_types

		return boxplot_df
		# no nan handling required since sweeps without an AP are not stored in the dataframe


	@classmethod
	# Here we should also denote if we have an increment for this we would need the location of the 
	def simple_plot_calc(self, result_table_list: list, database) -> tuple:
		"""Calculates the data for the experiment aggregated data used in lineplots

		Args:
			result_table_list (list): List of Result Tables 
			database (_type_): DataBase Handler

		Returns:
			tuple: The plot_dataframe with as long table with experiment name, 
			values and indeces
		"""
		plot_data = {"Unit": [],"values":[], "name":[], "meta_data":[], "index":[]}
		increment_list = []
  
		for table in result_table_list:
    			
			try:
				q = f'select condition from global_meta_data where experiment_name = (select experiment_name from ' \
				f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
				f'specific_result_table_name = \'{table}\'))'
				y_data, x_data, experiment_name, increment, sweep_table = self.fetch_x_and_y_data(table, database)
				meta_data_group = database.get_data_from_database(database.database, q)[0][0]
				plot_data["values"].extend(y_data)
				plot_data["Unit"].extend(x_data)
				plot_data["name"].extend(len(x_data) * [experiment_name])
				plot_data["meta_data"].extend(len(x_data) * [meta_data_group])
				plot_data["index"].extend(range(len(x_data)))
				increment_list.append(increment)
				
			except Exception as e:
				print(e)
				break
		print(len(set(plot_data["Unit"])))

		if (len(set(plot_data["Unit"])) == 1) or  (mean(increment_list)==0):
			increment = True
		else:
			increment = None

		plot_dataframe = pd.DataFrame(plot_data)
		return plot_dataframe, increment

	@classmethod
	def rheobase_calc(self, result_table_list:list, database):
		"""Specific calculation for Rheobase Data constructed by the Rheobase Function

		Args:
			result_table_list (list): Result Table List from Rheobase ID
			database (duckDb): Database Handler

		Returns:
			pd.DataFrame: long table pd.DataFrame with Data for boxplot and lineplot plotting
		"""
		meta_data_groups = []
		first_ap = []
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

	@classmethod
	def sweep_rheobase_calc(self, result_table_list, database):
		"""Get the max voltage per sweep for the Rheobase from the Result_Max tables

		Args:
			result_table_list (list): list of result table for series
			database (database_handler): datadb Class which should handle the database

		Returns:
			plot_dataframe	pd.DataFrame: Dataframe containing the data for plotting
		"""
		meta_data_groups = []
		max_voltage = []
		current = []
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

	@classmethod
	def rheoramp_calc(self, result_table_list:list, database):
		"""Calculates the #APs per Sweep 

		Args:
			result_table_list (list): Result Table List Rheoramp
			database (duckDB): Database Handler

		Returns:
			_type_: DataFrame with the #APs per sweep and experiment logn table
		"""
		count = []
		rheo = []
		meta_data = []
		experiment_names = []

		for table in result_table_list:
			print(table)
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
		
	@classmethod
	def ap_calc(self, result_table_list:list, database):
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

