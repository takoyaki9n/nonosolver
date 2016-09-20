# -*- coding: UTF-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from nonoSolver import *
from sheet import *

class TestWidget(QWidget):
    def __init__(self,parent=None):
        super(TestWidget, self).__init__()
        virticalLayout = QVBoxLayout()
        self.setLayout(virticalLayout)
        
        self.spinbox = QSpinBox(self)
        self.scrollArea=QScrollArea(parent=self)
        self.buttonPanel=ButtonPanel(parent=self.scrollArea)
        self.scrollArea.setWidget(self.buttonPanel)
        
        virticalLayout.addWidget(self.spinbox)
        virticalLayout.addWidget(self.scrollArea)
        
        self.spinbox.setMinimum(1)
        self.spinbox.valueChanged.connect(self.buttonPanel.setButtons)

class ButtonPanel(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        
        self.buttons=[]
        self.bheight=QPushButton().height()
        self.setButtons(1)
        
    def setButtons(self,num):
        length=len(self.buttons)
        if length<num:
            for i in range(num-length):
                button=QPushButton(str(length+1),parent=self)
                self.layout.addWidget(button)
                self.buttons.append(button)
        elif length>num:
            for button in self.buttons[-1:num-length-1:-1]:
                button.hide()
                self.layout.removeWidget(button)
                button.setParent(None)
            del self.buttons[num:]
        self.adjustSize()
        self.resize(self.parent().width(),40*len(self.buttons))

def main():
    app=QApplication(sys.argv)
    window=QMainWindow()
    window.setCentralWidget(NonoSolver())
    window.show()
    app.exec_()

if __name__=="__main__":
    print("===start===")
    main()
    print("====end====")
