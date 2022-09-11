import config as c
from datetime import datetime as dt


class MovieService:
    def __init__(self, storage_service):
        self.storage_service = storage_service

    def get(self):
        movies = self.storage_service.get(c.data_file)
        return movies

    def save(self, movies):
        return self.storage_service.save_or_update(c.data_file, movies, dt.now())

    def has_movies(self) -> bool:
        return self.storage_service.has_key(c.data_file)
