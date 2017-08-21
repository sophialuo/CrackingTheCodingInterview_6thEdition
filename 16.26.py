'''
Calculator: Given an arithmetic equation consiting of positive integers, +, -, *, and / (no parentheses), compare the result.

EXAMPLE
Input: 2*3+5/6*3+15
Output: 23.5
'''

import re

def calculator(equation):
	equation = re.split('(plus|[*, +, /, \s-])', equation)
	
	print(equation)
	#first evaluate * and /
	index = 0
	while index < len(equation):
		if equation[index] in ['*','/']:
			value = 0
			if equation[index] == '*':
				value = float(equation[index-1])*float(equation[index+1])
			else:
				value = float(equation[index-1])/float(equation[index+1])
			equation[index] = value
			del equation[index+1]
			del equation[index-1]
			index -= 1
		index += 1
	#then evaluate + and -
	index = 0
	while index < len(equation):
		if equation[index] in ['+','-']:
			value = 0
			if equation[index] == '+':
				value = float(equation[index-1])+float(equation[index+1])
			else:
				value = float(equation[index-1])-float(equation[index+1])
			equation[index] = value
			del equation[index+1]
			del equation[index-1]
			index -= 1
		index += 1
	
	return equation[0]


eq = "2*3+5/6*3+15-2"
print(calculator(eq))