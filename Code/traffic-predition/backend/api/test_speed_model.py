import joblib
import numpy as np

# Load the trained speed prediction model
model = joblib.load("model_speed.pkl")

# Test input: [latitude, longitude, free_flow_speed]
test_input = np.array([[28.6139, 77.2090, 45,50]])  # Example coordinates and free flow speed

# Predict current speed
predicted_speed = model.predict(test_input)

print(f"🚗 Predicted current speed: {predicted_speed[0]:.2f} km/h")
