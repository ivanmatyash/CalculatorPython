import math

def isOperation(elem):
	if elem == '+' or elem == '-' or elem == '*' or elem == '/' or elem == '(' or elem == ')' or elem == '\n':
		return True
	else:
		return False	

def makeOperation(operation):
	if priority(operation) > 3:
		right = result_str.pop()
		if operation == 'sin':
			result_str.append(math.sin(right))
		if operation == 'sqrt':
			result_str.append(math.sqrt(right))
		if operation == 'cos':
			result_str.append(math.cos(right))
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
	
def priority (operation):
	if operation in ('+', '-'):
		return 1
	elif operation in ('*', '/', '%'):
		return 2
	elif operation in ('sin', 'cos', 'sqrt'):
		return 4
	else:
		return -1

def printStacks():
	print("str= ", result_str)
	print("ope= ", operations)

input_str = '1*4+3.3/(3 + .3)*3*(sqrt(4))/(cos(0) + 1)'

operations = []
result_str = []

operand = ''
for elem in input_str:

	if elem == ' ':
		continue

	if elem == '(':
		if operand != '':
			if operand.isalnum():
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
