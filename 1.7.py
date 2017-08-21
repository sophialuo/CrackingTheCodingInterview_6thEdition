'''
Rotate matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to
rotate the image by 90 degrees. Can you do this in place?
'''

def rotate(mat):
	i, j = 0, len(mat)-1
	result = [[0 for y in range(j+1)] for x in range(j+1)]

	while i <= j:
		toprow, bottomrow = mat[i][i:j+1], mat[j][i:j+1]
		leftcol, rightcol = [],[]
		
		for x in range(i,j+1):
			leftcol.append(mat[x][i])
			rightcol.append(mat[x][j])
			#place top row
			result[x][j] = toprow[x-i]
			#place bottom row
			result[x][i] = bottomrow[x-i]

		leftcol, rightcol = leftcol[::-1], rightcol[::-1]
	
		#place columns if necessary
		if j-i+1 > 2:
			for y in range(i, j+1):
				result[i][y] = leftcol[y-i]
				result[j][y] = rightcol[y-i]

			
		i += 1
		j -= 1

	if i == j and i >= 0 and i < len(mat):
		result[i][j] = mat[i][j]
	
	return result

tests = [
			[[1]],

			[[1, 2], 
			 [3, 4]],
			
			[[1, 2, 3],
			 [4, 5, 6],
			 [7, 8, 9]],

			[['a','b','c','d'], 
			 ['e','f','g','h'], 
			 ['i','j','k','l'], 
			 ['m','n','o','p']],

			[['a','b','c','d','e'],
			 ['f','g','h','i','j'],
			 ['k','l','m','n','o'],
			 ['p','q','r','s','t'],
			 ['u','v','w','x','y']]

		]

answers  = [
			[[1]],

			[[3, 1], 
			 [4, 2]],
			
			[[7, 4, 1],
			 [8, 5, 2],
			 [9, 6, 3]],

			[['m','i','e','a'], 
			 ['n','j','f','b'], 
			 ['o','k','g','c'], 
			 ['p','l','h','d']],

			[['u','p','k','f','a'],
			 ['v','q','l','g','b'],
			 ['w','r','m','h','c'],
			 ['x','s','n','i','d'],
			 ['y','t','o','j','e']]

		]
count = 0

for index in range(len(answers)):
	mat, ans = tests[index], answers[index]
	result  = rotate(mat)
	flag = True
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if result[i][j] != ans[i][j]:
				print('incorrect for test case: ')
				print(mat)
				flag = False
				break
	
	if flag:
		print('correct')
		count += 1

if count == len(answers):
	print('all correct!')
	