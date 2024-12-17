from django.core.management.base import BaseCommand
from events.models import Event
from events.utils.importimages import fetch_image_from_google

class Command(BaseCommand):
    help = 'Fetch and replace images for all events from Google'

    def handle(self, *args, **kwargs):
        events = Event.objects.all()  # Fetch all events, regardless of current image status
        for event in events:
            image_url = fetch_image_from_google(event.title)
            if image_url:
                event.image_url = image_url
                event.save()
                self.stdout.write(self.style.SUCCESS(f'Replaced image for {event.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'No image found for {event.title}'))