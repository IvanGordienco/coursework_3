from flask_restx import Resource, Namespace

from project.helpers.decorators import admin_required, auth_required
from implemented import user_service, user_movie_service
from project.schemas.schemas import UserMovie

from project.views.users import users_schema

favorites_ns = Namespace('favorites')
users_movie = UserMovie(many=True)


@favorites_ns.route('/movies/<int:movie_id>')
class FavView(Resource):
    @auth_required
    def delete(self, user_id: int, movie_id: int):
        user_movie_service.get(user_id, movie_id)
        return "", 204

    @auth_required
    def post(self, user_id: int, movie_id: int):
        user_movie_service.create({'user_id': user_id, 'movie_id': movie_id})
        return "", 204
