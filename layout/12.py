import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize

from styles import APP_STYLE
from PyQt5.QtGui import QIcon
class AuthorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("author_page")
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(12)
        layout.setVerticalSpacing(12)

        name_label = QLabel("Name :")
        family_label = QLabel("Family :")
        activacheckbox_label = QLabel("Activate :")

        self.name_input = QLineEdit()
        self.name_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.name_input.setFixedHeight(250)

        self.family_input = QLineEdit()
        self.family_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.family_input.setFixedHeight(250)

        self.checkbox = QCheckBox()

        self.btn_send = QPushButton("Add Author")
        self.btn_send.setObjectName("btn_send")

        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.name_input, 0, 1)
        layout.addWidget(family_label, 1, 0)
        layout.addWidget(self.family_input, 1, 1)
        layout.addWidget(activacheckbox_label, 2, 0)
        layout.addWidget(self.checkbox, 2, 1)
        layout.addWidget(self.btn_send, 3, 1)
        layout.setRowStretch(4, 1)


from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QFrame, QSizePolicy
)
from PyQt5.QtCore import Qt

class BookPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("book_page")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        # Search bar
        search_layout = QHBoxLayout()
        search_label = QLabel("Search:")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search books...")
        self.search_input.textChanged.connect(self.filter_books)

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)

        # Scroll area for books
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.books_container = QWidget()
        self.books_layout = QVBoxLayout(self.books_container)
        self.books_layout.setAlignment(Qt.AlignTop)
        self.books_layout.setSpacing(10)

        self.scroll_area.setWidget(self.books_container)

        # Add-book form
        form_frame = QFrame()
        form_layout = QGridLayout(form_frame)
        form_layout.setHorizontalSpacing(12)
        form_layout.setVerticalSpacing(12)

        book_title_label = QLabel("Book Title :")
        author_label = QLabel("Author :")
        publisher_label = QLabel("Publisher :")

        self.book_title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.publisher_input = QLineEdit()

        self.btn_add_book = QPushButton("Add Book")
        self.btn_add_book.setObjectName("btn_add_book")

        form_layout.addWidget(book_title_label, 0, 0)
        form_layout.addWidget(self.book_title_input, 0, 1)
        form_layout.addWidget(author_label, 1, 0)
        form_layout.addWidget(self.author_input, 1, 1)
        form_layout.addWidget(publisher_label, 2, 0)
        form_layout.addWidget(self.publisher_input, 2, 1)
        form_layout.addWidget(self.btn_add_book, 3, 1)

        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.scroll_area)
        main_layout.addWidget(form_frame)


def set_books(self, books):
    # clear old widgets
    while self.books_layout.count():
        item = self.books_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

    self.all_books = books

    for book in books:
        label = QLabel(f"{book['title']} - {book['author']} - {book['publisher']}")
        label.setStyleSheet("padding: 8px; border: 1px solid #ccc; border-radius: 6px;")
        self.books_layout.addWidget(label)


class BookPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("book_page")
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(12)
        layout.setVerticalSpacing(12)

        book_title_label = QLabel("Book Title :")
        author_label = QLabel("Author :")
        publisher_label = QLabel("Publisher :")

        self.book_title_input = QLineEdit()
        self.book_title_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.book_title_input.setFixedHeight(25)

        self.author_input = QLineEdit()
        self.author_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.author_input.setFixedHeight(25)

        self.publisher_input = QLineEdit()
        self.publisher_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.publisher_input.setFixedHeight(25)

        self.btn_add_book = QPushButton("Add Book")
        self.btn_add_book.setObjectName("btn_add_book")

        layout.addWidget(book_title_label, 0, 0)
        layout.addWidget(self.book_title_input, 0, 1)
        layout.addWidget(author_label, 1, 0)
        layout.addWidget(self.author_input, 1, 1)
        layout.addWidget(publisher_label, 2, 0)
        layout.addWidget(self.publisher_input, 2, 1)
        layout.addWidget(self.btn_add_book, 3, 1)
        layout.setRowStretch(4, 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 500)
        self.setup_menu()
        self.setup_central_widget()

    def setup_menu(self):
        menu = self.menuBar()

        book_menu = menu.addMenu("Book")
        member_menu = menu.addMenu("Members")
        Setting_menu = menu.addMenu("Setting")
        help_menu =menu.addMenu("Help")

        book_menu.addAction(QAction("Add", self))
        book_menu.addAction(QAction("Edit", self))
        book_menu.addAction(QAction("Delete", self))
        book_menu.addAction(QAction("Search", self))

        member_menu.addAction(QAction("Add", self))
        member_menu.addAction(QAction("Edit", self))
        member_menu.addAction(QAction("Delete", self))
        member_menu.addAction(QAction("Search", self))

        Setting_menu.addAction(QAction("Theme", self))
        Setting_menu.addAction(QAction("Notification", self))

        help_menu.addAction(QAction("Setting", self))
        help_menu.addAction(QAction("FAQ", self))

        exit_action = QAction("Exit", self)
        help_menu.addAction(exit_action)
        exit_action.triggered.connect(self.close)

    def setup_central_widget(self):
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        left_panell = QWidget()
        left_panell.setObjectName("left_panell")
        left_panell.setFixedWidth(50)
        left_layout2 = QVBoxLayout(left_panell)
        left_layout2.setContentsMargins(0, 7, 2, 0)
        left_layout2.setSpacing(0)
        button_book = QPushButton("")
        button_book.setIcon(QIcon("img/book(w).svg"))

        button_user = QPushButton("")
        button_user.setIcon(QIcon("img/user(w).svg"))

        button_author = QPushButton("")
        button_author.setIcon(QIcon("img/pencil-alt(W).svg"))

        button_publisher = QPushButton("")
        button_publisher.setIcon(QIcon("img/newspaper(W).svg"))

        button_trans = QPushButton("")
        button_trans.setIcon(QIcon("img/earth-americas(W).svg"))

        button_language = QPushButton("")
        button_language.setIcon(QIcon("img/language(W).svg"))

        button_category = QPushButton("")
        button_category.setIcon(QIcon("img/layer-group(W).svg"))

        button_designer = QPushButton("")
        button_designer.setIcon(QIcon("img/compass-drafting(W).svg"))

        button_resources = QPushButton("")
        button_resources.setIcon(QIcon("img/file-brackets-curly(W).svg"))


        left_layout2.addWidget(button_book)
        left_layout2.addWidget(button_user)
        left_layout2.addWidget(button_author)
        left_layout2.addWidget(button_publisher)
        left_layout2.addWidget(button_trans)
        left_layout2.addWidget(button_language)
        left_layout2.addWidget(button_category)
        left_layout2.addWidget(button_designer)
        left_layout2.addWidget(button_resources)

        left_layout2.addStretch()

        left_panel = QWidget()
        left_panel.setObjectName("left_panel")
        left_panel.setFixedWidth(140)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 7, 2, 0)
        left_layout.setSpacing(0)

        self.btn_authors = QPushButton("Authors")
        self.btn_books = QPushButton("Books")

        left_layout.addWidget(self.btn_authors)
        left_layout.addWidget(self.btn_books)
        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget()

        self.author_page = AuthorPage()
        self.book_page = BookPage()

        # self.stack.addWidget(self.author_page)
        # self.stack.addWidget(self.book_page)

        right_layout.addWidget(self.stack)

        self.btn_authors.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_books.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        main_layout.addWidget(left_panell)
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
