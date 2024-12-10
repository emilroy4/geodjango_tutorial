from django.contrib import admin

# Register your models here.
from .models import Event  # Import your Event model

# Register the Event model with the admin interface
admin.site.register(Event)
