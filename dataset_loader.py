import os 
import tkinter 
from tkinter import filedialog

def csv_finder():
    # These two lines hide the main Tkinter window.
    root = tkinter.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title = "Select the Dataset to be Analyzed!",
        filetypes=[("csv files", "*.csv"), ("All Files", "*.*")]
    )

    return file_path 