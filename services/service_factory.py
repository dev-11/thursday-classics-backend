import config
import repositories.environment_repository as er
import repositories.s3_repository as s3r

from .storage_service import StorageService
from .secret_manager_service import SecretManagerService
from .tmdb_service import TMDBService
from .offer_service import OfferService
from .thursday_classics_service import ThursdayClassicsService
from .movie_service import MovieService
from .full_list_service import FullListService


class ServiceFactory:
    def __init__(self):
        """Service to create every service."""
        repo = s3r.S3Repository(config.data_bucket)
        env_repo = er.EnvironmentRepository()

        self._storage_service = StorageService(repo)
        self._secret_manager = SecretManagerService(env_repo)
        self._key = self._secret_manager.get_secret("tmdb_api_key")

        self._offer_service = OfferService(self._storage_service)
        self._movie_service = MovieService(self._storage_service)

    def get_thursday_classics_service(self):
        return ThursdayClassicsService(self._movie_service, self._offer_service, self.get_tmdb_service())

    def get_tmdb_service(self):
        service = TMDBService(self._key)
        return service

    def get_full_list_service(self):
        return FullListService(self._movie_service)
