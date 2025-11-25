import joblib
import numpy as np

# Step 1: Load trained model
model = joblib.load("congestion_model.pkl")

# Step 2: Test data → (latitude, longitude, current_speed, free_flow_speed)
test_input = np.array([[28.6139, 77.2090, 22, 24]])  # change values if needed

# Step 3: Make prediction
prediction = model.predict(test_input)

# Step 4: Print the result
print(f"Predicted congestion level: {prediction[0]:.4f}")
