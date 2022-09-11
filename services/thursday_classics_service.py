import config as c


class ThursdayClassicsService:
    def __init__(self, movie_service, offer_service, tmdb_service):
        self.movie_service = movie_service
        self.offer_service = offer_service
        self.tmdb_service = tmdb_service

    def get_movies(self):
        if not self.offer_service.has_offers():
            if not self.movie_service.has_movies():
                self.update_movies()

            self.update_offers()

        offers = self.offer_service.get_offers()
        return offers

    def update_movies(self):
        lst = self.tmdb_service.get_list(c.list_id)
        return self.movie_service.save(lst)

    def update_offers(self):
        movies = self.movie_service.get()
        offers = self.offer_service.generate_offers(movies)

        for o in offers:
            o[1] = f'{c.tmdb_endpoints["cdn_300"]}{o[1]}'

        return self.offer_service.save_offers(offers)
