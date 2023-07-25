import os

# this is just to clean the output file
f = open("simulator_output.txt", "w")
g = open("simulator_hier_output.txt", "w")
h = open("simulator_output3.txt", "w")
i = open("simulator_output4.txt", "w")
f.write("final_time | N | PPN | alpha1 | alpha2 | beta1 | beta2" + "\n")
g.write("final_time | N | PPN | alpha1 | alpha2 | beta1 | beta2" + "\n")
h.write("final_time | N | PPN | alpha1 | alpha2 | beta1 | beta2" + "\n")
i.write("final_time | N | PPN | alpha1 | alpha2 | beta1 | beta2" + "\n")
f.close()
g.close()
h.close()
i.close()
os.system("rm -rf ./*.png")
os.system("clear")