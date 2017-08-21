'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when
the previous stack exceeds some threshold. Impleement a data structue SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should
create a new one when the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop()
should return the same values as it woul if there were just a single stack). 

FOLLOW UP
Implement a function popAt(int index) which performs a pop operaiton on a specific sub-stack
'''


class SetOfStacks(object):

	def __init__(self, height):
		self.height = height
		self.stack = [[]]

	def pop(self):
		elem = self.stack[-1][-1]
		self.stack[-1] = self.stack[-1][:-1]

		if self.stack[-1] == []:
			self.stack = self.stack[:-1]

		return elem
	
	def push(self, elem):
		if len(self.stack[-1]) == self.height:
			self.stack.append([elem])
		else:
			self.stack[-1].append(elem)

	def popAt(self, index):
		elem = self.stack[index][-1]
		self.stack[index] = self.stack[index][:-1]

		if self.stack[-1] == []:
			self.stack = self.stack[:-1]

		return elem


plates = SetOfStacks(3)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
if plates.stack == [[1,2,3],[4, 5]]:
	print('correct, pushing works')

	five = plates.pop()
	four = plates.pop()
	if four == 4 and five == 5 and plates.stack == [[1,2,3]]:
		print('correct, popping works')

		plates.push(4)
		plates.push(5)
		three = plates.popAt(0)
		five = plates.popAt(1)
		four = plates.popAt(1)

		if three == 3 and five == 5 and four == 4 and plates.stack == [[1,2]]:
			print('correct, popping at an index works')
			print('all correct!')
		else:
			print('incorrect, check popping at an index')
	else:
		print('incorrect, check popping')

else:
	print('incorrect, check pushing')


