# main menu for the simulator, allows user to choose whether to output a single point data point or many
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

def call_single():
    window.quit()
    os.system("python3 simulator.py")
    return
def call_vary():
    os.system("python3 simulator_vary.py")
    window.quit()
    return

window = tkinter.Tk()
window.title("Main Menu")

label = tkinter.Label(window, text = "Choose a Simulation Option: ", justify = CENTER, anchor = "w")
label.grid(column = 0, row = 0, padx = 10, pady = 10)

button_single = tkinter.Button(window, text="Generate Single Data Point", command=call_single, justify=LEFT)
button_single.grid(column = 1, row = 0, padx = 10, pady = 10)
button_vary = tkinter.Button(window, text="Vary a Parameter (Generate Many Points)", command=call_vary, justify=LEFT)
button_vary.grid(column = 1, row = 1, padx = 10, pady = 10)


window.mainloop()
exit()







