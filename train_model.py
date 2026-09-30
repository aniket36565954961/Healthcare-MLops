import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

print("Loading metrics...")

data = pd.read_csv("metrics.csv")

model = IsolationForest(contamination=0.1)

print("Training anomaly detection model...")
model.fit(data)

joblib.dump(model,"anomaly_model.pkl")

print("Model saved as anomaly_model.pkl")