#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
#from Tkinter import *


# Klasse für das Hauptfenster
class MyWindow(QMainWindow): # Beginn der Klase mit 2 Funktionen
    def __init__(self):

        # Konstruktor von QMainWindow aufrufen
        super().__init__()
        self.setMinimumSize(QSize(500, 200))    
        self.setWindowTitle('Dezimal Binär Rechner Hrastnig') 

        wid = QWidget(self)
        self.setCentralWidget(wid)

        
        vbox= QVBoxLayout() 
        wid.setLayout(vbox)
        
      # Slider + Label Anzeige Dezimalwert
        sliderbox= QHBoxLayout() 
        wid.setLayout(sliderbox)
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setRange(0, 15)
        #bitlabel.clicked.connect(self.bin2dec)
        self.label = QLabel('0') 
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        
        vbox.addLayout(sliderbox)

       
        #self.bitlabels = [QCheckBox(wid), QCheckBox(wid), QCheckBox(wid), QCheckBox(wid)] #ein array voller checkboxes
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")] #ein array voller checkboxes
        # hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        vbox.addLayout(bitbox)   
        for bitlabel in self.bitlabels:
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(127, 127, 127);""selection-color: rgb(255, 0, 0);""text-aling: center;""border-width: 2px")
            
        
            
            
    #def bin2dec(self):  # hier wird die Umrechnung vorgenommen // jede memberfunktion braucht das self!
        #value = 0
        #numpy. flip(index) reverse etc hat nicht funktioniert
        #for self.slider
        #for index, bitlabel in enumerate(self.bitlabels):
            #for cb in reversed(list(self.checkboxes)):                
            #if bitlabel.isChecked():  #wenn angeklickt, dann berücksichtige sie
                #bbitlabel.setStyleSheet("background-color: rgb(255, 0, 0)")
                #exponents=4-index-1  # self.checkboxes.len() sowie .count() und .length() hat nicht funktioniert
                #value+=2**exponents        # um hochzahlen zu rechnen, 2hoch3 =>  2**3 in p
                #showValue=str(value)
        #self.label.setText(showValue)
        #self.setLayout(value)


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
