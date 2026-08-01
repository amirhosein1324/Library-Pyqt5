class Publisher:

    def __init__(self, id: int, name: str, address: str, website: str):
        self.id = id
        self.name = name
        self.address = address
        self.website = website

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        if isinstance(other, Publisher):
            return self.id == other.id
        return NotImplemented