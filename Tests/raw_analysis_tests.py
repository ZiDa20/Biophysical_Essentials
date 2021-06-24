
import sys
import os
sys.path.append(os.getcwd()[:-5] + "src")

import unittest
import asyncio
import tkinter as tk
from raw_analysis import *


class TestRawAnalysis(unittest.TestCase):
    """ Author MZ --> test the frontend page
    unittests """
    # this will run on a separate thread.
    def setUp(self):
        """ set up the testing enviroment """
        self.raw_analysis = AnalysisRaw()

    def test_bound_exception_thrown(self):
        """ write test for the raising of errors """
        with self.assertRaises(TypeError):
            self.raw_analysis.upper_bounds = "string used"
            self.raw_analysis.lower_bounds = "string used"

    def test_constructed_trace(self):
        self.raw_analysis.data = np.linspace(1,100,5000)
        self.raw_analysis.time = np.linspace(1,100, 5000)
        self.raw_analysis.construct_trace()
        self.assertEqual(self.raw_analysis.trace.shape[1], 2)

    def test_exception_trace(self):
        self.raw_analysis.data = np.linspace((1,2),(10,20),10)
        self.raw_analysis.time = np.linspace(1,100,5000)
        with self.assertRaises(ValueError):
            self.raw_analysis.construct_trace()

    def test_slicing_trace_exception(self):
        with self.assertRaises(ValueError):
            self.raw_analysis.slice_trace()

    def test_slicing_with_bounds(self):
        self.raw_analysis.data = np.linspace(1,100,5000)
        self.raw_analysis.time = np.linspace(1,100,5000)
        self.raw_analysis.lower_bounds = 10
        self.raw_analysis.upper_bounds = 20
        self.raw_analysis.construct_trace()
        self.raw_analysis.slice_trace()
        self.assertEqual(self.raw_analysis.sliced_trace.shape[0], 505)
        self.assertEqual(self.raw_analysis.sliced_trace.shape[1],2)


if __name__ == '__main__':
    unittest.main()