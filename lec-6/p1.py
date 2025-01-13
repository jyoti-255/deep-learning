#Handwritten Digit Classification using ANN

import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten

(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
print(x_train.shape)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))  # Flatten 2D to 1D
model.add(Dense(128, activation='relu'))  # Fully connected layer with 128 neurons
model.add(Dense(10, activation='softmax')) 

model.summary()
model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])

history=model.fit(x_train,y_train,epochs=10,validation_split=0.2)

model.predict(x_test)
y_prob=model.predict(x_test)
print(y_prob)
y_pred=y_prob.argmax(axis=1)

from sklearn.metrics import accuracy_score
x=accuracy_score(y_test,y_pred)
print(x)


plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

plt.imshow(x_test[1])
plt.show()

model.predict(x_test[1].reshape(1,28,28)).argmax(axis=1)