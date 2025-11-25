import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
columns = ["timestamp", "latitude", "longitude", "current_speed", "free_flow_speed", "congestion"]
df = pd.read_csv("traffic_data.csv", names=columns)

# Features and Target
X = df[["latitude", "longitude", "current_speed", "free_flow_speed"]]  
y = df["current_speed"]

# Model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "model_speed.pkl")
print("✅ Speed prediction model trained and saved.")
