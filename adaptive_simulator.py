# set up imports, not all are used
import numpy as np
import math
import time
import sys


if (len(sys.argv) < 7):
    print("You did not input enough cmd line arguments, expected: N, PPN, alpha1, alpha2, beta1, beta2")
    exit()

# setting up global vars

N = int(sys.argv[1]) # Number of Nodes
PPN = int(sys.argv[2]) # Processes Per Node
NP = PPN * N # Total Processes
alpha1 = float(sys.argv[3]) # Intranode latency
alpha2 = float(sys.argv[4]) # Internode latency
betan1 = float(sys.argv[5]) # Intranode bandwidth
betan2 = float(sys.argv[6])# Internode bandwidth

T_intra = alpha1 + betan1
T_inter = alpha2 + betan2

topology = [[] for i in range(N)]
timings = [np.inf for rank in range(NP)]
sends = [[] for rank in range(NP)]
recvs = [[] for rank in range(NP)]

node_idx = 0
for rank in range(NP):
    topology[node_idx].append(rank)
    node_idx = (node_idx + 1) % N

priority_list = [rank for rank in range(1, NP)]

def is_external_process(rank):
    for node in topology:
        if (node):
            if (rank == node[0]):
                return True
    return False

def get_send_type(src, dst, topology):
    for node in topology:
        if (src in node):
            if (dst in node):
                return "intra"
            else:
                return "inter"
    return "error"

timings[0] = 0.0

def find_next_sender(timings):
    return np.argmin(timings)

def find_next_receiver(sender):
    if (not priority_list):
        return -1
    for i, dst in enumerate(priority_list):
        if (get_send_type(sender, dst, topology) == "inter"):
            if (is_external_process(dst)):
                final_dst = dst
                priority_list.pop(i)
                return final_dst
        else:
            final_dst = dst
            priority_list.pop(i)
            return final_dst
    final_dst = priority_list[0]
    priority_list.pop(0)
    return final_dst

def get_copy_link(src, dst):
    send_type = get_send_type(src, dst, topology)
    if (send_type == "intra"):
        return T_intra / 2, 0
    else:
        return T_inter / 2, 0

while priority_list:
    sender = find_next_sender(timings)
    receiver = find_next_receiver(sender)
    recvs[receiver].append(sender)
    sends[sender].append(receiver)
    copy, link = get_copy_link(sender, receiver)
    timings[sender] += copy
    timings[receiver] = timings[sender] + copy + link

final_time = np.max(timings)

f = open("simulator_adapt_output.txt", "a")
f.write(str(final_time) + " " + str(N) + " " + str(PPN) + " " + str(alpha1) + " " + str(alpha2) + " " + str(betan1) + " " + str(betan2) + "\n")
f.close()