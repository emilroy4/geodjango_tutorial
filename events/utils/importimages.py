import requests

def fetch_image_from_google(query):
    api_key = 'YOUR_GOOGLE_API_KEY'
    search_engine_id = 'YOUR_SEARCH_ENGINE_ID'
    search_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": query,
        "cx": search_engine_id,
        "key": api_key,
        "searchType": "image",
        "num": 1  # Number of results to return
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        search_results = response.json()

        # Get the first image URL from the results
        if 'items' in search_results:
            return search_results['items'][0]['link']
    except requests.RequestException as e:
        print(f"Error fetching image from Google: {e}")
    return None

# Example usage
image_url = fetch_image_from_google("music concert")
if image_url:
    print(f"Fetched image URL: {image_url}")