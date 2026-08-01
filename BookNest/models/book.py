import datetime

from models.category import Category
from models.author import Author
from models.publisher import Publisher
from models.language import Language
from models.designer import CoverDesigner
from models.translator import Translator
from models.resource import Resources


class Book:

    def __init__(self, id: int, title: str, product_code: int, categories: list[Category],
                 age_group: str, release_date: datetime.date, authors: list[Author], price: int,
                 languages: list[Language], publisher: Publisher, cover_designers: list[CoverDesigner],
                 translators: list[Translator], resources: list[Resources]):
        self.id = id
        self.title = title
        self.product_code = product_code
        self.categories = categories
        self.age_group = age_group
        self.release_date = release_date
        self.authors = authors
        self.price = price
        self.languages = languages
        self.publisher = publisher
        self.cover_designers = cover_designers
        self.translators = translators
        self.resources = resources

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        if isinstance(other, Book):
            return self.id == other.id
        return NotImplemented
