import unittest
import services.tmdb_service as tmdb
import mock

from http import HTTPStatus
from tests.test_environment import mocks


class TestTMDBService(unittest.TestCase):
    def test_build_list_url_returns_correct_url(self):
        s = tmdb.TMDBService("test_api_key")
        url = s.build_list_url("test_list_id")
        self.assertEqual("https://api.themoviedb.org/3/list/test_list_id?api_key=test_api_key", url)

    @mock.patch('requests.get')
    def test_get_list_returns_correct_list_for_http_ok(self, mock_get):
        mock_get.return_value = mocks.get_mocked_response_for_tmdb_list()

        s = tmdb.TMDBService("test_api_key")
        lst = s.get_list("test_list_id")

        self.assertEqual([['test_title_01', 'test_poster_01'], ['test_title_02', 'test_poster_02']], lst)

    @mock.patch('requests.get')
    def test_get_list_returns_correct_list_for_http_bad_request(self, mock_get):
        mock_get.return_value = mocks.get_mocked_response_for_tmdb_list(HTTPStatus.BAD_REQUEST)

        s = tmdb.TMDBService("test_api_key")
        lst = s.get_list("test_list_id")

        self.assertEqual([], lst)
