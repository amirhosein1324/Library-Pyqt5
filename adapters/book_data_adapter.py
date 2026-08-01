import datetime

from models.book import Book
from adapters.db import get_connection

from adapters.author_data_adapter import AuthorDataAdapter
from adapters.publisher_data_adapter import PublisherDataAdapter
from adapters.category_data_adapter import CategoryDataAdapter
from adapters.language_data_adapter import LanguageDataAdapter
from adapters.designer_data_adapter import DesignerDataAdapter
from adapters.translator_data_adapter import TranslatorDataAdapter
from adapters.resource_data_adapter import ResourcesDataAdapter

_BASE_SELECT = """
    SELECT books.id, books.title, books.product_code, books.age_group,
           books.publisher_id, books.release_date, books.price,
           author_id, category_id, designer_id, language_id, translator_id, resource_id
    FROM books
    LEFT JOIN book_author ON book_author.book_id = books.id
    LEFT JOIN book_category ON book_category.book_id = books.id
    LEFT JOIN book_designer ON book_designer.book_id = books.id
    LEFT JOIN book_language ON book_language.book_id = books.id
    LEFT JOIN book_translator ON book_translator.book_id = books.id
    LEFT JOIN resources_book ON resources_book.book_id = books.id
"""


def _append_unique(items: list, item):
    if item is not None and item not in items:
        items.append(item)


def _in_clause(column: str, ids: list[int]):
    if not ids:
        return "1 = 0", []
    placeholders = ",".join("?" * len(ids))
    return f"{column} IN ({placeholders})", list(ids)


class BookDataAdapter:

    @staticmethod
    def _rows_to_books(rows) -> list[Book]:
        categories = {c.id: c for c in CategoryDataAdapter.get_all()}
        authors = {a.id: a for a in AuthorDataAdapter.get_all()}
        publishers = {p.id: p for p in PublisherDataAdapter.get_all()}
        languages = {l.id: l for l in LanguageDataAdapter.get_all()}
        designers = {d.id: d for d in DesignerDataAdapter.get_all()}
        translators = {t.id: t for t in TranslatorDataAdapter.get_all()}
        resources = {r.id: r for r in ResourcesDataAdapter.get_all()}

        books_by_id: dict[int, Book] = {}
        order: list[int] = []

        for row in rows:
            book_id = row[0]
            if book_id not in books_by_id:
                books_by_id[book_id] = Book(
                    id=book_id,
                    title=row[1],
                    product_code=row[2],
                    categories=[],
                    age_group=row[3],
                    authors=[],
                    publisher=publishers.get(row[4]),
                    release_date=datetime.date.fromisoformat(row[5]),
                    price=row[6],
                    languages=[],
                    cover_designers=[],
                    translators=[],
                    resources=[],
                )
                order.append(book_id)

            book = books_by_id[book_id]
            _append_unique(book.authors, authors.get(row[7]))
            _append_unique(book.categories, categories.get(row[8]))
            _append_unique(book.cover_designers, designers.get(row[9]))
            _append_unique(book.languages, languages.get(row[10]))
            _append_unique(book.translators, translators.get(row[11]))
            _append_unique(book.resources, resources.get(row[12]))

        return [books_by_id[book_id] for book_id in order]

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute(_BASE_SELECT).fetchall()
        return BookDataAdapter._rows_to_books(rows)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM books WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            connection.execute("DELETE FROM book_author WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM book_category WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM book_language WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM book_designer WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM book_translator WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM resources_book WHERE book_id = ?;", (id,))
            connection.execute("DELETE FROM books WHERE id = ?;", (id,))
        return True

    @staticmethod
    def insert(book: Book):
        with get_connection() as connection:
            cursor = connection.execute(
                """INSERT INTO books (title, product_code, age_group, publisher_id, release_date, price)
                   VALUES (?, ?, ?, ?, ?, ?);""",
                (book.title, book.product_code, book.age_group, book.publisher.id,
                 str(book.release_date), book.price),
            )
            book_id = cursor.lastrowid

            for author in book.authors:
                connection.execute(
                    "INSERT INTO book_author (book_id, author_id) VALUES (?, ?);", (book_id, author.id))
            for category in book.categories:
                connection.execute(
                    "INSERT INTO book_category (book_id, category_id) VALUES (?, ?);", (book_id, category.id))
            for designer in book.cover_designers:
                connection.execute(
                    "INSERT INTO book_designer (book_id, designer_id) VALUES (?, ?);", (book_id, designer.id))
            for language in book.languages:
                connection.execute(
                    "INSERT INTO book_language (book_id, language_id) VALUES (?, ?);", (book_id, language.id))
            for translator in book.translators:
                connection.execute(
                    "INSERT INTO book_translator (book_id, translator_id) VALUES (?, ?);", (book_id, translator.id))
            for resource in book.resources:
                connection.execute(
                    "INSERT INTO resources_book (book_id, resource_id) VALUES (?, ?);", (book_id, resource.id))

    @staticmethod
    def search(name: str = "", author_name: str = "", publisher_name: str = "", category_name: str = "",
               language_name: str = "", designer_name: str = "", translator_name: str = "", resource_name: str = ""):

        publisher_ids = [p.id for p in (
            PublisherDataAdapter.search(publisher_name) if publisher_name else PublisherDataAdapter.get_all())]
        author_ids = [a.id for a in (
            AuthorDataAdapter.search(author_name) if author_name else AuthorDataAdapter.get_all())]
        category_ids = [c.id for c in (
            CategoryDataAdapter.search(category_name) if category_name else CategoryDataAdapter.get_all())]
        language_ids = [l.id for l in (
            LanguageDataAdapter.search(language_name) if language_name else LanguageDataAdapter.get_all())]
        designer_ids = [d.id for d in (
            DesignerDataAdapter.search(designer_name) if designer_name else DesignerDataAdapter.get_all())]
        translator_ids = [t.id for t in (
            TranslatorDataAdapter.search(translator_name) if translator_name else TranslatorDataAdapter.get_all())]
        resource_ids = [r.id for r in (
            ResourcesDataAdapter.search(resource_name) if resource_name else ResourcesDataAdapter.get_all())]

        clauses = ["books.title LIKE ?"]
        params: list = [f"%{name}%"]

        for column, ids in (
            ("author_id", author_ids), ("publisher_id", publisher_ids), ("category_id", category_ids),
            ("designer_id", designer_ids), ("language_id", language_ids),
            ("translator_id", translator_ids), ("resource_id", resource_ids),
        ):
            clause, clause_params = _in_clause(column, ids)
            clauses.append(clause)
            params.extend(clause_params)

        sql = _BASE_SELECT + " WHERE " + " AND ".join(clauses)

        with get_connection() as connection:
            rows = connection.execute(sql, params).fetchall()

        return BookDataAdapter._rows_to_books(rows)