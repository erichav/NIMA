import uuid

class BaseModel:
    def __init__(self, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self, exclude=None, date_to_string=True):
        if exclude:
            return {
                attrib: [element.json(date_to_string=date_to_string) if not isinstance(element, str) else element for
                         element in self.__getattribute__(attrib)]
                if type(self.__getattribute__(attrib)) is list else self.__getattribute__(attrib)
                for attrib in self.__dict__.keys() if attrib not in exclude}

        return {
            attrib: [element.json(date_to_string=date_to_string) if not isinstance(element, str) else element for
                     element in
                     self.__getattribute__(attrib)]
            if type(self.__getattribute__(attrib)) is list else self.__getattribute__(attrib)
            for attrib in self.__dict__.keys()}