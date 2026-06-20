import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QLineEdit, QPushButton, QLabel, QMessageBox
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout")
        self.setGeometry(100, 100, 350, 200)
        self.setup_ui()

    def setup_ui(self):
        self.name_label = QLabel("Name:")
        self.age_label = QLabel("Age:")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("insert your name...")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("insert your age...")

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.greet_user)

        self.greeting_label = QLabel("")

        grid = QGridLayout()
        grid.addWidget(self.name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1)

        grid.addWidget(self.age_label, 1, 0)
        grid.addWidget(self.age_input, 1, 1)

        grid.addWidget(self.send_button, 2, 1)
        grid.addWidget(self.greeting_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def greet_user(self):
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()

        if name and age:
            self.greeting_label.setText(f"Hello {name}, you are {age} years old")
        else:
            QMessageBox.warning(
                self,
                "Error",
                "Please insert your name and age before clicking the send button."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())