'''
Minimal Tree: Given a sorted increasing order array with unique integer elemets, write an algorithm to create a binary search tree with minimal height
'''

class Node(object):

	def __init__(self, value = None, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

def minimal_tree(lst):
	if len(lst) == 1:
		return Node(value = lst[0])
	if len(lst) == 2:
		if lst[0] > lst[1]:
			return Node(value = lst[0], left = Node(value = lst[1]))
		else:
			return Node(value = lst[0], right = Node(value = lst[1]))
	start =  0
	end = len(lst)-1
	mid = int((end+start)/2)
	tree = Node(value = lst[mid])
	lst[mid] = None
	create_tree(lst, start, mid, end, tree)
	return tree

def create_tree(lst, start, mid, end, node):
	left_mid = int((start+mid)/2)
	right_mid = int((mid+end)/2)+1
	if left_mid >= 0 and lst[left_mid] != None:
		child = Node(value = lst[left_mid])
		node.left = child
		lst[left_mid] = None
		create_tree(lst, start, int(left_mid/2), left_mid, child)
	if right_mid < len(lst) and lst[right_mid] != None:
		child = Node(value = lst[right_mid])
		node.right = child
		lst[right_mid] = None
		create_tree(lst, right_mid, int(right_mid/2), end, child)
	


#for testing purposes - used solution to 4.4 and 4.5
def check_balanced(tree):
	if balanced_helper(tree) > 0:
		return True
	return False

def balanced_helper(tree):
	if tree == None:
		return 0
	
	left_height, right_height = balanced_helper(tree.left), balanced_helper(tree.right)
	if left_height == -1 or right_height == -1:
		return -1
	
	if abs(left_height - right_height) > 1:
		return -1
	return 1 + max(left_height, right_height)

def validate_bst(tree):
	return validate_helper(tree, -10000000, 10000000)

def validate_helper(tree, min_num, max_num):
	if tree == None:
		return True
	if tree.value < min_num or tree.value > max_num:
		return False
	
	return validate_helper(tree.left, min_num, tree.value-1) and validate_helper(tree.right, tree.value+1, max_num)


lst = [[0],[0,1],[0,1,2],[0,1,2,3,4],[0,1,2,3,4,5]]
count = 0
for i in range(len(lst)):
	tree = minimal_tree(lst[i])
	if check_balanced(tree) and validate_bst(tree):
		print('correct')
		count += 1
	else:
		print('incorrect, for test case ' + str(i))
if count == len(lst):
	print('all correct!')