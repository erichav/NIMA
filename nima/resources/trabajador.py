from flask_restful import Resource, reqparse
from nima.models.trabajadores.trabajador import Trabajador as TrabajadorModel
from nima.models.baseError import DocumentDoesNotExist
from nima.common.response import Response

class Trabajador(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('obra',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('nombre',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('rol',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('no_cuenta',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('nss',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    def post(self):
        data = Trabajador.parser.parse_args()
        try:
            return TrabajadorModel.post(data).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def get(self, id_trabajador):
        try:
            return TrabajadorModel.get(id_trabajador).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def delete(self, id_trabajador):
        try:
            TrabajadorModel.remove(id_trabajador)
            return Response(message="El trabajador fue eliminada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def put(self, id_trabajador):
        data = Trabajador.parser.parse_args()
        try:
            TrabajadorModel.update(id_trabajador, data)
            return Response(message="El trabajador fue actualizada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

class Trabajadores(Resource):
    def get(self):
        try:
            return [trabajador.json() for trabajador in TrabajadorModel.get()]
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404
