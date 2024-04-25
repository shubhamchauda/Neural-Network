import numpy as np




# one neuron  - 4 inputs
# inputs  = np.array([1,2,3,2.5])
#-----------------------------------------------
# biase = 2
# weights = np.array([0.2,0.8,-0.5,1.0])
# output = np.dot(inputs, weights)+biase
# print(output)
# ----------------------------------------------



#3 neurons - 4 input 
inputs  = np.array([1,2,3,2.5])

weights = np.array([[0.2,0.8,-0.5,1.0],
                    [0.5,-0.91,0.26,-0.5],
                    [-0.26,-0.27,0.17,0.87]])

biases = np.array([2,3,0.5])


output = np.dot(weights,inputs)+biases

print(output)








