from project.dao.director import DirectorDAO
from project.tools.functions import set_keys


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_d):
        return self.dao.create(director_d)

    def update(self, data, bid):
        update = self.dao.get_one(bid)
        set_keys(data, update)
        self.dao.update(update)

    def delete(self, rid):
        self.dao.delete(rid)

