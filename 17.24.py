'''
17.24 refer kadane's algorithm
Max Submatrix: Given an NxN matrix of positive and negtive integers, write code to find the submatrix with the largest possible sum 
'''

def kadane(arr):
	#max sum, start, end
	result = [-999999999, 0, -1]
	cur_sum, start = 0, 0

	for i in range(len(arr)):
		cur_sum += arr[i]
		if cur_sum < 0:
			cur_sum = 0
			start = i+1
		elif cur_sum > result[0]:
			result[0] = cur_sum
			result[1] = start
			result[2] = i

	if result[2] == -1:
		result[0] = 0
		for i in range(len(arr)):
			if arr[i] > result[0]:
				result[0] = a[i]
				result[1] = i
				result[2] = i

	return result

def max_submatrix(mat):
	max_sum = -9999999999
	l, r, t, b = 0, 0, 0, 0

	for left in range(len(mat[0])):
		dp = []
		for right in range(left+1, len(mat[0])):
			for row in range(len(mat)):
				if len(dp) != len(mat):
					dp.append(mat[row][right])
				else:
					dp[row] += mat[row][right]
			
			cur_result = kadane(dp)
			if cur_result[0] > max_sum:
				max_sum = cur_result[0]
				l = left
				r = right
				t = cur_result[1]
				b = cur_result[2]

	answer = "Max Sum: " + str(max_sum) + ", Left Col: " + str(l+1) + \
			 ", Right Col: " + str(r) + ", Top Row: " + str(t) + \
			 ", Bottom Row: " + str(b)

	return answer


arr = [[-1, 2, 3, 4, -10, 4, 6, 10, 1, -100],
	   [-1, 2, 3, 4, -10, 4, 6, 10, 1, -100],    
	   [-1, -2, -3, -4, -10, -4, -6, -10, -1, -100]]
	   
print(max_submatrix(arr))