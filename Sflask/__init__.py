from flask import Flask

from .view import account
from .view import home


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.DevelopmentConfig')
    app.secret_key = 'jbhjkhjbgjhvghf54535ertdtdfgfhj'
    app.debug = True
    # 绑定蓝图
    app.register_blueprint(account.account)
    app.register_blueprint(home.home)
    return app
