'''
Check Subtree: T1 and T2 are tow very large binary trees, with T2 much bigger than T1. Create an algorithm to determine if T1 is a subtree of T2
'''

class Node(object):

	def __init__(self, value = None, left = None, right = None):
		self.value, self.left, self.right = value, left, right

def find_root(t2, t1):
	queue = [t2]
	while queue:
		node = queue.pop()
		if node.value == t1.value:
			return node
		if node.left != None:
			queue.append(node.left)
		if node.right != None:
			queue.append(node.right)
	return None

def check_match(t2, t1):
	if t2.value != t1.value:
		return False

	if t2.left != None and t1.left != None:
		return check_match(t2.left, t1.left)
	elif (t2.left == None and t1.left != None) or (t2.left != None and t1.left == None):
		return False
	
	if t2.right != None and t1.right != None:
		return check_match(t2.right, t1.right)
	elif (t2.right == None and t1.right != None) or (t2.right != None and t1.right == None):
		return False
	
	return True

def check_subtree(t2, t1):
	root = find_root(t2, t1)
	if root == None:
		return False
	return check_match(root, t1)


one, two, three, four, five = Node(value = 1), Node(value = 2), Node(value = 3), Node(value = 4), Node(value = 5)
six, seven, eight, nine = Node(value = 6), Node(value = 7), Node(value = 8), Node(value = 9)

one.left, one.right = two, three
three.left, three.right = four, five
five.left, five.right = six, seven
seven.right = eight
eight.right = nine

tests = [(one, five), (one, nine), (one, four), (two, four), (seven, one)]
answers = [True, True, True, False, False]
counter = 0

for i in range(len(tests)):
	t2, t1 = tests[i][0], tests[i][1]
	ans = answers[i]
	if check_subtree(t2, t1) == ans:
		counter += 1
		print('correct')
	else:
		print('incorrect')

if counter == len(tests):
	print('all correct!')