'''
Sum Swap: Given two arrays of integers, find a pair of values (one value from each array) that you can swap to give the two arrays the
same sum. 

EXAMPLE
Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
Output: {1, 3}
'''

def sum_swap(A, B):
	sumA, sumB = sum(A), sum(B)
	numsA, numsB = set(A), set(B)
	
	for a in numsA:
		for b in numsB:
			if sumA - a + b == sumB - b + a:
				return (a, b)
	return None

A = [4, 1, 2, 1, 1, 2]
B = [3, 6, 3, 3]

print(sum_swap(A, B))

