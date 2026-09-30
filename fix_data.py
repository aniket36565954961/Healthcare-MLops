import pandas as pd

columns = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome"
]

df = pd.read_csv("diabetes_raw.csv", header=None)
df.columns = columns

df.to_csv("diabetes.csv", index=False)

print("Dataset fixed and saved as diabetes.csv")