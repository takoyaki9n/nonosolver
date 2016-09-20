# -*- coding: UTF-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TestWidget(QWidget):
    def __init__(self,parent=None):
        super(TestWidget, self).__init__()
        virticalLayout = QVBoxLayout()
        self.setLayout(virticalLayout)
        
        self.spinbox = QSpinBox(self)
        self.scrollArea=QScrollArea(parent=self)
        self.buttonPanel=ButtonPanel(parent=self.scrollArea)
        self.scrollArea.setWidget(self.buttonPanel)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        virticalLayout.addWidget(self.spinbox)
        virticalLayout.addWidget(self.scrollArea)
        
        self.spinbox.setMinimum(1)
        self.spinbox.valueChanged.connect(self.buttonPanel.setButtons)
        
    def resizeEvent(self, e):
        self.buttonPanel.resize(self.scrollArea.width()-19,self.buttonPanel.height())

class ButtonPanel(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSizeConstraint(QLayout.SetMinimumSize)
        
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
        width=self.width()
        self.adjustSize()
        self.resize(width,self.height())
    

if __name__=="__main__":
    print("===start===")
    app=QApplication(sys.argv)
    n=TestWidget()
    n.show()
    app.exec_()
    print("====end====")
