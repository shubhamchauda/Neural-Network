import numpy as np 
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X,y = spiral_data(100,3)
print(X.shape)



class Layer_Dense:
    def __init__(self,n_inputs_shape) -> None:
        self.weights = 0.10 * np.random.randn(n_inputs_shape[0],n_inputs_shape[1])
        self.biases  = np.zeros((1,n_inputs_shape[1]))
    def forward(self,inputs):
        self.outputs = np.dot(inputs,self.weights)+ self.biases


# Rectified Linear activation function
class Activation_ReLU:
    def forward(self,inputs):
        self.outputs = np.maximum(0,inputs)

layer1= Layer_Dense((2,5))
layer2 = Layer_Dense((5,2))
actv1= Activation_ReLU()
actv2= Activation_ReLU()
layer1.forward(X)
actv1.forward(layer1.outputs)
layer2.forward(actv1.outputs)
actv2.forward(layer2.outputs)
print(actv2.outputs)

