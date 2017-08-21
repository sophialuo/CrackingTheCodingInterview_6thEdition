'''
16.9
Operations: Write methods to implement the multiply, subtract, and divide operations for integers. The results of all of these are integers. 
Use only the add operator
'''

def multiply(a, b):
	if a == 0 or b == 0:
		return 0

	product = 0
	smaller, bigger = min(a, b), max(a, b)
	for i in range(smaller):
		product += bigger

	return product
print("6*8 = " + str(multiply(6, 8)))
print("3*5 = " + str(multiply(3, 5)))
print("0*1 = " + str(multiply(0, 1)))

def subtract(a, b):
	return a + (-b)

print("5-3 = " + str(subtract(5, 3)))
print("10-100 = " + str(subtract(10, 100)))


def divide(a, b):
	count = 0
	while a != 0:
		a -= b
		count += 1
	return count

print("60/5 = " + str(divide(60, 5)))
print("12/4 = " + str(divide(12, 4)))
print("12/1 = " + str(divide(12, 1)))
print("1/1 = " + str(divide(1, 1)))



