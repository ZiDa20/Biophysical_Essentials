
from Offline_Analysis.Analysis_Functions.MaxCurrent import *
from Offline_Analysis.Analysis_Functions.MinCurrent import *
from Offline_Analysis.Analysis_Functions.MeanCurrent import *
from Offline_Analysis.Analysis_Functions.ActionPotentialFitting import *
from Offline_Analysis.Analysis_Functions.RheobaseDetection import *
from Offline_Analysis.Analysis_Functions.RheorampDetection import *
from Offline_Analysis.Analysis_Functions.MeanVoltage import *
from Offline_Analysis.Analysis_Functions.TimeToMin import *

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
            "time_to_min":TimeToMin,
            "mean_voltage": MeanVoltage,
            "Action Potential Fitting" : ActionPotentialFitting,
            'Vmem [mV]' : ActionPotentialFitting,
            'Threshold_Amplitude [mV]' : ActionPotentialFitting,
            't_Threshold [ms]': ActionPotentialFitting,
            'delta_t_threshold [ms]': ActionPotentialFitting,
            'passive_repolarization [mV]': ActionPotentialFitting,
            'AP_Amplitude [mV]': ActionPotentialFitting,
            't_AP_Amplitude [ms]': ActionPotentialFitting,
            'delta_ap_threshold [mV]': ActionPotentialFitting,
            'delta_t_ap_threshold [ms]': ActionPotentialFitting,
            'AHP_Amplitude [mV]': ActionPotentialFitting,
            't_AHP [ms]': ActionPotentialFitting,
            't_threshold_ahp [ms]': ActionPotentialFitting,
            'max_first_derivate [mV/ms]': ActionPotentialFitting,
            't_max_1st_derivative [ms]': ActionPotentialFitting,
            'min_first_derivate [mV/ms]': ActionPotentialFitting,
            't_min_1st_derivative [ms]': ActionPotentialFitting,
            'dt t_min-t_max [ms]': ActionPotentialFitting,
            'AP_with [ms]': ActionPotentialFitting,
            'Rheobase-Detection':RheobaseDetection,
            'RheoRamp-Detection': RheorampDetection

        }
        return mapping.get(analysis_function_name,lambda: MaxCurrent)