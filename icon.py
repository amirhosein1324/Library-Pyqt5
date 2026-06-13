import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from styles import APP_STYLE


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
        self.setGeometry(100, 100, 700, 400)
        self.setup_menu()
        self.setup_central_widget()

    def setup_menu(self):
        menu = self.menuBar()

        book_menu = menu.addMenu("Book")
        member_menu = menu.addMenu("Members")
        Setting_menu = menu.addMenu("Setting")
        help_menu = menu.addMenu("Help")

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

        # Sidebar چپ
        left_panel = QWidget()
        left_panel.setObjectName("left_panel")
        left_panel.setFixedWidth(70)

        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 10, 0, 10)
        left_layout.setSpacing(10)
        left_layout.setAlignment(Qt.AlignTop)

        self.btn_authors = QPushButton()
        self.btn_authors.setIcon(QIcon("icons/authors.png"))  # مسیر آیکن خودت
        self.btn_authors.setIconSize(QSize(24, 24))
        self.btn_authors.setFixedSize(50, 50)
        self.btn_authors.setToolTip("Authors")

        self.btn_books = QPushButton()
        self.btn_books.setIcon(QIcon("icons/books.png"))  # مسیر آیکن خودت
        self.btn_books.setIconSize(QSize(24, 24))
        self.btn_books.setFixedSize(50, 50)
        self.btn_books.setToolTip("Books")

        left_layout.addWidget(self.btn_authors, alignment=Qt.AlignHCenter)
        left_layout.addWidget(self.btn_books, alignment=Qt.AlignHCenter)
        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)

        self.stack = QStackedWidget()

        self.author_page = AuthorPage()
        self.book_page = BookPage()

        self.stack.addWidget(self.author_page)
        self.stack.addWidget(self.book_page)

        right_layout.addWidget(self.stack)

        self.btn_authors.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_books.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys

app = QApplication(sys.argv)

window = QWidget()
layout = QVBoxLayout(window)

button = QPushButton("Click Me")
button.setIcon(QIcon("home-lg-alt.svg"))
layout.addWidget(button)

window.show()
sys.exit(app.exec_())