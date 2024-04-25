import numpy as np 


X  = np.array([[1.0,2.0,3.0,2.5],
                [2.0,5.0,-1.0,2.0],
                [-1.5,2.7,3.3,-0.8]])


class Layer_Dense:
    def __init__(self,n_inputs_shape) -> None:
        self.weights = 0.10 * np.random.randn(n_inputs_shape[0],n_inputs_shape[1])
        self.biases  = np.zeros((1,n_inputs_shape[1]))
    def forward(self,inputs):
        self.outputs = np.dot(inputs,self.weights)+ self.biases



layer1= Layer_Dense((4,5))
layer2 = Layer_Dense((5,2))
layer1.forward(X)
layer2.forward(layer1.outputs)
print(layer2.outputs)
