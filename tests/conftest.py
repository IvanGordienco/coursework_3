import pytest
from flask import current_app

from project.config import TestingConfig, DevelopmentConfig
from project.server import create_app
from project.setup_db import db as database
from project.tools.functions import create_tables_
from tests.services.test_genres_service import genre_dao_test
#Делаем импорт в конфтест для использования в проекте

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture()
def db(app):
    database.init_app(app)
    create_tables_("Fixtures", current_app.config['JSON_PATH'])
    yield database
    database.session.rollback()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client
