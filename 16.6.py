'''
Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each array) with the smallest
(non-negative) difference. Return the difference.

EXAMPLE
Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
Output: 3. That is, the pair (11, 8)
'''

def smallest_difference(arr1, arr2):
	arr1, arr2 = sorted(arr1), sorted(arr2)
	index1, index2 = 0, 0

	min_diff = 1000000 #some large number
	while index1 < len(arr1) and index2 < len(arr2):
		a, b = arr1[index1], arr2[index2]
		cur_diff = abs(a-b)
		if cur_diff < min_diff:
			min_diff = cur_diff

		if a < b:
			index1 += 1
			if index1 > len(arr1):
				index1 -= 1
				index2 += 1
		else:
			index2 += 1
			if index2 > len(arr2):
				index2 -=1
				index1 += 1
	return min_diff

print(smallest_difference([1, 3, 15, 11, 2],[23, 127, 235, 19, 8])) #should be 3
print(smallest_difference([1, 3, 15, 11, 2], [23, 125, 233, 14, 8])) #should be 1
		