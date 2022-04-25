#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause

leds1=LED(18)
leds2=LED(23)
leds3=LED(24)
leds4=LED(25)

class MyWindow(QMainWindow): 
    def __init__(self):
 
        super().__init__()
        self.setMinimumSize(QSize(500, 200))    
        self.setWindowTitle('Dezimal Binär Rechner Hrastnig') 

        wid = QWidget(self)
        self.setCentralWidget(wid)
        
        vbox= QVBoxLayout() 
        wid.setLayout(vbox)
          
        sliderbox= QHBoxLayout() 
        wid.setLayout(sliderbox)
        
        self.slider = QSlider(Qt.Horizontal,wid)
        self.slider.setRange(0, 15)        
        self.slider.setStyleSheet("QSlider::handle:horizontal {height: 18px;}"
            "QSlider::sub-page:horizontal {background-color:rgb(0,100,255);}"
            "QSlider::handle:horizontal {background-color: white; border: 1px solid gray; border-radius: 4px; width: 18px;  height: 18px;}")  
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged[int].connect(self.changeValue)
        self.label = QLabel('0') 
        sliderbox.addWidget(self.slider)
        sliderbox.addWidget(self.label)        
        vbox.addLayout(sliderbox)       
 
        self.bitlabels = [QLabel("8"), QLabel("4"), QLabel("2"), QLabel("1")]       
     
        bitbox = QHBoxLayout()       
        vboxBitboxes= QVBoxLayout()
        vboxBitboxes.addLayout(bitbox)        
        vboxBitboxes.setAlignment(Qt.AlignCenter)
        vbox.addLayout(vboxBitboxes)
        for index, bitlabel in enumerate(self.bitlabels):
            bitbox.addWidget(bitlabel)            
            bitlabel.setStyleSheet("background-color: rgb(127, 127, 127)")
            bitlabel.setFixedWidth(20)
            bitlabel.setFixedHeight(20)
            bitlabel.setAlignment(Qt.AlignCenter)
            
            
    def changeValue(self, value):  
        self.label.setText(str(value))        
        ar1=[1,3,5,7,9,11,13,15]
        if value in ar1:        
            self.bitlabels[3].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds1.on()            
        else:
            self.bitlabels[3].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds1.off()            
        ar2=[2,3,6,7,10,11,14,15]    
        if value in ar2:        
            self.bitlabels[2].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds2.on()            
        else:
            self.bitlabels[2].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds2.off()
        ar4=[4,5,6,7,12,13,14,15]
        if value in ar4:       
            self.bitlabels[1].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds3.on()
        else:
            self.bitlabels[1].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds3.off()
        ar8=[8,9,10,11,12,13,14,15]    
        if value in ar8:           
            self.bitlabels[0].setStyleSheet("background-color: rgb(255, 0, 0)")
            leds4.on()
        else:
            self.bitlabels[0].setStyleSheet("background-color: rgb(127, 127, 127)")
            leds4.off()

app = QtWidgets.QApplication([]) 
win = MyWindow()
win.show()
app.exec_()



