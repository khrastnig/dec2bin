#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox
from PyQt5.QtCore import Qt, QSize, QTimer


# Klasse für das Hauptfenster
class MyWindow(QMainWindow): # Beginn der Klase mit 2 Funktionen
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(250, 120))    
        self.setWindowTitle('Bit Representation') 

        wid = QWidget(self)
        self.setCentralWidget(wid)

        vlayout = QVBoxLayout()  # Layout vertikale Box // es geht immer von aussen nach innen
        wid.setLayout(vlayout)

        self.lcd_number = QLCDNumber(2, wid)
        vlayout.addWidget(self.lcd_number)  #  nummernblock // die lcd_nummern werdenin die vlayout eingelesen

        hlayout = QHBoxLayout()
        vlayout.addLayout(hlayout)

        #self.checkboxes = ["8":QCheckBox(wid), "4":QCheckBox(wid), "2":QCheckBox(wid), "1":QCheckBox(wid)] #ein array voller checkboxes
        self.checkboxes = [QCheckBox(wid), QCheckBox(wid), QCheckBox(wid), QCheckBox(wid)] #ein array voller checkboxes
        #for index, cb in enumerate(self.checkboxes):   #den index brauchen wir hier noch nicht, aber dann bei der Umrechnung
        for cb in self.checkboxes:                     
             hlayout.addWidget(cb)
             cb.clicked.connect(self.bin2dec)
             cb.setStyleSheet("background-color: rgb(127, 127, 127)")


    def bin2dec(self):  # hier wird die Umrechnung vorgenommen // jede memberfunktion braucht das self!
        value = 0
        #numpy. flip(index) kehrt 
        for index, cb in enumerate(self.checkboxes):
            #for cb in reversed(list(self.checkboxes)):                
            if cb.isChecked():  #wenn angeklickt, dann berücksichtige sie
                cb.setStyleSheet("background-color: rgb(255, 0, 0)")
                exponents=4-index-1
                value+=2**exponents        # um hochzalen zu rechnen, 2hoch3 =>  2**3 in p
        self.lcd_number.display(value)


app = QtWidgets.QApplication([]) # Start der Hauptfunktion
win = MyWindow()
win.show()
app.exec_()



################### zweiter Teil ########
'''
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
self.setLayout(vbox)'''
