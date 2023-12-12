import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to prepare data for plotting (convert AC System Output to Amps per phase)
def prepare_data_for_plotting(df):
    # Convert AC System Output from Watts to Amps per phase
    # Formula: Power (W) / Voltage (V) / 3 (for 3 phases) = Current (A)
    df['Amps per Phase'] = df['AC System Output (W)'] / 220 / 3
    return df

# Load the CSV files for Option A, Option B, and Option C
option_a_df = pd.read_csv('Option A.csv')
option_b_df = pd.read_csv('Option B.csv')
option_c_df = pd.read_csv('Option C.csv')

# Preparing data for each option
prepared_a_df = prepare_data_for_plotting(option_a_df)
prepared_b_df = prepare_data_for_plotting(option_b_df)
prepared_c_df = prepare_data_for_plotting(option_c_df)

# Selecting a typical day (1st of a mid-year month, e.g., June) for demonstration
typical_day_a = prepared_a_df[(prepared_a_df['Month'] == 6) & (prepared_a_df['Day'] == 1)]
typical_day_b = prepared_b_df[(prepared_b_df['Month'] == 6) & (prepared_b_df['Day'] == 1)]
typical_day_c = prepared_c_df[(prepared_c_df['Month'] == 6) & (prepared_c_df['Day'] == 1)]

# Plotting the typical day for all three options
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting for each option
ax.plot(typical_day_a['Hour'], typical_day_a['Amps per Phase'], label='Option A', linewidth=2)
ax.plot(typical_day_b['Hour'], typical_day_b['Amps per Phase'], label='Option B', linewidth=2)
ax.plot(typical_day_c['Hour'], typical_day_c['Amps per Phase'], label='Option C', linewidth=2)

# Setting titles and labels
ax.set_title('Solar Production Comparison - June 1st', fontsize=16)
ax.set_xlabel('Hour of the Day', fontsize=12)
ax.set_ylabel('Amps per Phase', fontsize=12)
ax.legend()

# Enhancing visual appeal
ax.set_xticks(np.arange(0, 25, 1))
ax.set_xlim([0, 24])
ax.grid(True)

plt.show()
