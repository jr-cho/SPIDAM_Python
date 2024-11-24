import wave
import numpy as np
import matplotlib.pyplot as plt

def plot_wav(file_path):
    with wave.open(file_path, 'r') as wav_file:
        n_frames = wav_file.getnframes()
        framerate = wav_file.getframerate()
        audio_data = wav_file.readframes(n_frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)

        time_axis = np.linspace(0, n_frames / framerate, num=n_frames)

    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_array, color='blue')
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.tight_layout()
    plt.show()
