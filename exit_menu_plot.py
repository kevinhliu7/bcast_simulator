import os
import sys
import subprocess
import pkg_resources

required_modules = {"tk"}
installed_modules = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed_modules
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import tkinter
from tkinter import *

def alpha1():
    os.system("python3 plotter.py alpha1 Yes")
    return

def alpha2():
    os.system("python3 plotter.py alpha2 Yes")
    return

def beta1():
    os.system("python3 plotter.py beta1 Yes")
    return

def beta2():
    os.system("python3 plotter.py beta2 Yes")
    return

def N():
    os.system("python3 plotter.py N Yes")
    return
def PPN():
    os.system("python3 plotter.py PPN Yes")
    return


plot_window = tkinter.Tk()
plot_window.title("Simulation Tool")
plot_window.resizable(False, False)

main_label = tkinter.Label(plot_window, text="Choose X-Axis Variable: ")
main_label.pack(padx = 10, pady = 10)
main_label.configure(font = ("Ariel", 12, "bold"))

alpha1_button = tkinter.Button(plot_window, text="Intranode Latency", command=alpha1)
alpha2_button = tkinter.Button(plot_window, text="Internode Latency", command=alpha2)
beta1_button = tkinter.Button(plot_window, text="Intranode Bandwidth", command=beta1)
beta2_button = tkinter.Button(plot_window, text="Internode Bandwidth", command=beta2)
N_button = tkinter.Button(plot_window, text="Number of Nodes", command=N)
PPN_button = tkinter.Button(plot_window, text = "Processes Per Node", command=PPN)

alpha1_button.pack(padx = 10, pady = 10)
alpha2_button.pack(padx = 10, pady = 10)
beta1_button.pack(padx = 10, pady = 10)
beta2_button.pack(padx = 10, pady = 10)
N_button.pack(padx = 10, pady = 10)
PPN_button.pack(padx = 10, pady = 10)

plot_window.mainloop()

