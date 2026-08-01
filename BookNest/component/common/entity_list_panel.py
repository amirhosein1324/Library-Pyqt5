import os
from typing import Callable

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QLineEdit

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_STYLE_PATH = os.path.join(_PROJECT_ROOT, "layout", "styles", "leftpanelstyles.qss")


class EntityListPanel(QWidget):


    item_clicked = pyqtSignal(str)

    def __init__(self, object_name: str, fetch_all: Callable[[], list],
                 label_fn: Callable[[object], str] = lambda item: item.name,
                 show_add_button: bool = False):
        super().__init__()
        self.setObjectName(object_name)
        self._fetch_all = fetch_all
        self._label_fn = label_fn
        self._items: list = []
        self._setup_ui(show_add_button)
        self.reload()

    def _setup_ui(self, show_add_button: bool):
        with open(_STYLE_PATH, "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 6, 6, 6)
        layout.setSpacing(8)

        top_row = QHBoxLayout()
        top_row.setSpacing(6)

        self.search_edit = QLineEdit()
        self.search_edit.setObjectName("searchBox")
        self.search_edit.setPlaceholderText("Search...")
        self.search_edit.textChanged.connect(self._apply_filter)
        top_row.addWidget(self.search_edit)

        if show_add_button:
            self.add_btn = QPushButton("+")
            self.add_btn.setObjectName("addButton")
            self.add_btn.setFixedSize(34, 34)
            top_row.addWidget(self.add_btn)

        layout.addLayout(top_row)

        self.scroll = QScrollArea()
        self.scroll.setObjectName("mainScroll")
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.content = QWidget()
        self.content.setObjectName("contentWidget")
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(2)

        self.scroll.setWidget(self.content)
        layout.addWidget(self.scroll)

    def reload(self):
        self._items = list(self._fetch_all())
        self.search_edit.clear()
        self._render(self._items)

    def _apply_filter(self, text: str):
        text = text.strip().lower()
        if not text:
            self._render(self._items)
            return
        self._render([item for item in self._items if text in self._label_fn(item).lower()])

    def _render(self, items: list):
        while self.content_layout.count():
            taken = self.content_layout.takeAt(0)
            widget = taken.widget()
            if widget:
                widget.deleteLater()

        for item in items:
            label = self._label_fn(item)
            btn = QPushButton(label)
            btn.setObjectName("boButton")
            btn.clicked.connect(lambda checked=False, name=label: self.item_clicked.emit(name))
            self.content_layout.addWidget(btn)

        self.content_layout.addStretch()