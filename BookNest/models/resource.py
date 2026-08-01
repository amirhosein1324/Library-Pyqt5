class Resources:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        if isinstance(other, int):
            return self.id == other
        if isinstance(other, Resources):
            return self.name == other.name
        return NotImplemented