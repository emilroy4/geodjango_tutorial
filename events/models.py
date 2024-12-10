from django.db import models

class Event(models.Model):
    title = models.TextField()  # Changed from CharField to TextField
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.TextField()  # Changed from CharField to TextField
    latitude = models.FloatField()
    longitude = models.FloatField()
    url = models.URLField(max_length=500, blank=True, null=True)
    event_type = models.TextField()  # Changed from CharField to TextField
    contact_url = models.URLField(max_length=500, blank=True, null=True)
    booking_url = models.URLField(max_length=500, blank=True, null=True)
    contact_phone_number = models.TextField(max_length=1000, blank=True, null=True)  # Can stay as CharField if phone numbers are short
    booking_phone_number = models.TextField(max_length=1000, blank=True, null=True)  # Can stay as CharField if phone numbers are short
    venue_name = models.TextField()  # Changed from CharField to TextField
    address = models.TextField()  # Changed from CharField to TextField
    county = models.TextField()  # Changed from CharField to TextField
    is_free_to_visit = models.TextField(max_length=100, blank=True, null=True)  # Can stay as CharField
    price = models.TextField(max_length=100, blank=True, null=True)  # Can stay as CharField
    start_time = models.TextField(max_length=100, blank=True, null=True)  # Can stay as CharField
    end_time = models.TextField(max_length=100, blank=True, null=True)  # Can stay as CharField

    def __str__(self):
        return self.title
