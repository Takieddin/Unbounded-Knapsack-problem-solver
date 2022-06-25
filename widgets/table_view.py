from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class table_view(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData(self.data)
        self.setStyleSheet(
            "QTableWidget"
            "{"

            "font-weight: bold;"
            "margin-top: 15px;"
            "}"

        )

    def setData(self,data):
        self.clear()
        self.data=data
        self.setRowCount(max(len(data['objs']),3))
        horHeaders = ['Objects', 'Volume', 'Valeur','Nombre d\'exemplires']
        self.setHorizontalHeaderLabels(horHeaders)
        for i in range(len(self.data['objs'])):
            obj = QTableWidgetItem(self.data['objs'][i])
            vols = QTableWidgetItem(self.data['vols'][i])
            values = QTableWidgetItem(self.data['values'][i])
            nb_exem = QTableWidgetItem(self.data['nb_exem'][i])
            self.setItem(i, 0, obj)
            self.setItem(i, 1, vols)
            self.setItem(i, 2, values)
            self.setItem(i, 3, nb_exem)
        


