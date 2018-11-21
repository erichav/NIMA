from flask import Flask
from flask_restful import Api
from nima.common.database import Database
from nima.resources.obra import Obras
from nima.resources.obra import Obra
from nima.resources.producto import Producto
from nima.resources.producto import Productos
from nima.resources.trabajador import Trabajador
from nima.resources.trabajador import Trabajadores

def create_app():
    app = Flask(__name__,static_url_path='/nima/static')
    api = Api(app)

    api.add_resource(Obras, '/obras')
    api.add_resource(Obra,'/obra', '/obra/<string:id_obra>')
    api.add_resource(Producto, '/producto', '/producto/<string:id_producto>')
    api.add_resource(Productos, '/productos')
    api.add_resource(Trabajador, '/trabajador', '/trabajador/<string:id_trabajador>')
    api.add_resource(Trabajadores, '/trabajadores')



    @app.route('/')
    def root():
        return app.send_static_file('index.html')

    @app.before_first_request
    def init_db():
        Database.initialize()



    return app
