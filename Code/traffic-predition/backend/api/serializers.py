from rest_framework import serializers
from .models import TrafficData

class TrafficDataSerializer(serializers.ModelSerializer):
    """Serializer for TrafficData model, ensuring structured API responses."""

    congestion_level = serializers.ChoiceField(choices=TrafficData.CONGESTION_CHOICES)  # ✅ Validate congestion levels

    class Meta:
        model = TrafficData
        fields = '__all__'  # ✅ Include all fields
        read_only_fields = ['recorded_at']  # ✅ Prevent manual changes to timestamps
