import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import utility
import os
from pylab import *

def calculate_time_hierarchical(B_inter, B_intra, a_inter, a_intra, m, N, PPN):
    return math.ceil(math.log2(N))*(B_inter * m + a_inter) + math.ceil(math.log2(PPN))*(B_intra * m + a_intra)

ph = ""
parameter_to_look_at = ""
try:
    parameter_to_look_at = sys.argv[1]
    ph = sys.argv[2]
except:
    print("Missing Parameter Argument")
try:
    f = open("simulator_adapt_output.txt", "r")
    g = open("simulator_hier_output.txt", "r")
    parameter_to_idx = {"N":1, "PPN":2, "alpha1":3, "alpha2":4, "beta1":5, "beta2":6}
    plot_hierarchical = {"Yes":True, "No":False}

    y_values = []
    x_values = []
    y_hierarchical = []

    skip_first = True
    for line in f:
        if (skip_first):
            skip_first = False
            continue
        
        parameters = line.split()
        y_values.append(float(parameters[0]))
        parameter_idx = parameter_to_idx[parameter_to_look_at]
        x_values.append(float(parameters[parameter_idx]))

        if (plot_hierarchical[ph]):
            ...
    skip_first = True
    for line in g:
        if (skip_first):
            skip_first = False
            continue
        parameters = line.split()
        y_hierarchical.append(float(parameters[0]))


    if (parameter_to_look_at == "PPN"):
        parameter_to_look_at = "PPN (Processes Per Node)"
    plt.title("Theoretical Time vs. " + parameter_to_look_at.split()[0], fontweight="bold")
    plt.xlabel(parameter_to_look_at, fontweight="bold")
    plt.ylabel("Theoretical Time (μs)", fontweight="bold")
    plt.grid()

    if (plot_hierarchical[ph]):
        rc('axes', linewidth=2)
        ax = gca()
        for tick in ax.xaxis.get_major_ticks():
            tick.label1.set_fontweight('bold')
        for tick in ax.yaxis.get_major_ticks():
            tick.label1.set_fontweight('bold')
        plt.plot(x_values, y_hierarchical, label="Hierarchical", linestyle = 'dashdot', color='black', marker=".")
        plot = plt.plot(x_values, y_values, label = "Adaptive", color='black', marker=".")
        plt.legend()
    else:
        rc('axes', linewidth=2)
        ax = gca()
        for tick in ax.xaxis.get_major_ticks():
            tick.label1.set_fontweight('bold')
        for tick in ax.yaxis.get_major_ticks():
            tick.label1.set_fontweight('bold')
        plot = plt.plot(x_values, y_values, label="Flat", color = 'black', marker='.')
    
    plot_file_name = "plot.png"
    plt.savefig(plot_file_name, bbox_inches='tight')
    


except:
    print("Something Went Wrong With the Plotting! Did you... ")
    print("Enter a valid parameter name? (N, PPN, alpha1, alpha2, beta1, beta2)")
    print("Make sure that the simulator_output file is formatted correctly?")
    



f.close()