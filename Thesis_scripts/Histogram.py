import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load data from a specified filepath."""
    data = pd.read_csv(filepath, delim_whitespace=True)
    return data

def plot_histogram(data):
    """Plot a histogram for each latency core."""
    num_cores = data.shape[1] - 1  # assuming the first column is 'Count'
    plt.figure(figsize=(12, num_cores * 2))  # Adjust size based on the number of cores
    
    for i in range(num_cores):
        ax = plt.subplot(num_cores, 1, i + 1)  # Create a subplot for each core
        # Plotting each core's latency distribution
        plt.bar(data['Count'], data[f'Lat{i}'], width=1.0, edgecolor='black')
        plt.title(f'Latency Distribution for Core {i}')
        plt.xlabel('Count')
        plt.ylabel('Max Latency')
        plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.savefig('multi_core_latency_distribution.png', dpi=300)
    plt.show()

def main():
    """Main function to run steps."""
    filepath = 'C:/Users/ar-wahaj.kayani/Downloads/Latency2.txt'  # Update this to your actual data file path
    data = load_data(filepath)
    plot_histogram(data)

if __name__ == '__main__':
    main()
