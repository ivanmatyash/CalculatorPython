import math

def isOperation(elem):
	if elem in ('+', '-', '*', '/', '(', ')', '^'):
		return True
	else:
		return False	

def isFloat(number):
	try:
		a = float(number)
		return True
	except ValueError as e:	
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
		elif operation == 'log10':
			result_str.append(math.log10(right))
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
	
def priority (operation):
	if operation in ('+', '-' ):
		return 1
	elif operation in ('*', '/', '%'):
		return 2
	elif operation in ('sin','^', 'cos', 'sqrt', 'log10'):

		return 4
	else:
		return -1

def printStacks():
	print("str= ", result_str)
	print("ope= ", operations)


operations = []
result_str = []

def calculate(input_str): 
	last_elem = None	
	operand = ''
	for elem in input_str:
		#printStacks()	
		if elem == ' ':
			last_elem = elem
			continue
		elif elem == 'e':
			result_str.append(math.e)
		elif elem == '(':
			if last_elem == ')':
				#print("Last element = " + last_elem)
				operations.append('*')
				#printStacks()
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
			continue
		elif elem == ')':
			if operand != '':
				result_str.append(float(operand))
				operand = ''
					
			while operations[-1] != '(':
			
				makeOperation(operations.pop())
			operations.pop()
			last_elem = elem
			continue
		elif isOperation(elem):
			if operand != '':
			#	print ("OPERAND =" + operand)
				result_str.append(float(operand))
				operand = ''
			while operations and priority(operations[-1]) >= priority(elem):
				makeOperation(operations.pop())
			
			operations.append(elem)
			last_elem = elem
		else:
			operand += elem
			last_elem = elem


	if (operand != '' and operand != '\n'):
		result_str.append(float(operand))


			 
	while operations:
		makeOperation(operations.pop())	
	#print ("Result = " + str(result_str))
	result = result_str[0]
	result_str.pop() 
	return result

input_file = open("input.txt", "rt")
for str_file in input_file:
	print('{0} = {1}'.format(str_file[:-1], calculate(str_file)))
input_file.close()
