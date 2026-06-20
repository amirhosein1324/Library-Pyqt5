import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qdarkstyle

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
win = QWidget()
win.setGeometry(100, 100, 415, 280)

def sayhello():
    entered = name_edit.text()
    age= age_edit.text()
    selqob=qombo.currentText()
    if entered!="" and age !="" :
        conname.setText("<h3>Hello {} . you are {} and you selected {} language</h3>".format(entered,age,selqob))
    else:
        QMessageBox.warning(win, "Error", "please insert your name.")


grid1 = QGridLayout()
name_label = QLabel("<h1>Name:</h1>")
name_edit = QLineEdit()
age_label = QLabel("<h1>Age:</h1>")
age_edit = QLineEdit()
validator = QIntValidator(1, 10, win)
age_edit.setValidator(validator)


qombo=QComboBox()
qombo.addItems(["Python","Java","C++","C#"])
grid1.addWidget(name_label, 0, 0)
grid1.addWidget(name_edit, 0, 1)
grid1.addWidget(age_label, 1, 0)
grid1.addWidget(age_edit, 1, 1)
grid1.addWidget(qombo,2,1)

# resultLabel = QLabel('', myWindow)

grid2= QGridLayout()
conname = QLabel("")
conname.setStyleSheet("""
    QLabel {
        font-family: "Tahoma", Arial, sans-serif;
        font-size: 10px;
        color: #2e7d32;
        
    }
""")
grid2.addWidget(conname, 0, 0)


grid3 = QGridLayout()
button1=QPushButton("Submit")
button1.clicked.connect(sayhello)
grid3.addWidget(button1, 1, 0)


main = QVBoxLayout()
main.addLayout(grid1)
main.addLayout(grid2)
main.addLayout(grid3)

win.setLayout(main)
win.setWindowTitle("")
win.show()
sys.exit(app.exec_())