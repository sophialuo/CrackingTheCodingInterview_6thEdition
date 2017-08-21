'''
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
'''

class Stack(object):

	def __init__(self):
		self.stack = []
	
	def push(self, elem):
		self.stack.append(elem)
	
	def pop(self):
		elem = self.stack[-1]
		self.stack = self.stack[:-1]
		return elem
	
	def peek(self):
		return self.stack[-1]


class MyQueue(object):

	def __init__(self):
		self.queue = Stack()
	
	def enqueue(self, elem):
		self.queue.push(elem)
	
	def dequeue(self):
		temp = Stack()
		while self.queue.stack != []:
			temp.push(self.queue.pop())
		
		elem = temp.pop()

		while temp.stack != []:
			self.queue.push(temp.pop())
		
		return elem
	
	def peek(self):
		temp = Stack()
		while self.queue.stack != []:
			temp.push(self.queue.pop())
		
		elem = temp.pop()
		temp.push(elem)

		while temp.stack != []:
			self.queue.push(temp.pop())

		return elem
	
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
if q.queue.stack == [1,2,3]:
	print('correct, enqueue works')

	one = q.dequeue()
	if one == 1 and q.queue.stack == [2,3]:
		print('correct, dequeue works')

		two = q.peek()
		if two == 2 and q.queue.stack == [2,3]:
			print('correct, peek works')
			print('all correct!')
		else:
			print(q.queue.stack)
			print('incorrect, check peek')
	else:
		print('incorrect, check dequeue')
else:
	print('incorrect, check enqueue')