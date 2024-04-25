import numpy as np


inputs = [-0.76671581,0.54806252,0,-1.53475832,0, 0.19255105]


# rectified liner activation function
outputs = []
for i in inputs:
    outputs.append(max(0,i))
print(outputs)