import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication(sys.argv)
win = QWidget()

hvox = QVBoxLayout()
hvox.addWidget(QPushButton("A"))
hvox.addWidget(QPushButton("B"))
hvox.addWidget(QPushButton("C"))
hvox.addStretch()
win.setLayout(hvox)
win.setWindowTitle("HBox Example")
win.show()
sys.exit(app.exec_())