from PyQt4 import QtGui, QtCore
import sys
import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QWidget):

    def __init__(self):
        super(MyWidget, self).__init__()
        self.initGui()

    def initGui(self):
        # add other widgets here
        okButton = QtGui.QPushButton("OK")
        cancelButton = QtGui.QPushButton("Cancel")

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)    

class MyMainWindow(QtGui.QMainWindow):

    def __init__(self, widget):
        """docstring for __init__"""
        super(MyMainWindow, self).__init__()
        self.widget = widget
        self.initGui()
        
    def initGui(self):
        """docstring for iniGui"""
        self.setCentralWidget(self.widget)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()
        pass
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()
    win = MyMainWindow(widget)
    sys.exit(app.exec_())
