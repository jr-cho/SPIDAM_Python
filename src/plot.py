import matplotlib.pyplot as plt
import wave
import numpy as np

def plot_waveform(file_path):
    try:
        with wave.open(file_path, 'r') as wav_file:
            n_frames = wav_file.getnframes()
            framerate = wav_file.getframerate()
            audio_data = wav_file.readframes(n_frames)
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            time_axis = np.linspace(0, n_frames / framerate, num=n_frames)
        
        plt.figure(figsize=(10, 5))
        plt.plot(time_axis, audio_array, color='blue')
        plt.title('Waveform')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

    except Exception as e:
        print(f"Error plotting waveform: {e}")

def plot_spectrogram(file_path):
    try:
        with wave.open(file_path, 'r') as wav_file:
            n_frames = wav_file.getnframes()
            framerate = wav_file.getframerate()
            audio_data = wav_file.readframes(n_frames)
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
        
        plt.specgram(audio_array, Fs=framerate, NFFT=1024, noverlap=512, cmap='viridis')
        plt.title('Spectrogram')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar(label='Intensity (dB)')
        plt.show()

    except Exception as e:
        print(f"Error plotting spectrogram: {e}")
