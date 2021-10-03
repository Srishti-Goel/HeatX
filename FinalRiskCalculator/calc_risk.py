from learning import model, max_values, train_X, train_Y, test_X, test_Y, sigmoid
import numpy as np
import sys

NDVI = float(sys.argv[1])
LST = float(sys.argv[2])
thermal_anomalies = float(sys.argv[3])

logistic_reg_model = model(train_X, train_Y, test_X, test_Y, num_iterations= 1000, learning_rate = 0.005, print_cost = False)
X = np.array([[NDVI], [LST], [thermal_anomalies]])
X[0] = X[0] / max_values[0][0]

X[1] = X[1] / max_values[1][0]

X[2] = X[2] / max_values[2][0]
A = sigmoid( np.dot(logistic_reg_model['w'].T, X) + logistic_reg_model['b'] )
A = np.squeeze(np.array(A))
risk = 'Bleh'
    
if A < 0.33:
    risk = 'GREEN'
else:
    if A < 0.67:
        risk = 'YELLOW'
    else:
        risk = 'RED'
    
print(risk)
sys.stdout.flush()
