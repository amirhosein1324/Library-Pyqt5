import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import qdarkstyle

app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

win = QMainWindow()
win.setGeometry(100, 100, 415, 280)

# ---------- Menu Bar ----------
menu = win.menuBar()

file_menu = menu.addMenu("File")
edit_menu = menu.addMenu("Edit")
help_menu = menu.addMenu("Help")

new_action = QAction("New", win)
file_menu.addAction(new_action)

save_action = QAction("Save", win)
file_menu.addAction(save_action)

saveas_action = QAction("Save as", win)
file_menu.addAction(saveas_action)

undo = QAction("Undo", win)
edit_menu.addAction(undo)

redo = QAction("Redo", win)
edit_menu.addAction(redo)

help_action = QAction("Help", win)
help_menu.addAction(help_action)

exit_action = QAction("Exit", win)
help_menu.addAction(exit_action)
exit_action.triggered.connect(app.quit)

# ---------- Central Widget ----------
central = QWidget()
win.setCentralWidget(central)

main_layout = QHBoxLayout(central)


left_panel = QWidget()
left_panel.setFixedWidth(150)
left_layout = QVBoxLayout(left_panel)
left_layout.addWidget(QLabel("Left Side"))
left_layout.addWidget(QPushButton("Button 1"))
left_layout.addWidget(QPushButton("Button 2"))
left_layout.addStretch()


right_panel = QWidget()
right_layout = QVBoxLayout(right_panel)
right_layout.addWidget(QLabel("Right Side"))
s=QTextEdit()
s.setStyleSheet("""
    QTextEdit {
        background-color: #1F5973;
        
    }

""")
right_layout.addWidget(s)
right_layout.addStretch()


main_layout.addWidget(left_panel, 0)   # stretch = 0
main_layout.addWidget(right_panel, 1)  # stretch = 1

win.show()
sys.exit(app.exec())
