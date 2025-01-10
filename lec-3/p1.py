from sklearn.datasets import make_classification
import numpy as np
x,y=make_classification(n_samples=100,n_features=2,n_informative=1,n_redundant=0,n_classes=2,n_clusters_per_class=1,random_state=41,hypercube=False,class_sep=10)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.scatter(x[:,0],x[:,1],c=y,cmap='winter',s=100)
plt.show()

def perceptron(x,y):
  w1=w2=b=1
  lr=0.1   #lr=learning rate
  for j in range(1000):
    for i in range(x.shape[0]):
       z=w1*x[i][0]+w2*x[i][1]+b
       if z*y[i]<0:
         w1=w1+lr*y[i]*x[i][0]
         w2=w2+lr*y[i]*x[i][1]
         b=b+lr*y[i]
    return w1,w2,b
w1,w2,b=perceptron(x,y)
print(w1,w2,b)

m=-(w1/w2)
c=-(b/w2)
print(m,c)

x_input=np.linspace(-3,3,100)
y_input=m*x_input+c
plt.figure(figsize=(10,6))
plt.plot(x_input,y_input,color='red',linewidth=3)
plt.scatter(x[:,0],x[:,1],c=y,cmap='winter',s=100)
plt.ylim(-3,2)
plt.show()