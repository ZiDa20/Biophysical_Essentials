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
		self.plot_type_options = ["No Split", "Split by Meta Data"]

		self.cslow_normalization = 1

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
	def live_data_for_entire_series(self, entire_sweep_table):
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
	def live_data_for_single_sweep(self,data):
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
	def run_late_register_feature(cls):
		print("not implemented for sweep wise")

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

		if visualization_type =="Boxplot":
			print("boxplot visualization")
			self.make_boxplot(parent_widget, canvas, result_table_names)


	@classmethod
	def make_boxplot(self,parent_widget, canvas, result_table_list):

		meta_data_groups = []
		meta_data_specific_df = []

		for table in result_table_list:

			self.database.database.execute(f'select * from {table}')
			query_data_df = self.database.database.fetchdf()

			print("querried data look like this")
			print(query_data_df)

			q = f'select meta_data_group from experiments where experiment_name = (select experiment_name from ' \
				f'experiment_series where Sweep_Table_Name = (select sweep_table_name from results where ' \
				f'specific_result_table_name = \'{table}\'))'

			meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

			# index has the same name as the function. Will not work if the names differ.
			try:
				x_data = 1000* query_data_df['Result'].values.tolist()[0]
			except Exception as e:
				break

			print("xdata  data look like this")
			print(x_data)

			if meta_data_group in meta_data_groups:
				specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
				specific_df.insert(0, str(table), x_data, True)
				meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df
			else:
				# add a new meta data group
				meta_data_groups.append(meta_data_group)
				meta_data_specific_df.append(pd.DataFrame({str(table): [x_data]}))

		# print(meta_data_specific_df[0])

		# make the boxplot
		ax = canvas.figure.subplots()

		boxplot_matrix = []
		for meta_data in meta_data_specific_df:
			boxplot_matrix.append(meta_data.iloc[0].values)

		# no nan handling required since sweeps without an AP are not stored in the dataframe
		filtered_box_plot_data = boxplot_matrix

		# print(filtered_box_plot_data)

		# make custom labels containing the correct meta data group and the number of evaluated cells
		custom_labels = []

		for i in range(0, len(meta_data_groups)):
			custom_labels.append(meta_data_groups[i] + ": " + str(len(filtered_box_plot_data[i])))

		plot = ax.boxplot(filtered_box_plot_data,  # notch=True,  # notch shape
						  vert=True,  # vertical box alignment
						  patch_artist=True)

		# ax.violinplot(filtered_box_plot_data)
		ax.set_xticks(np.arange(1, len(meta_data_groups) + 1), labels=meta_data_groups)
		ax.set_xlim(0.25, len(meta_data_groups) + 0.75)

		default_colors = ['k', 'b', 'r', 'g', 'c']

		for patch, color in zip(plot['boxes'], default_colors[0:len(plot['boxes'])]):
			patch.set_facecolor(color)

		ax.legend(plot['boxes'], custom_labels, loc='upper left')

		parent_widget.export_data_frame = pd.DataFrame(filtered_box_plot_data)
		parent_widget.export_data_frame = parent_widget.export_data_frame.transpose()
		parent_widget.export_data_frame.columns = meta_data_groups


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
		plot_data_frame = pd.DataFrame ()

		for table in result_table_list:
			y_data,x_data, experiment_name = self.fetch_x_and_y_data(table)
			new_df = pd.DataFrame(y_data, index=x_data,columns=[table])
			plot_data_frame  = pd.concat([plot_data_frame,new_df], axis=1)

			try:
				ax.plot(x_data,y_data, 'k', label=experiment_name)
				#parent_widget.export_data_frame.insert(0, experiment_name, y_data)
			except Exception as e:
				print(e)
				print(experiment_name)

		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
		# Put a legend below current axis
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
		canvas.show()

		print(plot_data_frame)
		parent_widget.export_data_frame = plot_data_frame
		print("succesfully stored data")


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
			q = f'select experiment_meta_data from global_meta_data where experiment_name = (select experiment_name from experiment_series where Sweep_Table_Name = \'{sweep_table_names[0]}\')'
			meta_data_group = self.database.get_data_from_database(self.database.database, q)[0][0]

			if meta_data_group in meta_data_groups:
				try:
					specific_df = meta_data_specific_df[meta_data_groups.index(meta_data_group)]
					specific_df.insert(0, str(result_table_list.index(table)), x_data, True)
					meta_data_specific_df[meta_data_groups.index(meta_data_group)] = specific_df
				except Exception as e:
					print("an error occured in split by meta data")
					print(e)
					print("the following table will not be added to results")
					print(table)
			else:
				# add a new meta data group
				meta_data_groups.append(meta_data_group)
				# start a new dataframe
				new_df = pd.DataFrame()
				new_df.insert(0,str(result_table_list.index(table)),x_data,True)
				meta_data_specific_df.append(pd.DataFrame(np.array(x_data)))

			print("finished meta data group calculation")
		ax = canvas.figure.subplots()

		plot_data_frame = pd.DataFrame()

		for group in meta_data_groups:

			# convert dataframe into numpy array = list of lists
			df_as_numpy_array = meta_data_specific_df[meta_data_groups.index(group)].to_numpy()
			mean_coordinate_value = []
			calc_std = []

			# for each row a mean will be calculated: each row reflects one sweep .. eg.
			# 			recording1 # recording2 # recording3
			# sweep 1

			for coordinate_row in df_as_numpy_array:
				print(coordinate_row)
				try:
					mean_coordinate_value.append(np.mean(coordinate_row))
					calc_std.append(np.std(coordinate_row)/np.sqrt(np.size(coordinate_row)))
				except Exception as e:
					print(e)
					print(coordinate_row)

			custom_label = group + ": n = " + str(np.size(df_as_numpy_array[0]))
			try:
				ax.errorbar(y_data,mean_coordinate_value, calc_std, mfc = 'k', label=custom_label)
				plot_data_frame = pd.concat([plot_data_frame,pd.DataFrame(mean_coordinate_value,index=y_data,columns=[group])],axis=1 )

			except Exception as e:
					print(e)
					print(group)

		box = ax.get_position()
		ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
		# Put a legend below current axis
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
		canvas.show()

		print(plot_data_frame)
		parent_widget.export_data_frame = plot_data_frame
		print("succesfully stored data")


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

		try:
			result_list = (list(zip(*result_list))[0])
		except Exception as e:
			print(e)
			result_list = []
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



