import random
import config as c
from datetime import datetime as dt


class OfferService:
    def __init__(self, storage_service) -> None:
        self.storage_service = storage_service

    def has_offers(self) -> bool:
        return self.storage_service.has_key(c.offer_file)

    def get_offers(self):
        offers = self.storage_service.get(c.offer_file)
        return offers

    def save_offers(self, offers):
        return self.storage_service.save_or_update(c.offer_file, offers, dt.now())

    def generate_offers(self, movies):
        ids = random.sample(range(0, len(movies)), 3)
        offers = [
            movies[ids[0]],
            movies[ids[1]],
            movies[ids[2]]
        ]

        return offers
