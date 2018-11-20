from nima.models.baseModel import BaseModel
from nima.common.database import Database
from nima.models.obras.constants import COLLECTION


class Obra(BaseModel):
    def __init__(self, nombre, ubicacion, comentarios, _id=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.comentarios = comentarios
        super().__init__(_id)


    @classmethod
    def get(cls, id_obra=None):
        if not id_obra:
            data_obra = Database.find(COLLECTION,{})
            return [cls(**obra) for obra in data_obra]
        data_obra = Database.find_one(COLLECTION, {"_id": id_obra})
        return cls(**data_obra)

    @classmethod
    def post(cls, data: dict):
        obra = cls(**data)
        Database.insert(COLLECTION, obra.json())
        return obra

    @classmethod
    def remove(cls, id_obra):
        cls.get(id_obra)
        Database.remove(COLLECTION, {'_id': id_obra})

    @classmethod
    def update(cls, id_obra, data: dict):
        obra = cls.get(id_obra)
        Database.update(COLLECTION, {'_id': id_obra}, data)
        return obra
