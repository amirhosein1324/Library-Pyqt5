import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QMessageBox
)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QHBoxLayout")
window.setGeometry(100, 100, 500, 100)


send_button1 = QPushButton("send")
send_button2 = QPushButton("send")
send_button3 = QPushButton("send")

greeting_label = QLabel("")


hbox = QHBoxLayout()

hbox.addWidget(send_button1)
hbox.addWidget(send_button2)
hbox.addWidget(send_button3)
hbox.addWidget(greeting_label)


window.setLayout(hbox)
window.show()
sys.exit(app.exec_())