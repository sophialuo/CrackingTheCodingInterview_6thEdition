'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. 
The robot can only move in two directions, right and down, but certain cells are "off limits" such
that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left
to the bottom right.
'''

def find_path(matrix):
	r, c = len(matrix), len(matrix[0])
	start, end = (0,0), (r-1, c-1)
	queue = [(start, [start])]
	adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	while queue:
		loc, path = queue.pop()
		r_loc, c_loc = loc
		if loc == end:
			return path

		for tup in adj:
			new_loc = (r_loc+tup[0], c_loc+tup[1])
			if is_valid(r, c, new_loc, matrix) and new_loc not in path:
				queue.append([new_loc, path + [new_loc]])
	return None
		
def is_valid(r, c, loc, matrix):
	r2, c2 = loc
	if r2 < 0 or r2 >= r or c2 < 0 or c2 >= c or matrix[r2][c2] == 1:
		return False
	return True

#test1 and test2 should return paths, test3 does not return a path
test1 = [
			[0,0,0,0,0,0,0],
			[0,1,1,0,0,1,1],
			[0,0,0,1,0,0,0],
			[0,1,1,0,0,1,0],
			[0,1,0,1,0,1,0]
		]
print(find_path(test1))
test2 = [
			[0,0,0,0,0,0,0],
			[0,1,1,1,1,1,1],
			[0,0,0,1,0,0,0],
			[0,1,0,0,0,1,0],
			[0,1,0,1,0,1,0]
		]
print(find_path(test2))
test3 = [
			[0,0,0,0,0,0,0],
			[1,1,1,0,0,1,1],
			[0,0,0,1,1,0,0],
			[0,1,1,0,0,1,0],
			[0,1,0,1,0,1,0]
		]
print(find_path(test3))

