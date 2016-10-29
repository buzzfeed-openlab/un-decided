from flask import Flask
from .app_config import DB_USER, DB_PW, DB_HOST, DB_NAME


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{0}:{1}@{2}/{3}".format(DB_USER, DB_PW, DB_HOST, DB_NAME)

    return app