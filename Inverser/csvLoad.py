import Inverser
import pandas
import numpy as np
from io import StringIO
# print("csvLoad")
def load_csv_value(csv_file="./output_file/tmp/ref_vel.csv"):
    data = pandas.read_csv(csv_file,sep=',')
    # print(data)
    arr = np.array(data.to_numpy())
    return arr
        
def load_vel(csv_file="./output_file/tmp/ref_vel.csv"):
    return load_csv_value(csv_file)

def load_input(csv_file="./input_file/motion.csv"):
    
    return load_csv_value(csv_file)