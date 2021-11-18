import os

from flask import Flask
from dotenv import load_dotenv
from .routes.v1.__init__ import configure_routes
from flask_restful import Api
import traceback

load_dotenv()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.errorhandler(500)
    def internal_error(exception):
        print("500 error caught")
        print(traceback.format_exc())

    configure_routes(api)

    return app
