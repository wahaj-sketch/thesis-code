import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load data from a specified filepath."""
    data = pd.read_csv(filepath, delim_whitespace=True)
    return data

def plot_histogram(data):
    """Plot a histogram using the loaded data."""
    plt.figure(figsize=(10, 6))
    plt.bar(data['Latency(us)'], data['Count'], width=1.0, edgecolor='black')
    plt.title('Latency Distribution')
    plt.xlabel('Latency (microseconds)')
    plt.ylabel('Count')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('latency_distribution.png', dpi=300)
    plt.show()

def main():
    """Main function to run steps."""
    filepath = 'C:/Users/ar-wahaj.kayani/Downloads/Latency_data.txt'  # Update this to your actual data file path
    data = load_data(filepath)
    plot_histogram(data)

if __name__ == '__main__':
    main()
