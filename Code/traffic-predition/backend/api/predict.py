import joblib
import pandas as pd

# Load model only once
model = joblib.load("congestion_model.pkl")

def predict_congestion(lat, lon, curr_speed, free_flow_speed):
    input_data = pd.DataFrame([[lat, lon, curr_speed, free_flow_speed]],
                              columns=["latitude", "longitude", "current_speed", "free_flow_speed"])
    prediction = model.predict(input_data)[0]
    return prediction
