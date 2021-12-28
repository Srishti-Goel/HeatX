import numpy as np
import matplotlib.pyplot as plt
from numpy.core.defchararray import array
import pandas as pd
import copy

import codecs, json 


all_dataset = pd.read_table('WildFire_Prediction_Data_Set.csv', sep = ',', header = 0, names = ['NDVI', 'LST', 'Thermal Anomalies', 'fire_status'], dtype = float)
all_Y = all_dataset['fire_status'].to_numpy()
m = all_Y.shape[0]
all_Y = all_Y.reshape((1, m))
all_X = all_dataset[['NDVI', 'LST', 'Thermal Anomalies']].to_numpy().T
max_values = np.amax(all_X, axis = 1).reshape((3,1))
all_X = all_X / max_values

train_X = all_X[:, 0:1371]
train_Y = all_Y[:, 0:1371]

dev_X = all_X[:, 1029:1371]
dev_Y = all_Y[:, 1029:1371]

test_X = all_X[:, 1371:m]
test_Y = all_Y[:, 1371:m]

def sigmoid(z):
    
    s = 1/ (1 + np.exp(-z))
    
    return s

def initialize_with_zeros(dim):
    w = np.random.random((dim, 1))
    b = 0.0
    return w, b

def propagate(w, b, X, Y):
    m = X.shape[1]
    
    A = sigmoid(np.dot(w.T, X) + b)
    
    cost = -1*(np.dot(Y, np.log(A).T) + np.dot((1 - Y), np.log(1 - A).T))/m
    
    
    dw = np.dot(X,(A - Y).T)/m
    db = np.sum(A - Y)/m
    
    cost = (np.squeeze(np.array(cost)))
    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost


def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False):
    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    
    costs = []
    for i in range(num_iterations):
        
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w = w - (learning_rate * dw)
        b = b - (learning_rate * db)
        
        if i % 100 == 0:
            costs.append(cost)
            
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

def predict(w, b, X):
    
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    A = sigmoid( np.dot(w.T, X) + b )
    
    for i in range(A.shape[1]):
        if(A[0, i] > 0.5):
            Y_prediction[0,i] = 1.0
        else:
            Y_prediction[0, i] = 0.0
    
    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    
    w, b = initialize_with_zeros(X_train.shape[0])
    params, grads, costs = optimize(w, b, X_train, Y_train, num_iterations=num_iterations, learning_rate=learning_rate, print_cost=True)
    w = params["w"]
    b = params["b"]
    Y_prediction_train = predict(w, b, X_train)
    Y_prediction_test = predict(w, b, X_test)
    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d

model = model(train_X, train_Y, test_X, test_Y, num_iterations= 1000, learning_rate = 0.005, print_cost = False)

w_list = model['w'].tolist()
b_list = model['b'].tolist()

w_list.append(b_list)

save_file_path = 'weights.json'

json.dump(w_list, codecs.open(save_file_path, 'w', encoding='utf-8'))

