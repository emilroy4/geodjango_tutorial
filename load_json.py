import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango_tutorial.settings")  # Ensure this is your correct settings path
django.setup()

from events.models import Event  # Import models after setting up the Django environment
import json
from datetime import datetime
from django.utils import timezone

# Function to load events from the JSON file
def load_events_from_json(file_name):
    # Construct the full file path relative to the current script location
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for item in data:
            try:
                # Parse date and make it timezone-aware
                start_date = timezone.make_aware(
                    datetime.strptime(item['Start Date'], '%d/%m/%Y')
                )
                end_date = timezone.make_aware(
                    datetime.strptime(item['End Date'], '%d/%m/%Y')
                )

                # Check for missing latitude and longitude
                latitude = item.get('Latitude')
                longitude = item.get('Longitude')

                # Skip event if latitude or longitude is missing
                if latitude is None or longitude is None:
                    print(f"Skipping event '{item['Name']}': Missing latitude or longitude.")
                    continue

                # Truncate fields if necessary
                title = item['Name'][:200]  # Limit to 200 characters
                event_type = item['Event Type'][:100]  # Adjust limit based on your model

                # Create or update the event
                Event.objects.update_or_create(
                    title=title,
                    event_type=event_type,
                    defaults={
                        'description': item.get('Description', '')[:500],  # Adjust limit as needed
                        'start_date': start_date,
                        'end_date': end_date,
                        'location': item.get('Location', '')[:200],  # Adjust limit as needed
                        'url': item.get('URL', '')[:200],  # Adjust limit as needed
                        'latitude': latitude,
                        'longitude': longitude,
                    }
                )
                print(f"Event '{title}' loaded successfully.")
            except Exception as e:
                print(f"Error loading event '{item['Name']}': {e}")

# Load events from the specified JSON file
load_events_from_json('limited_events.json')
