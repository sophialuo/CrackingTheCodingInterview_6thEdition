'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
'''

#algorithm: find all unique rows and columns that contain 0s and then replace those rows and columns with 0s
def zero_matrix(mat): 
	rows, cols = set(), set()
	#find all rows and cols that contain 0
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if mat[i][j] == 0:
				rows.add(i)
				cols.add(j)
	#replace columns that contain 0 with all zeros
	for col in cols:
		for i in range(len(mat)):
			mat[i][col] = 0
	#replace rows that contain 0 with all zeros
	for row in rows:
		for j in range(len(mat[0])):
			mat[row][j] = 0
	
	return mat


#testing
matrices = [
				[[1,1,1],
				 [1,0,1],
				 [1,1,1]],

				[[1,1,1],
				 [1,0,1],
				 [1,1,0]] ,

				[[1,0,1],
				 [1,0,1],
				 [1,0,1]],

				[[0,1]],

				[[0],
				 [1]],

				[[0]]
		   ]
answers = [
				[[1,0,1],
				 [0,0,0],
				 [1,0,1]],

				[[1,0,0],
				 [0,0,0],
				 [0,0,0]] ,

				[[0,0,0],
				 [0,0,0],
				 [0,0,0]],

				[[0,0]],

				[[0],
				 [0]],

				[[0]]
		   ]
count = 0

for i in range(len(matrices)):
	mat, ans = matrices[i], answers[i]
	if zero_matrix(mat) == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ')
		print(str(mat))

if count == len(matrices):
	print('all correct!')