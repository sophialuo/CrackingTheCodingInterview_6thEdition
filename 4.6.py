'''
Successor: Write an algorithm to find the next node (i.e. in-order successor) of a given node in a binary search tree. You may assume that each node
has a link to its parent
'''

class Node(object):

	def __init__(self, val = None, left = None, right = None, parent = None):
		self.val, self.left, self.right, self.parent = val, left,right, parent

def find_successor(tree):
	if tree.parent != None and tree == tree.parent.left and tree.right == None:
		return tree.parent

	if tree.right != None:
		cur = tree.right
		while cur.left != None:
			cur = cur.left
		
	else:
		cur = tree.parent
			
		while cur.parent != None and cur.parent.right != cur:
			cur = cur.parent
	
	if cur.val > tree.val:
		return cur

one, two, three, four, five, six, seven, eight, nine = Node(val = 1), Node(val = 2), Node(val = 3), Node(val = 4), Node(val = 5), \
												       Node(val = 6), Node(val = 7), Node(val = 8), Node(val = 9)
count = 0

one.left, one.right, one.parent = None, None, two
two.left, two.right, two.parent = one, five, six
three.left, three.right, three.parent = None, four, five
four.left, four.right, four.parent = None, None, three
five.left, five.right, five.parent = three, None, two
six.left, six.right, six.parent = two, nine, None
seven.left, seven.right, seven.parent = None, eight, nine
eight.left, eight.right, eight.parent = None, None, seven
nine.left, nine.right, nine.parent = seven, None, six


if find_successor(one).val == 2 and \
   find_successor(two).val == 3 and \
   find_successor(three).val == 4 and \
   find_successor(four).val == 5 and \
   find_successor(five).val == 6 and \
   find_successor(six).val == 7 and \
   find_successor(seven).val == 8 and \
   find_successor(eight).val == 9:
   print('all correct!')
else:
	print('incorrect')
