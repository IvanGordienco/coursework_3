
from project.config import DevelopmentConfig, TestingConfig
from project.dao.models import *  # noqa F401, F403
from project.server import create_app
from project.setup_db import db

app = create_app(TestingConfig)


