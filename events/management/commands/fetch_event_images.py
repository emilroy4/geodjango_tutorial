from django.core.management.base import BaseCommand
from events.models import Event
from events.utils.importimages import fetch_image_from_google

class Command(BaseCommand):
    help = 'Fetch images for events from Google'

    def handle(self, *args, **kwargs):
        events = Event.objects.filter(image_url__isnull=True)  # Only fetch for events without images
        for event in events:
            image_url = fetch_image_from_google(event.title)
            if image_url:
                event.image_url = image_url
                event.save()
                self.stdout.write(self.style.SUCCESS(f'Updated image for {event.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'No image found for {event.title}'))