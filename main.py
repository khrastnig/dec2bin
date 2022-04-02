#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause
#from Tkinter import *

#self.leds = LEDBoard(18, 23, 24, 25)
leds1=LED(18)
leds2=LED(23)
leds3=LED(24)
leds4=LED(25)

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
        self.slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel('0') 
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        
        vbox.addLayout(sliderbox)

       
        #self.bitlabels = [QCheckBox(wid), QCheckBox(wid), QCheckBox(wid), QCheckBox(wid)] #ein array voller checkboxes
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")] #ein array voller checkboxes
        
        


# hier bitlabels erstellen      
        bitbox = QHBoxLayout()
        vbox.addLayout(bitbox)   
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            #bitlabel.setStyleSheet("background-color: rgb(127, 127, 127)")            
    def changeValue(self, value):  # hier wird die Umrechnung vorgenommen // jede memberfunktion braucht das self!
        showValue=str(value)
        #print(value)
        self.label.setText(showValue)
        #ab hier nun die zuweisung zu den QLabel
        if value == 1 or value == 3 or value == 5 or value == 7 or value == 9 or value == 11 or value == 13 or value == 15:
            self.bitlabels[3].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds1.on()
        else:
            self.bitlabels[3].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds1.off()
        if value == 2 or value == 3 or value == 6 or value == 7 or value == 10 or value == 11 or value == 14 or value == 15:
            self.bitlabels[2].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds2.on()
        else:
            self.bitlabels[2].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds2.off()
        if value == 4 or value == 5 or value == 6 or value == 7 or value == 12 or value == 13 or value == 14 or value == 15:
            self.bitlabels[1].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds3.on()
        else:
            self.bitlabels[1].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds3.off()
        if value == 8 or value == 9 or value == 10 or value == 11 or value == 12 or value == 13 or value == 14 or value == 15:
            self.bitlabels[0].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds4.on()
        else:
            self.bitlabels[0].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds4.off()

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
