import config as c
import requests

from http import HTTPStatus


class TMDBService:
    def __init__(self, api_key) -> None:
        self._api_key = api_key

    def build_list_url(self, list_id, page):
        return f'{c.tmdb_endpoints["list"]}/{list_id}?page={page}api_key={self._api_key}'

    def get_list_by_page(self, list_id, page):
        r = requests.get(self.build_list_url(list_id, page))
        r.raise_for_status()
        result = r.json()
        
        return [[i.get('title', i.get('original_name')), i['poster_path']] for i in result['items']], r["total_pages"]

    def get_list(self, list_id):
        total_list = []

        first_page_items, last_page = self.get_list_by_page(list_id, 1)
        total_list.extend(first_page)

        for idx in range(2, last_page):
            actual_page_items, _ = self.get_list_by_page(list_id, idx)
            total_list.extend(actual_page_items)

        return total_list
