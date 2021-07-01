import os
from flask import Flask


def create_app():
    template_dir = os.path.abspath('./app/templates/')
    static_dir = os.path.abspath('./app/static/')
    app = Flask(__name__,
        template_folder=template_dir,
        static_folder=static_dir)

    from app.mod_main.routes import main

    app.register_blueprint(main)
    return app
