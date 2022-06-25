from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def menu_button(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(200)
    button.setFixedHeight(60)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 0px;"
                         "font-size: 14px;"
                         "text-align: left;"
                         "margin-top: 00px;"
                         "padding-left: 10px;"
                         "font-weight: medium;"
                         "background-color : #4CAF50;"#38753a
                         "color: 'white';"
                         "transition-duration: 0.4s;"
                         "}"
                         "QPushButton:hover {"
                         "background-color: #38753a; "
                         "}"

                         )
    return button
