import Inverser
import numpy as np
def simpleDirection(InputData, i ,j ):
    ans = [
        np.zeros_like(InputData[0]),
        np.zeros_like(InputData[1]),
    ]
    if (i==-1):
        ans[0][0,j] += 1
    else:
        ans[1][i,j] += 1
    return ans


def getLoss(
        InputData = Inverser.GenOutput.default_sim_input(), 
        maxBatch = 1000000
):
    output = Inverser.GenOutput.sim_run(init=InputData[0], command=InputData[1])
    groundTruth = np.loadtxt("input_file/route.csv",delimiter=' ')[:10]
    batchNum = min(output.shape[0],groundTruth.shape[0],maxBatch)
    err = output[:batchNum]-groundTruth[:batchNum]
    ans = np.sum(np.abs(err)**4)
    # print(ans)
    return ans
    # pass

def linear_update(
    InputData = Inverser.GenOutput.default_sim_input(),
    deltaX = None,
    i = 0,
    j = 0,
    step = 1000000,
):
    if deltaX is None:
        deltaX = Inverser.Grad.simpleDirection(InputData,i,j)
        pass
    # print(len(InputData))
    l = [InputData[_]-deltaX[_] for _ in range(len(InputData))]
    r = [InputData[_]+deltaX[_] for _ in range(len(InputData))]
    for step in range(30):
        ml = [l[_]*.6+r[_]*.4 for _ in range(len(InputData))]
        # print(ml)
        mr = [l[_]*.4+r[_]*.6 for _ in range(len(InputData))]
        vl = getLoss(InputData=ml,maxBatch=step)
        vr = getLoss(InputData=mr,maxBatch=step)
        if (vl<vr):
            r = mr
        else:
            l = ml
    return [l[_]*.5+r[_]*.5 for _ in range(len(InputData))]

def SimpleDescent(

):
    groundTruth = np.loadtxt("input_file/route.csv",delimiter=' ')[:10]
    inputData = Inverser.GenOutput.default_sim_input(length=groundTruth.shape[0])
    for i in range(groundTruth.shape[0]):
        for _ in range(10):
            for j in range(i-1,i):
                for k in range(9):
                    inputData = linear_update(InputData=inputData,i=j,j=k,step=i)
                    print(j,k)
                    pass
                pass
            pass
    pass
