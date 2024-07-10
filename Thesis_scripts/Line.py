import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_file = 'Tuned_line.txt'

# Read the data into a DataFrame
df = pd.read_csv(data_file, delim_whitespace=True)

# Calculate Max Latency for each row
df['MaxLatency'] = df[['Lat0', 'Lat1', 'Lat2', 'Lat3', 'Lat4', 'Lat5']].max(axis=1)

# Plot Max Latency over Count
plt.plot(df['Count'], df['MaxLatency'], color='purple', marker='o', linestyle='-')
plt.title('Default Max Latency after tuning: 8+ hr')
plt.xlabel('Iteration')
plt.ylabel('Max Latency (µs)')
plt.grid(True)
plt.show()
