'''
Validate BST: Implement a function to check if a binary tree is a binary search tree
'''

class Node(object):

	def __init__(self, val = None, left = None, right = None, parent = None):
		self.val, self.left, self.right, self.parent = val, left,right, parent
	
def validate_bst(tree):
	return helper(tree, -10000000, 10000000)

def helper(tree, min_num, max_num):
	if tree == None:
		return True
	if tree.val < min_num or tree.val > max_num:
		return False
	
	return helper(tree.left, min_num, tree.val-1) and helper(tree.right, tree.val+1, max_num)

#testing
one, two, three, four, five, seven, eight, nine = Node(val = 1), Node(val = 2), Node(val = 3), Node(val = 4), Node(val = 5), \
												  Node(val = 7), Node(val = 8), Node(val = 9)
count = 0

test1 = validate_bst(one)
if test1:
	print('correct')
	count += 1
else:
	print('incorrect, check test1')

one.right = two
two.right = three
test2 = validate_bst(one)
if test2:
	print('correct')
	count += 1
else:
	print('incorrect, check test2')

one.left, one.right = None, None
two.left, two.right = one, None
three.left, three.right = two, None
test3 = validate_bst(three)
if test3: 
	print('correct')
	count += 1
else:
	print('incorrect, check test3')

three.left, three.right = None, one
test4 = validate_bst(three)
three.left, three.right = five, None
test4_2 = validate_bst(three)
if not test4 and not test4_2:
	print('correct')
	count += 1
else:
	print('incorrect, check test4')


one.left, one.right = None, None
two.left, two.right = one, four
three.left, three.right = None, None
four.left, four.right = three, None
five.left, five.right = two, nine
nine.left = seven
seven.right = eight
test5 = validate_bst(five)
if test5:
	print('correct')
	count += 1
else:
	print('incorrect, check test5')


three.val = 10
test6 = validate_bst(five)
three.val = 3
eight.val = 0
test6_2 = validate_bst(five)
if not test6 and not test6_2:
	print('correct')
	count += 1
else:
	print('incorrect, check test6')

if count == 6:
	print('all correct!')