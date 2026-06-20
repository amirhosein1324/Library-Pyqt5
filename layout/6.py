import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
import qdarkstyle
import sqlite3

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout - Table Example")
        self.setGeometry(100, 100, 650, 400)
        self.setup_ui()

    def setup_ui(self):

        self.name_label = QLabel("Name:")
        self.age_label = QLabel("Age:")
        self.ct_label = QLabel("City:")


        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Insert your name...")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Insert your age...")
        self.age_validator = QIntValidator(1, 150, self)
        self.age_input.setValidator(self.age_validator)
        self.ct_input = QLineEdit()
        self.ct_input.setPlaceholderText("Insert your city...")


        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 6px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.clear_button = QPushButton("Clear Table")
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #FFA500;
                color: black;
                border-radius: 6px;
                padding: 6px;
                
            }
        """)

        self.send_button.clicked.connect(self.set_newtable)
        self.clear_button.clicked.connect(self.clear_table)


        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "City"])
        s = cursor.execute("Select * from users")
        firstlist=[]
        for i in s:
            firstlist.append([i[1],i[2],i[3]])
        for j in firstlist:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            self.table.setItem(row_position, 0, QTableWidgetItem(j[0]))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(j[1])))
            self.table.setItem(row_position, 2, QTableWidgetItem(j[2]))


        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        grid = QGridLayout()

        grid.addWidget(self.name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1)

        grid.addWidget(self.age_label, 1, 0)
        grid.addWidget(self.age_input, 1, 1)

        grid.addWidget(self.ct_label, 2, 0)
        grid.addWidget(self.ct_input, 2, 1)

        grid.addWidget(self.send_button, 3, 1)
        grid.addWidget(self.clear_button, 3, 0)

        grid.addWidget(self.table, 4, 0, 1, 2)

        self.setLayout(grid)


    def set_newtable(self):
        name = self.name_input.text().strip()
        age = self.age_input.text().strip()
        ct = self.ct_input.text().strip()

        if name and age and ct:

            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(age))
            self.table.setItem(row_position, 2, QTableWidgetItem(ct))

            cursor.execute("INSERT INTO users (`name`, `age`, `city`) VALUES ('{}', {}, '{}');".format(name,int(age),ct))
            connection.commit()
            self.name_input.clear()
            self.age_input.clear()
            self.ct_input.clear()

        else:
            QMessageBox.warning(
                self,
                "Error",
                "Please insert Name, Age and City."
            )

    def clear_table(self):
        self.table.setRowCount(0)
        cursor.execute("DROP TABLE IF EXISTS users;")
        connection.commit()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30),
age INTEGER,
city VARCHAR(30)
);
        """)
        connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("nac.db")
    cursor = connection.cursor()

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
