import os
import datetime

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QListWidget, QListWidgetItem, QAbstractItemView,
    QScrollArea, QMessageBox, QFrame, QSizePolicy,
)

from models.book import Book
from adapters.book_data_adapter import BookDataAdapter
from adapters.author_data_adapter import AuthorDataAdapter
from adapters.publisher_data_adapter import PublisherDataAdapter
from adapters.category_data_adapter import CategoryDataAdapter
from adapters.language_data_adapter import LanguageDataAdapter
from adapters.designer_data_adapter import DesignerDataAdapter
from adapters.translator_data_adapter import TranslatorDataAdapter
from adapters.resource_data_adapter import ResourcesDataAdapter

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_STYLE_PATH = os.path.join(_PROJECT_ROOT, "component", "styles", "formstyles.qss")

_LIST_HEIGHT = 96


class BookForm(QWidget):

    book_saved = pyqtSignal()
    form_cancelled = pyqtSignal()

    def __init__(self, right_stack=None):
        super().__init__()
        self.setObjectName("form")
        self.right_stack = right_stack
        self._editing_book_id = None

        with open(_STYLE_PATH, "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        self._setup_ui()
        self.reset_form()

    def _setup_ui(self):
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setSpacing(0)

        self.header = QLabel("Add New Book")
        self.header.setObjectName("formHeader")
        outer_layout.addWidget(self.header)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)

        content = QWidget()
        content.setObjectName("formContent")
        layout = QVBoxLayout(content)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(18)

        layout.addWidget(self._section_label("Basic Information"))

        self.txt_title = QLineEdit()
        self.txt_title.setPlaceholderText("Book title")
        layout.addLayout(self._field_block("Title", self.txt_title))

        basics_grid = QGridLayout()
        basics_grid.setHorizontalSpacing(16)
        basics_grid.setVerticalSpacing(6)

        self.txt_product_code = QLineEdit()
        self.txt_product_code.setPlaceholderText("e.g. 1234567890123")
        self.txt_price = QLineEdit()
        self.txt_price.setPlaceholderText("Price in Toman")
        self.txt_age_group = QLineEdit()
        self.txt_age_group.setPlaceholderText("e.g. Adult / Teen / Kids")
        self.txt_release_date = QLineEdit()
        self.txt_release_date.setPlaceholderText("YYYY-MM-DD")

        basics_grid.addLayout(self._field_block("Product Code", self.txt_product_code), 0, 0)
        basics_grid.addLayout(self._field_block("Price", self.txt_price), 0, 1)
        basics_grid.addLayout(self._field_block("Age Group", self.txt_age_group), 1, 0)
        basics_grid.addLayout(self._field_block("Release Date", self.txt_release_date), 1, 1)
        layout.addLayout(basics_grid)

        self.cmb_publisher = QComboBox()
        layout.addLayout(self._field_block("Publisher", self.cmb_publisher))

        layout.addWidget(self._divider())
        layout.addWidget(self._section_label("Relations"))

        relations_grid = QGridLayout()
        relations_grid.setHorizontalSpacing(16)
        relations_grid.setVerticalSpacing(14)

        self.lst_authors = self._new_list()
        self.lst_categories = self._new_list()
        self.lst_languages = self._new_list()
        self.lst_designers = self._new_list()
        self.lst_translators = self._new_list()
        self.lst_resources = self._new_list()

        relations_grid.addLayout(self._field_block("Authors", self.lst_authors), 0, 0)
        relations_grid.addLayout(self._field_block("Categories", self.lst_categories), 0, 1)
        relations_grid.addLayout(self._field_block("Languages", self.lst_languages), 1, 0)
        relations_grid.addLayout(self._field_block("Cover Designers", self.lst_designers), 1, 1)
        relations_grid.addLayout(self._field_block("Translators", self.lst_translators), 2, 0)
        relations_grid.addLayout(self._field_block("Resources", self.lst_resources), 2, 1)
        layout.addLayout(relations_grid)

        layout.addStretch()

        scroll.setWidget(content)
        outer_layout.addWidget(scroll)

        footer = QWidget()
        footer.setObjectName("formFooter")
        footer_layout = QHBoxLayout(footer)
        footer_layout.setContentsMargins(24, 14, 24, 14)
        footer_layout.setSpacing(10)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setObjectName("btnSecondary")
        self.btn_cancel.clicked.connect(self._on_cancel_clicked)

        self.btn_save = QPushButton("Save Book")
        self.btn_save.setObjectName("btnPrimary")
        self.btn_save.clicked.connect(self._on_save_clicked)

        footer_layout.addStretch()
        footer_layout.addWidget(self.btn_cancel)
        footer_layout.addWidget(self.btn_save)

        outer_layout.addWidget(footer)

    def _section_label(self, text: str) -> QLabel:
        label = QLabel(text.upper())
        label.setObjectName("sectionLabel")
        return label

    def _divider(self) -> QFrame:
        line = QFrame()
        line.setObjectName("divider")
        line.setFrameShape(QFrame.HLine)
        line.setFixedHeight(1)
        return line

    def _field_block(self, label_text: str, widget: QWidget) -> QVBoxLayout:
        block = QVBoxLayout()
        block.setSpacing(6)
        label = QLabel(label_text)
        label.setObjectName("fieldLabel")
        block.addWidget(label)
        block.addWidget(widget)
        return block

    def _new_list(self) -> QListWidget:
        list_widget = QListWidget()
        list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        list_widget.setFixedHeight(_LIST_HEIGHT)
        list_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return list_widget

    def _fill_list(self, list_widget: QListWidget, entities, label_fn):
        list_widget.clear()
        for entity in entities:
            list_item = QListWidgetItem(label_fn(entity))
            list_item.setData(Qt.UserRole, entity)
            list_widget.addItem(list_item)

    def _select_matching(self, list_widget: QListWidget, selected_entities):
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            item.setSelected(item.data(Qt.UserRole) in selected_entities)

    def _selected_entities(self, list_widget: QListWidget):
        return [item.data(Qt.UserRole) for item in list_widget.selectedItems()]

    def _load_reference_data(self):
        self.cmb_publisher.clear()
        for publisher in PublisherDataAdapter.get_all():
            self.cmb_publisher.addItem(publisher.name, publisher)

        self._fill_list(self.lst_authors, AuthorDataAdapter.get_all(), lambda a: a.name)
        self._fill_list(self.lst_categories, CategoryDataAdapter.get_all(), lambda c: c.name)
        self._fill_list(self.lst_languages, LanguageDataAdapter.get_all(), lambda l: l.name)
        self._fill_list(self.lst_designers, DesignerDataAdapter.get_all(), lambda d: d.name)
        self._fill_list(self.lst_translators, TranslatorDataAdapter.get_all(), lambda t: t.name)
        self._fill_list(self.lst_resources, ResourcesDataAdapter.get_all(), lambda r: r.name)

    def reset_form(self):
        self._editing_book_id = None
        self.header.setText("Add New Book")
        self.btn_save.setText("Save Book")

        self.txt_title.clear()
        self.txt_product_code.clear()
        self.txt_age_group.clear()
        self.txt_release_date.clear()
        self.txt_price.clear()

        self._load_reference_data()
        self.txt_title.setFocus()

    def on_item_clicked(self, name: str):
        if self.right_stack is not None:
            self.right_stack.setCurrentWidget(self)

        matches = BookDataAdapter.search(name=name)
        if not matches:
            return
        self._load_book(matches[0])

    def _load_book(self, book: Book):
        self._editing_book_id = book.id
        self.header.setText("Edit Book")
        self.btn_save.setText("Save Changes")

        self._load_reference_data()

        self.txt_title.setText(book.title)
        self.txt_product_code.setText(str(book.product_code))
        self.txt_age_group.setText(book.age_group)
        self.txt_release_date.setText(str(book.release_date))
        self.txt_price.setText(str(book.price))

        for i in range(self.cmb_publisher.count()):
            if self.cmb_publisher.itemData(i) == book.publisher:
                self.cmb_publisher.setCurrentIndex(i)
                break

        self._select_matching(self.lst_authors, book.authors)
        self._select_matching(self.lst_categories, book.categories)
        self._select_matching(self.lst_languages, book.languages)
        self._select_matching(self.lst_designers, book.cover_designers)
        self._select_matching(self.lst_translators, book.translators)
        self._select_matching(self.lst_resources, book.resources)

    def _on_cancel_clicked(self):
        self.reset_form()
        self.form_cancelled.emit()

    def _on_save_clicked(self):
        title = self.txt_title.text().strip()
        if not title:
            QMessageBox.warning(self, "Missing Data", "Please enter a title.")
            return

        if self.cmb_publisher.count() == 0 or self.cmb_publisher.currentIndex() < 0:
            QMessageBox.warning(self, "Missing Data", "Please select a publisher.")
            return

        try:
            product_code = int(self.txt_product_code.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Product code must be a number.")
            return

        try:
            price = int(self.txt_price.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Price must be a number.")
            return

        try:
            release_date = datetime.date.fromisoformat(self.txt_release_date.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Release date must be in YYYY-MM-DD format.")
            return

        age_group = self.txt_age_group.text().strip()
        publisher = self.cmb_publisher.currentData()

        book = Book(
            id=self._editing_book_id or 0,
            title=title,
            product_code=product_code,
            categories=self._selected_entities(self.lst_categories),
            age_group=age_group,
            release_date=release_date,
            authors=self._selected_entities(self.lst_authors),
            price=price,
            languages=self._selected_entities(self.lst_languages),
            publisher=publisher,
            cover_designers=self._selected_entities(self.lst_designers),
            translators=self._selected_entities(self.lst_translators),
            resources=self._selected_entities(self.lst_resources),
        )

        if self._editing_book_id is not None:
            BookDataAdapter.update(book)
            QMessageBox.information(self, "Success", "Book updated successfully.")
        else:
            BookDataAdapter.insert(book)
            QMessageBox.information(self, "Success", "Book added successfully.")

        self.book_saved.emit()
        self.reset_form()
