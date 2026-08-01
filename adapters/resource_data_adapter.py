from models.resource import Resources
from adapters.db import get_connection


class ResourcesDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute("SELECT id, name FROM resources;").fetchall()
        return [Resources(row[0], row[1]) for row in rows]

    @staticmethod
    def insert(resource: Resources):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO resources (name) VALUES (?);", (resource.name,))
            new_id = cursor.lastrowid
        return Resources(new_id, resource.name)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM resources WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM resources_book WHERE resource_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM resources WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name FROM resources WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Resources(row[0], row[1]) for row in rows]