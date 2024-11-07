import requests

class FailteIrelandAPI:
    def __init__(self, subscription_key):
        self.base_url = "https://failteireland.azure-api.net/opendata-api/v2/events"
        self.headers = {
            "Ocp-Apim-Subscription-Key": subscription_key
        }

    def get_events(self, params=None):
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
