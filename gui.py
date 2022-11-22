# import tkinter as tk
from tkinter import *
# from tkinter import ttk
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
root.geometry('200x150')


 
# Create a Button
btn1 = Button(root, text = 'Select dataset !',
                          command = func1())
btn2 = Button(root, text = 'Exit !', 
                          command = root.destroy)
 
# Set the position of button on the top of window. 
btn1.pack(side = 'top')  
btn2.pack(side = 'bottom')   
 
root.mainloop()