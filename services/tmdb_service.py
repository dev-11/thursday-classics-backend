import config as c
import requests
import json

from http import HTTPStatus


class TMDBService:
    def __init__(self, api_key) -> None:
        self._api_key = api_key

    def _build_list_url(self, list_id):
        return f'{c.tmdb_endpoints["list"]}/{list_id}?api_key={self._api_key}'

    def get_list(self, list_id):
        result = requests.get(self._build_list_url(list_id))

        if result.status_code == HTTPStatus.OK:
            api_response = json.loads(result.text)
            return [[i.get('title', i.get('original_name')), i['poster_path']] for i in api_response['items']]

        return []
