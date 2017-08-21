'''
Tic Tac Win: Design an algorithm to figur eout if someone has won a game of tic-tac-toe
'''

#hard coding if statements is O(1)

def find_winner(grid):
	for i in range(len(grid)):
		if grid[i][0] == grid[i][1] == grid[i][2]:
			return grid[i][0]
		if grid[0][i] == grid[1][i] == grid[2][i]:
			return grid[0][i]
	if grid[0][0] == grid[1][1] == grid[2][2]:
		return grid[0][0]
	if grid[0][2] == grid[1][1] == grid[2][0]:
		return grid[0][2]
	return None

grid = [[0, 1, 1],
		[1, 0, 0],
		[0, 1, 0]]

print(find_winner(grid)) #should be 0

grid = [[1, 1, 0],
		[1, 0, 0],
		[0, 1, 1]]

print(find_winner(grid)) #should be 0

grid = [[0, 0, 0],
		[1, 0, 0],
		[0, 1, 0]]

print(find_winner(grid)) #should be 0

grid = [[1, 0, 0],
		[1, 1, 0],
		[0, 1, 0]]

print(find_winner(grid)) #should be 0