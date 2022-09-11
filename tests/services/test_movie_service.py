import unittest

from services import MovieService
from tests.test_environment import mocks


class StorageServiceTests(unittest.TestCase):
    def test_get_returns_data_unchanged(self):
        ms = MovieService(mocks.get_mocked_storage_service())
        result = ms.get()
        self.assertEqual("asdf", result)

    def test_has_movies_returns_fetched_data_unchanged(self):
        ms = MovieService(mocks.get_mocked_storage_service())
        result = ms.has_movies()
        self.assertTrue(result)

    def test_save_returns_boolean_result(self):
        ms = MovieService(mocks.get_mocked_storage_service())
        result = ms.save(None)
        self.assertTrue(result)
