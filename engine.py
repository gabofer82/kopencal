#! /usr/bin/python



class CalcEngine(object):
	def __init__(self):
		self._operators = ['+', '-', '/', '*']
		self._equation = []
		self._number_buffer = ''

	def addSymbol(self, symbol):
		'''Add a simbol to ecuation'''
		if self._evaluateSymbol(symbol) and len(self._number_buffer) >= 1:
			self._equation.append(self._number_buffer)
			self._number_buffer = ''
			self._equation.append(symbol)

	def operate(self):
		'''Return a result string. Invoqued by gui's equal button.'''
		operation = ''
		print len(self._equation)
		self._equation.append(self._number_buffer)
		print self._equation
		for item in self._equation:
			operation = '%s%s' % (operation, item)

		if self._isOperator(self._equation[-1]):
			del self._equation[-1]

		return eval(operation)

	def cleanData(self):
		'''Clean number_buffer variable.'''
		self._number_buffer = ''
		self._equation = []

	def _evaluateSymbol(self, symbol):
		if self._isOperator(symbol):
			return True
		else:
			self._number_buffer = '%s%s' % (self._number_buffer, symbol,)

		return False

	def _isOperator(self, symbol):
		'''Determine if symbol is operator or numeric digit.
		Return True or False.'''
		if symbol in self._operators:
			return True

		return False
