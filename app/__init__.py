from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    if app.config["SECURE_HEADERS"]:
        from flask_talisman import Talisman

        Talisman(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app
