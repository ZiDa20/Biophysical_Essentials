import numpy as np
from scipy import interpolate
import math

from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.SweepWiseAnalysis import SweepWiseAnalysisTemplate
import matplotlib.pyplot as plt

class PhasePlanePlot(SweepWiseAnalysisTemplate):
    """make a phase plane plot of an action potential
    """
    def __init__(self):
        super().__init__()
        self.function_name = "PhasePlanePlot"
        self.plot_type_options = ["PhasePlanePlot"]
    
    def specific_calculation(self):
        """
        specific_calculation _summary_

        Args:
            data (_type_): _description_
            time (_type_): _description_
            column (_type_): _description_
        """

        dv = np.diff(self.sliced_volt*1000) # make mV
        #dv_max = np.argmax(dv)
        
        # Calculate dv_dt for the selected action potential
        dt_ap = np.diff(self.sliced_time)
        
        # Avoid division by zero
        dt_ap[dt_ap == 0] = np.nan
        dv_dt = dv / dt_ap
        #dv_dt_max = np.nanmax(dv_dt)

        # Remove the last element to match dv/dt array
        v_ap_array = self.sliced_volt[:-1]
        
        #plt.figure()
        #plt.title('Phase-plane plot')
        #plt.plot(v_ap_array, dv_dt)
        #plt.ylabel("dV/dt (mV/ms)")
        #plt.xlabel("V (mV)")
        #plt.show()

        return [v_ap_array, dv_dt]
        # Return the selected outputs from the function
        
        #return {
        #    'voltage': self.sliced_volt,
        #    'dv_dt': dv_dt,
        #    'dv_dt_max': dv_dt_max,
        #    'time': self.sliced_time,
        #    'voltage_array': v_ap_array
        #}
