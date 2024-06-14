import numpy as np
import matplotlib.pyplot as plt

# Function to generate synthetic earthquake signal
def generate_earthquake_signal(duration, sampling_rate, earthquake_type):
    time = np.linspace(0, duration, duration * sampling_rate)
    if earthquake_type == "tectonic":
        # Tectonic earthquake signal with broad frequency content
        signal = np.random.normal(0, 1, len(time))
    elif earthquake_type == "volcanic":
        # Volcanic earthquake signal with localized frequency content
        signal = np.sin(2 * np.pi * 10 * time) + np.random.normal(0, 0.5, len(time))
    return signal

# Function to compute power spectral density (PSD)
def power_spectral_density(signal, sampling_rate):
    fft_result = np.fft.fft(signal)
    power_spectrum = np.abs(fft_result) ** 2
    frequency_bins = np.fft.fftfreq(len(signal), 1/sampling_rate)
    return frequency_bins[:len(frequency_bins)//2], power_spectrum[:len(power_spectrum)//2]

# Function to compute energy spectral density (ESD)
def energy_spectral_density(signal, sampling_rate):
    freq_bins, power_spectrum = power_spectral_density(signal, sampling_rate)
    energy_density = power_spectrum / sampling_rate  # Normalize by sampling rate
    return freq_bins, energy_density

# Parameters
duration = 10  # Duration of the earthquake signal in seconds
sampling_rate = 1000  # Sampling rate in Hz

# Generate synthetic earthquake signals
tectonic_signal = generate_earthquake_signal(duration, sampling_rate, "tectonic")
volcanic_signal = generate_earthquake_signal(duration, sampling_rate, "volcanic")

# Compute PSD and ESD for tectonic earthquake signal
tectonic_freq, tectonic_psd = power_spectral_density(tectonic_signal, sampling_rate)
_, tectonic_esd = energy_spectral_density(tectonic_signal, sampling_rate)

# Compute PSD and ESD for volcanic earthquake signal
volcanic_freq, volcanic_psd = power_spectral_density(volcanic_signal, sampling_rate)
_, volcanic_esd = energy_spectral_density(volcanic_signal, sampling_rate)

# Plot PSD and ESD for tectonic earthquake signal
plt.figure(figsize=(12, 6))

# Plot PSD
plt.subplot(2, 1, 1)
plt.plot(tectonic_freq, tectonic_psd, color='blue', label='PSD')
plt.title('Power Spectral Density (PSD) and Energy Spectral Density (ESD) - Tectonic Earthquake Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.legend()

# Plot ESD
plt.subplot(2, 1, 2)
plt.plot(tectonic_freq, tectonic_esd, color='red', label='ESD')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy Density')
plt.legend()

plt.tight_layout()
plt.show()

# Plot PSD and ESD for volcanic earthquake signal
plt.figure(figsize=(12, 6))

# Plot PSD
plt.subplot(2, 1, 1)
plt.plot(volcanic_freq, volcanic_psd, color='blue', label='PSD')
plt.title('Power Spectral Density (PSD) and Energy Spectral Density (ESD) - Volcanic Earthquake Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.legend()

# Plot ESD
plt.subplot(2, 1, 2)
plt.plot(volcanic_freq, volcanic_esd, color='red', label='ESD')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy Density')
plt.legend()

plt.tight_layout()
plt.show()
