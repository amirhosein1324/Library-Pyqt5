from models.publisher import Publisher
from adapters.db import get_connection


class PublisherDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, address, website FROM publishers;").fetchall()
        return [Publisher(row[0], row[1], row[2], row[3]) for row in rows]

    @staticmethod
    def insert(publisher: Publisher):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO publishers (name, address, website) VALUES (?, ?, ?);",
                (publisher.name, publisher.address, publisher.website))
            new_id = cursor.lastrowid
        return Publisher(new_id, publisher.name, publisher.address, publisher.website)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM publishers WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM books WHERE publisher_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM publishers WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, address, website FROM publishers WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Publisher(row[0], row[1], row[2], row[3]) for row in rows]