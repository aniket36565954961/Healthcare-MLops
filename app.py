from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Healthcare ML API"}

@app.post("/predict")
def predict(data: dict):

    values = np.array([
        data["Pregnancies"],
        data["Glucose"],
        data["BloodPressure"],
        data["SkinThickness"],
        data["Insulin"],
        data["BMI"],
        data["DiabetesPedigreeFunction"],
        data["Age"]
    ]).reshape(1,-1)

    prediction = model.predict(values)

    return {"diabetes_prediction": int(prediction[0])}