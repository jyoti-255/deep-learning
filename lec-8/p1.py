'''
import numpy as np
import pandas as pd

data=pd.DataFrame([[8,8,4],[7,9,5],[6,10,6],[5,12,7]],columns=['cgpa','profile_score','lpa'])

print(data)

def initialize_parameters(layer_dims):
   np.random.seed(3)
   parameters={}
   L=len(layer_dims)
   for l in range(1,L):
    parameters['w'+str(l)]=np.ones((layer_dims[l-1],layer_dims[l]))*0.1
    parameters['b'+str(l)]=np.zeros((layer_dims[l],1))
   return parameters

def linear_forward(A_prev,W,b):
   Z=np.dot(W.T,A_prev)+b
   return Z
#Forward Prop
def L_layer_forward(X,parameters):
  A=X
  L=len(parameters)//2
  for l in range(1,L+1):
    A_Prev=A
    W1=parameters['w'+str(l)]
    b1=parameters['b'+str(l)]
    print("A"+str(l-1)+":",A_Prev)
    print("W"+str(l)+":",W1)
    print("b"+str(l)+":",b1)
    print("--"*20)
    A=linear_forward(A_prev,W1,b1)
    print("A"+str(l)+":",A)
    print("**"*20)
  return A,A_prev

X=data[['cgpa','profile_score']].values[0].reshape(2,1)
y=data[['lpa']].values[0][0]
parameters=initialize_parameters([2,2,1])
L_layer_forward(X,parameters)

'''
import numpy as np
import pandas as pd

# Data
data = pd.DataFrame([[8, 8, 4], [7, 9, 5], [6, 10, 6], [5, 12, 7]], 
                    columns=['cgpa', 'profile_score', 'lpa'])

print(data)

# Initialize parameters
def initialize_parameters(layer_dims):
    np.random.seed(3)
    parameters = {}
    L = len(layer_dims)
    
    for l in range(1, L):
        parameters['W' + str(l)] = np.ones((layer_dims[l], layer_dims[l-1])) * 0.1  # Corrected shape
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    
    return parameters

# Linear forward
def linear_forward(A_prev, W, b):
    Z = np.dot(W, A_prev) + b  # Corrected dot product
    return Z

# Forward propagation for L layers
def L_layer_forward(X, parameters):
    A = X
    L = len(parameters) // 2  # Number of layers
    
    for l in range(1, L + 1):
        A_prev = A
        W = parameters['W' + str(l)]
        b = parameters['b' + str(l)]
        
        print(f"A{l-1}:\n{A_prev}")
        print(f"W{l}:\n{W}")
        print(f"b{l}:\n{b}")
        print("--" * 20)
        
        A = linear_forward(A_prev, W, b)
        
        print(f"A{l}:\n{A}")
        print("**" * 20)
    
    return A  # Final output

# Input and parameters
X = data[['cgpa', 'profile_score']].values[0].reshape(2, 1)  # First row reshaped
y = data[['lpa']].values[0][0]
parameters = initialize_parameters([2, 2, 1])  # [input, hidden1, output]

# Perform forward propagation
output = L_layer_forward(X, parameters)
print(output)


def update_parameters(parameters,y,y_hat,A1,X):
  parameters['W2'][0][0]=parameters['W2'][0][0]+(0.001*2*(y-y_hat)*A1[0][0])
  parameters['W2'][1][0]=parameters['W2'][1][0]+(0.001*2*(y-y_hat)*A1[1][0])
  parameters['b2'][0][0]=parameters['W2'][1][0]+(0.001*2*(y-y_hat))

  parameters['W1'][0][0]=parameters['W1'][0][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0]*X[0][0])
  parameters['W1'][1][0]=parameters['W1'][0][1]+(0.001*2*(y-y_hat)*parameters['W2'][0][0]*X[1][0])
  parameters['b1'][0][0]=parameters['b1'][0][0]+(0.001*2*(y-y_hat)*parameters['W2'][0][0])


  parameters['W1'][1][0]=parameters['W1'][1][0]+(0.001*2*(y-y_hat)*parameters['W2'][1][0]*X[0][0])
  parameters['W1'][1][1]=parameters['W1'][1][1]+(0.001*2*(y-y_hat)*parameters['W2'][1][0]*X[1][0])
  parameters['b1'][1][0]=parameters['b1'][1][0]+(0.001*2*(y-y_hat)*parameters['W2'][1][0])


