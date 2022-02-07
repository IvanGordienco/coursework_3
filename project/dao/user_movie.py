from sqlalchemy import exc

from project.dao.models.user_movie import User_Movie


class User_MovieDAO:
    def __init__(self, session):
        self.session = session

    def create_user_movie(self, data):
        try:
            new_user = User_Movie(**data)
            self.session.add(new_user)
            self.session.commit()
            return new_user
        except exc.IntegrityError as e:
            # errorInfo = e.orig.args
            # print(f"{errorInfo}")
            self.session.rollback()