from nima.common.database import Database
from nima.models.baseModel import BaseModel
from nima.models.productos.constants import COLLECTION

class Producto(BaseModel):

    def __init__(self, nombre, cantidad, observaciones, _id=None):
        self.nombre = nombre
        self.cantidad = cantidad
        self.observaciones = observaciones
        super().__init__(_id)

    @classmethod
    def get(cls, id_producto=None):
        if not id_producto:
            data_producto = Database.find(COLLECTION,{})
            return [cls(**producto) for producto in data_producto]
        data_producto = Database.find_one(COLLECTION, {"_id": id_producto})
        return cls(**data_producto)

    @classmethod
    def post(cls, data: dict):
        producto = cls(**data)
        Database.insert(COLLECTION, producto.json())
        return producto

    @classmethod
    def remove(cls, id_producto):
        cls.get(id_producto)
        Database.remove(COLLECTION, {"_id": id_producto})

    @classmethod
    def update(cls, id_producto, data: dict):
        producto = cls.get(id_producto)
        Database.update(COLLECTION, {'_id': id_producto}, data)
        return producto