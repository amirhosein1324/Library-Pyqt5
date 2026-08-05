APP_STYLE = """
QMainWindow {
    background-color: #1e1e1e;
}

QMenuBar {
    background-color: #2b2b2b;
    color: #f0f0f0;
    border-bottom: 1px solid #7C5CFC;
    padding: 4px;
}

QMenuBar::item {
    background: transparent;
    padding: 5px 10px;
    margin: 2px;
    border-radius: 4px;
}

QMenuBar::item:selected {
    background-color: #3d3d3d;
}

QMenu {
    background-color: #2b2b2b;
    color: #f0f0f0;
    border: 1px solid #3a3a3a;
    padding: 4px;
}

QMenu::item {
    padding: 6px 18px;
    border-radius: 4px;
}

QMenu::item:selected {
    background-color: #4a4a4a;
}

/* Left panel */
QWidget#left_panel {
    background-color: #232323;
    border-right: 2px solid #3a3a3a;
}

QWidget#left_panel QPushButton {
    background-color: transparent;
    color: #d6d6d6;
    border: none;
    text-align: left;
    padding: 10px 14px;
    font-size: 11pt;
}
QWidget#left_panell QPushButton {
    background-color: transparent;
    color: #d6d6d6;
    border: none;
    text-align: left;
    padding: 10px 14px;
    font-size: 11pt;
}

QWidget#left_panel QPushButton:hover {
    background-color: #333333;
    color: white;
}

QWidget#left_panel QPushButton:pressed {
    background-color: #444444;
}

QWidget#left_panell QPushButton:hover {
    background-color: #333333;
    color: white;
}


QWidget#left_panell QPushButton:pressed {
    background-color: #444444;
}

/* Right pages */
QWidget#author_page, QWidget#book_page {
    background-color: #1f1f1f;
    color: #f0f0f0;
}

/* Labels */
QLabel {
    color: #f0f0f0;
    font-size: 10pt;
}

/* Input fields */
QLineEdit {
    background-color: #2b2b2b;
    color: #ffffff;
    border: 1px solid #4a4a4a;
    border-radius: 6px;
    padding: 4px 8px;
    min-height: 25px;
    selection-background-color: #7C5CFC;
}

QLineEdit:focus {
    border: 1px solid #7C5CFC;
    background-color: #333333;
}

/* ComboBox */
QComboBox {
    background-color: #2b2b2b;
    color: #ffffff;
    border: 1px solid #4a4a4a;
    border-radius: 6px;
    padding: 4px 8px;
    min-height: 25px;
}

QComboBox:hover {
    border: 1px solid #7C5CFC;
}

QComboBox:focus {
    border: 1px solid #7C5CFC;
    background-color: #333333;
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    background-color: #2b2b2b;
    color: #f0f0f0;
    border: 1px solid #3a3a3a;
    selection-background-color: #4a4a4a;
    outline: none;
    padding: 4px;
}

/* CheckBox */
QCheckBox {
    color: #f0f0f0;
    spacing: 8px;

}

QCheckBox::indicator {
    width: 15px;
    height: 15px;
    border-radius: 3px;
    border: 1px solid #5a5a5a;
    background-color: #2b2b2b;
}

QCheckBox::indicator:hover {
    border: 1px solid #7C5CFC;
}

QCheckBox::indicator:checked {
    background-color: #7C5CFC;
    border: 1px solid #7C5CFC;
}

/* Common buttons */
QPushButton {
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #555555;
    border-radius: 6px;
    padding: 7px 14px;
    min-height: 25px;
}

QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #666666;
}

QPushButton:pressed {
    background-color: #2f2f2f;
}

/* Specific buttons */
QPushButton#btn_send {
    background-color: #7C5CFC;
    border: 1px solid #7C5CFC;
}

QPushButton#btn_send:hover {
    background-color: #8F72FD;
}

QPushButton#btn_add_book {
    background-color: #9333EA;
    border: 1px solid #9333EA;
}

QPushButton#btn_add_book:hover {
    background-color: #A855F7;
}

/* Message boxes (warning / error / info / question popups) */
QMessageBox {
    background-color: #232323;
}

QMessageBox QLabel {
    color: #f0f0f0;
    font-size: 10pt;
}

QMessageBox QPushButton {
    background-color: #3a3a3a;
    color: white;
    border: 1px solid #555555;
    border-radius: 6px;
    padding: 7px 20px;
    min-width: 70px;
    min-height: 25px;
}

QMessageBox QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #666666;
}

QMessageBox QPushButton:pressed {
    background-color: #2f2f2f;
}

QMessageBox QPushButton:default {
    background-color: #7C5CFC;
    border: 1px solid #7C5CFC;
    color: white;
}

QMessageBox QPushButton:default:hover {
    background-color: #8F72FD;
}

/* Stack area */
QStackedWidget {
    border: none;
    # background-color: #1f1f1f;
}

#welcomeLabel {
    font-size: 200px;
    color: #555;
}

"""