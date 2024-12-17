import os
import requests

def fetch_image_from_unsplash(query):
    access_key = os.getenv('UNSPLASH_ACCESS_KEY')  # Ensure this is fetching the correct key
    print(f"Unsplash Access Key: {access_key}")  # Print the access key for verification
    if not access_key:
        raise ValueError("Unsplash access key is not set in environment variables.")
    
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
