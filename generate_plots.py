import os
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
# is_better = []
# not_better = []
os.system("python3 clean_output.py")
for N in [5, 16]:
    for PPN in range(1, 37):
        os.system("python3 binomial_simulator.py {} {} {} {} {} {}".format(N, PPN, 0.5, 2.9, int(0), int(0) ))
        os.system("python3 hierarchical_simulator.py {} {} {} {} {} {}".format(N, PPN, 0.5, 2.9, int(0), int(0)))

skip_first = True

hier = open("simulator_hier_output.txt", "r")
flat = open("simulator_output.txt", "r")

x_values = [i for i in range(1, 37)]
y_hier = []
y_flat = []
print(len(y_hier))
print(len(y_flat))
for line in hier:
    if skip_first:
        skip_first = False
        continue
    y_hier.append(line.split()[0])

skip_first = True
for line in flat:
    if skip_first:
        skip_first = False
        continue
    y_flat.append(line.split()[0])

y_hier_sections = [[], []]
y_flat_sections = [[], []]





y_hier_sections[0] = y_hier[0:36]
y_hier_sections[1] = y_hier[36:72]

y_flat_sections[0] = y_flat[0:36]
y_flat_sections[1] = y_flat[36:72]
rc('axes', linewidth=2)
ax = gca()
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for i, N in enumerate([5, 16]):
    plt.title("Theorectical Time vs. PPN \n {} Nodes, T_p2p_intra = 0.50 μs, T_p2p_inter = 2.9 μs".format(N), fontweight='bold')
    plt.xlabel("PPN (Processes Per Node)", fontweight='bold')
    plt.ylabel("Theorectical Time (μs)", fontweight='bold')
    plt.plot(x_values, y_flat_sections[i], label="Flat", color = 'black', marker='.')
    plt.plot(x_values, y_hier_sections[i], label="Topology-Aware", linestyle='dashdot', color = 'black', marker='.')
    plt.legend()
    plt.grid()
    temp = plt.show()
    plt.savefig("{}node_hier.png".format(N), bbox_inches="tight")
    

def calculate_time_hierarchical(B_inter, B_intra, a_inter, a_intra, m, N, PPN):
    # print(math.ceil(math.log2(N)) * (B_inter * m + a_inter))
    # return math.floor(math.log2(N))*(B_inter * m + a_inter) + math.floor(math.log2(PPN))*(B_intra * m + a_intra) # testing possible bug??
    return math.ceil(math.log2(N))*(B_inter * m + a_inter) + math.ceil(math.log2(PPN))*(B_intra * m + a_intra)

