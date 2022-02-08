import os

import pytest

from implemented import genre_service
from tests.acess_ import access_token


class TestGenresView:
    url = "/genres/"

    def test_get_genres(self, client):
        response = client.get(self.url, headers={'Authorization': access_token})
        assert response.status_code == 200
        genre = genre_service.get_one(1)
        assert genre.name == 'Комедия'

    def test_update(self, client):
        genre_d = {
            "name": "Dan2"
        }
        response = client.post(self.url, headers={'Authorization': access_token}, json=genre_d)
        genre_ = genre_service.get_one(19)
        genres_all = genre_service.get_all()
        assert response.status_code == 201
        assert genre_.name == 'Dan2', f'genre.name должен быть равно Dan2, но он равен {genre_.name},{len(genres_all)}'


class TestGenreView:
    url = "/genres/{genre_id}"
    def test_get_without_autorize(self, client):
        response = client.get(self.url.format(genre_id=1))
        assert response.status_code == 401

    def test_get_genre(self, client):
        genre = genre_service.get_one(1)
        response = client.get(self.url.format(genre_id=genre.id), headers={'Authorization': access_token})
        assert response.status_code == 200
        assert response.json == {"id": genre.id, "name": genre.name}

    def test_genre_not_found(self, client):
        response = client.get(self.url.format(genre_id='asda'), headers={'Authorization': access_token})
        assert response.status_code == 404


if __name__ == "__main__":
    os.system("pytest")
