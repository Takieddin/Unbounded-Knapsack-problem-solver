from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def parameter_input(self,name="param"):
    container2 = QHBoxLayout()
    container2.setContentsMargins(0, 0, 0, 0)

    plabel = QLabel(name)
    plabel.setStyleSheet(
        "QLabel"
        "{"
        "font-weight: bold;"
        "color: #000;"
        "}"
    )


    p = QLineEdit(self)
    p.setPlaceholderText('0')
    p.setFixedHeight(40)

    p.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "font-weight: bold;"
        "padding: 1px;"
        "}"
    )
    plabel.setBuddy(p)
    container2.addWidget(plabel)
    container2.addWidget(p)

    upload2 = QWidget()
    upload2.setLayout(container2)

    upload2.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )
    return upload2,p
