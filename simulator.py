# set up imports, not all are used
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math
import more_itertools as mit
import time

# important imports for running shell cmds, not all are used
import sys
import os
import subprocess
import pkg_resources

# install missing modules if needed, particularly important for installing tkinter if the user does not already have it
required_modules = {"tk", "matplotlib", "numpy"}
installed_modules = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed_modules
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import tkinter
from tkinter import *

def run_algorithm():
    N = text_extract_nodes.get() + " "
    PPN = text_extract_ppn.get() + " "
    alpha1 = text_extract_alpha1.get() + " "
    alpha2 = text_extract_alpha2.get() + " "
    beta1 = text_extract_beta1.get() + " "
    beta2 = text_extract_beta2.get()
    name_of_file = text_extract_algo.get() + " "
    try:
        int(N)
        int(PPN)
        float(alpha1)
        float(alpha2)
        float(beta1)
        float(beta2)
    except:
        print("Not valid inputs: Issue 1")
        return
    command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + alpha2 + beta1 + beta2
    os.system(command_to_execute)


window = tkinter.Tk()
window.title("Simulation Tool")

text_extract_nodes = tkinter.StringVar(window)
text_extract_ppn = tkinter.StringVar(window)
text_extract_alpha1 = tkinter.StringVar(window)
text_extract_alpha2 = tkinter.StringVar(window)
text_extract_beta1 = tkinter.StringVar(window)
text_extract_beta2 = tkinter.StringVar(window)
text_extract_algo = tkinter.StringVar(window)

label_nodes_text = tkinter.StringVar(window)
label_nodes = tkinter.Label(window, textvariable=label_nodes_text, justify="left", anchor="w")
label_nodes_text.set("Enter the number of nodes: ")
label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
entry_box_nodes = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

label_ppn_text = tkinter.StringVar(window)
label_ppn = tkinter.Label(window, textvariable=label_ppn_text, justify="left", anchor="w")
label_ppn_text.set("Enter the PPN (Processes Per Node): ")
label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
entry_box_ppn = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

label_alpha1_text = tkinter.StringVar(window)
label_alpha1 = tkinter.Label(window, textvariable=label_alpha1_text, justify="left", anchor="w")
label_alpha1_text.set("Enter the intranode latency (alpha_intra): ")
label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
entry_box_alpha1 = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

label_alpha2_text = tkinter.StringVar(window)
label_alpha2 = tkinter.Label(window, textvariable=label_alpha2_text, justify="left", anchor="w")
label_alpha2_text.set("Enter the internode latency (alpha_inter): ")
label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
entry_box_alpha2 = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


label_beta1_text = tkinter.StringVar(window)
label_beta1 = tkinter.Label(window, textvariable=label_beta1_text, justify="left", anchor="w")
label_beta1_text.set("Enter the intranode bandwidth (beta_intra): ")
label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
entry_box_beta1 = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

label_beta2_text = tkinter.StringVar(window)
label_beta2 = tkinter.Label(window, textvariable=label_beta2_text, justify = LEFT)
label_beta2_text.set("Enter the internode bandwidth (beta_inter): ")
label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
entry_box_beta2 = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

label_name_text = tkinter.StringVar(window)
label_name = tkinter.Label(window, textvariable=label_name_text, justify = LEFT)
label_name_text.set("Enter the name of the algorithm to execute (must be python file): ")
label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
entry_box_name = tkinter.Entry(window, bd = 2, justify = LEFT, textvariable=text_extract_algo)
entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

execute_cmd = tkinter.Button(window, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
execute_cmd.grid(padx = 10, pady = 10)

window.mainloop()

exit()







