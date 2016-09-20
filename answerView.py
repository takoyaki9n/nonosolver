# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from sheet import *
from canvas import *

class A(QObject):
    def __init__(self,parent=None):
        QObject.__init__(self,parent=parent)
        print("successed")

class AnswerView(QTabWidget):
    def __init__(self,answers,parent=None):
        QTabWidget.__init__(self,parent=parent)
        for i in range(len(answers)):
            self.addTab(AnswerPanel(answers[i]),str(i+1))

class AnswerPanel(QWidget):
    def __init__(self,answer,parent=None):
        QWidget.__init__(self,parent=parent)
        vLayout=QVBoxLayout()
        self.setLayout(vLayout)
        self.scrollArea=QScrollArea(parent=self)
        self.canvas=Canvas(answer)
        self.spinbox=QSpinBox(parent=self)
    
        self.spinbox.setMinimum(5)
        self.spinbox.setValue(self.canvas.cellSize)
        self.spinbox.valueChanged.connect(self.canvas.setCellSize)
        vLayout.addWidget(self.spinbox)
        
        self.scrollArea.setWidget(self.canvas)
        vLayout.addWidget(self.scrollArea)
        
if __name__=="__main__":
    print("===start===")
    app=QApplication(sys.argv)
    sheet=Sheet(parent=None)
    sheet.Solve([[1],[1]],[[1],[1]])
    c=AnswerView(sheet.answers)
    c.show()
    app.exec_()
    print("====end====")

        
