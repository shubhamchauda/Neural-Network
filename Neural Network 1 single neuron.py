
# single neuron with single output
inputs = [1.0,2.0,3.0,2.5]
weights = [0.5,1.0,1.5,0.2]
bias = 2

output  =inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3] + bias 
print(output)




# 3 neurons with 4 inputs
inputs = [1.0,2.0,3.0,2.5]
weights1 = [0.5,1.0,1.5,0.2]
weights2 = [0.5,0.2,0.25,0.12]
weights3 = [0.24,0.0,0.5,0.2]
bias1 = 2
bias2 =3
bias3 =0.5 

output  =[inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3] + bias3] 
print(output)