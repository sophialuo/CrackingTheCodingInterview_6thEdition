'''16.13
Bisect Squares: Given two squares on a two-dimensional plane, find a line that would cut these two
squares in half. Assume that the top and the bottom sides of the square run parallel to the x-axis. 
'''

class Square(object):
	#(px, py) top left corner; (qx, qy) bottom right corner
	def __init__(self, px, py, qx, qy):
		self.px, self.py = px, py
		self.qx, self.qy = qx, qy

def bisect_squares(A, B):
	midAx, midAy = float(A.px + A.qx)/2, float(A.py + A.qy)/2
	midBx, midBy = float(B.px + B.qx)/2, float(B.py + B.qy)/2

	slopeNum, slopeDenom = midBy - midAy, midBx - midAx
	slope = 0
	if slopeDenom == 0:
		slope = "undefined"
	else:
		slope = slopeNum/slopeDenom

	yInt = midAy - slope*midAx

	return ("slope: " + str(slope) + ", y-intercept: " + str(yInt))

A = Square(0, 3, 3, 0)
B = Square(0, 2, 2, 0)
print(bisect_squares(A, B))
