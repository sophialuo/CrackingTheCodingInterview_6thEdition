'''
16.14
Best Line: Given a two dimensional graph with points on it, find a line which passes the most number of points.
'''

class Point(object):
	def __init__(self, x, y):
		self.x, self.y = x, y


def generate_line(A, B):
	numerator = B.y-A.y
	denominator = B.x-A.x

	if denominator == 0:
		return ("undefined", A.x) #second elem is the x-intercept

	slope = 1.0*numerator/denominator
	intercept = B.y - slope*B.x
	return (slope, intercept)


def is_multiple(num1, num2):
	return num1 % num2 == 0 or num2 % num1 == 0


def best_line(points):
	lines = {}
	max_count = -1
	cur_line = (0,0)

	for i in range(len(points)):
		for j in range(i+1, len(points)):
			line = generate_line(points[i], points[j])
			
			if line in lines:
				lines[line] += 1
			else:
				lines[line] = 1

			if lines[line] > max_count:
					max_count = lines[line]
					cur_line = line
	
	return "slope: " + str(cur_line[0]) + ", intercept: " + str(cur_line[1])

points = [Point(-1, 1), Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(3, 4)]
print(best_line(points))

