#! /usr/bin/python


class CalcEngine(object):
	def __init__(self):
		self._operators = ['+', '-', '/', '*']
		self._equation = []
		self._number_buffer = ''

	def addSymbol(self, symbol):
		'''Add a simbol to ecuation'''
		if self._evaluateSymbol(symbol) and len(self._number_buffer) >= 1:
			self._equation.append(self._number_buffer)  # here add the number to equation
			self._equation.append(symbol)  # here add the operator to equation

	def getCurNumber(self):
		if len(self._number_buffer) == 0:
			return '0'
		return self._number_buffer

	def operate(self):
		'''Return a result string. Invoqued by gui's equal button.'''
		operation = ''
		result = None
		print len(self._equation)
		# append the last value tippying by user
		self._equation.append(self._number_buffer)
		for index, item in enumerate(self._equation):
			operation = '%s%s' % (operation, item)

			if (index % 2) == 0:
				operation = eval(operation)

		operation = str(operation)
		self.cleanData()
		self._number_buffer = operation
		return operation

	def cleanData(self):
		'''Clean number_buffer variable.'''
		self._number_buffer = ''
		self._equation = []

	def _evaluateSymbol(self, symbol):
		if self._isOperator(symbol):
			return True
		else:
			if len(self._equation) > 0:
				if self._isOperator(self._equation[-1]):
					self._number_buffer = ''
			# here add the digit
			self._number_buffer = '%s%s' % (self._number_buffer, symbol,)

		return False

	def _isOperator(self, symbol):
		'''Determine if symbol is operator or numeric digit.
		Return True or False.'''
		if symbol in self._operators:
			return True

		return False

	def isOperator(self, symbol):
		return self._isOperator(symbol)
