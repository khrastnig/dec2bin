#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause
#from Tkinter import *

#leds = LEDBoard(18, 23, 24, 25)
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
        self.slider.setStyleSheet("QSlider::handle:horizontal {height: 18px;}"
            "QSlider::sub-page:horizontal {background-color:rgb(0,100,255);}"
            "QSlider::handle:horizontal {background-color: white; border: 1px solid gray; border-radius: 4px; width: 18px;  height: 18px;}")  # die größeneinstellung des handler funktioniert irgendwie nicht
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel('0') 
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)
        
        vbox.addLayout(sliderbox)

       
        #self.bitlabels = [QCheckBox(wid), QCheckBox(wid), QCheckBox(wid), QCheckBox(wid)] #ein array voller checkboxes
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")] #ein array voller bitlabels
        
        


# hier bitlabels erstellen      
        bitbox = QHBoxLayout()       
        vboxBitboxes= QVBoxLayout()
        vboxBitboxes.addLayout(bitbox)
        #vbox2.setFixedWidth(120)
        vboxBitboxes.setAlignment(Qt.AlignCenter)
        vbox.addLayout(vboxBitboxes)
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(127, 127, 127)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)
            
            
    def changeValue(self, value):  # hier nun die aufzurufende funktion
        #showValue=str(value)
        #print(value)
        self.label.setText(str(value))
        #ab hier nun die zuweisung zu den QLabel
        ar1=[1,3,5,7,9,11,13,15]
        if value in ar1:
        #if value == 1 or value == 3 or value == 5 or value == 7 or value == 9 or value == 11 or value == 13 or value == 15:
            self.bitlabels[3].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds1.on()
            #leds[0].on()
        else:
            self.bitlabels[3].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds1.off()
            #leds[0].off()
        ar2=[2,3,6,7,10,11,14,15]    
        if value in ar2:
        #if value == 2 or value == 3 or value == 6 or value == 7 or value == 10 or value == 11 or value == 14 or value == 15:
            self.bitlabels[2].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds2.on()
            #leds[1].on()
        else:
            self.bitlabels[2].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds2.off()
        ar4=[4,5,6,7,12,13,14,15]
        if value in ar4:
        #if value == 4 or value == 5 or value == 6 or value == 7 or value == 12 or value == 13 or value == 14 or value == 15:
            self.bitlabels[1].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds3.on()
        else:
            self.bitlabels[1].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds3.off()
        ar8=[8,9,10,11,12,13,14,15]    
        if value in ar8:
        #if value == 8 or value == 9 or value == 10 or value == 11 or value == 12 or value == 13 or value == 14 or value == 15:    
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
