import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

app = QApplication(sys.argv)
win = QWidget()

hbox = QHBoxLayout()
hbox.addWidget(QPushButton("A"))
hbox.addWidget(QPushButton("B"))
hbox.addWidget(QPushButton("C"))

win.setLayout(hbox)
win.setWindowTitle("HBox Example")
win.show()
sys.exit(app.exec_())