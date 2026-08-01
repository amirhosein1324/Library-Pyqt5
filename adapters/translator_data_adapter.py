from models.translator import Translator
from adapters.db import get_connection
from adapters.language_data_adapter import LanguageDataAdapter


class TranslatorDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, language FROM translators;").fetchall()
        languages = LanguageDataAdapter.get_all()
        return [
            Translator(row[0], row[1], [lang for lang in languages if lang.name == row[2]])
            for row in rows
        ]

    @staticmethod
    def insert(translator: Translator):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO translators (name, language) VALUES (?, ?);",
                (translator.name, translator.languages))
            new_id = cursor.lastrowid
        return Translator(new_id, translator.name, translator.languages)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM translators WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM book_translator WHERE translator_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM translators WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, language FROM translators WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Translator(row[0], row[1], row[2]) for row in rows]