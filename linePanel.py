# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LinePanel(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.layout=QFormLayout()
        self.setLayout(self.layout)
        self.layout.setSizeConstraint(QLayout.SetMinimumSize)
                
        self.lines=[]
        self.labels=[]
        self.setLines(1)
        
    def setLines(self,num):
        l=len(self.lines)
        if l<num:
            for i in range(num-l):
                self.addLine()
        elif l>num:
            for i in range(l-1,num-1,-1):
                self.removeLine(i)
            del self.lines[num:]
            del self.labels[num:]
        height=0
        for line in self.lines:
            height+=line.height()
        self.adjustSize()
        
    def addLine(self):
        line=QLineEdit(parent=self)
        self.lines.append(line)
        label=QLabel(str(len(self.lines))+":",parent=self)
        self.labels.append(label)
        self.layout.addRow(label, line)

    
    def removeLine(self,num):                
        self.lines[num].hide()
        self.labels[num].hide()
        self.layout.removeWidget(self.lines[num])
        self.layout.removeWidget(self.labels[num])
        self.lines[num].setParent(None)
        self.labels[num].setParent(None)
        
