'''
Remove Dups: Write code to remove duplicates from an unsorted linked list

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

class Node(object):

	def __init__(self, val = 0, next_node = None):
		self.val = val
		self.next_node = next_node


def remove_dups(head):
	lst = [head.val]
	prev = head
	cur = head.next_node
	while cur != None:
		if cur.val in lst:
			cur = cur.next_node
			prev.next_node = None
		else:
			lst.append(cur.val)
			prev.next_node = cur
			prev = prev.next_node
			cur = prev.next_node
	return head

#testing
lists = [[1,2,3], [1,1,2], [2], [1,1,1]]
answers = [[1,2,3], [1,2], [2], [1]]
count = 0

for i in range(len(lists)):
	ll, ans = lists[i], answers[i]
	#create a linked list out of ll
	head = Node(val = ll[0])
	cur = head
	for elem in ll[1:]:
		cur.next_node = Node(val = elem)
		cur = cur.next_node
	#result from remove_dups
	head = remove_dups(head)
	#compare the modified linked list with ans
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

if count == len(lists):
	print('all correct!')
