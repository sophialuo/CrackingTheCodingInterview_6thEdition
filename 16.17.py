'''16.17
Contiguous Sequence: You are given an array of integers (both positive and negative). Find the
contiguous sequence with the largest sum. Return the sum.
EXAMPLE
Input: 2, -8, 3, -2, 4, -10
Output: 5 (i.e., {3, -2, 4})
'''

def contiguous_sequence(nums):
	cur_sum = nums[0]
	max_sum = nums[0]
	index = 1
	while index < len(nums):
		if cur_sum > max_sum:
			max_sum = cur_sum 
		if cur_sum < 0:
			cur_sum = nums[index]
		else:
			cur_sum += nums[index]
		index += 1
	return max_sum

lst = [2, -8, 3, -2, 4, 10]
print(contiguous_sequence(lst))
lst = [-1, -1, -1, -1, 5, -1, -1]
print(contiguous_sequence(lst))