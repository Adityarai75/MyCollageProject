import numpy as np
import pandas as pd


#**importing dataset**

df=pd.read_csv("rainfall in india 1901-2015.csv")
df.head()

#**selection of features and label**

features = df[['SUBDIVISION', 'YEAR']]
labels = df['ANNUAL']

print(features.head())

print(labels.head())

#**dealing whith impute data in label set**

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='most_frequent')
x=imputer.fit_transform(features.values)
y=imputer.fit_transform(labels.values.reshape(-1,1))

y.dtype

x.dtype

print(x[:5])

print(y[:5])

#**Spliting dataset**

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

#**preprocessing and pipeline and model building**

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
#from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Define the preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('state', StandardScaler(), [1]),  # Scale the integer feature
        ('rain', OneHotEncoder(), [0])    # One-hot encode the object feature
    ])
encoder = OneHotEncoder(handle_unknown='ignore')
# Create a pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LinearRegression())
])

model.fit(x_train,y_train)

model.score(x_test,y_test)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

x_train = pd.DataFrame(x_train)
x_test = pd.DataFrame(x_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)

x_test.head()

x_train.head()

y_train.head()

y_test.head()

model.score(x_test,y_test)

new_features = [["WEST UTTAR PRADESH",2010]]
predicted_rainfall = model.predict(new_features)
print("Predicted Rainfall:", predicted_rainfall)

import pickle
pickle.dump(model,open('model.pkl','wb'))