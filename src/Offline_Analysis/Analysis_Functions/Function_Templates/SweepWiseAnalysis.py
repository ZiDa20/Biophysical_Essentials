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
	def __init__(self):
		super().__init__()
		self.data_shape = None
		self.database = None
		self.analysis_function_id = None
		self.time = None
		self.logger = None
		#self.cslow_normalization = 1
		
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

	def construct_trace(self):
		""" construct the trace """
		try:
			self.trace = np.vstack((self.time, self.data)).T
		except ValueError as e:
			# we need to add logging here!
			raise ValueError("Please use the same dimension, only 1-dimensional arrays should be used")

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

	def live_data(self,lower_bound, upper_bound, experiment_name,series_identifier, database_handler, sweep_name = None):
		"""for each sweep, find correct x and y value to be plotted as live result
		@author: dz, 29.09.2022
		"""
		self.lower_bound = lower_bound
		self.upper_bound = upper_bound
		data_table_name = database_handler.get_sweep_table_name(experiment_name,series_identifier)
		self.time = database_handler.get_time_in_ms_of_by_sweep_table_name(data_table_name)
		entire_sweep_table = database_handler.get_entire_sweep_table(data_table_name)

		if not sweep_name:
			return self.live_data_for_entire_series(entire_sweep_table)

		data = entire_sweep_table.get(sweep_name)
		return [self.live_data_for_single_sweep(data)]

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

	@abstractmethod
	def specific_calculation(self):
		"""_summary_: Should implement the specific analyssis function in the abstractclass subclasses
		"""
		pass

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

	def calculate_results(self):
		"""
		iterate through each single sweep of all not discarded series in the database and save the calculated result
		to a new database table.
		:return:
		"""

		data_table_names = self.database.get_sweep_table_names_for_offline_analysis(self.series_name)
		
		unit_name = self.get_current_recording_type()

		if unit_name == "Voltage":
			#get the user defined normalization values -> were safed in the database 
			normalization_values = self.database.get_normalization_values(self.analysis_function_id)
			#normalization_values = None
			print("got normalization values", normalization_values)
		else:
			print("No normalization because of current clamp")

		# check here if current or voltage clamp and add the respective name of the unit to the table
		
			# set time to non - will be set by the first data frame
		# should assure that the time and bound setting will be only exeuted once since it is the same all the time
		column_names = ["Analysis_ID", "Function_Analysis_ID", "Sweep_Table_Name", "Sweep_Number", unit_name, "Result", "Increment","experiment_name"]
		merged_all_results = pd.DataFrame(columns = column_names)
		# get the pgf segment whic hwas selected by the user and stored in the db
		pgf_segment = self.database.database.execute(f'select pgf_segment from analysis_functions where analysis_function_id = {self.analysis_function_id}').fetchall()[0][0]

		for data_table in data_table_names:

			# retrieves the experiment name
			experiment_name = self.database.get_experiment_from_sweeptable_series(self.series_name,data_table)
			entire_sweep_table = self.database.get_entire_sweep_table(data_table)
			if self.time is None:
				self.time = self.database.get_time_in_ms_of_by_sweep_table_name(data_table)
			#set the current_time if it changes
			self.set_current_time_shape(entire_sweep_table,data_table)
			# pgf table is also just once per data_table and not per sweep
			pgf_data_frame = self.database.get_entire_pgf_table(data_table)

			# added function id since it can be that one selects 2x e.g. max_current and the ids are linked to the coursor bounds too
			# adding the name would increase readibility of the database ut also add a lot of redundant information
			for column in entire_sweep_table:
				self.data = entire_sweep_table.get(column)
				# This is the hickup why we have to use 
				if unit_name != "Voltage":
					y_min, y_max = self.database.get_ymin_from_metadata_by_sweep_table_name(data_table, column)
					self.data = np.interp(self.data, (self.data.min(), self.data.max()), (y_min, y_max))
				
				# slice trace according to coursor bounds
				self.construct_trace()
				self.slice_trace()
				res = self.specific_calculation()

				# normalize if necessary
				# toDO add logging here

				if unit_name == "Voltage":
					normalization_value = normalization_values[normalization_values["sweep_table_name"]==data_table]["normalization_value"].values[0]
					res = res / normalization_value

				# print("result = ", res)
				# get the sweep number
				sweep_number = column.split("_")
				sweep_number = int(sweep_number[1])

				# get the related pgf value
				#therefore get the pgf table for this series first
				
				# 	from the coursor bounds indentify the correct segment
				increment_list = pgf_data_frame["increment"].values
				voltage_list = pgf_data_frame["voltage"].values

				print("increment")
				print(pgf_data_frame)
				print(increment_list)
				print(voltage_list)
				print(pgf_segment)

				inc = (float(increment_list[pgf_segment-1])*1000)
				volt_val = (float(voltage_list[pgf_segment-1])*1000) + (sweep_number-1)*inc

				new_df = pd.DataFrame([[self.database.analysis_id,self.analysis_function_id,data_table,sweep_number,volt_val,res,inc,experiment_name]],columns = column_names)
				merged_all_results = pd.concat([merged_all_results,new_df])

				#print("sweep wise finished successfully")
		# write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table
		#print(f"This is the analysis function id : {self.analysis_function_id}")
		new_specific_result_table_name = self.database.create_new_specific_result_table_name(self.analysis_function_id, self.function_name)
		self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
																				self.analysis_function_id,
																				data_table,
																				new_specific_result_table_name,
																				merged_all_results)

		#print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')
	def get_current_recording_type(self):
		"""_summary_: Should return the current recording mode

		Returns:
			unit_name (str): The name of the current unit for recordings either Voltage or Current
		"""
		return (
			"Current"
			if self.database.get_recording_mode_from_analysis_series_table(self.series_name) != "Voltage Clamp"
			else "Voltage"
		)

	def set_current_time_shape(self, entire_sweep_table, current_data_table: str):
		"""_summary_: Function that should check the current shape of time and if it changes
			than time should be updated, might happen when different protocols with same names are used

		Args:
			entire_sweep_table (pd.DataFrame): _description_
			current_data_table (str): _description_
		"""
		if entire_sweep_table[list(entire_sweep_table.keys())[0]].shape != self.data_shape:
			self.data_shape = entire_sweep_table[list(entire_sweep_table.keys())[0]].shape
			self.time = self.database.get_time_in_ms_of_by_sweep_table_name(current_data_table)

	def run_late_register_feature(self):
		print("not implemented for sweep wise")

	@staticmethod
	def visualize_results(parent_widget,database) -> list:
		"""Function to retrieve the list result tables for the function analysis id

		Args:
			parent_widget (OfflineResultVisualizer): Widget to put the Analysis in 

		Returns:
			list: list of funciton id related tables
		"""
		return SweepWiseAnalysisTemplate.get_list_of_result_tables(parent_widget.analysis_id, parent_widget.analysis_function_id,database)


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

	@staticmethod
	def get_list_of_result_tables(analysis_id, analysis_function_id, database)-> list:
		""""""
		q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
		result_list = database.get_data_from_database(database.database, q,
															[analysis_id, analysis_function_id])
		print("debug query: " + q )
		print(analysis_id)
		print(analysis_function_id)

		result_list = (list(zip(*result_list))[0])
		return result_list