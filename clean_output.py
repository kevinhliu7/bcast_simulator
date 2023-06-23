import os

# this is just to clean the output file
f = open("simulator_output.txt", "w")
f.write("final_time | N | PPN | alpha1 | alpha2 | beta1 | beta2" + "\n")
f.close()
os.system("rm -rf find -type f -iname '*.png' -delete")
os.system("clear")