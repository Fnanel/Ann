# -*- coding: utf-8 -*-
"""Copy of artificial_neural_network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/193kPdWMX5Qho9xtGy9pooD8V-wS713CI

# Artificial Neural Network

### Importing the libraries
"""

import pandas as pd
import numpy as np
import tensorflow as tf

"""## Part 1 - Data Preprocessing

### Importing the dataset
"""

dataset= pd.read_csv('Churn_Modelling.csv')
x= dataset.iloc[:, 3:-1].values
y= dataset.iloc[:, -1].values

print(x)

print(y)

"""### Encoding categorical data

Label Encoding the "Gender" column
"""

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
x[:,2]= le.fit_transform(x[:,2])

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer as CT
ct= CT(transformers=[('encoding',OneHotEncoder(), [1])], remainder='passthrough')
x= np.array (ct.fit_transform(x))

print(x)

"""One Hot Encoding the "Geography" column

### Splitting the dataset into the Training set and Test set
"""

from sklearn.model_selection import train_test_split as tts
x_train, x_test, y_train, y_test = tts(x,y,test_size=0.2, random_state=0)

"""### Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train= sc.fit_transform(x_train)
x_test= sc.transform(x_test)

"""## Part 2 - Building the ANN

### Initializing the ANN
"""

ann= tf.keras.models.Sequential()

"""### Adding the input layer and the first hidden layer"""

ann.add(tf.keras.layers.Dense(units=6, activation= 'relu'))

"""### Adding the second hidden layer"""

ann.add(tf.keras.layers.Dense(units=6 , activation= "relu"))

"""### Adding the output layer"""

ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

"""## Part 3 - Training the ANN

### Compiling the ANN
"""

ann.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'], )

"""### Training the ANN on the Training set"""

ann.fit(x_train,y_train, batch_size= 32, epochs= 100)



Useing ANN model to predict if the customer with the following informations will leave the bank or not:

Geography: France

Credit Score: 600

Gender: Male

Age: 40 years old

Tenure: 3 years

Balance: \$ 60000

Number of Products: 2

Does this customer have a credit card ? Yes

Is this customer an Active Member: Yes

Estimated Salary: \$ 50000

So, should we say goodbye to that customer ?

**Solution**
print(ann.predict(sc.transform([[1,0,0, 600, 1, 40, 3, 60000, 2, 1,1, 50000]]))>0.5)
