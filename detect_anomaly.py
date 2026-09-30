import psutil
import numpy as np
import joblib
import time

print("Starting AIOps monitoring...")

model = joblib.load("anomaly_model.pkl")

while True:

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    data = np.array([[cpu, memory]])

    prediction = model.predict(data)

    print("\nCPU:", cpu)
    print("Memory:", memory)

    if prediction == -1:
        print("⚠️ ANOMALY DETECTED!")
    else:
        print("System normal")

    time.sleep(10)