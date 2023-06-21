import numpy as np
import matplotlib.pyplot as plt
import math
import sys

# unfortunately, this part is kind of hard coded, can fix this later if necessary
# hierarchical runtime
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
    f = open("simulator_output.txt", "r")

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
            y_hierarchical.append(calculate_time_hierarchical(float(parameters[6]), float(parameters[5]), float(parameters[4]), float(parameters[3]), 1, int(parameters[1]), int(parameters[2])))


    plt.title("Time vs. " + parameter_to_look_at)
    plt.xlabel(parameter_to_look_at)
    plt.ylabel("Time")
    plt.grid()
    if (plot_hierarchical[ph]):
        plot = plt.plot(x_values, y_values, y_hierarchical)
    else:
        plot = plt.plot(x_values, y_values)
    plt.savefig('plot.png')


except:
    print("Something Went Wrong With the Plotting! Did you... ")
    print("Enter a valid parameter name? (N, PPN, alpha1, alpha2, beta1, beta2)")
    print("Make sure that the simulator_output file is formatted correctly?")
    



f.close()