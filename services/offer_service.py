import random
import config as c


class OfferService:
    def __init__(self, storage_service) -> None:
        self.storage_service = storage_service

    def has_offers(self) -> bool:
        return False

    def get_offers(self):
        if self.has_offers():
            offers = self.storage_service.get("offer")
            return offers

        offers = self.generate_offers()
        self.storage_service.save_or_update(offers, None)
        return offers

    def generate_offers(self):
        movies = self.storage_service.get(c.data_file)
        ids = random.sample(range(1, len(movies)), 3)
        return [
            movies[ids[0]],
            movies[ids[1]],
            movies[ids[2]]
        ]
