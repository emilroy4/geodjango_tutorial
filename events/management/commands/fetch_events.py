# events/management/commands/fetch_events.py
import requests
from django.core.management.base import BaseCommand
from events.models import Event  # Replace with your actual model
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fetches events data from Fáilte Ireland API and updates the database'

    def handle(self, *args, **kwargs):
        url = "https://failteireland.azure-api.net/opendata-api/v2/events"
        headers = {
            'Ocp-Apim-Subscription-Key': 'YOUR_SUBSCRIPTION_KEY'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            events = response.json()  # Assuming response is in JSON format
            for event_data in events:
                Event.objects.update_or_create(
                    external_id=event_data['id'],  # Use a unique identifier
                    defaults={
                        'name': event_data['name'],
                        'description': event_data.get('description'),
                        'location': event_data.get('location'),
                        'start_date': event_data.get('start_date'),
                        'end_date': event_data.get('end_date'),
                        'updated_at': timezone.now(),
                        # Add other fields as required
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully fetched and updated events.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch events data.'))
