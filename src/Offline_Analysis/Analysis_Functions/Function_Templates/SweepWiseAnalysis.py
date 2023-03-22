import numpy as np
import pandas as pd
import seaborn as sns
from statistics import mean
import logging
from abc import ABC, abstractmethod

class SweepWiseAnalysisTemplate(ABC):
	"""
	Parent class to handle all analysis general processing to analyze each single sweep of a series:
	# Still this is not appropriately implemented --> basically never initalized
	"""
	database = None
	data_shape = None
	analysis_function_id = None
	time = None
	upper_bounds = None
	lower_bounds = None
	plot_type_options : list = ["No Split"]
	cslow_normalization = 1
	database = None  # database
		
  
	"""
	@property
	def lower_bounds(self) -> float:
		\""" get the lower and upper bounds 
    	\"""
		print("The lower bound: ")
		return self._lower_bounds

	@property
	def upper_bounds(self) -> float:
		print("The upper bound: ")
		return self._upper_bounds

	@lower_bounds.setter
	def lower_bounds(self, lower_bound: float):
		\""" set the lower and upper bound \"""
		if type(lower_bound) in [int, float]:
			self._lower_bounds = lower_bound
		else:
			raise TypeError("Wrong Input please specificy floats")

	@upper_bounds.setter
	def upper_bounds(self, upper_bound:float):
		\""" set the lower and upper bound \"""
		if type(upper_bound) in [int, float]:
			self._upper_bounds = upper_bound
		else:
			raise TypeError("Wrong Input please specificy floats")
	"""
 
 
	@classmethod
	def construct_trace(cls):
		""" construct the trace """
		try:
			cls.trace = np.vstack((cls.time, cls.data)).T
		except ValueError as e:
			# we need to add logging here!
			raise ValueError("Please use the same dimension, only 1-dimensional arrays should be used")

	@classmethod
	def slice_trace(cls):
		""" slice the trace based on the incoming upper and lower bounds """
		if all([cls.lower_bound, cls.upper_bound]):
			cls.sliced_trace = cls.trace[
				((cls.trace[:, 0] > cls.lower_bound) & (cls.trace[:, 0] < cls.upper_bound))]
			cls.sliced_volt = cls.sliced_trace[:, 1]
		else:
			raise ValueError("No upper and lower bonds set yet, please sets and use the rectangular function")

	def show_configuration_options(self):
		print("not implemented")

	@classmethod
	def live_data(cls,lower_bound, upper_bound, experiment_name,series_identifier, database_handler, sweep_name = None):
		"""for each sweep, find correct x and y value to be plotted as live result
		@author: dz, 29.09.2022
		"""
		cls.lower_bound = lower_bound
		cls.upper_bound = upper_bound
		data_table_name = database_handler.get_sweep_table_name(experiment_name,series_identifier)
		cls.time = database_handler.get_time_in_ms_of_by_sweep_table_name(data_table_name)
		entire_sweep_table = database_handler.get_entire_sweep_table(data_table_name)

		if not sweep_name:
			return cls.live_data_for_entire_series(entire_sweep_table)

		data = entire_sweep_table.get(sweep_name)
		return [cls.live_data_for_single_sweep(data)]

	@classmethod
	def live_data_for_entire_series(cls, entire_sweep_table) -> list:
		"""
		calculates a list of tuples (x_value, y-value) to be plotted on top in the trace plot for each sweep within a series
		@param entire_sweep_table:
		@return:
		@author: dz, 29.09.2022
		"""
		plot_data = []

		for column in entire_sweep_table:
			data = entire_sweep_table.get(column)
			plot_data.append((cls.live_data_for_single_sweep(data)))

		return(plot_data)

	@abstractmethod
	def specific_calculation(cls):
		"""_summary_: Should implement the specific analyssis function in the abstractclass subclasses
		"""
		pass

	@classmethod
	def live_data_for_single_sweep(cls, data):
		"""
		takes a single sweep, slices according defined coursor bounds and calculates the related x-yvalue tuple
		@param data:
		@return:
		@author: dz, 29.09.2022
		"""
		cls.data = data
		#@todo
		# if series_specific_recording_mode != "Voltage Clamp":
		# y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
		# self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))

		# slice trace according to coursor bounds
		cls.construct_trace()
		cls.slice_trace()
		return cls.live_data_calculation()

	@classmethod
	def calculate_results(cls):
		"""
		iterate through each single sweep of all not discarded series in the database and save the calculated result
		to a new database table.
		:return:
		"""

		data_table_names = cls.database.get_sweep_table_names_for_offline_analysis(cls.series_name)
		# check here if current or voltage clamp and add the respective name of the unit to the table
		unit_name = cls.get_current_recording_type()
			# set time to non - will be set by the first data frame
		# should assure that the time and bound setting will be only exeuted once since it is the same all the time
		column_names = ["Analysis_ID", "Function_Analysis_ID", "Sweep_Table_Name", "Sweep_Number", unit_name, "Result", "Increment","experiment_name"]
		merged_all_results = pd.DataFrame(columns = column_names)
		# get the pgf segment whic hwas selected by the user and stored in the db
		pgf_segment = cls.database.database.execute(f'select pgf_segment from analysis_functions where analysis_function_id = {cls.analysis_function_id}').fetchall()[0][0]
		
		for data_table in data_table_names:

			# retrieves the experiment name
			experiment_name = cls.database.get_experiment_from_sweeptable_series(cls.series_name,data_table)
			entire_sweep_table = cls.database.get_entire_sweep_table(data_table)
			if cls.time is None:
				cls.time = cls.database.get_time_in_ms_of_by_sweep_table_name(data_table)
			#set the current_time if it changes
			cls.set_current_time_shape(entire_sweep_table,data_table)
			# pgf table is also just once per data_table and not per sweep
			pgf_data_frame = cls.database.get_entire_pgf_table(data_table)
			if cls.cslow_normalization: # check normalization strategy --> here strategy pattern needs to be implemented!
					cslow = cls.database.get_cslow_value_for_sweep_table(data_table)
			
			# added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
			# adding the name would increase readibility of the database ut also add a lot of redundant information
			for column in entire_sweep_table:
				cls.data = entire_sweep_table.get(column)
				# This is the hickup why we have to use 
				if unit_name != "Voltage":
					y_min, y_max = cls.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
					cls.data = np.interp(cls.data, (cls.data.min(), cls.data.max()), (y_min, y_max))

				# slice trace according to coursor bounds
				cls.construct_trace()
				cls.slice_trace()
				res = cls.specific_calculation()

				# normalize if necessary
				# toDO add logging here

				if cls.cslow_normalization:
					res = res / cslow

				# get the sweep number
				sweep_number = column.split("_")
				sweep_number = int(sweep_number[1])

				# get the related pgf value
				#	therefore get the pgf table for this series first
				
				# 	from the coursor bounds indentify the correct segment
				increment_list = pgf_data_frame["increment"].values
				voltage_list = pgf_data_frame["voltage"].values

				inc = (float(increment_list[pgf_segment-1])*1000)
				volt_val = (float(voltage_list[pgf_segment-1])*1000) + (sweep_number-1)*inc
	
				new_df = pd.DataFrame([[cls.database.analysis_id,cls.analysis_function_id,data_table,sweep_number,volt_val,res,inc,experiment_name]],columns = column_names)
				merged_all_results = pd.concat([merged_all_results,new_df])


		# write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table
		#print(f"This is the analysis function id : {cls.analysis_function_id}")
		new_specific_result_table_name = cls.database.create_new_specific_result_table_name(cls.analysis_function_id, cls.function_name)
		cls.database.update_results_table_with_new_specific_result_table_name(cls.database.analysis_id,
																				cls.analysis_function_id,
																				data_table,
																				new_specific_result_table_name,
																				merged_all_results)

		#print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')
	@classmethod
	def get_current_recording_type(cls):
		"""_summary_: Should return the current recording mode

		Returns:
			unit_name (str): The name of the current unit for recordings either Voltage or Current
		"""
		return (
			"Current"
			if cls.database.get_recording_mode_from_analysis_series_table(cls.series_name) != "Voltage Clamp"
			else "Voltage"
		)

	@classmethod
	def set_current_time_shape(cls, entire_sweep_table, current_data_table: str):
		"""_summary_: Function that should check the current shape of time and if it changes
			than time should be updated, might happen when different protocols with same names are used

		Args:
			entire_sweep_table (pd.DataFrame): _description_
			current_data_table (str): _description_
		"""
		if entire_sweep_table[list(entire_sweep_table.keys())[0]].shape != cls.data_shape:
			cls.data_shape = entire_sweep_table[list(entire_sweep_table.keys())[0]].shape
			cls.time = cls.database.get_time_in_ms_of_by_sweep_table_name(current_data_table)

	def run_late_register_feature(self):
		print("not implemented for sweep wise")

	@classmethod
	def visualize_results(cls, parent_widget) -> list:
		"""Function to retrieve the list result tables for the function analysis id

		Args:
			parent_widget (OfflineResultVisualizer): Widget to put the Analysis in 

		Returns:
			list: list of funciton id related tables
		"""
		return cls.get_list_of_result_tables(parent_widget.analysis_id, parent_widget.analysis_function_id)

	@staticmethod
	def fetch_x_and_y_data(table_name: str,database) -> tuple:

		#@todo move this function to the database class ?
		# "Sweep_Table_Name", "Sweep_Number", "Voltage", "Result"
		# @toDO MZ check this function!
		# query data are quadruples of ("Sweep_Table_Name", "Sweep_Number", "Voltage", "Result")
		# therefore make lists of each tuple "column"
		q = f'select Sweep_Table_Name, Sweep_Number, Voltage, Result, Increment, experiment_name from {table_name[0]}'
		query_data = database.get_data_from_database(database.database, q, fetch_mode = 2)
		increment = None if (query_data["Increment"] > 0).any() else 1
		return query_data[["Sweep_Number","Voltage","Result","experiment_name"]], increment

	@classmethod
	def get_list_of_result_tables(cls,analysis_id, analysis_function_id)-> list:
		"""	
  		
    	"""
		q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
		result_list =  cls.database.get_data_from_database(cls.database.database, q,
														  [analysis_id, analysis_function_id])
		result_list = (list(zip(*result_list))[0])
		return result_list


	"""
	def plot_meta_data_wise(self,canvas, result_list:list, number_of_series:int, meta_data_groups:list):
		\"""
        rearrange the plot to color each trace according to it's meta data group.

        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :param meta_data_groups:
        :return:
        \"""
		print("metadata construction")
		number_of_sweeps = len(result_list) // number_of_series
		meta_data_types = list(dict.fromkeys(meta_data_groups))

		x_data, y_data, series_names = SweepWiseAnalysisTemplate.fetch_x_and_y_data(result_list, number_of_sweeps)
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
    """
