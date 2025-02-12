import tensorflow as tf
import numpy as np
import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt
import warnings
from mlxtend.plotting import plot_decision_regions
from matplotlib.colors import ListedColormap
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_circles
import seaborn as sns

x,y=make_circles(n_samples=100,noise=0.1,random_state=1)

sns.scatterplot(x=x[:, 0], y=x[:, 1], hue=y)
plt.show()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=2)

model=Sequential()
model.add(Dense(256,input_dim=2,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

history=model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=100,verbose=0)

plt.plot(history['loss'],label='train')
plt.plot(history.history['val_loss'],label='test')
plt.legend()
plt.show()



