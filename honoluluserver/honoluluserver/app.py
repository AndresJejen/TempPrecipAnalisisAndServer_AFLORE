from flask import Flask

from honoluluserver.rest import hololuluwheather
from honoluluserver.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(hololuluwheather.blueprint)
    return app