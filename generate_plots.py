import os
import sys

os.system("python3 clean_output.py")
for N in [1, 7]:
    for PPN in range(1, 101):
        os.system("python3 hierarchical_simulator.py {} {} {} {} {} {}".format(N, PPN, 0.5, 1, 0, 0))
    os.system("python3 plotter.py PPN Yes")
    os.system("python3 clean_output.py")