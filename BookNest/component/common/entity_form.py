import os
from dataclasses import dataclass
from typing import Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_STYLE_PATH = os.path.join(_PROJECT_ROOT, "component", "styles", "formstyles.qss")

_LABEL_WIDTH = 80


@dataclass
class FormField:
    label: str         
    attr: str            
    getter: Callable      
    readonly: bool = False


class EntityForm(QWidget):
  

    def __init__(self, title: str, fields: list[FormField], search_fn: Callable, right_stack=None):
        super().__init__()
        self.setObjectName("form")
        self.right_stack = right_stack
        self.fields = fields
        self.search_fn = search_fn

        with open(_STYLE_PATH, "r", encoding="utf-8") as f:
            self.setStyleSheet(f.read())

        self._setup_ui(title)

    def _setup_ui(self, title: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        title_row = QHBoxLayout()
        title_row.setSpacing(10)
        label_title = QLabel(title)
        label_title.setObjectName("title")
        title_row.addWidget(label_title, alignment=Qt.AlignLeft)
        layout.addLayout(title_row)

        for field in self.fields:
            row = QHBoxLayout()
            row.setSpacing(10)

            label = QLabel(field.label)
            label.setFixedWidth(_LABEL_WIDTH)

            line_edit = QLineEdit()
            line_edit.setReadOnly(field.readonly)
            setattr(self, field.attr, line_edit)

            row.addWidget(label, alignment=Qt.AlignTop)
            row.addWidget(line_edit, alignment=Qt.AlignTop)
            layout.addLayout(row)

        self.btn_save = QPushButton("Save")
        layout.addWidget(self.btn_save)
        layout.addStretch()

    def on_item_clicked(self, name: str):
        if self.right_stack is not None:
            self.right_stack.setCurrentWidget(self)

        entity = self.search_fn(name=name)[0]
        for field in self.fields:
            getattr(self, field.attr).setText(str(field.getter(entity)))