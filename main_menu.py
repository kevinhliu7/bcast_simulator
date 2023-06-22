# main menu for the simulator, allows user to choose whether to output a single point data point or many
import os
import sys
import pkg_resources
import subprocess

required_modules = {"tk"}
installed_modules = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed_modules
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import tkinter
from tkinter import *

def call_single():
    os.system("python3 simulator.py")
    return
def call_vary():
    os.system("python3 simulator_vary.py")
    return
def plotter():
    os.system("python3 exit_menu_plot.py")

window = tkinter.Tk()
window.title("Main Menu")
window.resizable(False, False)

label = tkinter.Label(window, text = "Choose a Simulation Option: ", justify = CENTER, anchor = "w")
label.configure(font = ("Ariel", 12, "bold"))
label.pack(padx = 10, pady = 5)

button_single = tkinter.Button(window, text="Generate Single Data Point", command=call_single, justify=LEFT)
button_single.pack(padx = 10, pady = 10)
button_vary = tkinter.Button(window, text="Generate Many Data Points", command=call_vary, justify=LEFT)
button_vary.pack(padx = 10, pady = 10)


label_plot = tkinter.Label(window, text = "Plot Graph Using Simulation Data: ", justify=CENTER, anchor="w")
label_plot.configure(font=("Ariel", 12, "bold"))
label_plot.pack(padx = 10, pady = 3)


button_plot = tkinter.Button(window, text="Plot Graph", command=plotter, justify=LEFT)
button_plot.pack(padx = 10, pady = 14)


window.mainloop()
exit()







