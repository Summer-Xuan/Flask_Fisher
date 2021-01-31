from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure') # flask导入文件
    app.config.from_object('app.setting') # flask导入文件
    register_blueprint(app)
    db.init_app(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)