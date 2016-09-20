# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from keyEditor import *
from sheet import *

class NonoSolver(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent=parent)

        self.rowEditor=KeyEditor("row:",parent=self)
        self.colEditor=KeyEditor("col:",parent=self)
        
        editorLayout=QHBoxLayout()
        editorLayout.addWidget(self.rowEditor)
        editorLayout.addWidget(self.colEditor)
        
        self.clearButton=QPushButton("Clear",parent=self)
        self.clearButton.clicked.connect(self.clearKeys)
        
        self.solveButton=QPushButton("Solve",parent=self)
        self.solveButton.clicked.connect(self.solve)
        
        layout=QVBoxLayout()
        layout.addLayout(editorLayout)
        layout.addWidget(self.clearButton)
        layout.addWidget(self.solveButton)
        self.setLayout(layout)
        
        self.sheet=Sheet()
#        self.solveThread=
        
    def clearKeys(self):
        self.rowEditor.clearLines()
        self.colEditor.clearLines()
        
    def solve(self):
        self.sheet.Solve(self.rowEditor.getKeys(), self.colEditor.getKeys())
        