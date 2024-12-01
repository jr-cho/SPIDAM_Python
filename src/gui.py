#importing necessary files
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from file import convert_to_wav
from plot import plot_waveform, plot_spectrogram
import os

DEFAULT_AUDIO_FILE = "./data/clap.m4a"

class AudioAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio to WAV Converter and Plotter")
        self.root.geometry("800x600")

        # Instance variable to store the current audio file path
        self.current_audio_file = None

        self.setup_ui()

    def setup_ui(self):
        # Plot frame for displaying graphs
        self.plot_frame = tk.Frame(self.root, width=800, height=300, relief=tk.SUNKEN, borderwidth=1)
        self.plot_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Button frame for user actions
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)

        # Buttons for file selection and graph generation
        btn_default_file = tk.Button(btn_frame, text="Use Default Audio File", command=self.use_default_file)
        btn_default_file.grid(row=0, column=0, padx=10)

        btn_custom_file = tk.Button(btn_frame, text="Add Custom Audio File", command=self.add_custom_file)
        btn_custom_file.grid(row=0, column=1, padx=10)

        btn_waveform = tk.Button(btn_frame, text="Plot Waveform", command=self.plot_waveform)
        btn_waveform.grid(row=1, column=0, padx=10)

        btn_spectrogram = tk.Button(btn_frame, text="Plot Spectrogram", command=self.plot_spectrogram)
        btn_spectrogram.grid(row=1, column=1, padx=10)

    def use_default_file(self):
        """Use the default audio file and convert it to WAV."""
        if os.path.exists(DEFAULT_AUDIO_FILE):
            try:
                self.current_audio_file = convert_to_wav(DEFAULT_AUDIO_FILE)
                messagebox.showinfo("Success", f"Default audio converted to WAV: {self.current_audio_file}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", f"Default audio file not found: {DEFAULT_AUDIO_FILE}")

    def add_custom_file(self):
        """Allow the user to select a custom audio file and convert it to WAV."""
        file_path = filedialog.askopenfilename(title="Select an Audio File")
        if file_path:
            try:
                self.current_audio_file = convert_to_wav(file_path)
                messagebox.showinfo("Success", f"Custom audio converted to WAV: {self.current_audio_file}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def plot_waveform(self):
        """Plot the waveform of the current audio file."""
        if not self.current_audio_file:
            messagebox.showerror("Error", "No audio file selected or converted.")
            return
        try:
            plot_waveform(self.current_audio_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot waveform: {e}")

    def plot_spectrogram(self):
        """Plot the spectrogram of the current audio file."""
        if not self.current_audio_file:
            messagebox.showerror("Error", "No audio file selected or converted.")
            return
        try:
            plot_spectrogram(self.current_audio_file)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot spectrogram: {e}")

def create_gui():
    root = tk.Tk()
    app = AudioAnalyzerGUI(root)
    root.mainloop()
