#!/usr/bin/env python3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber, QCheckBox, QSlider
from PyQt5.QtCore import Qt, QSize, QTimer
from gpiozero import LED, LEDBoard
from signal import pause
leds=[LED(18),LED(23),LED(24),LED(25)]
"""leds1=LED(18)
leds2=LED(23)
leds3=LED(24)
leds4=LED(25)"""

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
        #vbox.addLayout(sliderbox)
        
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
        self.length=len(self.bitlabels)
        #self.leds=[leds1, leds2 ,leds3, leds4];
        #print (self.length)
     
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
        #for j range(self.length):
        #rlabels=self.bitlabels[::-1]
        for j, led in enumerate(leds):
            i=self.length-1-j
            #print (j)
            if (value & 1<<j):
                #rlabels[j].setStyleSheet("background-color: rgb(255, 0, 0)")
                self.bitlabels[i].setStyleSheet("background-color: rgb(255, 0, 0)")
                #self.leds[j].on()
                led.on()
            else:
                self.bitlabels[i].setStyleSheet("background-color: rgb(127, 127, 127)")
                #self.leds[j].off()
                led.off()
                


app = QtWidgets.QApplication([]) 
win = MyWindow()
win.show()
app.exec_()




