from models.category import Category
from adapters.db import get_connection


class CategoryDataAdapter:

    @staticmethod
    def get_all():
        with get_connection() as connection:
            rows = connection.execute("SELECT id, name FROM categories;").fetchall()
        return [Category(row[0], row[1]) for row in rows]

    @staticmethod
    def insert(category: Category):
        with get_connection() as connection:
            cursor = connection.execute(
                "INSERT INTO categories (name) VALUES (?);", (category.name,))
            new_id = cursor.lastrowid
        return Category(new_id, category.name)

    @staticmethod
    def delete(id: int):
        with get_connection() as connection:
            exists = connection.execute(
                "SELECT id FROM categories WHERE id = ?;", (id,)).fetchone()
            if not exists:
                return False

            in_use = connection.execute(
                "SELECT 1 FROM book_category WHERE category_id = ? LIMIT 1;", (id,)).fetchone()
            if in_use:
                return False

            connection.execute("DELETE FROM categories WHERE id = ?;", (id,))
        return True

    @staticmethod
    def search(name: str = ""):
        with get_connection() as connection:
            rows = connection.execute(
                "SELECT id, name FROM categories WHERE name LIKE ?;",
                (f"%{name}%",)).fetchall()
        return [Category(row[0], row[1]) for row in rows]