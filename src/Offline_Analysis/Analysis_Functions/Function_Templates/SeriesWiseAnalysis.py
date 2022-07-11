import numpy as np
import pandas as pd

class SeriesWiseAnalysisTemplate(object):
	"""
	Parent class to handle all analysis general processing to analyze complete series:
	"""
	def __init__(self):

		# really needed ?
		self.function_name = None
		self.analysis_function_id = None

		self.data = None
		self.voltage = None

		self.database = None  # database
		self.plot_type_options = ["Boxplot"]

		self.lower_bound = None
		self.upper_bound = None
		self.time = None
		self.data = None

		self.sliced_volt = None

		self.database = None
		self.series_name = None



	def show_configuration_options(self):
		print("not implemented")

	@classmethod
	def calculate_results(self):
		"""
		iterate through each single sweep of all not discarded series in the database and save the calculated result
		to a new database table.
		:return:
		"""

		# @todo get this from the configuration window
		series_specific_recording_mode = self.database.get_recording_mode_from_analysis_series_table(self.series_name)


		# @todo Discuss - is that the case ?
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

				res = self.specific_calculation()

				#print("result")
				#print(res)
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

			new_specific_result_table_name = self.create_new_specific_result_table_name(self.database.analysis_id, data_table)
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
	def visualize_results(self, parent_widget, canvas, visualization_type):

		result_table_names = self.get_list_of_result_tables(parent_widget.analysis_id, parent_widget.analysis_function_id)

		if visualization_type == "No Split":
			print("no split visualization")
			self.simple_plot(parent_widget, canvas, result_table_names)

		if visualization_type == "Split by Meta Data":
			print("metadata mean visualization")
			self.plot_mean_per_meta_data(parent_widget, canvas, result_table_names)
			#print("not implemented")

	@classmethod
	def simple_plot(self, parent_widget, canvas, result_table_list):
		"""
        Plot all data together into one specific analysis plot widget without any differentiation between meta data groups
        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :return:
        :author: dz, 11.07.2022
        """
		ax = canvas.figure.subplots()
		for table in result_table_list:

			x_data, y_data, experiment_name = self.fetch_x_and_y_data(table)

			try:
				ax.plot(y_data,x_data, 'k', label=experiment_name)
				#parent_widget.export_data_frame.insert(0, experiment_name, y_data)
			except Exception as e:
				print(e)
				print(experiment_name)
		ax.legend()
		canvas.show()

	@classmethod
	def plot_mean_per_meta_data(self, parent_widget, canvas, result_table_list):
		"""
		before a mean can be plotted, it needs to be calculated first for each single meta data group
		"""

		meta_data_groups = []
		meta_data_specific_df = []
		y_data = []

		for table in result_table_list:

			# get the meta data group for each result table:
			# 1) from the specific result table load the sweep_table name
			q = f'select Sweep_Table_Name, Sweep_Number, Voltage, Result from {table}'
			query_data = self.database.get_data_from_database(self.database.database, q)

			# query data are quadruples of ("Sweep_Table_Name", "Sweep_Number", "Voltage", "Result")
			# therefore make lists of each tuple "column"
			x_data = (list(zip(*query_data))[3])
			y_data = (list(zip(*query_data))[2])
			sweep_table_names =  (list(zip(*query_data))[0])


			# 2) get experiment_name from experiment_series table and join with experiments table to get meta_data_group
			q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from experiment_series where Sweep_Table_Name = \'{sweep_table_names[0]}\')'
			meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

			if meta_data_group in meta_data_groups:
				#new_df = pd.DataFrame(np.array(x_data))
				#print(new_df)
				specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
				specific_df.insert(0, str(result_table_list.index(table)), x_data, True)
				meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df



			else:
				# add a new meta data group
				meta_data_groups.append(meta_data_group)
				# start a new dataframe
				new_df = pd.DataFrame()
				new_df.insert(0,str(result_table_list.index(table)),x_data,True)
				meta_data_specific_df.append(pd.DataFrame(np.array(x_data)))

			print("finished meta data group calculation")
		ax = canvas.figure.subplots()
		for group in meta_data_groups:

			# convert dataframe into numpy array = list of lists
			df_as_numpy_array = meta_data_specific_df[meta_data_groups.index(group)].to_numpy()
			mean_coordinate_value = []
			calc_std = []

			# for each row a mean will be calculated: each row reflects one sweep .. eg. sweep 1
			for coordinate_row in df_as_numpy_array:

				mean_coordinate_value.append(np.mean(coordinate_row))
				calc_std.append(np.std(coordinate_row))

			try:
				ax.plot(y_data,mean_coordinate_value, 'k', label=group)
				# parent_widget.export_data_frame.insert(0, experiment_name, y_data)
			except Exception as e:
					print(e)
					print(group)

			ax.legend()
			canvas.show()

	@classmethod
	def fetch_x_and_y_data(self, table_name):

		#@todo move this function to the database class ?
		# "Sweep_Table_Name", "Sweep_Number", "Voltage", "Result"

		q = f'select Sweep_Table_Name, Sweep_Number, Voltage, Result from {table_name}'
		query_data = self.database.get_data_from_database(self.database.database, q)

		# query data are quadruples of ("Sweep_Table_Name", "Sweep_Number", "Voltage", "Result")
		# therefore make lists of each tuple "column"
		x_data = (list(zip(*query_data))[3])
		y_data = (list(zip(*query_data))[2])
		sweep_enumeration = (list(zip(*query_data))[1])

		q = """select experiment_name from experiment_series where sweep_table_name = (?)"""
		experiment_name = self.database.get_data_from_database(self.database.database, q,
														  [query_data[0][0]]) [0][0]
		return x_data, y_data, experiment_name

	@classmethod
	def get_list_of_result_tables(self, analysis_id, analysis_function_id):
		"""

		"""
		q = """select specific_result_table_name from results where analysis_id =(?) and analysis_function_id =(?) """
		result_list = self.database.get_data_from_database(self.database.database, q,
														  [analysis_id, analysis_function_id])

		result_list = (list(zip(*result_list))[0])
		return result_list




	def plot_meta_data_wise(self, canvas, result_list, number_of_series, meta_data_groups):
		"""
        rearrange the plot to color each trace according to it's meta data group.

        :param analysis_specific_plot_widget:
        :param result_list:
        :param number_of_series:
        :param meta_data_groups:
        :return:
        """
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



