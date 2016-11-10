import math

#'@' == unary minus
#'$' == //
def isOperation(elem):
	if elem in ('@','+', '-', '*', '/', '(', ')', '^', '%', '$'):
		return True
	else:
		return False	

def isFloat(number):
	try:
		float(number)
		return True
	except ValueError as e:	
		return False

def makeOperation(operation):
	if priority(operation) > 3:
		right = result_str.pop()	
		if operation == '@':
			result_str.append(-1 * right)
		elif operation == 'sin':
			result_str.append(math.sin(right))
		elif operation == 'arcsin':
			result_str.append(math.asin(right))
		elif operation == 'arctan':
			result_str.append(math.atan(right))
		elif operation == 'sqrt':
			result_str.append(math.sqrt(right))
		elif operation == 'cos':
			result_str.append(math.cos(right))
		elif operation == 'abs':
			result_str.append(abs(right))
		elif operation == 'log10':
			result_str.append(math.log10(right))
		elif operation == 'ln':
			result_str.append(math.log1p(right))
		elif operation == '^':
			left = result_str.pop()
			result_str.append(left ** right)
	else:
		right = result_str.pop()
		left = result_str.pop()
		if operation == '+':
			result_str.append(right + left)
		elif operation == '-':
			result_str.append(left - right)
		elif operation == '*':
			result_str.append(left * right)
		elif operation == '/':
			result_str.append(left / right)
		elif operation == '^':
			result_str.append(left ** right)
		elif operation == '%':
			result_str.append(left % right)
		elif operation == '$':
			result_str.append(left // right)	

def priority(operation):
	if operation in ('+', '-'):
		return 1
	elif operation in ('*', '/', '%', '$'):
		return 2
	elif operation in ('arcsin', 'ln', 'arctan', 'sin','^', 'cos', 'sqrt', 'log10', 'abs'):
		return 4
	elif operation in ('@'):
		return 5
	else:
		return -1

def printStacks():
	print("str= ", result_str)
	print("ope= ", operations)

operations = []
result_str = []

def calculate(input_str): 
	maybeUnary = True
	last_elem = None	
	operand = ''

	for elem in input_str:	
		if elem == ' ':
			last_elem = elem
			continue
		elif elem == 'e':
			result_str.append(math.e)
		elif elem == '(':
			if last_elem == ')':	
				operations.append('*')
			if operand != '':
				if isFloat(operand):	
					result_str.append(float(operand))
					operations.append('*')
				elif operand.isalnum():
					operations.append(operand)
				else:
					result_str.append(float(operand))
				operand = ''
			operations.append(elem)
			last_elem = elem
			maybeUnary = True
			continue
		elif elem == ')':
			if operand != '':
				result_str.append(float(operand))
				operand = ''				
			while operations[-1] != '(':
				makeOperation(operations.pop())
			operations.pop()
			last_elem = elem
			maybeUnary = False
			continue
		elif isOperation(elem):
			if operand != '':	
				result_str.append(float(operand))
				operand = ''
			if elem == '-' and maybeUnary:
				operations.append('@')
				continue	
			while operations and priority(operations[-1]) >= priority(elem):
				makeOperation(operations.pop())	
			else:
				operations.append(elem)
			last_elem = elem
			maybeUnary = True
		else:
			operand += elem
			last_elem = elem
			maybeUnary = False

	if (operand != '' and operand != '\n'):
		result_str.append(float(operand))
			 
	while operations:
		makeOperation(operations.pop())	
	result = result_str[0]
	result_str.pop() 
	return result

input_file = open("input.txt", "rt")
for str_fileTemp in input_file:
	str_file = str_fileTemp.replace('//', '$')
	print('{0} = {1}'.format(str_fileTemp[:-1], calculate(str_file)))
input_file.close()
