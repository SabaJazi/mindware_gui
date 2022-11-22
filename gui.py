import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
# from pandas import DataFrame
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# from matplotlib.gridspec import GridSpec
# from tkinter import ALL

def func1():
    return()

# create a tkinter window
root = Tk()             
 
# Open window having dimension 100x100
root.geometry('450x300')

# the label for dataset
data_path = Label(root,
text = "data path").place(x = 40, y = 60) 
     
data_path_input_area = Entry(root,
width = 30).place(x = 110, y = 60) 
# ------------------------------------------------

load_button = Button(root,
text = "Load").place(x = 40, y = 130)

exit_button = Button(root,
text = "Exit").place(x = 140, y = 130)
# -------------------------------------------------------
  
# label
ttk.Label(root, text = "Select model type:",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 9, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
typechoosen = ttk.Combobox(root, width = 27, textvariable = n)
  
# Adding combobox drop down list
typechoosen['values'] = (' Classifyer', ' Bagging' )
  
typechoosen.grid(column = 1, row = 9)
typechoosen.current()
# ----------------------------------------------------------
# label
ttk.Label(root, text = "Select public dataset:",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 8, padx = 10, pady = 25)

n = tk.StringVar()
typechoosen = ttk.Combobox(root, width = 27, textvariable = n)
  
typechoosen['values'] = (' Boston house prices dataset',
 ' Iris plants dataset',
  'Diabetes dataset')
  
typechoosen.grid(column = 1, row = 8)
typechoosen.current()
#   --------------------------------------

root.mainloop()
print("test")