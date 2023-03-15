import os
from django.conf import settings
from django.core.files.storage import default_storage
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

import joblib

# Define your linear regression model and train it
model = LinearRegression()

dataset_path = os.path.join(settings.BASE_DIR, 'C:\Users\Hp\Desktop\DPS_Project\webapp\webapp', 'medical_charges.csv')

df=pd.read_csv("C:\Users\Hp\Desktop\DPS_Project\webapp\webapp\medical_charges.csv")

lblenc = preprocessing.LabelEncoder()   
df['sex']=lblenc.fit_transform(df['sex'])
df['smoker']=lblenc.fit_transform(df['smoker'])
df['region']=lblenc.fit_transform(df['region'])
X=df[['age','sex','bmi','children','smoker','region']]
y=df['charges']

model.fit(X,y)

# Serialize and save the model to the "models" directory
model_dir = os.path.join(settings.BASE_DIR, 'models')
model_file_name = 'trained_linear_regression_model.joblib'
model_file_path = os.path.join(model_dir, model_file_name)
joblib.dump(model, model_file_path)
model_file = default_storage.open(model_file_path, 'rb')
model_file_data = model_file.read()
default_storage.save(model_file_path, model_file_data)
model_file.close()