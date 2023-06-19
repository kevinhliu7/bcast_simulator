# set up imports
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

required_modules = {"tk", "matplotlib", "numpy"}
installed_modules = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed_modules
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import tkinter

top = tkinter.Tk()
top.mainloop()


exit()
N = input("Enter the number of nodes: \n") + " "
PPN = input("Enter the PPN (Processes Per Node): \n") + " "
alpha1 = input("Enter the intranode latency: \n") + " "
alpha2 = input("Enter the internode latency: \n") + " "
beta1 = input("Enter the intranode bandwidth \n") + " "
beta2 = input("Enter the internode bandwidth \n")

name_of_file = input("Enter the name of the algorithm to simulate (must be a python file): \n") + " "
command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + alpha2 + beta1 + beta2
os.system(command_to_execute)



