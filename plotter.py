import numpy as np
import matplotlib.pyplot as plt
import math
import sys

parameter_to_look_at = ""
try:
    parameter_to_look_at = sys.argv[1]
except:
    print("Missing Parameter Argument")
try:
    f = open("simulator_output.txt", "r")

    parameter_to_idx = {"N":1, "PPN":2, "alpha1":3, "alpha2":4, "beta1":5, "beta2":6}

    y_values = []
    x_values = []

    skip_first = True
    for line in f:
        if (skip_first):
            skip_first = False
            continue
        parameters = line.split()
        y_values.append(float(parameters[0]))
        parameter_idx = parameter_to_idx[parameter_to_look_at]
        x_values.append(float(parameters[parameter_idx]))

    plt.title("Time vs. " + parameter_to_look_at)
    plt.xlabel(parameter_to_look_at)
    plt.ylabel("Time")
    plt.grid()
    plot = plt.plot(x_values, y_values, color="red")
    plt.savefig('plot.png')


except:
    print("Something Went Wrong With the Plotting! Did you... ")
    print("Enter a valid parameter name? (N, PPN, alpha1, alpha2, beta1, beta2)")
    print("Make sure that the simulator_output file is formatted correctly?")
    



f.close()