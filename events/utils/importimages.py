from django.conf import settings
import requests

def fetch_image_from_google(query):
    api_key = settings.GOOGLE_API_KEY
    search_engine_id = settings.GOOGLE_SEARCH_ENGINE_ID
    search_url = "https://www.googleapis.com/customsearch/v1"

    if not api_key or not search_engine_id:
        print("Error: GOOGLE_API_KEY or GOOGLE_SEARCH_ENGINE_ID is not set.")
        return None

    query_with_exclusions = f"{query} -site:facebook.com"

    params = {
        "q": query_with_exclusions,
        "cx": search_engine_id,
        "key": api_key,
        "searchType": "image",
        "num": 1
    }

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        search_results = response.json()

        if 'items' in search_results:
            return search_results['items'][0]['link']
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
    return None
