# -*- coding: utf-8 -*-
"""linear_regression_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11waZAHt4o4LRWgOtxWP8lToZP9WePjpV

# Visualización y entrenamiento de un modelo de Regresión lineal con scikit-learn

## Importing Dependencies
"""

import pandas as pd # Data management
import seaborn as sns # Data data visualization and graphic creation 
import matplotlib.pyplot as plt # Charts creation dependency

"""## Exploring our data set"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/studentsperformance_15085fee-8bc7-4d33-a182-655428728fe1.csv')

df

df.head(10) # Reads the first 10 records

df.shape # Tells us how many rows and columns has our df

df.columns # Brings us only the columns in our df

df.dtypes # Data types of the columns in our df

"""### Creating a histogram"""

sns.histplot(data = df, x = 'writing score', hue = 'test preparation course', multiple = 'stack') # Allows us to graph a histogram
# hue attribute divides the information
# multiple = 'stack' atribute distributes the infromation for better visualization

"""### Data visualization"""

sns.scatterplot(data = df, x = 'reading score', y = 'writing score') # Visualizing scatter plot

"""### Creating frequency table"""

freq = df['writing score'].value_counts() # shows the distribution values ​​of each value
df_freq = freq.to_frame()
df_freq.reset_index(inplace = True) # inplace attribute places the index inside df
df_freq = df_freq.rename(columns = {'index': 'Writing Score', 'writing score': 'Number of Students'})
df_freq

"""### Scores' mean"""

df.mean()

"""### Scores' median"""

df.median()

"""## Training our model

***x*** will be the 'reading score'
& ***y*** will be the 'writing score'

We assume that if they get a good score in the reading test they should get a higher score in the writing test.
"""

x = df['reading score'].values
y = df['writing score'].values

x = x.reshape(-1,1)

# Divide data into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2) # Test size 20%, train test 80%

# Linear regression with ML
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(x_train, y_train)

print("Slope's value:", reg.coef_)
print("Bias' value:", reg.intercept_)
print(reg.score(x_train, y_train))

"""## Trained model visualization """

x_flat = x_train.flatten()

y_hat = reg.predict(x_train)

fig, ax = plt.subplots()
sns.scatterplot(x = x_flat, y = y_train)
plt.plot(x_train, y_hat, color = 'r')

"""## Model evaluation"""

from sklearn.metrics import mean_squared_error
y_pred = reg.predict(x_test)

# Calculates de mean quared error of our prediction 
print(mean_squared_error(y_test, y_pred))

value = pd.DataFrame({'Actual test': y_test.flatten(), 'Predict': y_pred.flatten()})
value

