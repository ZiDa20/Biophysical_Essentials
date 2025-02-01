import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import tkinter as tk
from tkinter import filedialog

# Exponential fitting functions
def biexponential(x, a1, t1, a2, t2, c):
    return a1 * np.exp(-x / t1) + a2 * np.exp(-x / t2) + c

def monoexponential(x, a1, t1, c):
    return a1 * np.exp(-x / t1) + c

# Function to fit and plot
def fit_and_plot(x_data, y_data, fit_type='biexponential'):
    if fit_type == 'biexponential':
        popt, _ = curve_fit(biexponential, x_data, y_data, p0=[-0.3, 1000, -0.05, 100, 0])
        plt.plot(x_data, biexponential(x_data, *popt), label='Double Exponential Fit')
        print("Double Exponential Fit Parameters:", popt)
    else:
        popt, _ = curve_fit(monoexponential, x_data, y_data, p0=[-0.3, 100, 0])
        plt.plot(x_data, monoexponential(x_data, *popt), label='Single Exponential Fit')
        print("Single Exponential Fit Parameters:", popt)

    plt.plot(x_data, y_data, 'o', label='Data')
    plt.legend()
    plt.xlabel('Time (ms)')
    plt.ylabel('Normalized Current')
    plt.show()
    return popt

# Interactive folder selection
root = tk.Tk()
root.withdraw()  # Hide the main window
path_to_data = filedialog.askdirectory(title="Select Data Folder")

# Load and process the data (assuming CSV files as an example)
all_files = [f for f in os.listdir(path_to_data) if f.endswith('.csv')]

results = []
for file in all_files:
    file_path = os.path.join(path_to_data, file)
    data = pd.read_csv(file_path)
    time = data['Time'].values
    current = data['Current'].values

    # Normalize current
    normalized_current = current / np.max(np.abs(current))

    # Plot and fit
    popt_biexp = fit_and_plot(time, normalized_current, fit_type='biexponential')
    popt_monoexp = fit_and_plot(time, normalized_current, fit_type='monoexponential')

    # Save results
    result = {
        'File': file,
        'A1_biexp': popt_biexp[0], 'Tau1_biexp': popt_biexp[1],
        'A2_biexp': popt_biexp[2], 'Tau2_biexp': popt_biexp[3], 'C_biexp': popt_biexp[4],
        'A1_monoexp': popt_monoexp[0], 'Tau1_monoexp': popt_monoexp[1], 'C_monoexp': popt_monoexp[2]
    }
    results.append(result)

# Save results to Excel
results_df = pd.DataFrame(results)
output_path = os.path.join(path_to_data, 'fitting_results.xlsx')
results_df.to_excel(output_path, index=False)
print(f"Results saved to {output_path}")
