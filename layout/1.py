import sys
# importing `QApplication` and all the required widgets
from PyQt5.QtWidgets import *
import qdarkstyle

def sayhello():
    entered = input.text()
    resultLabel.setText("<h1>Hello {}</h1>".format(entered))


myApp = QApplication(sys.argv)
myApp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
myWindow = QWidget()
myWindow.setWindowTitle('PyQt5 Application')
myWindow.setGeometry(100, 100, 615, 280)
myWindow.move(60, 15)
firstMsg = QLabel(
    '<h1>Name:</h1>', parent=myWindow)
firstMsg.move(60, 15)
butt = QPushButton("click", parent=myWindow,)
input = QLineEdit(parent=myWindow)
input.setFixedSize(200, 30)
input.move(190, 20)
butt.move(250, 70)
butt.setFixedSize(120, 30)
butt.clicked.connect(sayhello)
resultLabel = QLabel('', myWindow)
resultLabel.move(60, 110)
resultLabel.setFixedSize(480, 40)

myWindow.show()

# executing the event loop (or main loop) of the application
sys.exit(myApp.exec_())
