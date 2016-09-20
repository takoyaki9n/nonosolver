# -*- coding: UTF-8 -*-

import sys
import copy
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TestWidget(QWidget):
    def __init__(self,parent=None):
        super(TestWidget, self).__init__()
        virticalLayout = QVBoxLayout()
        self.setLayout(virticalLayout)
        
        self.start=QPushButton("start",parent=self)
        virticalLayout.addWidget(self.start)
        self.stop=QPushButton("stop",parent=self)
        virticalLayout.addWidget(self.stop)
        self.thr=MyThread()
        self.thr.sig.connect(self.lolo)
        self.start.clicked.connect(self.thr.start)
        self.stop.clicked.connect(self.thr.terminate)
    
    def lolo(self,a):
        print(a)
                
class MyThread(QThread):
    sig=pyqtSignal(str)
    def __init__(self,parent=None):
        QThread.__init__(self,parent=parent)
        
    def run(self):
        import time
        print("hello")
        for i in range(3):
            time.sleep(1)
            print(i)
        self.sig.emit("aaaaaa")
        print("a")

if __name__=="__main__":
    print("===start===")
    app=QApplication(sys.argv)
    n=TestWidget()
    n.show()
    app.exec_()
    print("====end====")