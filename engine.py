#! /usr/bin/python



class CalcEngine(object):
	def __init__(self):
		self.equation = []
		self.number_buffer = ''

	def addSimbol(self, symbol):
		'''Add a simbol to ecuation'''
		if self._evaluateSymbol(symbol) and len(self.equation) >= 1:
			self.equation.append(self.number_buffer)
			self.number_buffer = ''
			self.equation.append(symbol)

	def operate(self):
		'''Return a result string. Invoqued by gui's equal button.'''
		operation = ''
		for item in self.equation:
			operation = '%s%s' % (operation, item)


	def cleanData(self):
		'''Clean number_buffer variable.'''
		self.number_buffer = ''
		self.equation = []

	def _evaluateSymbol(self, symbol):
		if _isOperator():
			return True
		else:
			self.number_buffer = '%s%s' % (self.number_buffer, symbol,)

	def _isOperator(self, symbol):
		'''Determine if symbol is operator or numeric digit.
		Return True or False.'''
		pass
