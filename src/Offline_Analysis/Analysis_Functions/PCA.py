import numpy as np
import pandas as pd
import math
from Offline_Analysis.Analysis_Functions.Function_Templates.SweepWiseAnalysis import *

class PCA(SweepWiseAnalysisTemplate):
    """ Second level analysis function, 
    Run the Principle component analysis on the data and plot the results

    Args:
        SweepWiseAnalysisTemplate (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.plot_type_options =  ["PCA-Plot"]
        self.function_name = "Action_Potential_Fitting"

    def specific_calculation(self):
        a = "needed for instantion ? "

    def live_data_calculation(self):
        a = "needed for instantion ? "