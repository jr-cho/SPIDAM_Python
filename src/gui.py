import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .plot import plot_waveform, plot_spectrogram, plot_low_rt60, plot_mid_rt60, plot_high_rt60, plot_combined_rt60
import os

class AudioAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SPIDAM")
        self.root.geometry("800x600")
        self.root.configure(bg="lightgray")
        self.current_audio_file = None
        self.canvas = None
        self.graph_frame = tk.Frame(root, bg="white", width=800, height=400)
        self.graph_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.controls_frame = tk.Frame(root, bg="darkgray", height=200)
        self.controls_frame.pack(side=tk.BOTTOM, fill=tk.X)
        file_frame = tk.Frame(self.controls_frame, bg="darkgray")
        file_frame.pack(side=tk.LEFT, padx=20, pady=10)
        tk.Button(file_frame, text="Default", command=self.use_default_file, width=10, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(file_frame, text="Upload", command=self.add_custom_file, width=10, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)
        plot_frame = tk.Frame(self.controls_frame, bg="darkgray")
        plot_frame.pack(side=tk.RIGHT, padx=20, pady=10)
        tk.Button(plot_frame, text="Wave Form", command=self.plot_waveform, width=15, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(plot_frame, text="Spectro", command=self.plot_spectrogram, width=15, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(plot_frame, text="Low RT60", command=self.plot_low_rt60, width=15, font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(plot_frame, text="Mid RT60", command=self.plot_mid_rt60, width=15, font=("Arial", 10, "bold")).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(plot_frame, text="High RT60", command=self.plot_high_rt60, width=15, font=("Arial", 10, "bold")).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(plot_frame, text="Combined RT60", command=self.plot_combined_rt60, width=15, font=("Arial", 10, "bold")).grid(row=2, column=1, padx=10, pady=10)

    def use_default_file(self):
        default_file = "./data/clap.wav"
        if os.path.exists(default_file):
            self.current_audio_file = default_file
            messagebox.showinfo("Info", "Default file selected.")
        else:
            messagebox.showerror("Error", f"Default file not found: {default_file}")

    def add_custom_file(self):
        file_path = filedialog.askopenfilename(title="Select an Audio File")
        if file_path:
            self.current_audio_file = file_path
            messagebox.showinfo("Success", f"Loaded file: {file_path}")

    def clear_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None

    def plot_waveform(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_waveform(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_spectrogram(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_spectrogram(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_low_rt60(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_low_rt60(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_mid_rt60(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_mid_rt60(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_high_rt60(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_high_rt60(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_combined_rt60(self):
        if not self.current_audio_file:
            messagebox.showerror("Error", "No file selected.")
            return
        self.clear_graph()
        fig = plot_combined_rt60(self.current_audio_file)
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def create_gui():
    root = tk.Tk()
    app = AudioAnalyzerGUI(root)
    root.mainloop()
