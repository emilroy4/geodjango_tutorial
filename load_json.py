import csv
from datetime import datetime
from events.models import Event

# Path to the CSV file
file_path = '/home/ubuntu/geodjango_tutorial/Events.csv'

def load_events_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        
        # Loop through the rows of the CSV
        for row in reader:
            # Extract event details
            title = row['title']
            start_date = row['start_date']
            end_date = row['end_date']
            location = row['location']
            url = row['url'] if row['url'] else None

            # Parse dates (assuming CSV dates are in 'DD/MM/YYYY' format)
            try:
                start_date = datetime.strptime(start_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%d/%m/%Y').strftime('%Y-%m-%d')
            except ValueError as e:
                print(f"Skipping event due to date format issue: {e}")
                continue
            
            # Check if the event already exists
            existing_event = Event.objects.filter(title=title, start_date=start_date, end_date=end_date).first()
            if existing_event:
                print(f"Skipping duplicate event: {title}")
                continue  # Skip this event if it already exists
            
            # Create and save the new event
            Event.objects.create(
                title=title,
                start_date=start_date,
                end_date=end_date,
                location=location,
                url=url,
            )
            print(f"Event '{title}' loaded successfully.")

# Load events from CSV
load_events_from_csv(file_path)
