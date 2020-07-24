import Inverser
import sys
import os
# Inverser.GenOutput.sim()
# Inverser.GenOutput.run()
# print(Inverser.GenOutput.sim_run())
# print(Inverser.GenOutput.sim_run(init=Inverser.GenOutput.default_sim_input()[0]*10))
# print(Inverser.GenOutput.sim_run(init=Inverser.GenOutput.default_sim_input()[0]*1))
os.system("rm -r demo_saved_data")
Inverser.Grad.SimpleDescent()
# system("")