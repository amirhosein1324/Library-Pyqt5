from models.language import Language
from adapters.db import get_connection


class LanguageDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute("SELECT id, name FROM languages;").fetchall()
        return [Language(row[0], row[1]) for row in rows]

    @staticmethod
    def insert(language: Language):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO languages (name) VALUES (?);", (language.name,))
            new_id = cursor.lastrowid
        return Language(new_id, language.name)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM languages WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM book_language WHERE language_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM languages WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name FROM languages WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Language(row[0], row[1]) for row in rows]