import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
# New color palette
colors = ['#EABB1C', '#1CA4E0', '#41667B', '#95D1EB', '#5E8FAB', '#72725E', '#68501E']



# Function to prepare data for plotting (convert AC System Output to Amps per phase)
def prepare_data_for_plotting(df):
    df['Amps per Phase'] = df['AC System Output (W)'] / 220 / 3
    return df

# Function to adjust for DST
def adjust_for_dst(df):
    # DST in Lebanon is from April to October
    df['Hour'] = df.apply(lambda row: row['Hour'] + 1 if 4 <= row['Month'] <= 10 else row['Hour'], axis=1)
    df['Hour'] = df['Hour'] % 24  # Adjust hour if it goes beyond 23
    return df

# Load and prepare the CSV files
option_a_df = adjust_for_dst(prepare_data_for_plotting(pd.read_csv('Option A.csv')))
option_b_df = adjust_for_dst(prepare_data_for_plotting(pd.read_csv('Option B.csv')))
option_c_df = adjust_for_dst(prepare_data_for_plotting(pd.read_csv('Option C.csv')))

# Create a 'plots' subdirectory if it doesn't exist
plots_dir = 'plots'
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Function to plot and save solar production for each month
def plot_and_save_monthly_production():
    for month in range(1, 13):
        fig, ax = plt.subplots(figsize=(12, 6))
        # Include an enumeration to get both the dataframe and its index
        for i, (df, label) in enumerate(zip([option_a_df, option_b_df, option_c_df], ['Option A', 'Option B', 'Option C'])):
            monthly_data = df[(df['Month'] == month) & (df['Day'] == 1)]
            # Use the index 'i' to select color
            ax.plot(monthly_data['Hour'], monthly_data['Amps per Phase'], label=label, color=colors[i], linewidth=2)

        ax.set_title(f'Solar Production Comparison - Month {month:02d}', fontsize=16)
        ax.set_xlabel('Hour of the Day', fontsize=12)
        ax.set_ylabel('Amps per Phase', fontsize=12)
        ax.legend()
        ax.set_xticks(np.arange(0, 25, 1))
        ax.set_xlim([0, 24])
        ax.grid(True)

        # Save the figure in the 'plots' subdirectory
        plt.savefig(f'{plots_dir}/Solar_Production_DST_Adjusted_Month_{month:02d}.png')
        plt.close(fig)

# Generate and save plots for each month with DST adjustment
plot_and_save_monthly_production()




import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Function to calculate the average daily kWh production for each month
def calculate_average_daily_kwh(df):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    df['Average Daily kWh'] = df.apply(lambda row: row['AC System Output (kWh)'] / days_in_month[int(row['Month']) - 1], axis=1)
    return df[['Month', 'Average Daily kWh']]

# Load the monthly CSV files
option_a_monthly_df = pd.read_csv('option_ A_monthly.csv')
option_b_monthly_df = pd.read_csv('option_B_monthly.csv')
option_c_monthly_df = pd.read_csv('option_C_monthly.csv')

# Calculating the average daily kWh
avg_daily_kwh_a = calculate_average_daily_kwh(option_a_monthly_df)
avg_daily_kwh_b = calculate_average_daily_kwh(option_b_monthly_df)
avg_daily_kwh_c = calculate_average_daily_kwh(option_c_monthly_df)

# Create the /plots/monthly directory if it doesn't exist
plots_dir = 'plots/monthly'
if not os.path.exists(plots_dir):
    os.makedirs(plots_dir)

# Plotting the horizontal bar graph
fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.25
index = np.arange(12)

# Horizontal bar plot with new color scheme
bar1 = ax.barh(index, avg_daily_kwh_a['Average Daily kWh'], bar_height, label='Option A', color=colors[0])
bar2 = ax.barh(index + bar_height, avg_daily_kwh_b['Average Daily kWh'], bar_height, label='Option B', color=colors[1])
bar3 = ax.barh(index + 2 * bar_height, avg_daily_kwh_c['Average Daily kWh'], bar_height, label='Option C', color=colors[2])

ax.set_ylabel('Month')
ax.set_xlabel('Average Daily kWh Production')
ax.set_title('Average Daily kWh Production by Month and Option')
ax.set_yticks(index + bar_height)
ax.set_yticklabels([str(i) for i in range(1, 13)])
ax.legend()

# Save the figure in the /plots/monthly subdirectory
fig.savefig(f'{plots_dir}/Average_Daily_kWh_Production_Horizontal.png')
plt.close(fig)

