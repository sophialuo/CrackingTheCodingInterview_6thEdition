'''
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of olos), a point, and a new color,
fill the surrounding area until the color changes from the original color)
'''

#numbers represent colors; 1 represents a boundary
def paint_fill(matrix, new_color, loc):
	adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	if is_valid(matrix,loc):
		queue = [loc]
		visited = [loc]
		while queue:
			r, c= queue.pop()
			matrix[r][c] = new_color
			for tup in adj:
				r_new, c_new = r+tup[0], c+tup[1]
				if is_valid(matrix, (r_new, c_new)) and (r_new, c_new) not in visited:
					queue.append((r_new, c_new))
					visited.append((r_new, c_new))

	return matrix


def is_valid(matrix, loc):
	n, m = len(matrix), len(matrix[0])
	r, c = loc
	if r < 0 or c < 0 or r >= n or c >= m or matrix[r][c] == 1:
		return False
	return True


example = [
				[0,0,0,0,0,1,0],
				[0,0,0,1,1,1,0],
				[0,0,1,1,0,0,0],
				[0,0,1,0,0,0,0]
		  ]

print('paint with color 2 starting from location (1,1)')
paint_2 = paint_fill(example, 2, (1,1))
print(paint_2)
print('paint with color 3 starting from location (3,4)')
paint_3 = paint_fill(example, 3, (3,4))
print(paint_3)
print('try painting on a border with color 4 from location (3,2)')
paint_border = paint_fill(example, 4, (3,2))
print(paint_border)

