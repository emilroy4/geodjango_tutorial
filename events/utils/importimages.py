import requests

def fetch_image_from_pexels(query):
    api_key = '1airf5ys2Uph0Ir1LHcs0BHfDe3RjjcipQdxru4GhG7s2l7KSezpxLGx'
    headers = {
        'Authorization': api_key
    }
    url = f'https://api.pexels.com/v1/search?query={query}&per_page=1'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Get the first image URL from the results
        if data['photos']:
            return data['photos'][0]['src']['medium']
    except requests.RequestException as e:
        print(f"Error fetching image from Pexels: {e}")
    return None