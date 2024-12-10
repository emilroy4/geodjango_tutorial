import os
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango_tutorial.settings')

# Initialize Django
django.setup()

from events.models import Event

# Refined event types and associated keywords
event_types = {
    'Comedy': ['Comedy', 'Stand-up', 'Funny', 'Lately', 'Shelf Help', 'Gearóid Rage'],
    'Music': ['Concert', 'Band', 'Gig', 'Tour', 'Singer', 'Orchestra', 'Symphonic', 'Music', 'Choral'],
    'Festival': ['Festival', 'TradFest', 'Pride', 'Celebration'],
    'Theatre': ['Theatre', 'Play', 'Show', 'Panto', 'Red Riding Hood', 'Performance'],
    'Sports': ['Race', 'Marathon', 'Run', 'Swim', 'Sports', 'EPCR', 'Champions Cup'],
    'Christmas': ['Santa', 'Christmas', 'Elf', 'Holiday', 'Winter Wonderland', 'Pines', 'Festive', 'Tinsel'],
    'Halloween': ['Pumpkin', 'Scare', 'Haunted', 'Halloween', 'Spooky', 'Factory'],
    'History': ['History', 'Heritage', 'Legacy', 'James Joyce', 'Tour', 'Recovered Voices', 'Historical'],
    'Art': ['Art', 'Exhibition', 'Gallery', 'Painting', 'Drawing', 'Creative'],
    'Literature': ['Reading', 'Book', 'Literature', 'Poetry', 'Writer', 'Writing'],
    'Workshop': ['Workshop', 'Masterclass', 'DIY', 'Session', 'Make Your Own', 'Create', 'Painting', 'Craft'],
    'Dance': ['Dance', 'Ballet', 'Choreography', 'Swing', 'Ceili', 'Salsa', 'Jive'],
    'Film': ['Film', 'Movie', 'Cinema', 'Screening', 'Documentary'],
    'Social': ['Party', 'Networking', 'Meetup', 'Gathering', 'Social', 'Blizzard Ball'],
    'Food & Drink': ['Whiskey', 'Cocktail', 'Wine', 'Gin', 'Afternoon Tea', 'Tasting'],
    'Family': ['Family', 'Kids', 'Child', 'Children', 'Céilí'],
    'Nature': ['Trail', 'Park', 'Outdoor', 'Adventure', 'Eco', 'Woodland'],
    'Miscellaneous': ['Talent', 'Miscellaneous', 'Album Launch', 'Single Launch', 'Special Guests', 'Vision of Venus']
}

# Function to assign event type based on title
def assign_event_type(title):
    for event_type, keywords in event_types.items():
        if any(keyword.lower() in title.lower() for keyword in keywords):
            return event_type
    return 'General'  # Default if no keyword matches

# Get all events with event_type "General" or "Event"
events = Event.objects.filter(event_type__in=["General", "Event"])

# Update event type based on the title
updated_count = 0
skipped_count = 0
for event in events:
    updated_type = assign_event_type(event.title)
    if event.event_type in ["General", "Event"] and event.event_type != updated_type:
        event.event_type = updated_type
        event.save()
        updated_count += 1
        print(f"Updated event '{event.title}' to type '{updated_type}'")
    else:
        skipped_count += 1

print(f"Total updated events: {updated_count}")
print(f"Total skipped events: {skipped_count}")
print("Event types update process completed.")
