import numpy as np
import pandas as pd


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
		self.split_options = ("No Split", "Split by meta data")

		self.lower_bound = None
		self.upper_bound = None
		self.time = None
		self.data = None

		self.sliced_volt = None

		self.database = None
		self.series_name = None

	@property
	def lower_bounds(self):
		""" get the lower and upper bounds """
		print("The lower bound: ")
		return self._lower_bounds

	@property
	def upper_bounds(self):
		print("The upper bound: ")
		return self._upper_bounds

	@lower_bounds.setter
	def lower_bounds(self, lower_bound):
		""" set the lower and upper bound """
		if type(lower_bound) in [int, float]:
			self._lower_bounds = lower_bound
		else:
			raise TypeError("Wrong Input please specificy floats")

	@upper_bounds.setter
	def upper_bounds(self, upper_bound):
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
	def calculate_results(self):
		"""

		:return:
		"""
		# @todo get this from the configuration window
		series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)

		try:
			if series_specific_recording_mode == "Voltage Clamp":
				cslow_normalization = 1
			else:
				cslow_normalization = 0
		except Exception as e:
			print("Error in Excecute_Single_Series_Analysis")
			print(e)
			cslow_normalization = 0

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
				if cslow_normalization:
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
				print(self.lower_bound)
				print(self.upper_bound)
				print(pgf_data_frame)

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


				print(volt_val)
				new_df = pd.DataFrame([[self.database.analysis_id,self.analysis_function_id,data_table,sweep_number,volt_val,res]],columns = column_names)

				result_data_frame = pd.concat([result_data_frame,new_df])

			# write the result dataframe into database -> therefore create a new table with the results and insert the name into the results table

			new_specific_result_table_name = self.create_new_specific_result_table_name(self.database.analysis_id, data_table)
			print(new_specific_result_table_name)

			self.database.update_results_table_with_new_specific_result_table_name(self.database.analysis_id,
																				   self.analysis_function_id,
																				   data_table,
																				   new_specific_result_table_name,
																				   result_data_frame)

			print(f'Successfully calculated results and wrote specific result table {new_specific_result_table_name} ')

	@classmethod
	def create_new_specific_result_table_name(cls, analysis_function_id, data_table_name):
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
	def visualize_results(self):
		# get the result table names for current offline analysis id and analysis function id

		# for each table


		print("Parent: not implemented")
