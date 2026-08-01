import datetime

from models.designer import CoverDesigner
from adapters.db import get_connection


class DesignerDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, birthdate, nationality FROM cover_designers;").fetchall()
        return [CoverDesigner(row[0], row[1], datetime.date.fromisoformat(row[2]), row[3]) for row in rows]

    @staticmethod
    def insert(designer: CoverDesigner):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO cover_designers (name, birthdate, nationality) VALUES (?, ?, ?);",
                (designer.name, str(designer.birthdate), designer.nationality))
            new_id = cursor.lastrowid
        return CoverDesigner(new_id, designer.name, designer.birthdate, designer.nationality)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM cover_designers WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM book_designer WHERE designer_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM cover_designers WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name, birthdate, nationality FROM cover_designers WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [CoverDesigner(row[0], row[1], row[2], row[3]) for row in rows]