import pandas as pd

def create_dataset_from_features(*features):
    # Assuming each feature list has the same length
    num_samples = len(features[0])

    # Create a dictionary with the features
    data = {
        'Mean': features[0],
        'Median': features[1],
        'PeakAmplitude': features[2],
        'RootMeanSquare': features[3],
        'StandardDeviation': features[4],
        'CrestFactor': features[5],
        'PeakToPeak': features[6],
        'MeanFrequency': features[7],
        'PeakFrequency': features[8],
        'SpectralCentroid': features[9],
        'SpectralSpread': features[10],
        'SpectralEntropy': features[11],
        'SpectralSkewness': features[12],
        'SpectralKurtosis': features[13],
        'RateOfChangeCentroid': features[14],
        'RateOfChangeSpread': features[15],
        'Duration': features[16],
        'Depth': features[17],
        'Skewness': features[18],
        'Kurtosis': features[19]
        # Add more features if needed
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('features_dataset.csv', index=False)
