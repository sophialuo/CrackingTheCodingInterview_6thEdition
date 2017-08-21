'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater
than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right 
partitions

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output:3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

class Node(object):

	def __init__(self, val = 0, next_node = None):
		self.val = val
		self.next_node = next_node

#algorithm: create two linked lists, one that contains elements less than the partition while the other contains elements greater than 
#or equal to the partition. merge the two linked lists afterwards
def partition(head, pivot):
	left, right = Node(val = None), Node(val = None)

	cur = head
	while cur != None:
		node = Node(cur.val)
		if cur.val < pivot:
			if left.val == None:
				left = node
				cur_left = left
			else:
				cur_left.next_node = node
				cur_left = cur_left.next_node
		else:
			if right.val == None:
				right = node
				cur_right = right
			else:
				cur_right.next_node = node
				cur_right = cur_right.next_node
		cur = cur.next_node
	
	#if one of the linked lists is empty
	if left.val == None:
		return right
	if right.val == None:
		return left

	cur_left.next_node = right #merge the two linked lists
	return left

#testing
tests = [([3, 5, 8, 5, 10, 2, 1], 5), ([3, 5, 8, 5, 10, 2, 1], 10), ([3, 5, 8, 5, 10, 2, 1], 1), ([3, 5, 8, 5, 10, 2, 1], 2), ([3, 5, 8, 5, 10, 2, 1], 3), \
([3, 5, 8, 5, 10, 2, 1], 8)]
count = 0

for i in range(len(tests)):
	ll, pivot = tests[i][0], tests[i][1]
	#create a linked list out of ll
	head = Node(val = ll[0])
	cur = head
	for val in ll[1:]:
		cur.next_node = Node(val = val)
		cur = cur.next_node
	#result from partition
	result = partition(head, pivot)
	#check answer
	flag = True
	cur = result
	correct = True
	lst = []
	while cur != None:
		lst.append(cur.val)
		if cur.val >= pivot:
			flag = False
		if not flag and cur.val < pivot:
			print('incorrect for test case: ' + str(tests[i]))
			correct = False
			break
		cur = cur.next_node
	
	if correct:
		print('correct: ' + str(lst) + ' ' + str(pivot)) 
		count += 1

if count == len(tests):
	print('all correct!')

