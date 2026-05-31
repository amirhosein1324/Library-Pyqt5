import models.model as model
import sqlite3
import re
import json
import datetime

from models.category import Category
from models.author import Author
from models.publisher import Publisher
from models.language import Language
from models.designer import CoverDesigner
from models.translator import Translator
from models.resource import Resources
from models.book import Book

publisher = Publisher(1, "ali", "alsas", "wfmwf")
category = Category(1, "fiction")
author = Author(1, "ali", datetime.datetime.today(), "british")
language = Language(1, "engrghr")
designer = CoverDesigner(1, "ali", datetime.datetime.today(), "scsd")
trans = Translator(1, "ali", [language])
resource = Resources(1, "als")
book = Book(1, "tkjgb", 1001, [category], "adult", [
            author], publisher, datetime.datetime.today(), 50, [language], [designer], [trans], [resource])
