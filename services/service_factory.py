import config
import repositories.environment_repository as er
# import repositories.s3_repository as s3r
from .secret_manager_service import SecretManagerService
from .tmdb_service import TMDBService


class ServiceFactory:
    def __init__(self):
        """Service to create every service."""
        # repo = s3r.S3Repository(config.data_bucket)
        env_repo = er.EnvironmentRepository()
        self._secret_manager = SecretManagerService(env_repo)
        self._key = self._secret_manager.get_secret("tmdb_api_key")

    # def get_all_services(self):
    #     return [
    #     ]

    def get_secret_manager(self):
        return self._secret_manager

    def get_tmdb_service(self):
        service = TMDBService(self._key)
        return service


def get_enabled_services():
    return [
        service
        for service in ServiceFactory().get_all_services()
        if service.get_service_full_name() in config.enabled_services
    ]