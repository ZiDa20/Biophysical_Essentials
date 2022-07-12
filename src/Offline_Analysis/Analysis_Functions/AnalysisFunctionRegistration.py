
from Offline_Analysis.Analysis_Functions.MaxCurrent import *
from Offline_Analysis.Analysis_Functions.ActionPotentialFitting import *

class AnalysisFunctionRegistration():
    """
    Class that holds the mapping between analysis name and associated analysis class object holding
    result calculations and visualizations for this specific function.
    """
    @classmethod
    def get_registered_analysis_class(cls,analysis_function_name):
        mapping = {
            "max_current":MaxCurrent,
            "Action Potential Fitting" : ActionPotentialFitting,
            "AP_Amplitude": ActionPotentialFitting
        }
        return mapping.get(analysis_function_name,lambda: MaxCurrent)