from project.dao.user_movie import User_MovieDAO


class UserMovieService:
    def __init__(self, dao: User_MovieDAO):
        self.dao = dao

    def create(self, user_movie_d):
        return self.dao.create_user_movie(user_movie_d)