# -*- coding: UTF-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from sheet import *
from answerView import *

class Canvas(QWidget):
    def __init__(self,matrix,parent=None):
        QWidget.__init__(self,parent=parent)
        self.setPalette(QPalette(Qt.white))
        
        self.matrix=matrix
        self.setCellSize(15)
    
    def paintEvent(self,e):
        self.painter=QPainter()
        self.painter.begin(self)
        self.drawContent()
        self.drawMesh()
        self.painter.end()
    
    def drawMesh(self):
        meshColor=QColor(64,64,64)
        bpen=QPen(QBrush(meshColor,Qt.SolidPattern),3)
        self.painter.setPen(bpen)
        self.painter.drawRect(0,0,self.mWidth,self.mHeight)
        tpen=QPen(QBrush(meshColor,Qt.SolidPattern),1)
        for x in range(1,len(self.matrix[0])):
            if x%5==0:
                self.painter.setPen(bpen)
            else:
                self.painter.setPen(tpen)
            self.painter.drawLine(x*self.cellSize,0,x*self.cellSize,self.mHeight)
        for y in range(1,len(self.matrix)):
            if y%5==0:
                self.painter.setPen(bpen)
            else:
                self.painter.setPen(tpen)
            self.painter.drawLine(0,y*self.cellSize,self.mWidth,y*self.cellSize)
    
    def drawContent(self):
        self.painter.setPen(QPen(QBrush(Qt.gray,Qt.SolidPattern),1))
        for x in range(len(self.matrix[0])):
            for y in range(len(self.matrix)):
                if self.matrix[y][x]==1:
                    self.painter.fillRect(x*self.cellSize,y*self.cellSize,self.cellSize,self.cellSize,Qt.black)
                elif self.matrix[y][x]==-1:
                    self.painter.drawLine(x*self.cellSize,y*self.cellSize,(x+1)*self.cellSize,(y+1)*self.cellSize)
                    self.painter.drawLine((x+1)*self.cellSize,y*self.cellSize,x*self.cellSize,(y+1)*self.cellSize)

    def setCellSize(self,size):
        self.cellSize=size
        self.mWidth=len(self.matrix[0])*self.cellSize
        self.mHeight=len(self.matrix)*self.cellSize
        self.setMinimumSize(len(self.matrix[0])*self.cellSize,len(self.matrix)*self.cellSize)
        self.setMaximumSize(len(self.matrix[0])*self.cellSize,len(self.matrix)*self.cellSize)

if __name__=="__main__":
    print("===start===")
    app=QApplication(sys.argv)
    sheet=Sheet()
    sheet.Solve(kam[0],kam[1])
    c=Canvas(sheet.answers[0])
    c.show()
    app.exec_()
    print("====end====")
