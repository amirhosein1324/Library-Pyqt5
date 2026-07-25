Library-PyQt5: A Robust Relational Library Management Engine
Motivation
Managing a library’s metadata—spanning authors, publishers, translators, and complex book relations—often leads to fragmented, error-prone database code. While Python’s sqlite3 provides a powerful engine, implementing a consistent interface for relational CRUD operations and cross-referencing is a recurring challenge.

Library-PyQt5 was created to bridge this gap. It provides an abstraction layer over raw SQL, allowing developers to manage library records using intuitive Python objects. By separating data models from database adapters, this project ensures that developers spend less time writing boilerplate SQL queries and more time building functional library tools.

Architecture
This project follows a modular design pattern, ensuring that data definitions, persistence, and interface logic remain decoupled.

Model Layer (model.py): Defines the core data entities and their relationships.
Adapter Layer (LibraryDataAdapter.py): The engine that translates high-level Python commands into secure SQL operations.
Interface Layer (main.py): Provides a terminal-based CLI for end-to-end management.
Storage Layer (Library.sql, NewLibrary.db): Uses SQLite for portable, persistent storage.
Features
Relational Mapping: Handles multi-author, multi-translator, and multi-category assignments seamlessly.
Advanced Search Engine: Provides a powerful filtering mechanism for books based on any metadata field (Author, Publisher, Designer, etc.).
Simplified CLI: Executes database operations through human-readable commands.
Extensible Design: Easily integrate new modules or UI frameworks (like PyQt5) by interacting with the DataAdapter.
Quick Start (CLI)
Run the application to manage records via the terminal:

bash
python main.py
Command Examples
Add Author: insert author [name] [birthdate] [nationality]
Add Book: insert book [title] [product_code] [categories] ...
Delete Record: delete book [book_id]
Programmatic Usage (test.py)
For advanced data querying and integration, utilize the LibraryDataAdapter:

python
from LibraryDataAdapter import BookDataAdapter

# Perform complex search with filters
results = BookDataAdapter.search(name="the whis", publisher_name="Press")

for book in results:
    print(f"ID: {book.id} | Title: {book.title} | Publisher: {book.publisher.name}")
Technology Stack
Language: Python 3.x
Persistence: SQLite3
Design Pattern: Data Adapter / MVC-inspired
Interface: Command Line (Extensible to PyQt5)
Installation & Setup
Clone the repository:
bash
   git clone https://github.com/amirhosein1324/Library-Pyqt5
Initialize Database:Use Library.sql to generate the schema if the database file is missing.
Run: Execute main.py to begin managing your library.
