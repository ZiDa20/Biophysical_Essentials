from Backend.OfflineAnalysis.AnalysisFunctions.MaxCurrent import *
from Backend.OfflineAnalysis.AnalysisFunctions.MinCurrent import *
from Backend.OfflineAnalysis.AnalysisFunctions.MeanCurrent import *
from Backend.OfflineAnalysis.AnalysisFunctions.ActionPotentialFitting import *
from Backend.OfflineAnalysis.AnalysisFunctions.RheobaseDetection import *
from Backend.OfflineAnalysis.AnalysisFunctions.Firing_Pattern_CLassification import *
from Backend.OfflineAnalysis.AnalysisFunctions.MeanVoltage import *
from Backend.OfflineAnalysis.AnalysisFunctions.TimeToMin import *
from Backend.OfflineAnalysis.AnalysisFunctions.TimeToMax import *
from Backend.OfflineAnalysis.AnalysisFunctions.InputResistance import *
from Backend.OfflineAnalysis.AnalysisFunctions.PeakFinding import *
from Backend.OfflineAnalysis.AnalysisFunctions.CapacitanceMeasure import CapacitanceMeasurements
from Backend.OfflineAnalysis.AnalysisFunctions.AreaUnderTheCurve import AreaUnderTheCurve
from Backend.OfflineAnalysis.AnalysisFunctions.Rheoramp_Detection import RheorampDetection
from Backend.OfflineAnalysis.AnalysisFunctions.Firing_Pattern_CLassification import FiringPatternCLassification
from Backend.OfflineAnalysis.AnalysisFunctions.PCA import PCA


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
        "Action_Potential_Fitting": ActionPotentialFitting,
        "InputResistance": InputResistance,
        "Rheobase-Detection": RheobaseDetection,
        "RheoRamp-Detection": RheorampDetection,
        "Peak-Detection": PeakFinding,
        "CapacitanceMeasurements": CapacitanceMeasurements,
        "AreaUnderTheCurve": AreaUnderTheCurve,
        "Firing_Pattern": FiringPatternCLassification,
        "PCA":PCA
    }

    @classmethod
    def get_registered_analysis_class(cls,analysis_function_name):
        """_summary_

        Args:
            analysis_function_name (_type_): _description_

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        operands = ["+", "-", "*", "/", "(", ")"]

        try:
            try:
                analysis_function_name =analysis_function_name.replace("(","").split()[0]
                res = cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name]
                #print(cls.ANALYSIS_FUNCTION_MAPPING)
                
                #print(res)
                #print(cls.ANALYSIS_FUNCTION_MAPPING.get(analysis_function_name))
                return cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name]
            except Exception as e:
                print(e)
                return cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name]
            
        except KeyError:
            raise ValueError(f"No analysis function found with name '{analysis_function_name}'")

    @classmethod
    def register_analysis_function(cls, analysis_function_name, analysis_function_class):
        """_summary_

        Args:
            analysis_function_name (_type_): _description_
            analysis_function_class (_type_): _description_
        """
        cls.ANALYSIS_FUNCTION_MAPPING[analysis_function_name] = analysis_function_class

    @staticmethod
    def get_elements(recording_mode):
        """_summary_

        Args:
            recording_mode (_type_): _description_

        Returns:
            _type_: _description_
        """
        if recording_mode == "Voltage Clamp":
            return ["max_current",
                    "min_current",
                    "mean_current", 
                    "time_to_min",
                    "time_to_max", 
                    "CapacitanceMeasurements",
                    "AreaUnderTheCurve"] #,"area_current","time-to-maximum","time-to-minimum"]
        else:
            return ["mean_voltage",  
                    "Action_Potential_Fitting",
                    "Rheobase-Detection", 
                    "RheoRamp-Detection", 
                    "InputResistance", 
                    "Peak-Detection",
                    "AreaUnderTheCurve",
                    "Firing_Pattern"] # "Cluster",