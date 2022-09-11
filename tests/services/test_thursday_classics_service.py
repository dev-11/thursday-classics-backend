import unittest

from services import ThursdayClassicsService
from tests.test_environment import mocks


class ThursdayClassicsServiceTests(unittest.TestCase):
    def test_get_movies_returns_list(self):
        tcs = ThursdayClassicsService(mocks.get_mocked_movie_service(),
                                      mocks.get_mocked_offer_service(),
                                      mocks.get_mocked_tmdb_service())

        movies = tcs.get_movies()
        self.assertEqual([['title1', 'poster1'], ['title2', 'poster2'], ['title3', 'poster3']], movies)

    def test_update_movies_returns_boolean_result(self):
        tcs = ThursdayClassicsService(mocks.get_mocked_movie_service(),
                                      mocks.get_mocked_offer_service(),
                                      mocks.get_mocked_tmdb_service())

        result = tcs.update_movies()
        self.assertTrue(result)

    def test_update_offers_returns_boolean_result(self):
        tcs = ThursdayClassicsService(mocks.get_mocked_movie_service(),
                                      mocks.get_mocked_offer_service(),
                                      mocks.get_mocked_tmdb_service())

        result = tcs.update_offers()
        self.assertTrue(result)
