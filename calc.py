def isOperation(elem):
	if elem == '+' or elem == '-' or elem == '*' or elem == '/' or elem == '(' or elem == ')' or elem == '\n':
		return True
	else:
		return False	

def makeOperation(operation):
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
	else:
		return -1

def printStacks():
	print(result_str)
	print(operations)

input_str = '1 + 3 / 3 * 31 + 123 - 123 / 123 + 123 *3'

operations = []
result_str = []

operand = ''
for elem in input_str:
	if elem == ' ':
		continue

	if elem == '(':
		if operand != '':
			result_str.append(float(operand))
			operand = ''
		operations.append(elem)
		printStacks()
		continue
	elif elem == ')':
		if operand != '':
			result_str.append(float(operand))
			operand = ''
			printStacks()
			print('CRASH')
		while operations[-1] != '(':
			makeOperation(operations.pop())
		operations.pop()
		printStacks()
		continue
	elif isOperation(elem):
		if operand != '':
			print ("OPERAND =" + operand)
			result_str.append(float(operand))
			operand = ''
		while operations and priority(operations[-1]) >= priority(elem):
			makeOperation(operations.pop())
		operations.append(elem)
		printStacks()
	else:
		operand += elem


if (operand != ''):
	result_str.append(float(operand))
		 
while operations:
	makeOperation(operations.pop())	
printStacks()
		
print('lol')
print (result_str)
print (operations)
