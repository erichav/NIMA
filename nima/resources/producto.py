from flask_restful import reqparse, Resource
from nima.models.productos.producto import Producto as ProductoModel
from nima.models.baseError import DocumentDoesNotExist
from nima.common.response import Response

class Producto(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nombre',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('cantidad',
                        type=int,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('observaciones',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )

    def post(self):
        data = Producto.parser.parse_args()
        return ProductoModel.post(data).json()

    def get(self, id_producto):
        try:
            return ProductoModel.get(id_producto).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def delete(self, id_producto):
        try:
            ProductoModel.remove(id_producto)
            return Response(message="El producto fue eliminada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def put(self, id_producto):
        data = Producto.parser.parse_args()
        try:
            ProductoModel.update(id_producto, data)
            return Response(message="El producto fue actualizada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

class Productos(Resource):
    def get(self):
        try:
            return [producto.json() for producto in ProductoModel.get()]
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404