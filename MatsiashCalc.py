import math

#'@a' == -a (unary minus)
#'a$b' == a // b
#'a,b' == hypot(a,b)
#'a&b' == log(a,b)

def isOperation(elem):
	if elem in ('@','+', '-', '*', '/', '(', ')', '^', '%', '$', ',', '&'):
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
		elif operation == 'asin':
			result_str.append(math.asin(right))
		elif operation == 'atan':
			result_str.append(math.atan(right))
		elif operation == 'sqrt':
			result_str.append(math.sqrt(right))
		elif operation == 'cos':
			result_str.append(math.cos(right))
		elif operation == 'acos':
			result_str.append(math.acos(right))
		elif operation == 'abs':
			result_str.append(abs(right))
		elif operation == 'log10':
			result_str.append(math.log10(right))
		elif operation == 'log1p':
			result_str.append(math.log1p(right))
		elif operation == '^':
			left = result_str.pop()
			result_str.append(left ** right)
		elif operation == 'factorial':
			result_str.append(math.factorial(right))
		elif operation == 'tan':
			result_str.append(math.tan(right))
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
		elif operation == ',':
			result_str.append(math.hypot(left, right))	
		elif operation == '&':
			result_str.append(math.log(left, right))

def priority(operation):
	if operation in ('+', '-', ',', '&'):
		return 1
	elif operation in ('*', '/', '%', '$'):
		return 2
	elif operation in ('factorial', 'asin', 'tan', 'log1p', 'atan', 'sin','^', 'cos', 'acos', 'sqrt', 'log10', 'abs'):
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

def calc(input_str): 
	#replace 'log(a, b)' -> '(a & b)'
	pos = input_str.find("log(")
	if pos != -1:
		while pos != -1:
			pos1 = input_str.find(",", pos)
			s = list(input_str)
			s[pos1] = "&"
			input_str = "".join(s)
			pos = input_str.find("log(", pos + 1)
	input_str = input_str.replace('log(', '(')
	
	#replace 'a // b' -> 'a $ b'
	input_str = input_str.replace('//', '$')
	#replace 'hypot(a,b)' -> '(a , b)'
	input_str = input_str.replace('hypot', '')

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


def test_func():
	try:
		input_file = open("input.txt", "rt")
		right_file = open("right", "rt")
	except Exception as e:
		input_file.close()
		right_file.close()
	res_list = []
	for temp in right_file:
		res_list.append(temp)

	amount = 0
	amount_right = 0
	counter = 0
	for str_fileTemp in input_file:
		try:
			amount += 1
			print('{0} = {1}'.format(str_fileTemp[:-1], calc(str_fileTemp)))
			print("right value = " + res_list[counter][:-1])
			if (calc(str_fileTemp)  - float(res_list[counter])) <= 1e-10:
				print("TRUE\n")
				amount_right += 1
			else:
				print("FALSE\n")
			counter += 1
		except Exception as e:
			print('{0} = error!'.format(str_fileTemp[:-1]))
			print("FALSE\n")
	print("{0}/{1}".format(amount_right, amount))
	input_file.close()
	right_file.close()

test_func()
