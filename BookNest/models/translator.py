from models.language import Language


class Translator:

    def __init__(self, id: int, name: str, languages: list[Language]):
        self.id = id
        self.name = name
        self.languages = languages

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        if isinstance(other, Translator):
            return self.id == other.id
        return NotImplemented