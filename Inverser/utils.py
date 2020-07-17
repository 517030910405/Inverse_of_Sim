import Inverser
import numpy as np
# print("utils")
def get_pose(vel_file="./output_file/tmp/ref_vel.csv"):
    vel = Inverser.csvLoad.load_vel(vel_file)
    ans = np.zeros_like(vel)
    for i in range(ans.shape[0]-1):
        ans[i+1] = ans[i] + vel[i-1]*1e-2
    return ans
