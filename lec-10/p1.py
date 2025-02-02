import numpy as np
import pandas as pd
import time

data=pd.read_csv('/content/Social_Network_Ads.csv')

print(data.head())
data=data[['Age',EstimatedSalary','Purchased']]
print(data.head())
x=data.iloc[:,0:2]
y=data.iloc[:,-1]
print(x)
print(y)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
print(X_scaled.shape)


import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense
model=Sequential()
model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

print(model.summary())

model.compile(loss='binary_crossentropy',metrics=['accuracy'])
#start = time.time()
history = model.fit(X_scaled,y,epochs=500,batch_size=1,validation_split=0.2)
#print(time.time() - start)

model = Sequential()

model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',metrics=['accuracy'])
#start = time.time()
history = model.fit(X_scaled,y,epochs=10,batch_size=250,validation_split=0.2)
#print(time.time() - start)
plt.plot(history.history['loss'])