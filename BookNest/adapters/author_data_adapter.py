import datetime

from models.author import Author
from adapters.db import get_connection


class AuthorDataAdapter:

    @staticmethod
    def update(id: int, name: str, birthdate: datetime.date, nationality: str):
        with get_connection() as connection:
            connection.execute(
                "UPDATE authors SET name = ?, birthdate = ?, nationality = ? WHERE id = ?;",
                (name, str(birthdate), nationality, id))

    @staticmethod
    def get_one(id: int):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, birthdate, nationality FROM authors WHERE id = ?;", (id,)).fetchall()
        return [Author(row[0], row[1], row[2], row[3]) for row in rows]

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, birthdate, nationality FROM authors;").fetchall()
        return [Author(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in rows]

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM authors WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT author_id FROM book_author WHERE author_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM authors WHERE id = ?;", (id,))
        return True

    @staticmethod
    def insert(author: Author):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO authors (name, birthdate, nationality) VALUES (?, ?, ?);",
                (author.name, str(author.birthdate), author.nationality))
            new_id = cursor.lastrowid
        return Author(new_id, author.name, author.birthdate, author.nationality)

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, birthdate, nationality FROM authors WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Author(row[0], row[1], row[2], row[3]) for row in rows]