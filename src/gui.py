#importing necessary files
from tkinter import*
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#creating the tinker GUI
root = Tk()
#creating the settings for the title and size
root.title("SPIDAM Project")
root.geometry('750x750')
#creating the frame for the plot to be displayed it
frame = Frame(root,width = 250, height = 250)
frame.pack()
frame.place(anchor = 'center', relx = 0.5,rely = 0.5)
#creating introduction text and labels
first_lbl = Label(root,text = "Thanks for using our program! To begin, please upload a .mov or .wav file")
first_lbl.grid(row = 0, column = 0)
file_lbl = Label(root, text = "Please upload a .mov or .wav file")
file_lbl.place(x=100,y=31)
#creating a function to intake a file that is either a .mov or .wav

#creating a function to display the plot when the plot button is clicked

#creating buttons

#running the GUI until the user closes it
root.mainloop()