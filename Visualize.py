import pandas as pd
import matplotlib.pyplot as plt

def visualize_features(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Get the list of features (excluding the index column)
    features = df.columns.tolist()

    # Plot bar plots for each feature
    for feature in features:
        plt.figure(figsize=(8, 6))
        plt.bar(df.index, df[feature], color='skyblue')
        plt.xlabel('Sample')
        plt.ylabel(feature)
        plt.title(f'{feature} Bar Plot')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
