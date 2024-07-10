import matplotlib.pyplot as plt
import pandas as pd

# Load data from a file
data_file = 'Baseline_perf.txt'

# Read the data into a DataFrame
df = pd.read_csv(data_file, delim_whitespace=True)

# Plot each latency column
for column in df.columns[1:]:
    plt.scatter(df['Count'], df[column], s=1, label=column)

# Customize the plot
plt.title('Cyclictest results Baseline for 6 hours')
plt.xlabel('Iteration')
plt.ylabel('Latency (µs)')
plt.ylim(0, 10000)  # Adjust the y-axis limit as needed
plt.legend()
plt.show()
