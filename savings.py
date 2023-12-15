import matplotlib.pyplot as plt
import numpy as np

# Define the color scheme
colors = ['#EABB1C', '#1CA4E0']

# Initial investment costs
cost_option_b = 149712.5  # Option B with Battery
cost_battery_only = 122937.5  # Battery System Only

# Yearly savings calculations
savings_per_hour_option_b = 17.5 * 7 * 365  # $17.5/hr for 7 hours a night
savings_per_hour_battery_only = 12.5 * 7 * 365  # $12.5/hr for 7 hours a night

# Calculate cumulative savings over 6 years
years = np.arange(2024, 2030)
cumulative_savings_option_b = np.cumsum(np.full(6, savings_per_hour_option_b))
cumulative_savings_battery_only = np.cumsum(np.full(6, savings_per_hour_battery_only))

# Create line graph
plt.figure(figsize=(10, 6))

# Plot for Option B with Battery
plt.plot(years, -cost_option_b + cumulative_savings_option_b, label='Option B with Battery', color=colors[0])

# Plot for Battery System Only
plt.plot(years, -cost_battery_only + cumulative_savings_battery_only, label='Battery System Only', color=colors[1])

# Add labels, title, and legend
plt.title('Financial Projection Over 6 Years')
plt.xlabel('Years')
plt.ylabel('Net Savings ($)')
plt.axhline(0, color='grey', lw=0.5)  # Add a line at y=0 for reference
plt.legend()

# Show plot
plt.show()

