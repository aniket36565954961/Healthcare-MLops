import subprocess
import pandas as pd

print("Fetching Kubernetes pod metrics...")

result = subprocess.check_output(
    ["kubectl","top","pods","-n","dev"]
).decode()

print(result)