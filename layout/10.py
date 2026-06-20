from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt
import qdarkstyle
import sys

class secondwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.resize(400, 300)


        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        layout = QGridLayout(self)
        layout.addWidget(QLabel("This is the second window"), 0, 0)

class firstwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manage Window State")

        self.btn_open = QPushButton("Open Second Window", self)

        central_widget = QWidget()
        grid = QGridLayout(central_widget)
        grid.addWidget(self.btn_open, 0, 0)
        self.setCentralWidget(central_widget)

        self.second_window = None
        self.btn_open.clicked.connect(self.open_second)

    def open_second(self):
        if self.second_window is None:
            self.second_window = secondwindow()
        self.second_window.show()
        self.second_window.raise_()
        self.second_window.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = firstwindow()
    w.showMaximized()
    sys.exit(app.exec_())
