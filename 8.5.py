'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
You can use addition subtraction, and bit shifting, but you should minimize the number of those operations
'''


def recursive_multiply(x, y):
	if x == 0 or y == 0:
		return 0
	if x%2 == 1 and y%2 == 1:
		return multiply(min(x, y), max(x, y))
	elif x%2 == 0:
		return multiply(2, recursive_multiply(int(x/2), y))
	elif y%2 == 0:
		return multiply(2, recursive_multiply(int(y/2), x))

def multiply(small, big):
	total = 0
	for num in range(small):
		total += big
	return total


test_cases = [(1,2), (0,2), (6, 8), (7, 9), (3, 12), (100, 55)]
count = 0

for i in range(len(test_cases)):
	x, y = test_cases[i]
	if x*y == recursive_multiply(x, y):
		count += 1
		print("correct")
	else:
		print("incorrect, check test case: " + str(test_cases[i]))


if count == len(test_cases):
	print("all correct")