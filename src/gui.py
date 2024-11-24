#importing necessary files
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from file import convert_to_wav
import os
import wave
import numpy as np
import matplotlib.pyplot as plt

DEFAULT_AUDIO_FILE = "./data/clap.m4a"

def plot_to_gui(file_path, plot_frame):
    with wave.open(file_path, 'r') as wav_file:
        n_frames = wav_file.getnframes()
        framerate = wav_file.getframerate()
        audio_data = wav_file.readframes(n_frames)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)
        time_axis = np.linspace(0, n_frames / framerate, num=n_frames)
    for widget in plot_frame.winfo_children():
        widget.destroy()
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(time_axis, audio_array, color='blue')
    ax.set_title('Waveform')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.grid()
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    canvas.draw()

def use_default_file(plot_frame):
    if os.path.exists(DEFAULT_AUDIO_FILE):
        try:
            wav_path = convert_to_wav(DEFAULT_AUDIO_FILE)
            messagebox.showinfo("Success", f"Default audio converted to WAV: {wav_path}")
            plot_to_gui(wav_path, plot_frame)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", f"Default audio file not found: {DEFAULT_AUDIO_FILE}")

def add_custom_file(plot_frame):
    file_path = filedialog.askopenfilename(title="Select an Audio File")
    if file_path:
        try:
            wav_path = convert_to_wav(file_path)
            messagebox.showinfo("Success", f"Custom audio converted to WAV: {wav_path}")
            plot_to_gui(wav_path, plot_frame)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def create_gui():
    root = tk.Tk()
    root.title("Audio to WAV Converter and Plotter")
    root.geometry("800x600")
    plot_frame = tk.Frame(root, width=800, height=300, relief=tk.SUNKEN, borderwidth=1)
    plot_frame.pack(pady=20, fill=tk.BOTH, expand=True)
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=20)
    btn_default_file = tk.Button(btn_frame, text="Use Default Audio File", command=lambda: use_default_file(plot_frame))
    btn_default_file.grid(row=0, column=0, padx=10)
    btn_custom_file = tk.Button(btn_frame, text="Add Custom Audio File", command=lambda: add_custom_file(plot_frame))
    btn_custom_file.grid(row=0, column=1, padx=10)
    root.mainloop()