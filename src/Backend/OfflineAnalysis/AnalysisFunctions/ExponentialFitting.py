
from Backend.OfflineAnalysis.AnalysisFunctions.FunctionTemplate.SweepWiseAnalysis import *

class ExponentialFitting(SweepWiseAnalysisTemplate):
    
    def __init__(self):
        super().__init__()
        self.function_name = 'min_current'
        self.plot_type_options = ["No Split", "Split by Meta Data"]
    
        # Define a function for a bi-exponential fit
    def biexponential(x, a1, t1, a2, t2, c):
        """
        Bi-exponential function.
        Args:
            x (array): Independent variable (e.g., time).
            a1 (float): Amplitude of the first exponential component.
            t1 (float): Time constant of the first exponential component.
            a2 (float): Amplitude of the second exponential component.
            t2 (float): Time constant of the second exponential component.
            c (float): Offset constant.
        Returns:
            array: Computed bi-exponential values.
        """
        return a1 * np.exp(-x / t1) + a2 * np.exp(-x / t2) + c

    # Define a function for a mono-exponential fit
    def monoexponential(x, a1, t1, c):
        """
        Mono-exponential function.
        Args:
            x (array): Independent variable (e.g., time).
            a1 (float): Amplitude of the exponential component.
            t1 (float): Time constant of the exponential component.
            c (float): Offset constant.
        Returns:
            array: Computed mono-exponential values.
        """
        return a1 * np.exp(-x / t1) + c
    
    def specific_calculation(self):
            """Finds the minimum voltage in the sliced signal and calculates the mean voltage 
            in a ±50 ms window around it.
            """
            self.cslow_normalization = 1  # Not clear why this is needed, but keeping it

            # Identify the index of the minimum voltage value in the sliced signal
            min_index = np.argmin(self.sliced_volt)

            # Get the time at this minimum voltage
            min_time = self.sliced_time[min_index]

            # Define threshold time window (±50 ms)
            lower_thresh = min_time - 50
            upper_thresh = min_time + 50

            # Find indices within the threshold time range
            mask = (self.sliced_time >= lower_thresh) & (self.sliced_time <= upper_thresh)

            # Compute the mean voltage within this window
            mean_voltage = np.mean(self.sliced_volt[mask])

            return mean_voltage  # Return the calculated mean voltage

        
    def live_data_calculation(self):
        """
        the points that will be plotted during analysis function selection
        @return:
        """
        #self.cslow_normalization = 1
        # Identify the index of the minimum voltage value in the sliced signal
        #min_index = np.argmin(self.sliced_volt)
        #x_val = self.sliced_time[self.sliced_volt] +self.lower_bound

        #return tuple((x_val, self.sliced_volt[min_index]))
 
        self.cslow_normalization = 1
        min_val = np.min(self.sliced_volt)
        pos = np.where(self.sliced_volt == min_val)
        x_val = self.time[pos][0] +self.lower_bound
        return tuple((x_val, min_val))
 


    # Function to fit and plot data
    def fit_and_plot(x_data, y_data, fit_type='biexponential'):
        """
        Fit data using the specified exponential model and plot the results.
        Args:
            x_data (array): Independent variable data (e.g., time).
            y_data (array): Dependent variable data (e.g., current).
            fit_type (str): Type of fit ('biexponential' or 'monoexponential').
        Returns:
            list: Optimized fit parameters.
        """
        if fit_type == 'biexponential':
            # Initial guess for bi-exponential parameters
            popt, _ = curve_fit(biexponential, x_data, y_data, p0=[-0.3, 1000, -0.05, 100, 0])
            plt.plot(x_data, biexponential(x_data, *popt), label='Double Exponential Fit')
            print("Double Exponential Fit Parameters:", popt)
        else:
            # Initial guess for mono-exponential parameters
            popt, _ = curve_fit(monoexponential, x_data, y_data, p0=[-0.3, 100, 0])
            plt.plot(x_data, monoexponential(x_data, *popt), label='Single Exponential Fit')
            print("Single Exponential Fit Parameters:", popt)

        # Plot the raw data points
        plt.plot(x_data, y_data, 'o', label='Data')
        plt.legend()
        plt.xlabel('Time (ms)')  # X-axis label
        plt.ylabel('Normalized Current')  # Y-axis label
        plt.show()
        return popt

    # Initialize Tkinter for folder selection
    root = tk.Tk()  # Create the root window
    root.withdraw()  # Hide the main window

    # Prompt the user to select a folder containing data files
    path_to_data = filedialog.askdirectory(title="Select Data Folder")

    # List all CSV files in the selected folder
    all_files = [f for f in os.listdir(path_to_data) if f.endswith('.csv')]

    # Store the fitting results for each file
    results = []

    # Loop through each file to load and process the data
    for file in all_files:
        file_path = os.path.join(path_to_data, file)  # Full path to the file
        data = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
        time = data['Time'].values  # Extract time values from the DataFrame
        current = data['Current'].values  # Extract current values from the DataFrame

        # Normalize the current values by dividing by the maximum absolute value
        normalized_current = current / np.max(np.abs(current))

        # Fit the data using bi-exponential and mono-exponential models
        popt_biexp = fit_and_plot(time, normalized_current, fit_type='biexponential')
        popt_monoexp = fit_and_plot(time, normalized_current, fit_type='monoexponential')

        # Store the fitting results for the current file
        result = {
            'File': file,
            'A1_biexp': popt_biexp[0], 'Tau1_biexp': popt_biexp[1],
            'A2_biexp': popt_biexp[2], 'Tau2_biexp': popt_biexp[3], 'C_biexp': popt_biexp[4],
            'A1_monoexp': popt_monoexp[0], 'Tau1_monoexp': popt_monoexp[1], 'C_monoexp': popt_monoexp[2]
        }
        results.append(result)

    # Save the fitting results to an Excel file
    results_df = pd.DataFrame(results)  # Convert results to a DataFrame
    output_path = os.path.join(path_to_data, 'fitting_results.xlsx')  # Path for the output file
    results_df.to_excel(output_path, index=False)  # Save the DataFrame to Excel
    print(f"Results saved to {output_path}")  # Notify the user
