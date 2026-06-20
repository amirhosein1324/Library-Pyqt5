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
