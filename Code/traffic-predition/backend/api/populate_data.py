import os
import sys
import django
import random
from datetime import datetime, timedelta

# Add your Django project's root directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # ✅ Dynamically set path

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

# Now import models
from api.models import TrafficData

# Sample locations
LOCATIONS = ["New York", "Los Angeles", "Chicago", "San Francisco", "Houston", "Miami", "Seattle", "Boston"]

# Allowed congestion levels (Ensures valid choices)
CONGESTION_LEVELS = ["High", "Medium", "Low"]  # ✅ Using predefined choices


def generate_fake_data(records=20):
    """Generates sample traffic data and inserts it into the database."""
    try:
        data_entries = []
        for _ in range(records):
            location = random.choice(LOCATIONS)
            congestion_level = random.choice(CONGESTION_LEVELS)  # ✅ Pick a valid congestion level
            accident_count = random.randint(0, 5)  # Random accident count
            recorded_at = datetime.now() - timedelta(minutes=random.randint(0, 1440))  # Last 24 hours

            data_entries.append(
                TrafficData(
                    location=location,
                    congestion_level=congestion_level,
                    accident_count=accident_count,
                    recorded_at=recorded_at
                )
            )
        
        # ✅ Bulk insert for better performance
        TrafficData.objects.bulk_create(data_entries)
        print(f"✅ Successfully inserted {records} new records!")

    except Exception as e:
        print(f"❌ Error while populating data: {e}")


# Run the function only when executed directly
if __name__ == "__main__":
    generate_fake_data(20)  # ✅ Default to 20 records, but easily changeable
