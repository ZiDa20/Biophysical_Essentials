from Offline_Analysis.Analysis_Functions.MaxCurrent import *
from Offline_Analysis.Analysis_Functions.MinCurrent import *
from Offline_Analysis.Analysis_Functions.MeanCurrent import *
from Offline_Analysis.Analysis_Functions.ActionPotentialFitting import *
from Offline_Analysis.Analysis_Functions.RheobaseDetection import *
from Offline_Analysis.Analysis_Functions.RheorampDetection import *
from Offline_Analysis.Analysis_Functions.MeanVoltage import *
from Offline_Analysis.Analysis_Functions.TimeToMin import *
from Offline_Analysis.Analysis_Functions.TimeToMax import *
from Offline_Analysis.Analysis_Functions.InputResistance import *

class AnalysisFunctionRegistration():
    """
    Class that holds the mapping between analysis name and associated analysis class object holding
    result calculations and visualizations for this specific function.
    """
    ANALYSIS_FUNCTION_MAPPING = {
        "max_current": MaxCurrent,
        "min_current": MinCurrent,
        "mean_current": MeanCurrent,
        "time_to_min": TimeToMin,
        "time_to_max": TimeToMax,
        "mean_voltage": MeanVoltage,
        "Action Potential Fitting": ActionPotentialFitting,
        "Input Resistance": InputResistance,
        "Rheobase-Detection": RheobaseDetection,
        "RheoRamp-Detection": RheorampDetection,
    }

    @classmethod
    def get_registered_analysis_class(cls,analysis_function_name):
        try:
            return cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name]
        except KeyError:
            raise ValueError(f"No analysis function found with name '{analysis_function_name}'")

    @classmethod
    def register_analysis_function(cls, analysis_function_name, analysis_function_class):
        cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name] = analysis_function_class

    @staticmethod
    def get_elements(recording_mode):
        if recording_mode == "Voltage Clamp":
            return ["max_current","min_current","mean_current", "time_to_min", "time_to_max"] #,"area_current","time-to-maximum","time-to-minimum"]
        else:
            return ["mean_voltage",  "Action Potential Fitting",
                    "Rheobase-Detection", "RheoRamp-Detection", "Input Resistance"] # "Cluster",