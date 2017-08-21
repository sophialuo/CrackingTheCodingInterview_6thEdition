'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop

EXAMPLE
Input: A -> B -> C -> D -> E -> C (the same C as earlier)
Output: C
'''

class Node(object):

	def __init__(self, val = None, next_node = None):
		self.val = val
		self.next_node = next_node

#algorithm: p1 and p2 point to the beginning of the linked list, p1 moves one node at a time and p2 moves two nodes at a time. when 
#p1 and p2 equal each other, set p1 back to the beginning of the linked list. now, p1 and p2 both move one node at a time. p1 and
#p2 meet at the beginning of the loop

def detect_loop(head):
	p1 = head
	p2 = head
	begin = True
	while True: 
		if begin:
			begin = False
		elif p1 == p2:
			break
		p1 = p1.next_node
		p2 = p2.next_node.next_node
	
	p1 = head
	while p1 != p2:
		p1 = p1.next_node
		p2 = p2.next_node
	
	return p2.val


#testing
a = Node(val = 'A')
b = Node(val = 'B')
c = Node(val = 'C')
d = Node(val = 'D')
e = Node(val = 'E')
a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
e.next_node = c

if detect_loop(a) == 'C' and detect_loop(b) == 'C' and detect_loop(c) == 'C' and detect_loop(d) == 'D' and detect_loop(e) == 'E':
	print('all correct!')
else:
	print('incorrect')

