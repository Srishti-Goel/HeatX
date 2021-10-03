from learning import model, max_values, train_X, train_Y, test_X, test_Y, sigmoid
import numpy as np
import sys

NDVI = 1
LST = 35
thermal_anomalies = 1

logistic_reg_model = model(train_X, train_Y, test_X, test_Y, num_iterations= 1000, learning_rate = 0.005, print_cost = False)
X = np.array([[NDVI], [LST], [thermal_anomalies]])
X = X / max_values
A = sigmoid( np.dot(logistic_reg_model['w'].T, X) + logistic_reg_model['b'] )
A = np.squeeze(np.array(A))
risk = ''
    
if A < 0.33:
    risk = 'GREEN'
else:
    if A < 0.67:
        risk = 'YELLOW'
    else:
        risk = 'RED'
    
print(risk)
sys.stdout.flush()
