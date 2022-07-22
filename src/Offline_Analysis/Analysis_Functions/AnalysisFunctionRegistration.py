
from Offline_Analysis.Analysis_Functions.MaxCurrent import *
from Offline_Analysis.Analysis_Functions.MinCurrent import *
from Offline_Analysis.Analysis_Functions.MeanCurrent import *
from Offline_Analysis.Analysis_Functions.ActionPotentialFitting import *
from Offline_Analysis.Analysis_Functions.RheobaseDetection import *
from Offline_Analysis.Analysis_Functions.RheorampDetection import *
from Offline_Analysis.Analysis_Functions.MeanVoltage import *

class AnalysisFunctionRegistration():
    """
    Class that holds the mapping between analysis name and associated analysis class object holding
    result calculations and visualizations for this specific function.
    """
    @classmethod
    def get_registered_analysis_class(cls,analysis_function_name):
        mapping = {
            "max_current": MaxCurrent,
            "min_current": MinCurrent,
            "mean_current": MeanCurrent,
            "mean_voltage": MeanVoltage,
            "Action Potential Fitting" : ActionPotentialFitting,
            "AP_Amplitude": ActionPotentialFitting,
            'Threshold_Amplitude': ActionPotentialFitting,
            'AHP_Amplitude': ActionPotentialFitting,
            't_AHP': ActionPotentialFitting,
            'time_to_ahp': ActionPotentialFitting,
            'delta_ap_threshold': ActionPotentialFitting,
            'max_first_derivate': ActionPotentialFitting,
            'min_first_derivate':ActionPotentialFitting,
            'Rheobase-Detection':RheobaseDetection,
            'RheoRamp-Detection': RheorampDetection

        }
        return mapping.get(analysis_function_name,lambda: MaxCurrent)