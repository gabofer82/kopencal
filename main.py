#! /usr/bin/python

import engine

def initApp():
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
