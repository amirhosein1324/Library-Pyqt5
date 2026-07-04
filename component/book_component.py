import sqlite3

class LibraryDB:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_books(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM Book
            ORDER BY BookTitle
        """)

        books = [dict(row) for row in cur.fetchall()]
        conn.close()

        return books
    class BookPage(QWidget):


    def set_books(self, books):

        while self.books_layout.count():
            item = self.books_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.all_books = books

        for book in books:

            frame = QFrame()
            frame.setStyleSheet("""
                QFrame{
                    border:1px solid gray;
                    border-radius:5px;
                    padding:5px;
                }
            """)

            layout = QVBoxLayout(frame)

            layout.addWidget(QLabel(f"Title : {book['BookTitle']}"))
            layout.addWidget(QLabel(f"Author : {book['AuthorName']}"))
            layout.addWidget(QLabel(f"Publisher : {book['PublisherName']}"))

            self.books_layout.addWidget(frame)