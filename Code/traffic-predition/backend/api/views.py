from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
import joblib
import numpy as np
from .models import TrafficData
from .serializers import TrafficDataSerializer
from django.conf import settings
import os

    # TomTom API Key for real-time traffic data
    # Load the trained models for prediction
congestion_model = joblib.load(os.path.join(settings.BASE_DIR, "api", "congestion_model.pkl"))
print("✅ Congestion model features:", congestion_model.n_features_in_)  # This should be 4
speed_model = joblib.load(os.path.join(settings.BASE_DIR, "api", "model_speed.pkl"))
accident_model = joblib.load(os.path.join(settings.BASE_DIR, "api", "model_accident.pkl"))



@api_view(['GET'])
def get_traffic_data(request):
    try:
        data = TrafficData.objects.all()
        if not data.exists():
            return Response({"message": "No traffic data available."}, status=status.HTTP_204_NO_CONTENT)

        serialized_data = TrafficDataSerializer(data, many=True)
        return Response({"traffic_data": serialized_data.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 🔴 NEW VIEW FUNCTION
@api_view(['GET'])
def get_live_traffic(request):
        """
        Get real-time traffic data from TomTom API based on lat/lon.
        Example: /api/live-traffic/?lat=28.6139&lon=77.2090&zoom=10
        """
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        zoom = request.GET.get('zoom', 10)

        if not lat or not lon:
            return Response(
                {"error": "Please provide both 'lat' and 'lon' query parameters."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            url = (
                    f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?"
                    f"point={lat},{lon}&unit=KMPH&key={settings.TOMTOM_API_KEY}"
    )
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return Response({"live_traffic": data}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": f"Failed to fetch traffic data: {response.status_code}"},
                    status=status.HTTP_502_BAD_GATEWAY
                )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 🔴 NEW VIEW FUNCTION FOR PREDICTION
@api_view(['POST'])
def predict_traffic(request):
    try:
        print("📥 Incoming request data:", request.data)

        lat = float(request.data.get('latitude'))
        lon = float(request.data.get('longitude'))
        current_speed = float(request.data.get('current_speed'))
        free_flow_speed = float(request.data.get('free_flow_speed'))

        print(f"🔍 Inputs received: lat={lat}, lon={lon}, current_speed={current_speed}, free_flow_speed={free_flow_speed}")

        # Step 1: Prepare input for congestion & speed models
        input_features = np.array([[lat, lon, current_speed, free_flow_speed]])

        # Step 2: Run predictions
        congestion = congestion_model.predict(input_features)[0]
        predicted_speed = speed_model.predict(input_features)[0]

        # Step 3: Calculate congestion level for accident model
        congestion_level = free_flow_speed / current_speed
        accident_input = np.array([[lat, lon, current_speed, free_flow_speed, congestion_level]])

        # Step 4: Predict accident risk
        accident_prob = accident_model.predict(accident_input)[0]
        accident_risk = "High" if accident_prob == 1 else "Low"

        return Response(
            {
                "congestion_level": round(congestion, 2),
                "predicted_speed": round(predicted_speed, 2),
                "accident_risk": accident_risk,
            },
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print("❌ Prediction failed:", str(e))
        return Response({"error": f"Error processing request: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
