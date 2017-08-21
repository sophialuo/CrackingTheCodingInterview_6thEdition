'''
Check Balanced: Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced tree is defined to be a tree
such that the heights of the two subtrees of any node never differ by more than one.
'''

class Node(object):

	def __init__(self, val = None, left = None, right = None, parent = None):
		self.val, self.left, self.right, self.parent = val, left,right, parent
	

def check_balanced(tree):
	if helper(tree) > 0:
		return True
	return False

def helper(tree):
	if tree == None:
		return 0
	
	left_height, right_height = helper(tree.left), helper(tree.right)
	if left_height == -1 or right_height == -1:
		return -1
	
	if abs(left_height - right_height) > 1:
		return -1
	return 1 + max(left_height, right_height)

counter = 0
a, b, c, d, e = Node(val = 'a'), Node(val = 'b'), Node(val = 'c'), Node(val = 'd'), Node(val = 'e')

test1 = check_balanced(a)
if test1:
	print('correct, test1')
	counter += 1
else:
	print('incorrect, check test1')

a.left = b
a.right = c
test2 = check_balanced(a)
if test2:
	print('correct, test2')
	counter += 1
else:
	print('incorrect, check test2')

c.right = d
test3 = check_balanced(a)
if test3:
	print('correct, test3')
	counter += 1
else:
	print('incorrect, check test3')

a.left = b
a.right = None
test4 = check_balanced(a)
if test4:
	print('correct, test4')
	counter += 1
else:
	print('incorrect, check test4')

a.left, a.right = b, None
b.left, b.right = c, None
c.left,c.right = None, None
test5 = check_balanced(a)

if not test5:
	print('correct, test5')
	counter += 1
else:
	print('incorrect, check test5')

a.left, a.right = b, c
b.left, b.right = None, None
c.left, c.right = None, d
d.left, d.right = None, e
test6 = check_balanced(a)
if not test6:
	print('correct, test6')
	counter += 1
else:
	print('incorrect, check test6')

if counter == 6:
	print('all correct!')