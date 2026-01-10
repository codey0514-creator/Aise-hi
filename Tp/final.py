import matplotlib.pyplot as plt
import math
# We will assume the relationship between Y and X as linear so we can write 
# Y = a + b.X + e
patients_data = {
1:  {'diabetes_count': 2, 'bmi': 26.5},2: {'diabetes_count': 5, 'bmi': 30.2},3: {'diabetes_count': 3, 'bmi': 22.8},
4:  {'diabetes_count': 7, 'bmi': 28.1},5: {'diabetes_count': 4, 'bmi': 24.7},6: {'diabetes_count': 8, 'bmi': 31.0},
7:  {'diabetes_count': 6, 'bmi': 27.3},8: {'diabetes_count': 9, 'bmi': 29.5},9: {'diabetes_count': 3, 'bmi': 23.9},
10: {'diabetes_count': 5, 'bmi': 25.6},11: {'diabetes_count': 7, 'bmi': 28.9},12: {'diabetes_count': 2, 'bmi': 21.7},
13: {'diabetes_count': 9, 'bmi': 32.1},14: {'diabetes_count': 4, 'bmi': 26.0},15: {'diabetes_count': 3, 'bmi': 24.3},
16: {'diabetes_count': 8, 'bmi': 29.1},17: {'diabetes_count': 6, 'bmi': 27.6},18: {'diabetes_count': 3, 'bmi': 23.4},
19: {'diabetes_count': 9, 'bmi': 30.7},20: {'diabetes_count': 5, 'bmi': 25.0},21: {'diabetes_count': 7, 'bmi': 28.4},
22: {'diabetes_count': 2, 'bmi': 22.5},23: {'diabetes_count': 9, 'bmi': 31.5},24: {'diabetes_count': 6, 'bmi': 26.8},
25: {'diabetes_count': 4, 'bmi': 24.1},26: {'diabetes_count': 8, 'bmi': 29.8},27: {'diabetes_count': 6, 'bmi': 27.1},
28: {'diabetes_count': 3, 'bmi': 23.7},29: {'diabetes_count': 9, 'bmi': 30.4},30: {'diabetes_count': 5, 'bmi': 25.4},
31: {'diabetes_count': 7, 'bmi': 28.7},
32: {'diabetes_count': 2, 'bmi': 21.9},33: {'diabetes_count': 9, 'bmi': 32.5},34: {'diabetes_count': 4, 'bmi': 26.2},
35: {'diabetes_count': 3, 'bmi': 24.5},36: {'diabetes_count': 8, 'bmi': 29.3},37: {'diabetes_count': 6, 'bmi': 27.8},
38: {'diabetes_count': 3, 'bmi': 23.2},39: {'diabetes_count': 9, 'bmi': 31.1},40: {'diabetes_count': 5, 'bmi': 25.2},
41: {'diabetes_count': 7, 'bmi': 28.6},42: {'diabetes_count': 2, 'bmi': 22.7},43: {'diabetes_count': 9, 'bmi': 30.9},
44: {'diabetes_count': 4, 'bmi': 26.4},45: {'diabetes_count': 3, 'bmi': 24.0},46: {'diabetes_count': 8, 'bmi': 29.0},
47: {'diabetes_count': 6, 'bmi': 27.4},48: {'diabetes_count': 3, 'bmi': 23.5},49: {'diabetes_count': 9, 'bmi': 30.6},
50: {'diabetes_count': 5, 'bmi': 25.5},51: {'diabetes_count': 7, 'bmi': 28.3},52: {'diabetes_count': 2, 'bmi': 22.3},
53: {'diabetes_count': 9, 'bmi': 31.8},54: {'diabetes_count': 6, 'bmi': 26.9},55: {'diabetes_count': 4, 'bmi': 24.2},
56: {'diabetes_count': 8, 'bmi': 29.6},57: {'diabetes_count': 6, 'bmi': 27.2},58: {'diabetes_count': 3, 'bmi': 23.8},
59: {'diabetes_count': 9, 'bmi': 30.3},60: {'diabetes_count': 5, 'bmi': 25.3},61: {'diabetes_count': 7, 'bmi': 28.8},
63: {'diabetes_count': 9, 'bmi': 32.2},64: {'diabetes_count': 4, 'bmi': 26.1},65: {'diabetes_count': 3, 'bmi': 24.4},
66: {'diabetes_count': 8, 'bmi': 29.2},76: {'diabetes_count': 8, 'bmi': 29.4},62: {'diabetes_count': 2, 'bmi': 21.8},
67: {'diabetes_count': 6, 'bmi': 27.7},68: {'diabetes_count': 3, 'bmi': 23.3},69: {'diabetes_count': 9, 'bmi': 31.2},
70: {'diabetes_count': 5, 'bmi': 25.1},71: {'diabetes_count': 7, 'bmi': 28.5},72: {'diabetes_count': 2, 'bmi': 22.6},
73: {'diabetes_count': 9, 'bmi': 30.8},74: {'diabetes_count': 4, 'bmi': 26.6},75: {'diabetes_count': 3, 'bmi': 24.6},
77: {'diabetes_count': 6, 'bmi': 27.0},78: {'diabetes_count': 3, 'bmi': 23.6},79: {'diabetes_count': 9, 'bmi': 30.5},
80: {'diabetes_count': 5, 'bmi': 25.7},81: {'diabetes_count': 7, 'bmi': 28.2},82: {'diabetes_count': 2, 'bmi': 22.4},
83: {'diabetes_count': 9, 'bmi': 31.6},84: {'diabetes_count': 4, 'bmi': 26.7},85: {'diabetes_count': 3, 'bmi': 24.9},
86: {'diabetes_count': 8, 'bmi': 29.7},87: {'diabetes_count': 6, 'bmi': 27.5},88: {'diabetes_count': 3, 'bmi': 23.1},
89: {'diabetes_count': 9, 'bmi': 30.1},90: {'diabetes_count': 5, 'bmi': 25.8},91: {'diabetes_count': 7, 'bmi': 28.0},
92: {'diabetes_count': 2, 'bmi': 21.6},93: {'diabetes_count': 9, 'bmi': 32.0},94: {'diabetes_count': 4, 'bmi': 26.3},
95: {'diabetes_count': 3, 'bmi': 24.8},96: {'diabetes_count': 8, 'bmi': 29.9},97: {'diabetes_count': 6, 'bmi': 27.9},
98: {'diabetes_count': 3, 'bmi': 23.0},99: {'diabetes_count': 9, 'bmi': 30.0},100: {'diabetes_count': 5, 'bmi': 25.9}
}
############################################################
import random
noise_level = 2.5      
for patient in patients_data.values():                  # We are doing this so that our data looks more scattered(that is where ml helps)
    noise = random.uniform(-noise_level, noise_level)
    patient["diabetes_count"] += noise
###########################################################
sum1 , sum2 = 0 , 0
for i in range(1,len(patients_data)+1):
    sum1 += patients_data[i]["bmi"]
    sum2 += patients_data[i]["diabetes_count"]
X_bar = sum1 / len(patients_data)
Y_bar = sum2 / len(patients_data)
n , p , q = 0 , 0 , 0
for i in range(1,len(patients_data)+1):
    n += (patients_data[i]["bmi"] - X_bar)* (patients_data[i]["diabetes_count"] - Y_bar) 
    p += (patients_data[i]["bmi"] -X_bar)**2
    q += (patients_data[i]["diabetes_count"] - Y_bar) ** 2
b = n / p 
a = Y_bar - b* X_bar
####################### Calculaitng correlation and errors
r = n / (math.sqrt(p*q))
error = 0
for i in patients_data :
    error += (patients_data[i]["diabetes_count"] - (a + b * patients_data[i]["bmi"]))**2    # Squared errror
mse = error / len(patients_data)                                                            # Mean squared error
# Extract X and Y
X = [patients_data[i]["bmi"] for i in patients_data]
Y = [patients_data[i]["diabetes_count"] for i in patients_data]
# Regression line values
X_line = sorted(X)
Y_line = [a + b*x for x in X_line]
# Plot
threshold = 0.5
#Assesing the accuracy of model with the help of correlation 
if abs(r) < threshold:
    print("Not a strong linear relationship. Regression not reliable.")
else:
    print("Strong linear relationship. Plotting regression line...")
    # plotting code here
    plt.scatter(X, Y)
    plt.plot(X_line, Y_line)
    plt.xlabel("BMI")
    plt.ylabel("Diabetes Count")
    print( r , mse)
    plt.title("Linear Regression: Diabetes vs BMI")
    plt.legend()
    plt.show()
    print("is it this?")