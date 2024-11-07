# geodjango_tutorial/events/populate_events.py

import requests
import json
from django.conf import settings
from django.utils import timezone
from .models import Event  # Ensure Event model is defined in models.py with appropriate fields

# This URL should point to the API endpoint for Fáilte Ireland's events
API_URL = "https://failteireland.azure-api.net/opendata-api/v2/events"

def fetch_events():
    """
    Fetch events data from Fáilte Ireland's Open Data API.
    """
    headers = {
        'Ocp-Apim-Subscription-Key': settings.FAILTE_API_KEY  # Ensure this key is added to settings
    }
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        events_data = response.json()
        return events_data.get('items', [])  # Adjust according to API's response structure
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def populate_events():
    """
    Populate the database with event data fetched from the API.
    """
    events = fetch_events()

    for event in events:
        # Extract relevant data fields from the event data
        title = event.get("title")
        description = event.get("description")
        start_date = event.get("start_date")
        end_date = event.get("end_date")
        location = event.get("location")  # Adjust fields based on actual response
        
        # Create or update the event in the database
        obj, created = Event.objects.update_or_create(
            title=title,
            defaults={
                "description": description,
                "start_date": timezone.datetime.fromisoformat(start_date) if start_date else None,
                "end_date": timezone.datetime.fromisoformat(end_date) if end_date else None,
                "location": location,
            },
        )
        if created:
            print(f"Added new event: {title}")
        else:
            print(f"Updated event: {title}")

    print("Event data population complete.")
