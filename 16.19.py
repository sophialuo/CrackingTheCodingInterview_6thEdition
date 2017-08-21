'''
Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location represents the height above
sea level. A value of zero indices water. A pond is a region of water connected vertically, horizontally, or diagonally. The 
size of the pond is the total number of conncte water cells. Write a method to compute the sizes of all pons in the matrix.

EXAMPLE
Input: 
	0 2 1 0
	0 1 0 1
	1 1 0 1
	0 1 0 1
Output: 2, 4, 1
'''

def pond_sizes(mat):
	adj = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	sizes = []
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			start = mat[i][j]
			if start == 0:
				cur_queue = [(i, j)]
				cur_count  = 0
				while cur_queue:
					r, c = cur_queue.pop()
					if mat[r][c] == 0:
						cur_count += 1
						mat[r][c] = -1 #marked as visited
					for tup in adj:
						r2, c2 = r + tup[0], c + tup[1]
						if is_valid(r2, c2, mat) and mat[r2][c2] == 0:
							cur_queue.append((r2, c2))
				sizes.append(cur_count)
	return sizes


def is_valid(r, c, mat):
	if r >= 0 and c >= 0 and r < len(mat) and c < len(mat[0]):
		return True
	return False


mat = [ [0, 2, 1, 0],
		[0, 1, 0, 1],
		[1, 1, 0, 1],
		[0, 1, 0, 1]]
print(pond_sizes(mat))