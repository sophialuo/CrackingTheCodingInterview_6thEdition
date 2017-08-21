'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e. any node but the first and last node, not necessarily the exact middle) of 
a singly linked list, given only access to that node

EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a-> b -> d -> e -> f
'''

class Node(object):

	def __init__(self, val = 0, next_node = None):
		self.val = val
		self.next_node = next_node

def delete_middle_node(head, elem):
	prev = head.next_node #deleted element can't be the first node
	if prev != None:
		cur = prev.next_node
		while cur.next_node != None: #deleted element can't be the last node
			if cur.val == elem:
				prev.next_node = cur.next_node
				break
			else:
				prev = prev.next_node
				cur = prev.next_node

#testing
tests = [([1, 2, 3, 4, 5], 3), ([1, 2, 1, 2, 3], 1), ([2, 3, 1],1), ([1], 1)]
answers = [[1,2,4,5], [1,2,2,3], [2,3,1], [1]]
count = 0


for i in range(len(tests)):
	ll, elem, ans = tests[i][0], tests[i][1], answers[i]
	#create a linked list out of ll
	head = Node(val = ll[0])
	cur = head
	for val in ll[1:]:
		cur.next_node = Node(val = val)
		cur = cur.next_node
	#result from delete_middle_node
	delete_middle_node(head, elem)
	#compare answers
	cur = head
	index = 0
	flag = True
	while cur != None:
		if index >= len(ans) or cur.val != ans[index]:
			print('incorrect for test case: ' + str(ll))
			flag = False
			break
		else:
			index += 1
			cur = cur.next_node
	
	if flag:
		print('correct') 
		count += 1

if count == len(tests):
	print('all correct!')

