from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from apps.config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Config
    app.config.from_object(Config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # blueprints
    for module_name in ('app1', 'app2'):
        module = import_module(f'apps.{module_name}.routes')
        app.register_blueprint(module.blueprint)

    return app
