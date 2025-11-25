from django.db import models

class TrafficData(models.Model):
    CONGESTION_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    location = models.CharField(max_length=255, db_index=True)  # ✅ Indexing for faster queries
    congestion_level = models.CharField(max_length=10, choices=CONGESTION_CHOICES, db_index=True)  # ✅ Index choices for better filtering
    accident_count = models.PositiveIntegerField(default=0)  # ✅ Ensure no negative values
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-recorded_at"]  # ✅ Show latest data first
        verbose_name_plural = "Traffic Data"  # ✅ Better admin display

    def __str__(self):
        return f"{self.location} - Congestion: {self.congestion_level} - Accidents: {self.accident_count}"
