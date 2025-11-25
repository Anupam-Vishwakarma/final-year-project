import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Add column names manually
columns = ["timestamp", "latitude", "longitude", "current_speed", "free_flow_speed", "congestion"]
df = pd.read_csv("traffic_data.csv", names=columns)

# Features & Target
X = df[["latitude", "longitude", "current_speed", "free_flow_speed"]]
y = df["congestion"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)
print(f"Mean Squared Error: {mse:.4f}")

# Save model
joblib.dump(model, "congestion_model.pkl")
print("✅ Model trained and saved as congestion_model.pkl")
