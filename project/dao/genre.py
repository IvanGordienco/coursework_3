import sqlalchemy
from sqlalchemy.orm.exc import NoResultFound

from project.dao.models import Genre
from project.exceptions import ItemNotFound


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        genre = self.session.query(Genre).get(bid)
        if not genre:
            raise ItemNotFound("Не найден Genre!")
        else:
            return genre

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, update):
        self.session.add(update)
        self.session.commit()
