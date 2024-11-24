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
def open_file():
    file = filedialog.askopenfilename(filetypes = [('Mov Files', '*.mov'),('Wav Files', '*.wav'),('All Files', '*.*')])
    if file:
        file_lbl.config(text = "File Successfully obtained")
        file.close()
    else:
        file_lbl.config(text = "Incorrect File Type or No File Selected")
#creating a function to display the plot when the plot button is clicked
def plot():
    #using text variables to check if the function works as intended
    #in the final version, fig will equal a function from plot.py
    #fig is equal to the data
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4],[1,4,9,16])
    #creating a canvas for the plot
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
#creating buttons
plot_btn = Button(root, text = "Show Plot", command = plot)
plot_btn.place(x = 0, y = 60)
file_btn = Button(root, text = "Import File",command = open_file)
file_btn.place(x = 0, y = 30)
#running the GUI until the user closes it
root.mainloop()