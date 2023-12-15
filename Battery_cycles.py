import matplotlib.pyplot as plt
import pandas as pd

# Constants
start_year = 2024
cycles = 9000
initial_SOH = 100  # State of Health in %
final_SOH = 80  # State of Health after 9000 cycles
line_color = '#EABB1C'  # Color from the provided palette

# Creating a date range from 1 Jan 2024 for 9000 days
dates = pd.date_range(start=f"{start_year}-01-01", periods=cycles)

# Calculating the linear decrease in State of Health
soh = [initial_SOH - (initial_SOH - final_SOH) * (i / cycles) for i in range(cycles)]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(dates, soh, color=line_color)
plt.title('Battery State of Health Over Time')
plt.xlabel('Date')
plt.ylabel('State of Health (%)')
plt.grid(True)
plt.show()
