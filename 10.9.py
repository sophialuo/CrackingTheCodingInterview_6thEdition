'''
Sorted Marix Search: Given an MxN marix in which each row and each column is sorted in ascending order, write
a method to find an element
'''

def sorted_matrix_search(mat, num):
	m, n= len(mat), len(mat[0])
	top, bottom, left, right = 0, m-1, 0, n-1
	while mat[top][left] != num:
		if left > right or bottom < top:
			return (-1,-1) #not in the matrix

		#eliminate cols on right
		while mat[top][right] > num:
			right = right -1
			if not is_valid(top, right, m, n):
				return (-1,-1)
		#eliminate cols on left
		while mat[bottom][left] < num:
			left = left + 1
			if not is_valid(bottom, left, m, n):
				return (-1,-1)
		#eliminate cols on top
		while mat[top][right] < num:
			top = top + 1
			if not is_valid(top, right, m, n):
				return (-1,-1)
		#eliminate cols on bottom
		while mat[bottom][left] > num:
			bottom = bottom - 1
			if not is_valid(bottom, left, m, n):
				return (-1,-1)
		

	return (top, left)

def is_valid(r, c, m, n):
	if r < 0 or r >= m or c < 0 or c >= n:
		return False
	return True

matrix = [
			[15, 22, 30, 40, 85],
			[20, 35, 44, 83, 95],
			[31, 55, 60, 96, 105],
			[42, 82, 90, 100, 120]
		 ]
test_cases = [(0, (-1,-1)), (15, (0,0)), (35, (1,1)), (90, (3,2)), (83, (1, 3)), (120, (3,4))]
counter = 0
print(matrix)
for i in range(len(test_cases)):
	num, ans = test_cases[i]
	result = sorted_matrix_search(matrix, num)
	if result == ans:
		counter += 1
		print("correct")
	else:
		print("incorrect for test case: " + str(test_cases[i]))

if counter == len(test_cases):
	print("all correct")