'''
BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search
tree with distinct elements, print all possible arrays that could have led to this tree. 
'''
import itertools

class Node(object):

	def __init__(self, value = None, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right


def depths(root):
	lst = [[root.value]]
	queue = [[root]]
	cur_values = []
	cur_nodes = []
	while queue:
		level = queue.pop()
		for node in level:
			if node.left != None:
				cur_values.append(node.left.value)
				cur_nodes.append(node.left)
			if node.right != None:
				cur_values.append(node.right.value)
				cur_nodes.append(node.right)
		if cur_values != []:
			lst.append(cur_values)
			queue.append(cur_nodes)
		cur_values, cur_nodes = [], []
	return lst

def bst_sequences(root):
	lsts = depths(root)
	return list(itertools.product(*lsts))

one, two, three, four, five, six, seven, eight, nine, ten = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), \
															Node(8), Node(9), Node(10)
														
eight.left, eight.right = six, ten
six.left, six.right = four, seven
ten.left = nine
four.left, four.right = two, three
two.left = one
three.right = five

print(bst_sequences(eight))