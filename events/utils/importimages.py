from django.conf import settings
import requests

def fetch_image_from_google(query):
    api_key = settings.GOOGLE_API_KEY
    search_engine_id = settings.GOOGLE_SEARCH_ENGINE_ID
    search_url = "https://www.googleapis.com/customsearch/v1"

    # Exclude images from Facebook using -site:facebook.com
    query_with_exclusions = f"{query} -site:facebook.com"

    params = {
        "q": query_with_exclusions,  # Query with exclusions
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
        else:
            print(f"No images found for query: {query}")
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
    return None
