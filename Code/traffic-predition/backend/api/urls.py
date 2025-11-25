from django.urls import path
from .views import get_traffic_data, get_live_traffic , predict_traffic # ⬅️ import new view

app_name = "api"

urlpatterns = [
    path("traffic/", get_traffic_data, name="traffic-data"),
    path("live-traffic/", get_live_traffic, name="live-traffic"),  # ⬅️ NEW ENDPOINT
    path("predict-traffic/", predict_traffic, name="predict-traffic"),  # ⬅️ NEW PREDICTION ENDPOINT
]
