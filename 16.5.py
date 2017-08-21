'''16.5 
Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial
'''
def factorial_zeros(n):
	factors = list(range(1, n+1))
	count = 0
	for num in factors:
		count += count5s(num)
	return count

def count5s(num):
	count = 0
	while num > 0:
		if num % 5 == 0:
			count += 1
			num = num/5
		else:
			break
	return count

print(factorial_zeros(1)) #0
print(factorial_zeros(3)) #0
print(factorial_zeros(5)) #1
print(factorial_zeros(20)) #4
print(factorial_zeros(100)) #24