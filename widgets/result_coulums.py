from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def calculte_button(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(335)
    button.setFixedHeight(74)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 12px;"
                         "font-size: 12px;"
                         "background-color : #00CED1;"
                         "color: 'white';"
                         "margin-top: 30px;"
                         "font-weight: bold;"
                         "}"

                         )
    return button
