from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class BookForm(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.btn_save = QPushButton("👉👈")
        layout.addWidget(self.btn_save)