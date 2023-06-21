import os
import sys
import pkg_resources

required_modules = {"tk"}
installed_modules = {pkg.key for pkg in pkg_resources.working_set}
missing = required_modules - installed_modules
if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import tkinter
from tkinter import *
def clean():
    os.system("python3 clean_output.py")
def vary_alpha1():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)

    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_alpha1_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    entry_box_alpha1.insert(0, "lower bound...")
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_alpha1_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1_upper)
    entry_box_alpha1_upper.insert(0, "upper bound...")
    entry_box_alpha1_upper.grid(padx=8, pady=5, column = 2, row = 3)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        alpha1_upper = text_extract_alpha1_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            int(N)
            int(PPN)
            iter_lower = float(alpha1)
            float(alpha2)
            float(beta1)
            float(beta2)
            iter_upper = float(alpha1_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + N + PPN + str(iter_lower) + " " + alpha2 + beta1 + beta2
            os.system(command_to_execute)
            iter_lower += 1


    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return

def vary_alpha2():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)

    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_alpha2_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_alpha2_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2_upper)
    entry_box_alpha2_upper.insert(0, "upper bound...")
    entry_box_alpha2_upper.grid(padx=8, pady=5, column = 2, row = 4)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.insert(0, "lower bound...")
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        alpha2_upper = text_extract_alpha2_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            int(N)
            int(PPN)
            float(alpha1)
            iter_lower = float(alpha2)
            float(beta1)
            float(beta2)
            iter_upper = float(alpha2_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + str(iter_lower) + " " + beta1 + beta2
            os.system(command_to_execute)
            iter_lower += 1
        return
    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return

def vary_beta1():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)

    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_beta1_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_beta1_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1_upper)
    entry_box_beta1_upper.insert(0, "upper bound...")
    entry_box_beta1_upper.grid(padx=8, pady=5, column = 2, row = 5)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    entry_box_beta1.insert(0, "lower bound...")
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        beta1_upper = text_extract_beta1_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            int(N)
            int(PPN)
            float(alpha1)
            float(alpha2)
            iter_lower = float(beta1)
            float(beta2)
            iter_upper = float(beta1_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + alpha2 + str(iter_lower) + " " + beta2
            os.system(command_to_execute)
            iter_lower += 1
        return
    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return

def vary_beta2():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)

    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_beta2_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_beta2_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2_upper)
    entry_box_beta2_upper.insert(0, "upper bound...")
    entry_box_beta2_upper.grid(padx=8, pady=5, column = 2, row = 6)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_beta2.insert(0, "lower bound...")
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        beta2_upper = text_extract_beta2_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            int(N)
            int(PPN)
            float(alpha1)
            float(alpha2)
            float(beta1)
            iter_lower = float(beta2)
            iter_upper = float(beta2_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + N + PPN + alpha1 + alpha2 + beta1 + str(iter_lower)
            os.system(command_to_execute)
            iter_lower += 1
        return
    def clean():
        return
    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return

def vary_N():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)
    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_N_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_N_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_N_upper)
    entry_box_N_upper.insert(0, "upper bound...")
    entry_box_N_upper.grid(padx=8, pady=5, column = 2, row = 1)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_nodes.insert(0, "lower bound...")
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        N_upper = text_extract_N_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            iter_lower = int(N)
            int(PPN)
            float(alpha1)
            float(alpha2)
            float(beta1)
            float(beta2)
            iter_upper = int(N_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + str(iter_lower) + " " + PPN + alpha1 + alpha2 + beta1 + beta2
            os.system(command_to_execute)
            iter_lower += 1
        return
    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return

def vary_PPN():
    w = tkinter.Tk()
    w.title("Simulation Tool")
    w.resizable(False, False)

    text_extract_nodes = tkinter.StringVar(w)
    text_extract_ppn = tkinter.StringVar(w)
    text_extract_alpha1 = tkinter.StringVar(w)
    text_extract_alpha2 = tkinter.StringVar(w)
    text_extract_beta1 = tkinter.StringVar(w)
    text_extract_beta2 = tkinter.StringVar(w)
    text_extract_algo = tkinter.StringVar(w)
    # upperbound
    text_extract_PPN_upper = tkinter.StringVar(w)

    label_nodes_text = tkinter.StringVar(w)
    label_nodes = tkinter.Label(w, textvariable=label_nodes_text, justify="left", anchor="w")
    label_nodes_text.set("Number of Nodes: ")
    label_nodes.grid(padx = 10, pady = 10, column = 0, row = 1)
    entry_box_nodes = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_nodes)
    entry_box_nodes.grid(padx=10, pady=10, column = 1, row = 1)

    label_ppn_text = tkinter.StringVar(w)
    label_ppn = tkinter.Label(w, textvariable=label_ppn_text, justify="left", anchor="w")
    label_ppn_text.set("PPN (Processes Per Node): ")
    label_ppn.grid(padx = 10, pady = 10, column = 0, row = 2)
    entry_box_ppn = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_ppn)
    entry_box_ppn.grid(padx=10, pady=10, column = 1, row = 2)

    label_alpha1_text = tkinter.StringVar(w)
    label_alpha1 = tkinter.Label(w, textvariable=label_alpha1_text, justify="left", anchor="w")
    label_alpha1_text.set("Intranode Latency (alpha_intra): ")
    label_alpha1.grid(padx = 10, pady = 10, column = 0, row = 3)
    entry_box_alpha1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha1)
    
    entry_box_alpha1.grid(padx=10, pady=10, column = 1, row = 3)

    entry_box_PPN_upper = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_PPN_upper)
    entry_box_PPN_upper.insert(0, "upper bound...")
    entry_box_PPN_upper.grid(padx=8, pady=5, column = 2, row = 2)

    label_alpha2_text = tkinter.StringVar(w)
    label_alpha2 = tkinter.Label(w, textvariable=label_alpha2_text, justify="left", anchor="w")
    label_alpha2_text.set("Internode Latency (alpha_inter): ")
    label_alpha2.grid(padx = 10, pady = 10, column = 0, row = 4)
    entry_box_alpha2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_alpha2)
    entry_box_alpha2.grid(padx=10, pady=10, column = 1, row = 4)


    label_beta1_text = tkinter.StringVar(w)
    label_beta1 = tkinter.Label(w, textvariable=label_beta1_text, justify="left", anchor="w")
    label_beta1_text.set("Intranode Bandwidth (beta_intra): ")
    label_beta1.grid(padx = 10, pady = 10, column = 0, row = 5)
    entry_box_beta1 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta1)
    
    entry_box_beta1.grid(padx=10, pady=10, column = 1, row = 5)

    label_beta2_text = tkinter.StringVar(w)
    label_beta2 = tkinter.Label(w, textvariable=label_beta2_text, justify = LEFT)
    label_beta2_text.set("Internode Bandwidth (beta_inter): ")
    label_beta2.grid(padx = 10, pady = 10, column = 0, row = 6)
    entry_box_beta2 = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_beta2)
    entry_box_ppn.insert(0, "lower bound...")
    entry_box_beta2.grid(padx=10, pady=10, column = 1, row = 6)

    label_name_text = tkinter.StringVar(w)
    label_name = tkinter.Label(w, textvariable=label_name_text, justify = LEFT)
    label_name_text.set("Algorithm to Execute (must be python file): ")
    label_name.grid(padx = 10, pady = 10, column = 0, row = 7)
    entry_box_name = tkinter.Entry(w, bd = 2, justify = LEFT, textvariable=text_extract_algo)
    entry_box_name.grid(padx=10, pady=10, column = 1, row = 7)

    def run_algorithm():
        N = text_extract_nodes.get() + " "
        PPN = text_extract_ppn.get() + " "
        alpha1 = text_extract_alpha1.get() + " "
        alpha2 = text_extract_alpha2.get() + " "
        beta1 = text_extract_beta1.get() + " "
        beta2 = text_extract_beta2.get()
        name_of_file = text_extract_algo.get() + " "
        PPN_upper = text_extract_PPN_upper.get()
        iter_lower = 0
        iter_upper = 0
        try:
            int(N)
            iter_lower = int(PPN)
            float(alpha1)
            float(alpha2)
            float(beta1)
            float(beta2)
            iter_upper = int(PPN_upper)
        except:
            print("Not valid inputs: Issue 1")
            return
        if (iter_lower < 0):
            iter_lower = 0
        while (iter_lower <= iter_upper):
            command_to_execute = "python3 " + name_of_file + N + str(iter_lower) + " " + alpha1 + alpha2 + beta1 + beta2
            os.system(command_to_execute)
            iter_lower += 1
        return
    execute_algo = tkinter.Button(w, command=run_algorithm, text="Execute", justify=CENTER, anchor = "w")
    execute_algo.grid(padx = 10, pady = 10, column = 0, row = 8)

    execute_clean = tkinter.Button(w, command = clean, text = "Reset", justify=CENTER, anchor ="w")
    execute_clean.grid(padx = 10, pady = 10, column = 1, row = 8)

    w.mainloop()
    return


























# Vary Menu

window = tkinter.Tk()
window.title("Simulation Tool")
window.resizable(False, False)


choose_label = tkinter.Label(window, text="Choose a Variable to Vary: ", justify=CENTER, anchor="w")
choose_label.configure(font = ("Ariel", 12, "bold"))
choose_label.pack(padx=10, pady=5)

button_N = tkinter.Button(window, text = "Number of Nodes", justify=CENTER, anchor="w", command=vary_N)
button_N.pack(padx = 10, pady = 10)

button_PPN = tkinter.Button(window, text = "Processes Per Node", justify=CENTER, anchor="w", command=vary_PPN)
button_PPN.pack(padx = 10, pady = 10)

button_alpha1 = tkinter.Button(window, text = "Intranode Latency", justify=CENTER, anchor="w", command=vary_alpha1)
button_alpha1.pack(padx = 10, pady = 10)

button_alpha2 = tkinter.Button(window, text = "Internode Latency", justify=CENTER, anchor="w", command=vary_alpha2)
button_alpha2.pack(padx = 10, pady = 10)

button_beta1 = tkinter.Button(window, text = "Intranode Bandwidth", justify=CENTER, anchor="w", command=vary_beta1)
button_beta1.pack(padx = 10, pady = 10)

button_beta2 = tkinter.Button(window, text = "Internode Bandwidth", justify=CENTER, anchor="w",command=vary_beta2)
button_beta2.pack(padx = 10, pady = 13)

window.mainloop()

exit()
