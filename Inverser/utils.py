import Inverser
import numpy as np
import pandas
# print("utils")
def get_pose(vel_file="./output_file/tmp/ref_vel.csv"):
    vel = Inverser.csvLoad.load_vel(vel_file)
    ans = np.zeros_like(vel)
    for i in range(ans.shape[0]-1):
        ans[i+1] = ans[i] + vel[i-1]*1e-2
    return ans


def get_input(input_file="input_file/motion2.csv"):
    a = open(input_file,"r").read()
    a = a.split("\n")
    open("tmp/tmp1.csv","w").write("\n".join(a[0:2]))
    open("tmp/tmp2.csv","w").write("\n".join(a[2:]))    
    # open(input_file+".tmp.csv","wb").write(a)
    px = pandas.read_csv("tmp/tmp1.csv",sep=',')
    px = px.to_numpy().astype(np.float64)
    py = pandas.read_csv("tmp/tmp2.csv",sep=',')
    py = py.to_numpy().astype(np.float64)
    return {
        "init":px,
        "command":py,
        "template":a,
    }

def put_input(init,x,template,input_file="input_file/motion_tmp.csv"):
    np.savetxt("tmp/tmp1.csv",init,delimiter=',',fmt="%.9f")
    np.savetxt("tmp/tmp2.csv",x[:,1:],delimiter=',',fmt="%.9f")
    in1 = open("tmp/tmp1.csv","r").read().split('\n')
    in2_ = open("tmp/tmp2.csv","r").read().split('\n')
    in2 = [("1,"+ss) for ss in in2_]
    open(input_file,"w").write("\n".join(template[0:1]+in1[:1]+template[2:3]+in2[:len(in2)-1]))
    pass

def run():
    pass
