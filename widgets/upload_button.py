from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


def upload_button(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(335)
    button.setFixedHeight(74)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 12px;"
                         "font-size: 12px;"
                         "background-color : #00CED1;"
                         "font-weight: bold;"
                         "color: 'white';"
                         "}"

                         )
    return button
