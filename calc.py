import math

def isOperation(elem):
	if elem == '+' or elem == '-' or elem == '*' or elem == '/' or elem == '(' or elem == ')' or elem == '^':
		return True
	else:
		return False	

def isFloat(number):
	try:
		a = float(number)
		return True
	except ValueError as e:
		print "lel"
		return False

def makeOperation(operation):
	if priority(operation) > 3:
		right = result_str.pop()
		if operation == 'sin':
			result_str.append(math.sin(right))
		elif operation == 'sqrt':
			result_str.append(math.sqrt(right))
		elif operation == 'cos':
			result_str.append(math.cos(right))
		elif operation == 'abs':
			result_str.append(math.abs(right))
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
	
def priority (operation):
	if operation in ('+', '-'):
		return 1
	elif operation in ('*', '/', '%', '^'):
		return 2
	elif operation in ('sin', 'cos', 'sqrt'):
		return 4
	else:
		return -1

def printStacks():
	print("str= ", result_str)
	print("ope= ", operations)

#input_str = '(2 + sqrt(15) - 3 * 1/3)^5 + 1'
input_str = '1*4+3.3/(3 + .3)*3(sqrt(4))/5(sin(0) + 1)'
operations = []
result_str = []

operand = ''
for elem in input_str:

	if elem == ' ':
		continue

	if elem == '(':
		if operand != '':
			if isFloat(operand):
				print "work!"
				result_str.append(float(operand))
				operations.append('*')
			elif operand.isalnum():
				operations.append(operand)
			else:
				result_str.append(float(operand))
			operand = ''
		operations.append(elem)
		
		continue
	elif elem == ')':
		if operand != '':
			result_str.append(float(operand))
			operand = ''
					
		while operations[-1] != '(':
			
			makeOperation(operations.pop())
		operations.pop()
		
		continue
	elif isOperation(elem):
		if operand != '':
		#	print ("OPERAND =" + operand)
			result_str.append(float(operand))
			operand = ''
		while operations and priority(operations[-1]) >= priority(elem):
			makeOperation(operations.pop())
			
		operations.append(elem)
		
	else:
		operand += elem


if (operand != ''):
	result_str.append(float(operand))


		 
while operations:
	makeOperation(operations.pop())	

		
print('lol')
print (result_str)
print (operations)
