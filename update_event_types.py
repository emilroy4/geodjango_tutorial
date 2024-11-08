import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango_tutorial.settings")  # Adjust to your settings path
django.setup()

from events.models import Event  # Import your Event model

# Define the mapping of event titles to their corresponding allowed event types
event_type_updates = {
    'Soda Blonde': 'Music',
    'Muireann Bradley': 'Music',
    'Ed Byrne - Tragedy Plus Time': 'Comedy',
    'Cinema: Vanya (Extra Screening)': 'Film',
    'CoisCéim Dance Theatre: THE PIECE WITH THE DRUMS': 'Dance',
    'Ronan Collins - Showband Hits & Stories': 'Music',
    'Monday Night Cinema: The Crime is Mine': 'Film',
    'Stepping Out by Richard Harris': 'Theatre',
    'Iarla Ó Lionáird Trio as part of Between the Notes': 'Music',
    'Monday Night Cinema: Radical': 'Film',
    'OUTRAGE by Deirdre Kinahan': 'Theatre',
    'Big Screen Musicals: Girl from the North Country': 'Film',
    'David O’Doherty - Tiny Piano Man': 'Comedy',
    'Tom Dunne, Fiachna Ó Braonáin & Alan Connor: On the Road Again': 'Music',
    'Live Traditional Irish Music and Dance': 'Music',
    'Guided History Tour & Irish Coffee Demonstration': 'Workshop',
    'Exclusive Whiskey Tastings with West Cork Distillers': 'Workshop',
    'Beats, Rhymes & Life Presents: Tidal Wave Tour': 'Music',
    'Keenan - Live at The Black Box': 'Music',
    'Dublin Fringe Festival': 'Festival',
    'Christmas Willow Wreath Weaving Workshops': 'Workshop',
    'Getdown Services': 'Social',
    'Gaelforce River Fest': 'Festival',
    'Farmaphobia': 'Halloween',
    'Dom Martin': 'Music',
    'Michael Fry & The Indie Band': 'Music',
    'Gaelforce Great River Swim 2025': 'Sports',
    'Meryl Streek': 'Comedy',
    'MANA': 'Dance',
    'The Scare Factory': 'Halloween',
    'It’s Wine O’Clock': 'Social',
    'Gearóid Farrelly: Gearóid Rage': 'Comedy',
    'Mayo Dark Sky Festival 2024': 'Festival',
    'Cinema: Widow Clicquot': 'Film',
    'Catherine Young Dance - Floating on a Dead Sea': 'Dance',
    'Lisa Lambe - NightVisiting: Songs & Stories from the Hearth': 'Music',
    'Exhibition on Screen - Van Gogh: Poets & Lovers': 'Exhibition',
    'Guys and Dolls': 'Theatre',
    'Luke Carrig': 'Exhibition',
    'Chamber Music Series - Lumiere Quartet': 'Music',
    'Cassandra Jenkins': 'Music',
    'Frances Wilde': 'Comedy',
    'Memorial': 'Comedy',
    'Really Good Time': 'Comedy',
    'Eoin Kenny': 'Festival',
    'The Hans Zimmer Experience': 'Music',
    'Monday Night Cinema: Thelma': 'Film',
    'Halloween Event - Dark History Tours': 'Halloween',
    'An Evening With Michael Harding': 'Social',
    'Damien Dempsey plus Special Guests Aslan': 'Music',
    'The Phantom of the Opera at the Royal Albert Hall': 'Theatre',
    'Invisible String: The Taylor Swift Project': 'Music',
    'Cheek to Cheek - The Life & Music of Irving Berlin': 'Music',
    'Seán Joyce': 'Comedy',
    'Stepping Out by Richard Harris': 'Theatre',
    'Street Spectacle - Kerry Homecoming Festival - Kenmare': 'Festival',
    'Street Spectacle - Kerry Homecoming Festival - Listowel': 'Festival',
    'Leap Scarecrow Festival': 'Festival',
    'Stella Sings Ella: A Tribute to Ella Fitzgerald': 'Music',
    'Pumpkins in the Pines': 'Halloween',
    'Schubertreise XXXI': 'Music',
    'The Tallis Scholars: Chant': 'Music',
    'Tara Erraught & Laurence Cummings - NCH Friends Gala': 'Music',
    'The Dublin Legends': 'Music',
    'Street Spectacle - Kerry Homecoming Festival - Tralee': 'Festival',
    'Street Spectacle - Kerry Homecoming Festival - Dingle': 'Festival',
    'RTÉ Radio 1 - RTÉ Arena Live': 'Broadcast',
}

# Step 2: Update events
events_to_update = []

for title, event_type in event_type_updates.items():
    events = Event.objects.filter(title=title)
    for event in events:
        event.event_type = event_type
        events_to_update.append(event)

# Perform the bulk update if there are events to update
if events_to_update:
    Event.objects.bulk_update(events_to_update, ['event_type'])

print("Event types updated successfully.")
