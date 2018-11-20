from flask import Flask
from flask_restful import Api
from nima.common.database import Database


def create_app():
    app = Flask(__name__,static_url_path='/nima/static')
    # api = Api(app)

    @app.route('/')
    def root():
        return app.send_static_file('index.html')

    @app.route('/add')
    def add():
        Database.insert('users', {'name': 'Pablo'})
        return "user added"

    @app.before_first_request
    def init_db():
        Database.initialize()



    return app
