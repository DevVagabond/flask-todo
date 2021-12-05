from flask_sqlalchemy import SQLAlchemy
from .model.task_model import initiateTaskModel
from flask_migrate import Migrate

models = {}


def connectDatabase(app):
    global models
    DB = SQLAlchemy(app)
    Migrate(app, DB)
    DB.create_all()
    models['DB'] = DB
    models['TaskModel'] = initiateTaskModel(DB)
    return DB


def getDbModels():
    global models
    return models
