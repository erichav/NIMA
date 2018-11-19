from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__,static_url_path='/nima/static')
    # api = Api(app)

    @app.route('/')
    def root():
        return app.send_static_file('index.html')
    return app
