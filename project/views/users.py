from flask_restx import Resource, Namespace

from project.helpers.decorators import admin_required, auth_required
from implemented import user_service
from project.schemas.schemas import UserSchema
from flask import request, abort, jsonify, make_response

from project.tools.security import compare_passwords

users_ns = Namespace('users')
user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)



@users_ns.route('/')
class UsersView(Resource):
    #@admin_required
    def get(self):
        role = request.args.get('role')
        username = request.args.get('username')
        data = {
            "username": username,
            "role": role
        }
        return users_schema.dump(user_service.get_all(data))

@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self, user_id: int):
        role = request.args.get('role')
        username = request.args.get('username')
        data = {
            "username": username,
            "role": role
        }
        return users_schema.dump(user_service.get_all(data))

    @auth_required
    def delete(self, user_id: int):
        user_service.delete(user_id)
        return "", 204

    @auth_required
    def patch(self, user_id: int):
        req_json = request.json
        user_service.update(req_json, user_id)
        return "", 204

#А зачем два раза пароль отправлять?
@user_ns.route('/password')
class UsersView(Resource):
    @auth_required
    def put(self, user_id: int):
        data = request.json
        password_1 = data.get("old_password", None)
        password_2 = data.get("new_password", None)
        if None in [password_1, password_2]:
            abort(400)
        user = user_service.get_one(user_id)
        if not user or not compare_passwords(user.password, password_1):
            abort(401)
        user_service.update_password({'password': password_2}, user_id)
        return "", 204


@users_ns.route('/<int:uid>')
class UserView(Resource):
    @admin_required
    def get(self, user_id, uid):
        return make_response(jsonify(user_schema.dump(user_service.get_one(uid))), 200)





