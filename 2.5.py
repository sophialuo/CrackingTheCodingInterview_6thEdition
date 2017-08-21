'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, 
such that the 1s digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list

EXAMPLE
Input: (7 -> 1 -> 6) + (5 - > 9 -> 2). That is, 617 + 295
Output: 2 -> 1 -> 9. That is, 912

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem
EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5)
Output: 9 -> 1 -> 2
'''

class Node(object):
	def __init__ (self, val = None, next_node = None):
		self.val = val
		self.next_node = next_node

#there are two ways to approach this problem:
#1) cast the linked lists into strings, reverse the strings as necessary depending on what version of the problem you're doing, cast 
#   the strings into ints, then add the ints together
#2) linked list approach where you add values as you iterate through the linked lists and store the sum into another linked list
#
#I will be implementing the second approach and using the first approach to test my code

def sum_list_backward(head1, head2):
	result = Node()
	cur1, cur2 = head1, head2
	carry_over = 0

	while cur1 != None or cur2 != None:
		#iterating through the two linked lists and summing corresponding digits together
		if cur2 == None:
			num = carry_over + cur1.val
			cur1 = cur1.next_node
		elif cur1 == None:
			num = carry_over + cur2.val
			cur2 = cur2.next_node
		else:
			num = carry_over + cur1.val + cur2.val
			cur1 = cur1.next_node
			cur2 = cur2.next_node

		carry_over = 0 #resetting carry_over
		#if the sum of the two digits is greater than 10, must carry 1 to the next digit place
		if num >= 10:
			carry_over = 1
			num = num - 10
		

		if result.val == None: #if we're at the start of the resulting linked list
			result = Node(val = num)
			cur = result
		else: #appending on to existing linked list
			cur.next_node = Node(val = num)
			cur = cur.next_node
	
	#when the number of digits of the sum of the two numbers exceeds the number of digits of the two numbers
	#ex:  9 + 2 = 11
	if carry_over != 0:
		cur.next_node = Node(val = carry_over)

	return result

#testing for sum_list_backward
print('testing for sum_list_backward')
tests = [([7, 1, 6], [5, 9, 2]), ([1], [9,9]), ([9], [2]), ([6], [0])]
count = 0

for i in range(len(tests)):
	ll_1, ll_2 = tests[i][0], tests[i][1]

	#create linked lists and strings out of ll_1 and ll_2 
	head1, head2 = Node(val = ll_1[0]), Node(val = ll_2[0])
	cur1 = head1
	str1 = str(head1.val)
	for val in ll_1[1:]:
		cur1.next_node = Node(val = val)
		cur1 = cur1.next_node
		str1 += str(val)
	str1 = int(str1[::-1])

	cur2 = head2
	str2 = str(head2.val)
	for val in ll_2[1:]:
		cur2.next_node = Node(val = val)
		cur2 = cur2.next_node
		str2 += str(val)
	str2 = int(str2[::-1])

	#result from sum_list_backward
	result = sum_list_backward(head1, head2)
	result_str = ''
	cur = result
	while cur != None:
		result_str += str(cur.val)
		cur = cur.next_node
	result_str = int(result_str[::-1])
	#correct answer 
	ans = str1 + str2
	#check answer
	if result_str == ans:
		print('correct')
		count += 1
	else:
		print('incorect for test case: ' + str(tests[i]))

if count == len(tests):
	print('all correct!')

#precondition: when adding two numbers together that differ by the number of digits, the shorter number is buffered with 0s
#EXAMPLE: 11 + 9
# (1 -> 1) + (0 -> 9)
def sum_list_forward(head1, head2):
	result = Node()
	cur1, cur2 = head1, head2
	while cur1 != None and cur2 != None: #the two numbers should be the same length
		num = cur1.val + cur2.val

		#dealing with carry over cases
		if num >= 10:
			if result.val == None: #at the beginning of the new linked list
				result = Node(val = 1)
				cur = result
				cur.next_node = Node(val = num-10)
			else: #appending to an existing linked list
				cur.val += 1
				cur.next_node = Node(val = num-10)
				cur = cur.next_node
		#at the beginning of the new linked list
		elif result.val == None:
			result = Node(val = num)
			cur = result
		#appending to an existing linked list
		else:
			cur.next_node = Node(val = num)

		cur1 = cur1.next_node
		cur2 = cur2.next_node
	return result
	
#testing for sum_list_forward
print('testing for sum_list_forward')
tests = [([6, 1, 7], [2, 9, 5]), ([0, 1], [9,9]), ([9], [2]), ([6], [0])]
count = 0

for i in range(len(tests)):
	ll_1, ll_2 = tests[i][0], tests[i][1]

	#create linked lists and strings out of ll_1 and ll_2 
	head1, head2 = Node(val = ll_1[0]), Node(val = ll_2[0])
	cur1 = head1
	str1 = str(head1.val)
	for val in ll_1[1:]:
		cur1.next_node = Node(val = val)
		cur1 = cur1.next_node
		str1 += str(val)
	str1 = int(str1)

	cur2 = head2
	str2 = str(head2.val)
	for val in ll_2[1:]:
		cur2.next_node = Node(val = val)
		cur2 = cur2.next_node
		str2 += str(val)
	str2 = int(str2)

	#result from sum_list_forward
	result = sum_list_forward(head1, head2)
	result_str = ''
	cur = result
	while cur != None:
		result_str += str(cur.val)
		cur = cur.next_node
	result_str = int(result_str)
	#correct answer 
	ans = str1 + str2
	#check answer
	if result_str == ans:
		print('correct')
		count += 1
	else:
		print('incorect for test case: ' + str(tests[i]))

if count == len(tests):
	print('all correct!')