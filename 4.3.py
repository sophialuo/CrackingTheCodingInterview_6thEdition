'''
List of Depths: Given a binary tree, design an algoritm which creates a linked list of all the noes at each dept (e.g. if you a tree with depth D,
you'll have D linked lists)
'''

class Node(object):

	def __init__(self, value = None, left = None, right = None):
		self.value, self.left, self.right = value, left, right
	
class LinkedList(object):

	def __init__(self, value = None, next_ll = None):
		self.value, self.next_ll = value, next_ll

def create_ll(lst):
	head = LinkedList(value = lst[0].value)
	cur = head
	if len(lst) > 1:
		for elem in lst[1:]:
			ll = LinkedList(value = elem.value)
			cur.next_ll = ll
			cur = cur.next_ll
	return head

def list_of_depths(tree):
	if tree.left == None and tree.right == None:
		return [LinkedList(value = tree.value)]
	queue = [[tree]]
	depths = []
	while queue:
		level = queue.pop()
		depths.append(create_ll(level))
		next_level = []
		for node in level:
			if node.left != None:
				next_level.append(node.left)
			if node.right != None: 
				next_level.append(node.right)
		
		if next_level != []:
			queue.append(next_level)
	return depths
	

#for testing purposes, using 4.2 to create sample trees
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

#for debugging purposes
def inorder_print(tree):
	if tree != None:
		print(tree.value)
		left = inorder_print(tree.left)
		right = inorder_print(tree.right)
		if left != None:
			print(left.value)
		if right != None: 
			print(right.value)

def print_ll(ll):
	string = ''
	cur = ll
	while cur != None:
		string += str(cur.value) + ' '
		cur = cur.next_ll
	print(string)

zero = LinkedList(value = 0)
one = LinkedList(value = 1)
two = LinkedList(value = 2)
three = LinkedList(value = 3)
four = LinkedList(value = 4)
five = LinkedList(value = 5)

lst1 = [0]
ans1 = zero
'''
0
'''

lst2 = [0,1]
ans2 = [zero, one]
'''
0
1
'''

lst3 = [0,1,2]
zero.next_ll = two
ans3 = [one, zero]
'''
1
0 2
'''

lst4 = [0,1,2,3,4,5]
one.next_ll = four
zero.next_ll = three
three.next_ll = five
ans4 = [two, one, zero]
'''
2
1 4
0 3
'''

lsts = [lst1,lst2,lst3,lst4]
answers = [ans1,ans2,ans3,ans4]

#check by eye
for i in range(len(lsts)):
	lst, ans = lsts[i], answers[i]
	tree = minimal_tree(lst)
	print('--')
	depths = list_of_depths(tree)
	for d in depths:
		print_ll(d)
