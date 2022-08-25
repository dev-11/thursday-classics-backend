import config as c
import requests
import json
import data_classes as dc


class TMDBService:
    def __init__(self, api_key) -> None:
        self._api_key = api_key

    def _build_list_url(self, list_id):
        return f'{c.tmdb_endpoints["list"]}/{list_id}?api_key={self._api_key}'

    def get_list(self, list_id):
        result = requests.get(self._build_list_url(list_id))
        titles = []
        if result.status_code == 200:
            api_response = json.loads(result.text)
            titles.append([dc.Movie(i['title'], i['poster_path']) for i in api_response['items']])

            return titles

        return []
