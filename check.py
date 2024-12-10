import os
import django
import pandas as pd
from datetime import datetime

# Set the Django settings module environment variable explicitly
os.environ['DJANGO_SETTINGS_MODULE'] = 'geodjango_tutorial.settings'

# Initialize Django
django.setup()

# Now import the model after setting up Django
from events.models import Event

# Load the CSV file into a DataFrame
csv_file = '/home/ubuntu/geodjango_tutorial/Events.csv'  # Adjust the path as needed
df = pd.read_csv(csv_file)

# Function to convert date format
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except Exception as e:
        print(f"Error converting date {date_str}: {e}")
        return None

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Create a full location by merging venue name and address
    full_location = f"{row['Venue Name']} - {row['Address']}"

    # Convert start and end dates to proper format
    start_date = convert_date(row['Start Date'])
    end_date = convert_date(row['End Date'])

    # Check if the event already exists in the database based on title and location
    if start_date and end_date and not Event.objects.filter(title=row['Name'], location=full_location).exists():
        try:
            # Create and save the event object
            event = Event(
                title=row['Name'],
                location=full_location,
                event_type=row['Event Type'],
                description=row['Description'],
                contact_url=row['Contact URL'],
                booking_url=row['Booking URL'],
                contact_phone_number=row['Contact Phone Number'],
                booking_phone_number=row['Booking Phone Number'],
                venue_name=row['Venue Name'],
                address=row['Address'],
                county=row['County'],
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                is_free_to_visit=row['Is Free To Visit'],
                price=row['Price'],
                start_date=start_date,  # Use the converted date
                end_date=end_date,  # Use the converted date
                start_time=row['Start Time'],
                end_time=row['End Time'],
            )
            event.save()
            print(f"Event '{row['Name']}' loaded successfully.")
        except Exception as e:
            print(f"Error processing event '{row['Name']}': {e}")
    else:
        print(f"Duplicate event skipped: {row['Name']}")
