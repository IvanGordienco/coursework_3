from project.dao import GenreDAO
from project.tools.functions import set_keys


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_d):
        return self.dao.create(genre_d)

    def update(self, data, bid):
        update = self.dao.get_one(bid)
        set_keys(data, update)
        return self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

