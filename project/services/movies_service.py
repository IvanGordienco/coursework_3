from project.dao.movie import MovieDAO
from project.tools.functions import set_keys


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, data, bid):
        update = self.dao.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

