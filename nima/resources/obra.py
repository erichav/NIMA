from flask_restful import Resource, reqparse
from nima.models.obras.obra import Obra as ObraModel
from nima.models.baseError import DocumentDoesNotExist
from nima.common.response import Response


class Obra(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('nombre',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('ubicacion',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )
    parser.add_argument('comentarios',
                        type=str,
                        required=True,
                        help="Este campo no puede ser dejado en blanco."
                        )

    def post(self):
        data = Obra.parser.parse_args()
        return ObraModel.post(data).json()

    def get(self, id_obra):
        try:
            return ObraModel.get(id_obra).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def delete(self, id_obra):
        try:
            ObraModel.remove(id_obra)
            return Response(message="La obra fue eliminada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404

    def put(self, id_obra):
        data = Obra.parser.parse_args()
        try:
            ObraModel.update(id_obra, data)
            return Response(message="La obra fue actualizada con exito",success=True).json(), 200
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404


class Obras(Resource):
    def get(self):
        try:
            return [obra.json() for obra in ObraModel.get()]
        except DocumentDoesNotExist as e:
            return Response(message=e.message).json(), 404
