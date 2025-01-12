#Customer churn prediction using ANN
import numpy as np
import pandas as pd

data=pd.read_csv('Churn_Modelling.csv')
print(data)
print(data.head())
print(data.duplicated().sum())
print(data['Exited'].value_counts())

data.drop(columns=['RowNumber','CustomerId','Surname'],inplace=True)
print(data.head())
data=pd.get_dummies(data,columns=['Geography','Gender'],drop_first=True)

x=data.drop(columns=['Exited'])
y=data['Exited']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
print(x_train_scaled)
print(x_test_scaled)

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model=Sequential()
model.add(Dense(3,activation='sigmoid',input_dim=11))
model.add(Dense(1,activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',optimizer='Adam')
model.fit(x_train_scaled,y_train,epochs=10)

model.layers[0].get_weights()
y_log=model.predict(x_test_scaled)
y_pred=np.where(y_log>0.5,1,0)


from sklearn.metrics import accuracy_score
x=accuracy_score(y_test,y_pred)
print(x)