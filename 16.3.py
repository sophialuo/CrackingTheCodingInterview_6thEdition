'''
16.3
Intersection: Given two sraight line segments (represented as a start point and an end point), compute the point of intersection,
if any.

https://www.topcoder.com/community/data-science/data-science-tutorials/geometry-concepts-line-intersection-and-its-applications/
'''

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Segment(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

def generate_eq(segment):
	start, end = segment.start, segment.end
	x1, y1, x2, y2 = start.x, start.y, end.x, end.y

	A = y2-y1
	B = x1-x2
	C = A*x1 + B*y1

	return [A, B, C]

def between_two_points(start, end, point):
	return ((start.x <= point.x and point.x <= end.x) or (end.x <= point.x and point.x <= start.x)) and \
	       ((start.y <= point.y and point.y <= end.y) or (end.y <= point.y and point.y <= start.y))


#A and B are instances of Segment
def intersection(segment1, segment2):
	segment1_A, segment1_B, segment1_C = generate_eq(segment1)
	segment2_A, segment2_B, segment2_C = generate_eq(segment2)

	det = segment1_A*segment2_B - segment2_A*segment1_B
	if det == 0:
		return None #parallel or same line
	else:
		x = 1.0*(segment2_B*segment1_C - segment1_B*segment2_C)/det
		y = 1.0*(segment1_A*segment2_C - segment2_A*segment1_C)/det


	if between_two_points(segment1.start, segment1.end, Point(x, y)) and \
	   between_two_points(segment2.start, segment2.end, Point(x, y)):
	   return (x, y)
	else:
	   return None #no intersection


segment1 = Segment(Point(0, 1), Point(3, 2))
segment2 = Segment(Point(1, 0), Point(2, 3))
print(intersection(segment1, segment2))

segment1 = Segment(Point(2, 0), Point(4, 6))
segment2 = Segment(Point(1, 0), Point(2, 3))
print(intersection(segment1, segment2))

segment1 = Segment(Point(1, 0), Point(2, 3))
segment2 = Segment(Point(1, 0), Point(2, 3))
print(intersection(segment1, segment2))

