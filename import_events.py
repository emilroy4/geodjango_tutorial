import json
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("dbname='gis' user='docker' host='172.29.0.2' password='docker'")
cursor = conn.cursor()

# Load the JSON file
with open('csvjson.json', 'r') as file:
    events = json.load(file)

    for event in events:
        cursor.execute("""
            INSERT INTO events_event (title, description, start_date, end_date, location, latitude, longitude, url, event_type, contact_url, booking_url, contact_phone_number, booking_phone_number, venue_name, address, county, is_free_to_visit, price, start_time, end_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            event.get('Name'),  # Adjusted to match JSON key
            event.get('Description'),
            event.get('Start Date'),  # Adjust this if your JSON has specific date formats
            event.get('End Date'),    # Adjust this if your JSON has specific date formats
            event.get('Venue Name'),   # Adjusted to match JSON key
            event.get('Latitude'),     # Ensure this key matches the JSON
            event.get('Longitude'),    # Ensure this key matches the JSON
            event.get('Booking URL'),  # Adjusted to match JSON key
            event.get('Event Type'),   # Adjusted to match JSON key
            event.get('Contact URL'),  # Adjusted to match JSON key
            event.get('Booking URL'),   # Adjusted to match JSON key
            event.get('Contact Phone Number'),  # Adjusted to match JSON key
            event.get('Booking Phone Number'),   # Adjusted to match JSON key
            event.get('Venue Name'),   # Adjusted to match JSON key
            event.get('Address'),       # Add this key if your JSON contains it
            event.get('County'),        # Add this key if your JSON contains it
            event.get('Is Free To Visit'), # Adjusted to match JSON key
            event.get('Price'),         # Add this key if your JSON contains it
            event.get('Start Time'),    # Add this key if your JSON contains it
            event.get('End Time')       # Add this key if your JSON contains it
        ))

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
