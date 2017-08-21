'''
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use an additional
temporary stack, but you may not copy the elements into any other data strucutre (such as an array). The stack supports
the following operations: push, pop, peek, and isEmpty
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
	
	def isEmpty(self):
		return self.stack == []
	


	def sort_stack(self):
		other = Stack()
		while not self.isEmpty():
			cur = self.pop()
			while not other.isEmpty() and other.peek() < cur:
				self.push(other.pop())
			other.push(cur)
		
		self.stack = other.stack

s = Stack()
s.push(3)
s.push(1)
s.push(4)
s.push(2)
s.sort_stack()
t = Stack()
t.push(1)
t.push(2)
t.push(3)
t.push(4)
t.sort_stack()
if s.stack == [4,3,2,1] and t.stack == [4,3,2,1]:
	print('correct!')
else:
	print('incorrect')
			
