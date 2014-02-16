#! /usr/bin/python

import sys
import os
from PySide import QtGui
from kopencal import ControlMainWindow
import engine

def initApp():
	app = QtGui.QApplication(sys.argv)

    	w = ControlMainWindow()
    	#w.resize(250, 150)
    	#w.move(300, 300)
    	#w.setWindowTitle('Simple')
    	w.show()
    
    	sys.exit(app.exec_())



def test():
	eng = engine.CalcEngine()
	eng.addSymbol('2')
	eng.addSymbol('+')
	eng.addSymbol('2')
	eng.addSymbol('+')
	eng.addSymbol('2')
	eng.addSymbol('/')
	eng.addSymbol('2')
	print eng.operate()

if __name__ == "__main__":
	initApp()
