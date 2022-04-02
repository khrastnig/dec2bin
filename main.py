#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox
from PyQt5.QtCore import Qt, QSize, QTimer


# Klasse für das Hauptfenster
class MyWindow(QMainWindow):
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(250, 120))    
        self.setWindowTitle('Bit Representation') 

        wid = QWidget(self)
        self.setCentralWidget(wid)

        vlayout = QVBoxLayout()
        wid.setLayout(vlayout)

        self.lcd_number = QLCDNumber(2, wid)
        vlayout.addWidget(self.lcd_number)

        hlayout = QHBoxLayout()
        vlayout.addLayout(hlayout)

        self.checkboxes = [QCheckBox(wid), QCheckBox(wid), QCheckBox(wid), QCheckBox(wid)]
        for index, cb in enumerate(self.checkboxes):
             hlayout.addWidget(cb)
             cb.clicked.connect(self.bin2dec)


    def bin2dec(self):
        value = 0
        for index, cb in enumerate(self.checkboxes):
            if cb.isChecked():
                value+=1
        self.lcd_number.display(value)


app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()

################### zweiter Teil ########
# Slider + Label Anzeige Dezimalwert
self.slider = QSlider(Qt.Horizontal)
self.label = QLabel('0') 
sliderbox = QHBoxLayout()
sliderbox.addWidget(self.slider)
sliderbox.addWidget(self.label)

# Labels fuer 4 Bits
self.bitlabels = [] # Liste 
# hier bitlabels erstellen      
bitbox = QHBoxLayout()
for bitlabel in self.bitlabels:
    bitbox.addWidget(bitlabel)

# Layout zusammenbauen
vbox = QVBoxLayout()
vbox.addLayout(sliderbox)
vbox.addLayout(bitbox)

# vbox anzeigen in QWidget
self.setLayout(vbox)
