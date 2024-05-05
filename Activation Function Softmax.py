import math
import numpy as np
# inputs = [-1.76671581,2.54806252,0,3.53475832,0, -1.19255105]
# outputs= []

# exp = math.e
# print(inputs)
# exponential do not lose the meaning of -iv value


#---------------------------------------------
# exponential values
# for i in inputs:
#     outputs.append(exp**i)
# print(outputs)
#---------------------------------------------

#---------------------------------------------
# need to normalize exponential values
# Normalization
# norm_base = sum(outputs)
# norm_values  = []
# for i in outputs:
#     norm_values.append(i/norm_base)
# print(norm_values)
#---------------------------------------------



#using numpy

# outpus = np.exp(inputs)
# norm_outputs = outpus/np.sum(outputs)
# print(inputs)
# print(outpus)
# print(norm_outputs)




input_output = [[4.8,1.21,2.385],
                [8.9,-1.81,0.02],
                [1.41,1.051,0.026]]
exp_output = np.exp(input_output)
sum_exp_output = np.sum(exp_output,axis = 1,keepdims=True)

print(exp_output/sum_exp_output)


print(input_output-np.max(input_output, axis=1, keepdims=True))
