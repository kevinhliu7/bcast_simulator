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

# import for setting up GUI for easier use
# import Tkinter
import pkg_resources
N = input("Enter the number of nodes: \n") + " "
PPN = input("Enter the PPN (Processes Per Node): \n") + " "
alpha1 = input("Enter the intranode latency: \n") + " "
alpha2 = input("Enter the internode latency: \n") + " "
beta1 = input("Enter the intranode bandwidth \n") + " "
beta2 = input("Enter the internode bandwidth \n")

name_of_file = input("Enter the name of the algorithm to simulate (must be a python file): \n") + " "
command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + alpha2 + beta1 + beta2
os.system(command_to_execute)



