import numpy as np
diabetes_data = {
    "patient_1":  {"bp": 78, "sugar": 118, "insulin": 65,  "bmi": 22.4},
    "patient_2":  {"bp": 82, "sugar": 125, "insulin": 70,  "bmi": 23.1},
    "patient_3":  {"bp": 85, "sugar": 130, "insulin": 75,  "bmi": 24.0},
    "patient_4":  {"bp": 80, "sugar": 120, "insulin": 68,  "bmi": 22.8},
    "patient_5":  {"bp": 88, "sugar": 140, "insulin": 90,  "bmi": 27.5},

    "patient_6":  {"bp": 90, "sugar": 150, "insulin": 95,  "bmi": 29.0},
    "patient_7":  {"bp": 92, "sugar": 155, "insulin": 100, "bmi": 30.2},
    "patient_8":  {"bp": 95, "sugar": 160, "insulin": 105, "bmi": 31.0},
    "patient_9":  {"bp": 98, "sugar": 165, "insulin": 110, "bmi": 32.4},
    "patient_10": {"bp": 100,"sugar": 170, "insulin": 115, "bmi": 33.1},

    "patient_11": {"bp": 76, "sugar": 110, "insulin": 60,  "bmi": 21.9},
    "patient_12": {"bp": 79, "sugar": 115, "insulin": 63,  "bmi": 22.2},
    "patient_13": {"bp": 83, "sugar": 128, "insulin": 72,  "bmi": 23.8},
    "patient_14": {"bp": 87, "sugar": 135, "insulin": 85,  "bmi": 26.1},
    "patient_15": {"bp": 91, "sugar": 145, "insulin": 92,  "bmi": 28.0},

    "patient_16": {"bp": 84, "sugar": 132, "insulin": 78,  "bmi": 24.9},
    "patient_17": {"bp": 86, "sugar": 138, "insulin": 82,  "bmi": 25.7},
    "patient_18": {"bp": 89, "sugar": 142, "insulin": 88,  "bmi": 27.0},
    "patient_19": {"bp": 93, "sugar": 158, "insulin": 108, "bmi": 31.8},
    "patient_20": {"bp": 96, "sugar": 162, "insulin": 112, "bmi": 32.6},

    "patient_21": {"bp": 77, "sugar": 112, "insulin": 62,  "bmi": 22.0},
    "patient_22": {"bp": 81, "sugar": 122, "insulin": 67,  "bmi": 22.9},
    "patient_23": {"bp": 85, "sugar": 130, "insulin": 74,  "bmi": 24.3},
    "patient_24": {"bp": 88, "sugar": 140, "insulin": 89,  "bmi": 27.4},
    "patient_25": {"bp": 94, "sugar": 160, "insulin": 107, "bmi": 31.5},

    "patient_26": {"bp": 99, "sugar": 168, "insulin": 114, "bmi": 33.0},
    "patient_27": {"bp": 101,"sugar": 172, "insulin": 118, "bmi": 34.2},
    "patient_28": {"bp": 104,"sugar": 178, "insulin": 122, "bmi": 35.1},
    "patient_29": {"bp": 107,"sugar": 185, "insulin": 130, "bmi": 36.8},
    "patient_30": {"bp": 110,"sugar": 190, "insulin": 135, "bmi": 38.0},

    # repeating structured variability (not duplicates)
    "patient_31": {"bp": 82, "sugar": 124, "insulin": 69,  "bmi": 23.0},
    "patient_32": {"bp": 84, "sugar": 129, "insulin": 73,  "bmi": 23.9},
    "patient_33": {"bp": 86, "sugar": 134, "insulin": 80,  "bmi": 25.0},
    "patient_34": {"bp": 88, "sugar": 139, "insulin": 86,  "bmi": 26.2},
    "patient_35": {"bp": 90, "sugar": 145, "insulin": 92,  "bmi": 27.9},

    "patient_36": {"bp": 92, "sugar": 150, "insulin": 97,  "bmi": 29.1},
    "patient_37": {"bp": 94, "sugar": 155, "insulin": 102, "bmi": 30.0},
    "patient_38": {"bp": 96, "sugar": 160, "insulin": 108, "bmi": 31.2},
    "patient_39": {"bp": 98, "sugar": 165, "insulin": 112, "bmi": 32.0},
    "patient_40": {"bp": 100,"sugar": 170, "insulin": 118, "bmi": 33.3},

    # last batch
    "patient_41": {"bp": 79, "sugar": 116, "insulin": 64,  "bmi": 22.3},
    "patient_42": {"bp": 83, "sugar": 126, "insulin": 71,  "bmi": 23.5},
    "patient_43": {"bp": 87, "sugar": 136, "insulin": 84,  "bmi": 25.9},
    "patient_44": {"bp": 91, "sugar": 148, "insulin": 96,  "bmi": 28.7},
    "patient_45": {"bp": 95, "sugar": 160, "insulin": 110, "bmi": 32.1},

    "patient_46": {"bp": 97, "sugar": 165, "insulin": 115, "bmi": 33.0},
    "patient_47": {"bp": 99, "sugar": 170, "insulin": 120, "bmi": 34.0},
    "patient_48": {"bp": 102,"sugar": 176, "insulin": 125, "bmi": 35.0},
    "patient_49": {"bp": 105,"sugar": 182, "insulin": 130, "bmi": 36.1},
    "patient_50": {"bp": 108,"sugar": 188, "insulin": 136, "bmi": 37.4}
}
X1_bp = np.array([v["bp"] for v in diabetes_data.values()])
X2_sugar = np.array([v["sugar"] for v in diabetes_data.values()])
X3_insulin = np.array([v["insulin"] for v in diabetes_data.values()])
X4_bmi = np.array([v["bmi"] for v in diabetes_data.values()])
X = np.array([[X1_bp] , [X2_sugar] , [X3_insulin] , [X4_bmi]])
X_T = X.T
A = np.matmul( X_T , X )
