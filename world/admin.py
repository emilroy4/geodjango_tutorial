from django.contrib import admin
from django.contrib.gis import admin
from .models import WorldBorder

# Use GISModelAdmin for geographic data display in the admin interface
admin.site.register(WorldBorder, admin.GISModelAdmin)
