import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
import qdarkstyle

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
win = QMainWindow()
win.setGeometry(100, 100, 415, 280)

menu = win.menuBar()

file=menu.addMenu("File")
edit=menu.addMenu("Edit")
help=menu.addMenu("Help")

new_action = QAction("New", win)
file.addAction(new_action)
save_action=QAction("Save", win)
file.addAction(save_action)
saveas_action=QAction("Save as", win)
file.addAction(saveas_action)

undo=QAction("Undo", win)
edit.addAction(undo)
redo=QAction("Redo", win)
edit.addAction(redo)

help2=QAction("Help",win)
help.addAction(help2)

exit=QAction("Exit",win)
help.addAction(exit)
exit.triggered.connect(app.quit)

win.show()
sys.exit(app.exec())