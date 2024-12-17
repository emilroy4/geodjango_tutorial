import requests

def fetch_image_from_google(query):
    api_key = 'AIzaSyCc3u3VoEUngJ2iAVFSMnkmtfrBNrt52Jo'
    search_engine_id = '153795a42ec054306'
    search_url = "https://www.googleapis.com/customsearch/v1"

    # Exclude Facebook and lookaside URLs
    query_with_exclusions = f"{query} -site:facebook.com -site:lookaside.fbsbx.com"

    params = {
        "q": query_with_exclusions,
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
            image_url = search_results['items'][0]['link']
            # Validate that the URL does not contain lookaside.fbsbx.com
            if "lookaside.fbsbx.com" not in image_url:
                return image_url
            else:
                print("Excluded image due to lookaside.fbsbx.com URL.")
    except requests.RequestException as e:
        print(f"Error fetching image from Google: {e}")
    return None

# Example usage
image_url = fetch_image_from_google("music concert")
if image_url:
    print(f"Fetched image URL: {image_url}")
else:
    print("No valid image found.")
