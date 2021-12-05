import os

from flask import Flask
from dotenv import load_dotenv
from .routes.v1.__init__ import configure_routes
from flask_restful import Api
import traceback
from .db.__init__ import connectDatabase

load_dotenv()

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


@app.errorhandler(500)
def internal_error(exception):
    print("500 error caught")
    print(traceback.format_exc())


api = Api(app)
db = connectDatabase(app)
configure_routes(api)


if __name__ == '__main__':
    db.create_all()
    DEBUG_MODE = os.getenv('FLASK_ENV') != 'production'
    app.run(debug=DEBUG_MODE)
