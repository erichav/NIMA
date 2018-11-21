from nima.models.baseModel import BaseModel
from nima.common.database import Database
from nima.models.trabajadores.constants import COLLECTION
from nima.models.obras.obra import Obra as ObraModel

class Trabajador(BaseModel):
    def __init__(self, obra, nombre, rol, no_cuenta, nss, _id=None):
        self.obra = obra
        self.nombre = nombre
        self.rol = rol
        self.no_cuenta = no_cuenta
        self.nss = nss
        super().__init__(_id)

    @classmethod
    def get(cls, id_trabajador=None):
        if not id_trabajador:
            data_trabajador = Database.find(COLLECTION,{})
            return [cls(**trabajador) for trabajador in data_trabajador]
        data_trabajador = Database.find_one(COLLECTION, {"_id": id_trabajador})
        return cls(**data_trabajador)

    @classmethod
    def post(cls, data: dict):
        ObraModel.get(data['obra'])
        trabajador = cls(**data)
        Database.insert(COLLECTION, trabajador.json())
        return trabajador

    @classmethod
    def remove(cls, id_trabajador):
        cls.get(id_trabajador)
        Database.remove(COLLECTION, {'_id': id_trabajador})

    @classmethod
    def update(cls, id_trabajador, data: dict):
        ObraModel.get(data['obra'])
        trabajador = cls.get(id_trabajador)
        Database.update(COLLECTION, {'_id': id_trabajador}, data)
        return trabajador