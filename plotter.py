import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import utility
import os

# unfortunately, this part is kind of hard coded, can fix this later if necessary
# hierarchical runtime
def calculate_time_hierarchical(B_inter, B_intra, a_inter, a_intra, m, N, PPN):
    # print(math.ceil(math.log2(N)) * (B_inter * m + a_inter))
    # return math.floor(math.log2(N))*(B_inter * m + a_inter) + math.floor(math.log2(PPN))*(B_intra * m + a_intra) # testing possible bug??
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
    is_power_of_two = []

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
            y_hierarchical.append(calculate_time_hierarchical(float(parameters[6]), float(parameters[5]), float(parameters[4]), float(parameters[3]), 0, int(parameters[1]), int(parameters[2])))
            PPN_N = int(parameters[1]) * int(parameters[2])
            is_power_of_two.append(utility.power_of_two(int(parameters[2])))


    plt.title("Time vs. " + parameter_to_look_at)
    plt.xlabel(parameter_to_look_at)
    plt.ylabel("Time")
    plt.grid()
    if (plot_hierarchical[ph]):
        #plt.plot(x_values, is_power_of_two, label="N*PPN pof2")
        plt.plot(x_values, y_hierarchical, label="Hierarchical")
        plot = plt.plot(x_values, y_values, label = "Hierarchical True")
        plt.legend()
    else:
        plot = plt.plot(x_values, y_values, label="Flat")
        plt.legend()
    plot_file_name = 'plot-N={}.png'.format(int(parameters[1]))
    plt.savefig(plot_file_name)
    os.system("mv {} $HOME/Pictures/hier_vs_hier_true_analysis_PPN=100".format(plot_file_name))


except:
    print("Something Went Wrong With the Plotting! Did you... ")
    print("Enter a valid parameter name? (N, PPN, alpha1, alpha2, beta1, beta2)")
    print("Make sure that the simulator_output file is formatted correctly?")
    



f.close()