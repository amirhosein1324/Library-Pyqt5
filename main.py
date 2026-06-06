import models.model as model
import sqlite3
import re
import json
import datetime

from models.category import Category
from models.author import Author
from models.publisher import Publisher
from models.language import Language
from models.designer import CoverDesigner
from models.translator import Translator
from models.resource import Resources
from models.book import Book

import adapters.author_data_adapter as AuthorDataAdapter
import adapters.publisher_data_adapter as PublisherDataAdapter
import adapters.category_data_adapter as CategoryDataAdapter
import adapters.language_data_adapter as LanguageDataAdapter
import adapters.designer_data_adapter as DesignerDataAdapter
import adapters.translator_data_adapter as TranslatorDataAdapter
import adapters.resource_data_adapter as ResourcesDataAdapter
import adapters.book_data_adapter as  BookDataAdapter

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QAction, QLabel, QLineEdit,
    QGridLayout, QCheckBox, QFrame
)
from PyQt5.QtCore import Qt


class BooksWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Books")
        title.setObjectName("TitleLabel")

        subtitle = QLabel("Enter book details below")
        subtitle.setObjectName("SubtitleLabel")

        grid = QGridLayout()
        grid.setHorizontalSpacing(12)
        grid.setVerticalSpacing(12)

        grid.addWidget(QLabel("Name:"), 0, 0)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Book name")
        grid.addWidget(self.name_edit, 0, 1)

        grid.addWidget(QLabel("Title:"), 1, 0)
        self.title_edit = QLineEdit()
        self.title_edit.setPlaceholderText("Book title")
        grid.addWidget(self.title_edit, 1, 1)

        self.save_btn = QPushButton("Save Book")
        grid.addWidget(self.save_btn, 2, 0, 1, 2)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(grid)
        layout.addStretch()


class AuthorsWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title = QLabel("Authors")
        title.setObjectName("TitleLabel")

        subtitle = QLabel("Enter author details below")
        subtitle.setObjectName("SubtitleLabel")

        grid = QGridLayout()
        grid.setHorizontalSpacing(12)
        grid.setVerticalSpacing(12)

        grid.addWidget(QLabel("Name:"), 0, 0)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Author name")
        grid.addWidget(self.name_edit, 0, 1)

        grid.addWidget(QLabel("Family:"), 1, 0)
        self.family_edit = QLineEdit()
        self.family_edit.setPlaceholderText("Author family")
        grid.addWidget(self.family_edit, 1, 1)

        grid.addWidget(QLabel("Activity:"), 2, 0)
        self.activity_check = QCheckBox("Active")
        grid.addWidget(self.activity_check, 2, 1)

        self.save_btn = QPushButton("Save Author")
        grid.addWidget(self.save_btn, 3, 0, 1, 2)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addLayout(grid)
        layout.addStretch()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Library Manager")
        self.resize(1100, 700)

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        help_menu = menu_bar.addMenu("Help")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        about_action = QAction("About", self)
        help_menu.addAction(about_action)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # Sidebar
        self.left_panel = QFrame()
        self.left_panel.setObjectName("Sidebar")
        self.left_panel.setFixedWidth(210)
        left_layout = QVBoxLayout(self.left_panel)
        left_layout.setContentsMargins(15, 15, 15, 15)
        left_layout.setSpacing(12)

        sidebar_title = QLabel("Navigation")
        sidebar_title.setObjectName("SidebarTitle")
        left_layout.addWidget(sidebar_title)

        self.authors_btn = QPushButton("Authors")
        self.authors_btn.setObjectName("SideButton")
        self.authors_btn.setCheckable(True)

        self.books_btn = QPushButton("Books")
        self.books_btn.setObjectName("SideButton")
        self.books_btn.setCheckable(True)

        left_layout.addWidget(self.authors_btn)
        left_layout.addWidget(self.books_btn)
        left_layout.addStretch()

        # Content area
        self.right_panel = QFrame()
        self.right_panel.setObjectName("ContentArea")
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        self.placeholder = QLabel("Select Books or Authors from the left panel")
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setObjectName("PlaceholderLabel")
        self.right_layout.addWidget(self.placeholder)

        # Add panels
        main_layout.addWidget(self.left_panel)
        main_layout.addWidget(self.right_panel)
        main_layout.setStretch(0, 0)
        main_layout.setStretch(1, 1)

        # Connections
        self.books_btn.clicked.connect(self.show_books)
        self.authors_btn.clicked.connect(self.show_authors)

        self.books_widget = None
        self.authors_widget = None

        # Default view
        self.show_books()

    def clear_right_panel(self):
        while self.right_layout.count():
            item = self.right_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

    def set_active_button(self, active_button):
        self.books_btn.setChecked(active_button == self.books_btn)
        self.authors_btn.setChecked(active_button == self.authors_btn)

    def show_books(self):
        self.set_active_button(self.books_btn)
        self.clear_right_panel()
        self.books_widget = BooksWidget()
        self.right_layout.addWidget(self.books_widget)

    def show_authors(self):
        self.set_active_button(self.authors_btn)
        self.clear_right_panel()
        self.authors_widget = AuthorsWidget()
        self.right_layout.addWidget(self.authors_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load external stylesheet
    with open("ui\style.qss", "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
