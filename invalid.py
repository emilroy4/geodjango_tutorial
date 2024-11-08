import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango_tutorial.settings")  # Adjust this path as needed
django.setup()

from events.models import Event  # Import your Event model

# Define the mapping of event titles to their corresponding event types
event_type_updates = {
    "It’s Wine O’Clock": "Social",
    "Catherine Young Dance - Floating on a Dead Sea": "Dance",
    "Lisa Lambe - NightVisiting: Songs & Stories from the Hearth": "Music",
    "Exhibition on Screen - Van Gogh: Poets & Lovers": "Exhibition",
    "RTÉ Radio 1 - RTÉ Arena Live": "Broadcast",
    "Kids’ Halloween Party at The Science Gallery": "Halloween",  # Adjust to allowed types if needed
    "Winter Wonderland at Dublin Zoo": "Festival",  # Adjust to allowed types if needed
    "Swiftly into a Culwick Christmas": "Festival",  # Adjust to allowed types if needed
}

# Update the event types
for title, new_event_type in event_type_updates.items():
    events = Event.objects.filter(title=title)
    for event in events:
        # Only update if the new event type is in the allowed list
        if new_event_type in [
            'Comedy', 'Festival', 'Sports', 'Music', 
            'Halloween', 'Workshop', 'Social', 
            'Dance', 'Film', 'Theatre', 
            'Broadcast', 'Exhibition', 'Family', 'Christmas'  # Include Family and Christmas if they are allowed
        ]:
            event.event_type = new_event_type
            event.save()
            print(f"Updated '{event.title}' to event type '{new_event_type}'")
        else:
            print(f"'{new_event_type}' is not an allowed event type for '{event.title}'")

print("Event types updated successfully.")
