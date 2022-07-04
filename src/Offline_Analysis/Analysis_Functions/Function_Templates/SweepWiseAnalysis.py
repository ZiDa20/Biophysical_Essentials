
import numpy as np

class SweepWiseAnalysisTemplate(object):

	def __init__(self):

		self.function_name = None
		self.data = None
		self.voltage = None

		self.database = None#database
		self.split_options = ("No Split", "Split by meta data")



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

	def construct_trace(self):
		""" construct the trace """
		try:
			self.trace = np.vstack((self.time, self.data)).T
		except:
			raise ValueError("Please use the same dimension, only 1-dimensional arrays should be used")

	def slice_trace(self):
		""" slice the trace based on the incoming upper and lower bounds """
		if all([self._lower_bounds, self._upper_bounds]):
			self.sliced_trace = self.trace[
				((self.trace[:, 0] > self._lower_bounds) & (self.trace[:, 0] < self._upper_bounds))]
			self.sliced_volt = self.sliced_trace[:, 1]
		else:
			raise ValueError("No upper and lower bonds set yet, please sets and use the rectangular function")


	def show_configuration_options(self):
		print("not implemented")



	@classmethod
	def calculate_results(self):
		# slice trace according to coursor bounds
		# call specific_calculation
		# write the result into database -> therefore create a new table with the results and insert the name into the results table
		print("Parent: not implemented")

	def specific_calculation(self,sliced_trace):
		# return None
		print("specific result calculation")

	@classmethod
	def visualize_results(self):
		print("Parent: not implemented")