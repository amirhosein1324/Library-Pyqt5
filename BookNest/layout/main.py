import os
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QAction, QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget, QButtonGroup,
)

from layout.styles.styles import APP_STYLE

from component.book.book_menu import BookWin
from component.book.Book_form import BookForm
from component.author.Author_menu import AuthorWin
from component.author.Author_form import AuthorForm
from component.category.Catergory_menu import CategoryWin
from component.category.category_form import CategoryForm
from component.designer.Designer_menu import DesignerWin
from component.designer.designer_form import DesignerForm
from component.language.Language_menu import LanguageWin
from component.language.language_form import LanguageForm
from component.publisher.Publisher_menu import PublisherWin
from component.publisher.publisher_form import PublisherForm
from component.resource.Resource_menu import ResourceWin
from component.resource.resource_form import ResourceForm
from component.translator.Translator_menu import TranslatorWin
from component.translator.translator_form import TransForm

_ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

_ENTITY_PAGES = [
    ("pencil-alt", "Authors", AuthorWin, AuthorForm),
    ("newspaper", "Publishers", PublisherWin, PublisherForm),
    ("earth-americas", "Translators", TranslatorWin, TransForm),
    ("language", "Languages", LanguageWin, LanguageForm),
    ("layer-group", "Categories", CategoryWin, CategoryForm),
    ("compass-drafting", "Cover Designers", DesignerWin, DesignerForm),
    ("file-brackets-curly", "Resources", ResourceWin, ResourceForm),
]


def _icon(file_name: str) -> QIcon:
    return QIcon(os.path.join(_ICON_DIR, file_name))


class _NavButton(QPushButton):


    def __init__(self, icon_base: str, tooltip: str = ""):
        super().__init__()
        self.setObjectName("navButton")
        self.setCheckable(True)
        self.setIconSize(QSize(20, 20))
        self.setCursor(Qt.PointingHandCursor)
        if tooltip:
            self.setToolTip(tooltip)
        self._normal_icon = _icon(f"{icon_base}.svg")
        self._active_icon = _icon(f"{icon_base}(W).svg")
        self.setIcon(self._normal_icon)
        self.toggled.connect(self._on_toggled)

    def _on_toggled(self, checked: bool):
        self.setIcon(self._active_icon if checked else self._normal_icon)


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
        setting_menu = menu.addMenu("Setting")
        help_menu = menu.addMenu("Help")

        for label in ("Add", "Edit", "Delete", "Search"):
            book_menu.addAction(QAction(label, self))
            member_menu.addAction(QAction(label, self))

        setting_menu.addAction(QAction("Theme", self))
        setting_menu.addAction(QAction("Notification", self))

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

        icon_bar = self._build_pages()

        left_panel = QWidget()
        left_panel.setObjectName("left_panel")
        left_panel.setFixedWidth(220)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.addWidget(self.left_stack)
        left_layout.addStretch()

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.addWidget(self.right_stack)

        main_layout.addWidget(icon_bar)
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)

    def _build_pages(self) -> QWidget:
        icon_bar = QWidget()
        icon_bar.setObjectName("left_panell")
        icon_bar.setFixedWidth(52)
        icon_layout = QVBoxLayout(icon_bar)
        icon_layout.setContentsMargins(0, 10, 0, 0)
        icon_layout.setSpacing(2)

        self.left_stack = QStackedWidget()
        self.right_stack = QStackedWidget()
        nav_group = QButtonGroup(self)
        nav_group.setExclusive(True)


        book_page = BookWin()
        book_form = BookForm()
        self.left_stack.addWidget(book_page)
        self.right_stack.addWidget(book_form)
        book_page.item_clicked.connect(lambda _name: self.right_stack.setCurrentWidget(book_form))

        book_btn = _NavButton("book", tooltip="Books")
        book_btn.setChecked(True)
        book_btn.clicked.connect(lambda: self.left_stack.setCurrentWidget(book_page))
        nav_group.addButton(book_btn)
        icon_layout.addWidget(book_btn)

   
        user_btn = QPushButton("")
        user_btn.setObjectName("navButton")
        user_btn.setIconSize(QSize(20, 20))
        user_btn.setIcon(_icon("user.svg"))
        user_btn.setToolTip("Members")
        icon_layout.addWidget(user_btn)

        for icon_base, label, page_cls, form_cls in _ENTITY_PAGES:
            page = page_cls()
            form = form_cls(right_stack=self.right_stack)
            page.item_clicked.connect(form.on_item_clicked)

            self.left_stack.addWidget(page)
            self.right_stack.addWidget(form)

            btn = _NavButton(icon_base, tooltip=label)
            btn.clicked.connect(lambda checked=False, p=page: self.left_stack.setCurrentWidget(p))
            nav_group.addButton(btn)
            icon_layout.addWidget(btn)

        icon_layout.addStretch()
        return icon_bar


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())