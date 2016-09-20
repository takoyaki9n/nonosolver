# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from linePanel import *

class KeyEditor(QWidget):
    def __init__(self,label,parent=None):
        QWidget.__init__(self,parent=parent)
        self.mainlayout=QVBoxLayout()
        self.setLayout(self.mainlayout)
        
        self.spinbix=QSpinBox(parent=self)
        spinLayout=QFormLayout()
        spinLayout.addRow(label, self.spinbix)
        
        self.scrollArea=QScrollArea(parent=self)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.linePanel=LinePanel(parent=self.scrollArea)
        self.scrollArea.setWidget(self.linePanel)
        self.scrollArea.setWidgetResizable(True)
        
        self.spinbix.setMinimum(1)
        self.spinbix.valueChanged.connect(self.linePanel.setLines)
        
        self.mainlayout.addLayout(spinLayout)
        self.mainlayout.addWidget(self.scrollArea)
    
    def clearLines(self):
        for line in self.linePanel.lines:
            line.clear()
            
    def getKeys(self):
        keys=[]
        for line in self.linePanel.lines:
            text=line.text()
            key=tuple([int(x) for x in text.split(",")])
            keys.append(key)
        return tuple(keys)