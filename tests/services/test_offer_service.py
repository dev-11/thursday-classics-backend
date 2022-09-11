import unittest

from services import OfferService
from tests.test_environment import mocks


class OfferServiceTests(unittest.TestCase):
    def test_get_returns_data_unchanged(self):
        ms = OfferService(mocks.get_mocked_storage_service())
        result = ms.get_offers()
        self.assertEqual("asdf", result)

    def test_has_movies_returns_fetched_data_unchanged(self):
        ms = OfferService(mocks.get_mocked_storage_service())
        result = ms.has_offers()
        self.assertTrue(result)

    def test_save_returns_boolean_result(self):
        ms = OfferService(mocks.get_mocked_storage_service())
        result = ms.save_offers(None)
        self.assertTrue(result)
