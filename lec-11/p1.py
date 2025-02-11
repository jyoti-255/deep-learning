#Vanishing Gradient Problem in ANN

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential


x,y=make_moons(n_samples=250,noise=0.05,random_state=42)

plt.scatter(x[:,0],x[:,1],c=y,s=100)
plt.show()

model=Sequential()
model.add(Dense(10,activation='sigmoid',input_dim=2))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(10,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.get_weights()[0]

old_weights=model.get_weights()[0]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)

model.fit(x_train,y_train,epochs=100)
new_weights = model.get_weights()[0]
model.optimizer.get_config()["learning_rate"]

gradient = (old_weights - new_weights)/ 0.001
percent_change = abs(100*(old_weights - new_weights)/ old_weights)
print(gradient)

print(percent_change)
print(old_weights)
print(new_weights)
model=Sequential()
model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

old_weights=model.get_weights()[0]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=42)

model.fit(x_train,y_train,epochs=100)


new_weights-model.get_weights()[0]
model.optimizer.get_config()["learning_rate"]


gradient = (old_weights - new_weights)/ 0.001
percent_change = abs(100*(old_weights - new_weights)/ old_weights)

print(gradient)
print(percent_change)
print(old_weights)
print(new_weights)




