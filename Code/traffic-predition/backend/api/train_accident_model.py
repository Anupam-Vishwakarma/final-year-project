import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Load data
columns = ["timestamp", "latitude", "longitude", "current_speed", "free_flow_speed", "congestion"]
df = pd.read_csv("traffic_data.csv", names=columns)
# Recalculate congestion level (since it may not be saved)
df["congestion_level"] = df["free_flow_speed"] / df["current_speed"]

# Simulate accident label: 1 if congestion high or speed too low
df["accident"] = ((df["current_speed"] < 10) | (df["congestion_level"] > 1.5)).astype(int)

# Features and Target
X = df[["latitude", "longitude", "current_speed", "free_flow_speed", "congestion_level"]]
y = df["accident"]

# Model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model_accident.pkl")
print("✅ Accident prediction model trained and saved.")
