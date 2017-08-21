'''
Palindrome: Implement a function to check if a linked list is a palindrome
'''

class Node(object):

	def __init__(self, val = None, next_node = None):
		self.val = val
		self.next_node = next_node
	
#algorithm:
#There are many approaches to the problem, one of which involves turning the linked list into a string and simply checking if the string
#is equal to the reverse of itself (str[::-1]). In order to solve this problem in a similar manner but with a linked list approach, 
#I will be instead creating #another linked list that is the reverse of the original and then comparing the two linked lists 
def is_palindrome(head):
	tail = Node(val = head.val)

	cur = head.next_node
	while cur != None:
		node = Node(val = cur.val, next_node = tail)
		tail = node
		cur = cur.next_node

	cur_orig = head
	cur_reversed = tail
	while cur_orig != None:
		if cur_orig.val != cur_reversed.val:
			return False
		cur_orig = cur_orig.next_node
		cur_reversed = cur_reversed.next_node
	
	return True

#testing
tests = [[1], [1, 2, 1], [1, 2, 3]]
answers = [True, True, False]
count = 0

for i in range(len(tests)):
	ll, ans = tests[i], answers[i]
	#create a linked list out of ll
	head = Node(val = ll[0])
	cur = head
	for val in ll[1:]:
		cur.next_node = Node(val = val)
		cur = cur.next_node
	#result from is_palindrome
	result = is_palindrome(head)
	#check answer
	if result == ans:
		print('correct')
		count += 1
	else:
		print('incorrect for test case: ' + str(tests[i]))

if count == len(tests):
	print('all correct!')

