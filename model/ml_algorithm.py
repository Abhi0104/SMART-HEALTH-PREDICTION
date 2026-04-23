from multiprocessing.pool import RUN
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from sklearn.metrics import accuracy_score
warnings.filterwarnings('ignore')

#read data from training dataset
data = pd.read_csv("new_training_data.csv")

#load symptoms and disease from train dataset.
features = data.iloc[:,:-1]
target = data['prognosis']



#split data into two files test and train 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.25, random_state = 1)



#KNN model train
from sklearn.neighbors import KNeighborsClassifier
KN = KNeighborsClassifier(n_neighbors =4)
modelKN = KN.fit(X_train,y_train)



#save train model in pickle file as a string
import pickle
with open('ml_algo_pred.pkl', 'wb') as file:
    pickle.dump(modelKN, file)
    

