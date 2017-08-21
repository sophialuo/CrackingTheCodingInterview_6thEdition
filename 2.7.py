'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection
is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth
node of the second linked list, then they are intersecting 
'''

class Node(object):

	def __init__(self, val = None, next_node = None):
		self.val = val
		self.next_node = next_node
	
		
def intersection(head1, head2):
	#id gets  the address of the object in memory
	address = []
	cur = head1
	while cur != None:
		address.append(id(head1))
		cur = cur.next_node

	cur = head2
	while cur != None:
		if id(cur) in address:
			return cur
		cur = cur.next_node

	return None

#testing
test1 = Node(val = 1, next_node = Node(val = 2, next_node = Node(val = 3, next_node = None)))
test2 = Node(val = 2, next_node = test1)
test3 = Node(val = 1, next_node = Node(val = 2, next_node = Node(val = 3, next_node = None)))
test4 = test1

count = 0
#intersecting node reference
if id(intersection(test1, test2)) == id(test1):
	print('correct')
	count += 1
else:
	print('incorrect for test1 and test2')
#intersecting node reference
if id(intersection(test1, test4)) ==id(test1):
	print('correct')
	count += 1
else:
	print('incorrect for test1 and test4')
#same values but no intersecting references
if intersection(test1, test3) == None:
	print('correct')
	count += 1
else:
	print('incorrect for test1 and test3')

if count == 3:
	print('all correct!')
