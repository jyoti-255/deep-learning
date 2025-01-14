#Graduate Admission Prediction using ANN
#Regression Problem
import pandas as pd

data=pd.read_csv('Admission_Predict_Ver1.1.csv')
print(data)
print(data.info())
print(data.shape)
print(data.head())
print(data.duplicated().sum())
data.drop(columns=['Serial No.'],inplace=True)
print(data.head())
x=data.iloc[:,0,-1]
y=data.iloc[:,0,-1]

from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y)
print(x_train)
print(y_train)