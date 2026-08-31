import datetime


class CoverDesigner:

    def __init__(self, id: int, name: str, birthdate: datetime.date, nationality: str):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.nationality = nationality

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        if isinstance(other, CoverDesigner):
            return self.id == other.id
        return NotImplemented