import numpy as np
from scipy import interpolate
import math
import pickle
import datetime
from scipy.signal import savgol_filter
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
        filename = None
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"trace_{timestamp}.pkl"

        # Apply smoothing

        smoothed_v_ap, smoothed_dv_dt = self.smooth_data(v_ap_array, dv_dt)

        trace_data = {
            'v_ap_array': v_ap_array,
            'dv_dt': smoothed_dv_dt
        }

        with open(filename, 'wb') as f:
            pickle.dump(trace_data, f)

        print(f"Trace saved to {filename}")
        return [v_ap_array, smoothed_dv_dt]
        # Return the selected outputs from the function
        
        #return {
        #    'voltage': self.sliced_volt,
        #    'dv_dt': dv_dt,
        #    'dv_dt_max': dv_dt_max,
        #    'time': self.sliced_time,
        #    'voltage_array': v_ap_array
        #}
    def smooth_data(self,v_ap_array, dv_dt, window_length=10, polyorder=2):
        """
        Apply Savitzky-Golay smoothing to the data.
        """
        smoothed_v_ap = savgol_filter(v_ap_array, window_length, polyorder)
        smoothed_dv_dt = savgol_filter(dv_dt, window_length, polyorder)
        return smoothed_v_ap, smoothed_dv_dt