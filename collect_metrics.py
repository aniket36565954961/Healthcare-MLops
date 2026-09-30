import psutil
import pandas as pd
import time

data = []

print("Collecting system metrics...")

for i in range(60):
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    data.append([cpu, memory])
    print(f"CPU: {cpu}  Memory: {memory}")

    time.sleep(1)

df = pd.DataFrame(data, columns=["cpu","memory"])
df.to_csv("metrics.csv", index=False)

print("Metrics saved to metrics.csv")