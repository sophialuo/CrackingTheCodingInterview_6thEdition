'''
Pairs with Sum: Design an algorithm to find al pairs of integers within an array which sum to a specified value.
'''

def pairs_with_sum(arr, value):
	arr = set(sorted(arr)) #O(1) access
	pairs = set()
	for num in arr:
		if value-num in arr:
			temp = sorted([num, value-num])
			pairs.add(tuple(temp))
	return pairs

arr = [1, 2, 3, 4, 5, 6]
value = 5
print(pairs_with_sum(arr, value))