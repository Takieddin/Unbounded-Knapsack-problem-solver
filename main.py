from screens.SplashScreen import SplashScreen
from screens.HomeScreen import HomeScreen

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import * 

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet('''
            #title_label {
                font-size: 50px;
                color: #ffffff;
            }
        

            #desc_label {
                font-size: 20px;
                color: #c2ced1;
            }
            #loading_label {
                font-size: 30px;
                color: #e8e8eb;
            }
            QFrame {
                background-color: #8f101f;"
                color: #c8c8c8;
            }
            QProgressBar {
                background-color: #000000;
                color: #c8c8c8;
                border-style: none;
                border-radius: 5px;
                text-align: center;
                font-size: 25px;
            }
            QProgressBar::chunk {
                border-radius: 5px;
                background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #00CED1);
            }
    ''')

    HomeScreen().show()
    # splash = SplashScreen()
    # splash.show()
    sys.exit(app.exec_())
