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

import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter
import adapters.book_data_adapter as  BookDataAdapter

publisher = Publisher(1, "ali", "alsas", "wfmwf")
category = Category(1, "fiction")
author = Author(1, "ali", datetime.datetime.today(), "british")
language = Language(1, "engrghr")
designer = CoverDesigner(1, "ali", datetime.datetime.today(), "scsd")
trans = Translator(1, "ali", [language])
resource = Resources(1, "als")
book = Book(1, "tkjgb", 1001, [category], "adult", [
            author], publisher, datetime.datetime.today(), 50, [language], [designer], [trans], [resource])
print(BookDataAdapter.BookDataAdapter.search(name="the"))
