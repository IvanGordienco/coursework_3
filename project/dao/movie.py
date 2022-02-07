from project.dao.models.movie import Movie
from project.exceptions import ItemNotFound


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        movie = self.session.query(Movie).get(bid)
        if not movie:
            raise ItemNotFound("Не найден Movie!")
        else:
            return movie

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, update):
        self.session.add(update)
        self.session.commit()