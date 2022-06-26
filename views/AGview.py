from Algorithms.rs import rstalgo
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from numpy import result_type
from Algorithms.BranchBound import BranchBound, import_csv
from widgets.calculte_button import calculte_button
from widgets.upload_button import upload_button
from widgets.table_view import table_view
from widgets.parameter_input import parameter_input


def run(self,bvt,dt,vut,ont, weight,t0param,alphaparam,maxitparam):
    array = import_csv(self.fname[:len(self.fname)-4])
    duration, best_value, volume_taken, objs, vols,values, nb_exem = rstalgo(weight, array,t0param,alphaparam,maxitparam)

    data = {
        'Best Value': str(best_value),
        'Volume_taken': str(volume_taken),
        'objs' :objs,
        'vols' :vols,
        'values' :values,
        'nb_exem' :nb_exem,
        'Duration': str(duration)
    }  
    bvt.setText(str(best_value))
    dt.setText(str(duration))
    vut.setText(str(volume_taken))
    ont.setText(str(len(objs)))

    showResult(self, data)



def agTab(self):
    self.data = {
        'Best Value': str(0),
        'Volume_taken': str(0),
        'objs' :[],
        'vols' :[],
        'values' :[],
        'nb_exem' :[],
        'Duration': str(0),
    }


    self.main_layout = QVBoxLayout()
    welcome = QLabel('Genetic algorithm')
    welcome.setStyleSheet(
        "QLabel"
        "{"
        "font-size: 32px;"
        "font-weight: bold;"
        "color: #000;"
        "}"
    )

    container = QHBoxLayout()
    container.setContentsMargins(0, 0, 0, 0)

    url = QLineEdit(self)
    url.setPlaceholderText('url')
    url.setFixedHeight(60)
    url.setStyleSheet(
        "QLineEdit"
        "{"
        "border: 1px solid #000;"
        "border-radius: 12px;"
        "font-weight: bold;"
        "padding: 5px;"
        "}"
    )
    upload_csv = upload_button('Upload csv file', self)
    upload_csv.setFixedWidth(120)
    upload_csv.setFixedHeight(60)
    upload_csv.clicked.connect(lambda: uploadFile(self,url))
    container.addWidget(url)
    container.addWidget(upload_csv)
    upload = QWidget()
    upload.setLayout(container)
    upload.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )


    #parametres:

    # instanciate parametres
    maxWeight, pmw = parameter_input(self,name='maxWeight')
    p2, t0param = parameter_input(self,name=': T0')
    p3, alphaparam = parameter_input(self,name=': alpha')
    p4,maxitparam = parameter_input(self,name=': max_it')


    #put parameter in horizontal container
    param_container = QHBoxLayout()
    param_container.setContentsMargins(0, 0, 0, 0)
    param_container.addWidget(maxWeight)
    param_container.addWidget(p2)
    param_container.addWidget(p3)
    param_container.addWidget(p4)

    # transform container to widget
    p = QWidget()
    p.setLayout(param_container)

    p.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )




    self.main_layout.addWidget(welcome)
    self.main_layout.addWidget(upload)

    #add paramerter  widgets to view
    self.main_layout.addWidget(p)



    calcualte = calculte_button('Calculate', self)
    calcualte.clicked.connect(lambda: run(
        self,bvt,dt,vut,ont ,float(pmw.text()),float(t0param.text()),float(alphaparam.text()),float(maxitparam.text())))

    calcualte.setFixedWidth(300)
    calcualte.setFixedHeight(60)

    self.main_layout.addWidget(calcualte)

    self.main_layout.addStretch(2)
    bv, bvt = parameter_input(self,name='Best Value')
    d, dt = parameter_input(self,name='Duration  ')
    vu,vut = parameter_input(self,name='volume used')
    on,ont = parameter_input(self,name='objects number')

    result_container = QHBoxLayout()
    result_container.setContentsMargins(0, 0, 0, 0)
    result_container.addWidget(bv)
    result_container.addWidget(vu)
    result_container.addWidget(on)

    res_c_w = QWidget()
    res_c_w.setLayout(result_container)
    res_c_w.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )

    duration_container = QHBoxLayout()
    duration_container.setContentsMargins(0, 0, 0, 0)
    duration_container.addWidget(d)

    dur_c_w = QWidget()
    dur_c_w.setLayout(duration_container)
    dur_c_w.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )
    res_container = QVBoxLayout()
    res_container.setContentsMargins(0, 0, 0, 0)
    res_container.addWidget(res_c_w)
    res_container.addWidget(dur_c_w)

    res = QWidget()
    res.setLayout(res_container)

    res.setStyleSheet(
        "QWidget"
        "{"
        "margin-top: 15px;"
        "}"
    )
    self.main_layout.addWidget(res)

    main = QWidget()
    main.setLayout(self.main_layout)
    makeTable(self)
    self.main_layout.addStretch(5)

    return main

def uploadFile(self,url):
    fname, _ = QFileDialog.getOpenFileName(
        self, "Import CSV", "", "CSV data files fq (*.csv)")
    url.setText(fname)
    self.fname = fname

def showResult(self, data):
    self.table.setData(data)

def makeTable(self):
    
    
    self.table = table_view(self.data,4, 4)
    self.table.verticalHeader().setVisible(False)
    self.table.setStyleSheet(
        "QTableView"
        "{"
        "margin-right: 10px;"
        "margin-top: 15px;"
        "}"
    )
    header = self.table.horizontalHeader()
    header.setMaximumWidth(760)
    header.setSectionResizeMode(0, QHeaderView.Stretch)
    header.setSectionResizeMode(1, QHeaderView.Stretch)
    header.setSectionResizeMode(2, QHeaderView.Stretch)
    header.setSectionResizeMode(3, QHeaderView.Stretch)
    self.table.setFixedWidth(1200)
    self.main_layout.addWidget(self.table)