class FullListService:
    def __init__(self, movies_service):
        self._movies_service = movies_service

    def get_grouped_full_list(self):
        movies = self._movies_service.get()
        grouped = self.group_by_decade(movies)
        return grouped

    def get_year(self, s):
        return int(s.split('-')[0])

    def group_by_decade(self, lst):
        grouped = {}

        for item in lst:
            year = self.get_year(item[2])
            decade = year - (year % 10)
            if decade in grouped:
                grouped[decade].append(item)
            else:
                grouped[decade] = [item]

        return grouped
