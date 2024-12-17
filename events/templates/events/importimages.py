import os
import requests

def fetch_image_from_unsplash(query):
    access_key = os.getenv('UNSPLASH_ACCESS_KEY')  # Use environment variable for security
    url = f'https://api.unsplash.com/search/photos?query={query}&client_id={access_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Get the first image URL from the results
        if data['results']:
            return data['results'][0]['urls']['regular']
    except requests.RequestException as e:
        print(f"Error fetching image from Unsplash: {e}")
    return None

# Example usage
event_type = 'music concert'
image_url = fetch_image_from_unsplash(event_type)
if image_url:
    print(f"Fetched image URL: {image_url}")