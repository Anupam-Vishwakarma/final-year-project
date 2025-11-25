import joblib
import numpy as np

# Load the trained accident prediction model
model = joblib.load("model_accident.pkl")

# Test input: [latitude, longitude, current_speed, free_flow_speed, congestion_level]
current_speed = 8
free_flow_speed = 40
congestion_level = free_flow_speed / current_speed

test_input = np.array([[28.6139, 77.2090, current_speed, free_flow_speed, congestion_level]])

# Predict accident probability (0 = No, 1 = Yes)
accident_prediction = model.predict(test_input)

print("🚨 Accident likely!" if accident_prediction[0] == 1 else "✅ No accident expected.")
