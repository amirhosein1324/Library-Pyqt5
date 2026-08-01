APP_STYLE = """
* {
    font-family: "Segoe UI", "Vazirmatn", sans-serif;
}

QMainWindow {
    background-color: #14161c;
}

QMenuBar {
    background-color: #1a1d24;
    color: #eceef2;
    border-bottom: 1px solid #262a33;
    padding: 4px;
}

QMenuBar::item {
    background: transparent;
    padding: 6px 12px;
    margin: 2px;
    border-radius: 6px;
}

QMenuBar::item:selected {
    background-color: #262a33;
}

QMenu {
    background-color: #1a1d24;
    color: #eceef2;
    border: 1px solid #2a2e38;
    border-radius: 8px;
    padding: 6px;
}

QMenu::item {
    padding: 7px 20px;
    border-radius: 6px;
}

QMenu::item:selected {
    background-color: #16c98d;
    color: #0e1512;
}

/* Left panel: icon bar + entity list */
QWidget#left_panel, QWidget#left_panell {
    background-color: #1a1d24;
    border-right: 1px solid #262a33;
}

QWidget#left_panel QPushButton, QWidget#left_panell QPushButton {
    background-color: transparent;
    color: #b7bcc6;
    border: none;
    text-align: left;
    padding: 10px 14px;
    font-size: 11pt;
    border-radius: 6px;
}

QWidget#left_panel QPushButton:hover, QWidget#left_panell QPushButton:hover {
    background-color: #232730;
    color: white;
}

QWidget#left_panel QPushButton:pressed, QWidget#left_panell QPushButton:pressed {
    background-color: #2a2f3a;
}

/* Icon-bar navigation buttons: show intended active/inactive icon state */
QPushButton#navButton {
    background-color: transparent;
    border: none;
    border-radius: 10px;
    padding: 10px;
    margin: 3px 8px;
}

QPushButton#navButton:hover {
    background-color: #232730;
}

QPushButton#navButton:checked {
    background-color: #16c98d;
}

/* Page backgrounds */
QWidget#author_page, QWidget#book_page {
    background-color: #17191f;
    color: #eceef2;
}

QLabel {
    color: #eceef2;
    font-size: 10pt;
}

QLineEdit {
    background-color: #20242c;
    color: #ffffff;
    border: 1px solid #2e333e;
    border-radius: 8px;
    padding: 6px 10px;
    min-height: 25px;
    selection-background-color: #16c98d;
}

QLineEdit:focus {
    border: 1px solid #16c98d;
    background-color: #262b34;
}

QCheckBox {
    color: #eceef2;
    spacing: 8px;
}

QCheckBox::indicator {
    width: 15px;
    height: 15px;
    border-radius: 4px;
    border: 1px solid #3a3f4b;
    background-color: #20242c;
}

QCheckBox::indicator:hover {
    border: 1px solid #16c98d;
}

QCheckBox::indicator:checked {
    background-color: #16c98d;
    border: 1px solid #16c98d;
}

QPushButton {
    background-color: #262a33;
    color: white;
    border: 1px solid #343a46;
    border-radius: 8px;
    padding: 8px 16px;
    min-height: 25px;
}

QPushButton:hover {
    background-color: #2e333e;
    border: 1px solid #3f4552;
}

QPushButton:pressed {
    background-color: #1f232b;
}

QPushButton#btn_send, QPushButton#btn_add_book {
    background-color: #16c98d;
    border: 1px solid #16c98d;
    color: #0e1512;
    font-weight: 600;
}

QPushButton#btn_send:hover, QPushButton#btn_add_book:hover {
    background-color: #22e39f;
}

QStackedWidget {
    border: none;
}

QScrollBar:vertical {
    background: transparent;
    width: 8px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: #343a46;
    border-radius: 4px;
    min-height: 24px;
}

QScrollBar::handle:vertical:hover {
    background: #454c5a;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QToolTip {
    background-color: #20242c;
    color: #eceef2;
    border: 1px solid #343a46;
    padding: 5px 8px;
    border-radius: 6px;
}
"""