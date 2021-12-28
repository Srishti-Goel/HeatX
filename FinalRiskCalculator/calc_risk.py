from learning import max_values,sigmoid
import numpy as np
import sys
import json

NDVI = float(sys.argv[1])
LST = float(sys.argv[2])
thermal_anomalies = float(sys.argv[3])

weights = {}

save_file_path = "weights.json"

with open(save_file_path) as f:
    data = json.load(f)

    array_data = np.array(data, dtype=object)

    w = np.array([array_data[0][0], array_data[1][0], array_data[2][0]])
    w = w.reshape(-1, 1)

    weights['w'] = w
    weights['b'] = array_data[1]


#logistic_reg_model = model(train_X, train_Y, test_X, test_Y, num_iterations= 1000, learning_rate = 0.005, print_cost = False)
X = np.array([[NDVI], [LST], [thermal_anomalies]])
X[0] = X[0] / max_values[0][0]

X[1] = X[1] / max_values[1][0]

X[2] = X[2] / max_values[2][0]
A = sigmoid( np.dot(weights['w'].T, X) + weights['b'] )
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
