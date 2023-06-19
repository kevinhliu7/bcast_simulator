# set up imports
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math
import more_itertools as mit
import time
import sys

# setting up global vars

if (len(sys.argv) < 7):
    print("You did not input enough cmd line arguments, expected: N, PPN, alpha1, alpha2, beta1, beta2")
    exit()

N = int(sys.argv[1]) # Number of Nodes
PPN = int(sys.argv[2]) # Processes Per Node
NP = PPN * N # Total Processes
alpha1 = float(sys.argv[3]) # Intranode latency
alpha2 = float(sys.argv[4]) # Internode latency
betan1 = float(sys.argv[5]) # Intranode bandwidth
betan2 = float(sys.argv[6])# Internode bandwidth

sends = []
recvs = []
times = [0.0 for i in range(NP)]
final_time = 0.0

# populates the list

def populate(rank, sends, recvs):
    mask = 0x1
    while (mask < NP):
        if (not(rank & mask == 0)):
            src = rank - mask + NP
            recvs.append({"src":src})
            break
        mask <<= 1
    mask >>= 1
    while (mask > 0):
        if (rank + mask < NP):
            dst = (rank + mask) % NP
            sends.append({"dst":dst})
        mask >>= 1  



def get_alpha_beta(src, dst):
    src_id = src // PPN
    dst_id = dst // PPN
    if (src_id == dst_id):
        return (alpha1 + betan1) / 2, 0
    else:
        return (alpha2 + betan2) / 2, 0

def update_message(src, dst, time):
    for t in recvs[dst]:
        if (t["src"] == src):
            t["time"] = time
            break

def progress(rank, sends, recvs):
    global final_time
    while recvs:
        if "time" in recvs[0]:
            copy, link = get_alpha_beta(recvs[0]["src"], rank)
            if (times[rank] < recvs[0]["time"]):
                times[rank] = recvs[0]["time"]
            times[rank] += copy
            recvs.pop(0)
        else:
            break
    if (not recvs):
        for t in sends:
            copy, link = get_alpha_beta(rank, t["dst"])
            times[rank] += copy
            update_message(rank, t["dst"], times[rank] + link)
        if (final_time < times[rank]):
            final_time = times[rank]
        return 1
    return 0

for i in range(NP):
    sends.append([])
    recvs.append([])
    populate(i, sends[i], recvs[i])
    ...

# call show_sends_recv
# call simulate
# dump final_time

n_complete = 0
while (n_complete < NP):
    for i in range(NP):
        n_complete += progress(i, sends[i], recvs[i])


f = open("simulator_output.txt", "a")
f.write(str(final_time) + "\n")