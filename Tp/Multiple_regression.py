#In this data set the big problem is that bp , sugar , insulin all factors are related to each othe
#That is they are giving us same results.........
import numpy as np
from scipy.stats import t                # Importing the t distribution static graph
import matplotlib.pyplot as plt
diabetes_data = {
    "patient_1":  {"bp": 78,  "sugar": 118, "insulin": 65,  "bmi": 22.4, "y": 48.68},
    "patient_2":  {"bp": 82,  "sugar": 125, "insulin": 70,  "bmi": 23.1, "y": 50.12},
    "patient_3":  {"bp": 85,  "sugar": 130, "insulin": 75,  "bmi": 24.0, "y": 51.50},
    "patient_4":  {"bp": 80,  "sugar": 120, "insulin": 68,  "bmi": 22.8, "y": 49.16},
    "patient_5":  {"bp": 88,  "sugar": 140, "insulin": 90,  "bmi": 27.5, "y": 55.30},

    "patient_6":  {"bp": 90,  "sugar": 150, "insulin": 95,  "bmi": 29.0, "y": 58.00},
    "patient_7":  {"bp": 92,  "sugar": 155, "insulin": 100, "bmi": 30.2, "y": 59.54},
    "patient_8":  {"bp": 95,  "sugar": 160, "insulin": 105, "bmi": 31.0, "y": 60.70},
    "patient_9":  {"bp": 98,  "sugar": 165, "insulin": 110, "bmi": 32.4, "y": 62.58},
    "patient_10": {"bp": 100, "sugar": 170, "insulin": 115, "bmi": 33.1, "y": 63.62},

    "patient_11": {"bp": 76,  "sugar": 110, "insulin": 60,  "bmi": 21.9, "y": 46.38},
    "patient_12": {"bp": 79,  "sugar": 115, "insulin": 63,  "bmi": 22.2, "y": 47.44},
    "patient_13": {"bp": 83,  "sugar": 128, "insulin": 72,  "bmi": 23.8, "y": 50.06},
    "patient_14": {"bp": 87,  "sugar": 135, "insulin": 85,  "bmi": 26.1, "y": 52.92},
    "patient_15": {"bp": 91,  "sugar": 145, "insulin": 92,  "bmi": 28.0, "y": 56.10},

    "patient_16": {"bp": 84,  "sugar": 132, "insulin": 78,  "bmi": 24.9, "y": 51.18},
    "patient_17": {"bp": 86,  "sugar": 138, "insulin": 82,  "bmi": 25.7, "y": 52.54},
    "patient_18": {"bp": 89,  "sugar": 142, "insulin": 88,  "bmi": 27.0, "y": 54.10},
    "patient_19": {"bp": 93,  "sugar": 158, "insulin": 108, "bmi": 31.8, "y": 60.36},
    "patient_20": {"bp": 96,  "sugar": 162, "insulin": 112, "bmi": 32.6, "y": 61.52},

    "patient_21": {"bp": 77,  "sugar": 112, "insulin": 62,  "bmi": 22.0, "y": 46.80},
    "patient_22": {"bp": 81,  "sugar": 122, "insulin": 67,  "bmi": 22.9, "y": 48.78},
    "patient_23": {"bp": 85,  "sugar": 130, "insulin": 74,  "bmi": 24.3, "y": 51.36},
    "patient_24": {"bp": 88,  "sugar": 140, "insulin": 89,  "bmi": 27.4, "y": 55.28},
    "patient_25": {"bp": 94,  "sugar": 160, "insulin": 107, "bmi": 31.5, "y": 61.30},

    "patient_26": {"bp": 99,  "sugar": 168, "insulin": 114, "bmi": 33.0, "y": 63.30},
    "patient_27": {"bp": 101, "sugar": 172, "insulin": 118, "bmi": 34.2, "y": 64.54},
    "patient_28": {"bp": 104, "sugar": 178, "insulin": 122, "bmi": 35.1, "y": 66.02},
    "patient_29": {"bp": 107, "sugar": 185, "insulin": 130, "bmi": 36.8, "y": 68.36},
    "patient_30": {"bp": 110, "sugar": 190, "insulin": 135, "bmi": 38.0, "y": 70.10},

    "patient_31": {"bp": 82,  "sugar": 124, "insulin": 69,  "bmi": 23.0, "y": 49.10},
    "patient_32": {"bp": 84,  "sugar": 129, "insulin": 73,  "bmi": 23.9, "y": 50.36},
    "patient_33": {"bp": 86,  "sugar": 134, "insulin": 80,  "bmi": 25.0, "y": 51.80},
    "patient_34": {"bp": 88,  "sugar": 139, "insulin": 86,  "bmi": 26.2, "y": 53.26},
    "patient_35": {"bp": 90,  "sugar": 145, "insulin": 92,  "bmi": 27.9, "y": 55.08},

    "patient_36": {"bp": 92,  "sugar": 150, "insulin": 97,  "bmi": 29.1, "y": 56.82},
    "patient_37": {"bp": 94,  "sugar": 155, "insulin": 102, "bmi": 30.0, "y": 58.00},
    "patient_38": {"bp": 96,  "sugar": 160, "insulin": 108, "bmi": 31.2, "y": 59.64},
    "patient_39": {"bp": 98,  "sugar": 165, "insulin": 112, "bmi": 32.0, "y": 61.10},
    "patient_40": {"bp": 100, "sugar": 170, "insulin": 118, "bmi": 33.3, "y": 62.66},

    "patient_41": {"bp": 79,  "sugar": 116, "insulin": 64,  "bmi": 22.3, "y": 47.66},
    "patient_42": {"bp": 83,  "sugar": 126, "insulin": 71,  "bmi": 23.5, "y": 49.86},
    "patient_43": {"bp": 87,  "sugar": 136, "insulin": 84,  "bmi": 25.9, "y": 52.78},
    "patient_44": {"bp": 91,  "sugar": 148, "insulin": 96,  "bmi": 28.7, "y": 56.44},
    "patient_45": {"bp": 95,  "sugar": 160, "insulin": 110, "bmi": 32.1, "y": 61.92},

    "patient_46": {"bp": 97,  "sugar": 165, "insulin": 115, "bmi": 33.0, "y": 63.10},
    "patient_47": {"bp": 99,  "sugar": 170, "insulin": 120, "bmi": 34.0, "y": 64.30},
    "patient_48": {"bp": 102, "sugar": 176, "insulin": 125, "bmi": 35.0, "y": 65.80},
    "patient_49": {"bp": 105, "sugar": 182, "insulin": 130, "bmi": 36.1, "y": 67.42},
    "patient_50": {"bp": 108, "sugar": 188, "insulin": 136, "bmi": 37.4, "y": 69.22}
}
X1_bp = np.array([v["bp"] for v in diabetes_data.values()])
X2_sugar = np.array([v["sugar"] for v in diabetes_data.values()])
X3_insulin = np.array([v["insulin"] for v in diabetes_data.values()])
X4_bmi = np.array([v["bmi"] for v in diabetes_data.values()])
Y = np.array([v["y"] for v in diabetes_data.values()])
############################################################
import random
noise_level = 2.5      
Y_realistic = np.array([v["y"] + random.uniform(-noise_level, noise_level)for v in diabetes_data.values()]).reshape(50,1)
###########################################################
X = np.array([X1_bp , X2_sugar , X3_insulin , X4_bmi]).T
original_shape = X.shape
X_T = X.T
Y = Y.reshape(50 , 1)
print(X.shape , X_T.shape , Y.shape)
# If there is a problem in matrix multiplication then try to reshape them as per need
# X = X.reshape(4,50)
# X_T = X_T.reshape(50,4)           
# # print(X.shape , X_T.shape)
A = np.matmul(X_T , X)
B = np.matmul(X_T , Y_realistic)
#A_pinv is the psuedo inverse matrix of A (this is an in built way of finding inverse of a matrix) using numpy inbuild attributes
A_pinv = np.linalg.pinv(A)       
Beta = np.matmul(A_pinv , B)   # These are the coefficients of bp , sugar , insulin , bmi 
Y_predicted = np.matmul(X , Beta)
###########################################
MSE = np.sum((Y - Y_predicted)**2) / (len(diabetes_data) - len(Beta))
SE = np.sqrt(np.diag(A_pinv) * MSE)
t_stats = Beta.flatten() / SE
p_values = 2 * (1 - t.cdf(np.abs(t_stats), len(diabetes_data) - len(Beta)))
for i in range(len(p_values)-1 , -1 , -1):
    if p_values[i] > 0.05 :
        X = np.delete(X , i , axis = 1)
###########################################
if original_shape != X.shape :
    X_T = X.T
    A = np.matmul(X_T , X)
    B = np.matmul(X_T , Y_realistic)
    #A_pinv is the psuedo inverse matrix of A (this is an in built way of finding inverse of a matrix) using numpy inbuild attributes
    A_pinv = np.linalg.pinv(A)       
    Beta = np.matmul(A_pinv , B)   # These are the coefficients of bp , sugar , insulin , bmi 
    Y_predicted = np.matmul(X , Beta)
SS_res = np.sum((Y - Y_predicted)**2)  # Sum of Squared Residuals (errors)
SS_tot = np.sum((Y - np.mean(Y))**2)   # Total Sum of Squares (total variance)
R2 = 1 - (SS_res / SS_tot)
print(np.round(p_values , 4) , Beta , R2)
y_min = Y_realistic.min()
y_max = Y_realistic.max()
plt.plot([y_min, y_max], [y_min, y_max],
         color='black', linewidth=2, linestyle='-',
         label='Perfect Fit Line (y = x)')
plt.scatter(Y_realistic, Y_predicted, color='red', alpha=0.5, label='Predicted Y')
plt.xlabel('Actual Y')
plt.ylabel('Predicted Y')
plt.title('Actual vs Predicted Values')
plt.grid(True)
plt.legend(loc='upper right')
plt.show()

