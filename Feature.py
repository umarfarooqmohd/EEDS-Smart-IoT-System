from scipy.stats import skew as skewness, kurtosis, entropy
from scipy import signal
import numpy as np

# Statistical Features
def compute_features(Magnitude):
    # Initializing lists to store the features
    mean = []
    median = []
    peak_amp = []
    RMS = []
    std_dev = []
    crest_factor = []
    peak_to_peak = []
    mean_freq = []
    peak_freq = []
    spec_centroid = []
    spec_spread = []
    spec_entropy = []
    spec_skewness = []
    spec_kurtosis = []
    rate_change_centroid = []
    rate_change_spread = []
    duration = []
    depth = []
    skewness_values = []
    kurtosis_values = []
    
    if Magnitude:
        # Mean, Median, and Standard Deviation
        mean_value = np.mean(Magnitude)
        median_value = np.median(Magnitude)
        std_dev_value = np.std(Magnitude)

        mean.append(mean_value)
        median.append(median_value)
        std_dev.append(std_dev_value)

        if len(Magnitude) > 0:
            # Amplitude Features
            peak_amplitude = np.max(Magnitude)
            average_amplitude = np.mean(Magnitude)
            rms = np.sqrt(np.mean(np.square(Magnitude)))
            crest_factor_value = peak_amplitude / rms
            peak_to_peak_value = np.ptp(Magnitude)

            peak_amp.append(peak_amplitude)
            RMS.append(rms)
            crest_factor.append(crest_factor_value)
            peak_to_peak.append(peak_to_peak_value)

            # Frequency-Domain Feature
            nperseg_value = min(10, len(Magnitude))
            frequencies, power_spectrum = signal.welch(Magnitude, fs=1000, nperseg=nperseg_value)
            #dominant frequency
            dominant_frequency = frequencies[np.argmax(power_spectrum)]
            mean_frequency = np.sum(frequencies * power_spectrum) / np.sum(power_spectrum)
            dominant_frequency = frequencies[np.argmax(power_spectrum)]
            spectral_centroid = np.sum(frequencies * np.abs(power_spectrum)) / np.sum(np.abs(power_spectrum))
            geometric_mean = np.exp(np.mean(np.log(power_spectrum)))
            arithmetic_mean = np.mean(power_spectrum)
            spectral_flat = geometric_mean / arithmetic_mean
            spectral_spread = np.sqrt(np.sum((frequencies - spectral_centroid) ** 2 * np.abs(power_spectrum)) / np.sum(np.abs(power_spectrum)))
            spectral_skewness = skewness(np.abs(frequencies))
            spectral_kurtosis_value = kurtosis(np.abs(frequencies))
            spectral_entropy_value = entropy(np.abs(frequencies))

            mean_freq.append(mean_frequency)
            peak_freq.append(peak_frequency)
            spec_centroid.append(spectral_centroid)
            spec_spread.append(spectral_spread)
            spec_skewness.append(spectral_skewness)
            spec_kurtosis.append(spectral_kurtosis_value)
            spec_entropy.append(spectral_entropy_value)

                sorted_indices = np.argsort(f)
    sorted_psd = psd[sorted_indices]
    cumulative_power = np.cumsum(sorted_psd)
    percentage_power = cumulative_power / total_power
    frequency_range_indices = np.where(percentage_power >= power_percentage)[0]

    # Calculate the bandwidth as the difference between the upper and lower frequency limits
    lower_index = np.min(frequency_range_indices)
    upper_index = np.max(frequency_range_indices)
    lower_frequency = f[sorted_indices[lower_index]]
    upper_frequency = f[sorted_indices[upper_index]]
    bandwidth = upper_frequency - lower_frequency

            # Rate of change of features
            rate_of_change_centroid = np.gradient(spectral_centroid)
            rate_of_change_spread = np.gradient(spectral_spread)

            rate_change_centroid.append(rate_of_change_centroid)
            rate_change_spread.append(rate_of_change_spread)

            # Time-Frequency Domain Feature
            f, t, Sxx = signal.spectrogram(np.array(Magnitude), fs=1000, nperseg=nperseg_value)

            # Duration of Signal
            threshold = 3.88
            above_threshold_indices = np.where(np.array(Magnitude) > threshold)[0]

            if len(above_threshold_indices) > 0:
                start_time = above_threshold_indices[0] / 1000
                end_time = above_threshold_indices[-1] / 1000
                duration_value = end_time - start_time
            else:
                duration_value = 0.0

            duration.append(duration_value)

            # Depth
            depth_value = (np.max(Magnitude) * duration_value) / 2
            depth.append(depth_value)

            # Time-Domain Feature
            skewness_value = skewness(np.array(Magnitude))
            kurtosis_value = kurtosis(np.array(Magnitude))
            skewness_values.append(skewness_value)
            kurtosis_values.append(kurtosis_value)

    return (mean, median, peak_amp, RMS, std_dev, crest_factor, peak_to_peak, mean_freq, peak_freq,
            spec_centroid, spec_spread, spec_entropy, spec_skewness, spec_kurtosis,
            rate_change_centroid, rate_change_spread, duration, depth, skewness_values, kurtosis_values)
