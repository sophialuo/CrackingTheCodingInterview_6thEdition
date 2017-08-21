'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list
'''

class Node(object):

	def __init__(self, val = 0, next_node = None):
		self.val = val
		self.next_node = next_node


def kth_to_last(head, k):
	cur = head
	k_away = cur
	for i in range(k):
		k_away = k_away.next_node
	
	while k_away != None:
		cur = cur.next_node
		k_away = k_away.next_node

	return cur.val


#testing
tests = [([1], 1), ([1,2,3], 1), ([1,2,3], 2), ([1,2,3], 3)]
answers = [1, 3, 2, 1]
count = 0

for i in range(len(tests)):
	ll, k, ans = tests[i][0], tests[i][1], answers[i]
	#create a linked list out of ll
	head = Node(val = ll[0])
	cur = head
	for elem in ll[1:]:
		cur.next_node = Node(val = elem)
		cur = cur.next_node
	#result from kth_to_last
	num = kth_to_last(head, k)
	#compare answers
	if num == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ' + str(tests[i]))

if count == len(tests):
	print('all correct!')
