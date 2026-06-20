from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication([])

table = QTableWidget()
table.setRowCount(3)
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["Name", "Age", "City"])


table.setItem(0, 0, QTableWidgetItem("Ali"))
table.setItem(0, 1, QTableWidgetItem("22"))
table.setItem(0, 2, QTableWidgetItem("Tehran"))


# table.show()
app.exec_()