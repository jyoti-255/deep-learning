import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv('placement.csv')
print(data)
sns.scatterplot(x=data['cgpa'], y=data['resume_score'], hue=data['placed'])
plt.show()

x=data.iloc[:,0:2]
y=data.iloc[:,-1]

from sklearn.linear_model import Perceptron
p=Perceptron()
print(p.fit(x,y))
print(p.coef_)
print(p.intercept_)
from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x.values,y.values,clf=p,legend=2)
plt.show()