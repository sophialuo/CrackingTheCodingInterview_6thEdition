'''
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People
must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. 
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
You may use the built-in LinkedList data structure. 
'''


class Animal(object):

	def __init__(self, string, identifier):
		#string can be 'dog' or 'cat'
		self.species = string
		#identifier could be name (string) or a numeric id (int)
		self.id = identifier 

class AnimalShelter(object):

	def __init__(self):
		self.both, self.dogs, self.cats = [],[],[]
		self.removed = []
	
	def enqueue(self, animal):
		self.both.append(animal)
		if animal.species == 'cat':
			self.cats.append(animal)
		else:
			self.dogs.append(animal)
	
	def dequeueAny(self):
		animal = self.both[0]
		self.both = self.both[1:]
		while animal in self.removed:
			animal = self.both[0]
			self.both = self.both[1:]

		if animal.species == 'cat':
			self.cats = self.cats[1:]
		else:
			self.dogs = self.dogs[1:]
		return animal
	
	def dequeueCat(self):
		cat = self.cats[0]
		self.cats = self.cats[1:]
		self.removed.append(cat)
		return cat

	def dequeueDog(self):
		dog = self.dogs[0]
		self.dogs = self.dogs[1:]
		self.removed.append(dog)
		return dog


#testing
shelter = AnimalShelter()
a, b, c, d, e, f, g, h, i, j = Animal('cat', 'a'), Animal('cat', 'b'), Animal('cat', 'c'), Animal('cat', 'd'), Animal('dog', 'e'), \
							   Animal('cat', 'f'), Animal('dog', 'g'), Animal('cat', 'h'), Animal('dog', 'i'), Animal('dog', 'j')
shelter.enqueue(a)
shelter.enqueue(b)
shelter.enqueue(c)
shelter.enqueue(d)
shelter.enqueue(e)
shelter.enqueue(f)
shelter.enqueue(g)
shelter.enqueue(h)
shelter.enqueue(i)
shelter.enqueue(j)
if shelter.both == [a, b, c, d, e, f, g, h, i, j] and shelter.cats == [a, b, c, d, f, h] and shelter.dogs == [e, g, i, j]:
	print('correct, enqueue works')
	count = 0
	temp = shelter.dequeueAny()
	if shelter.both == [b, c, d, e, f, g, h, i, j] and shelter.cats == [b, c, d, f, h] and shelter.dogs == [e, g, i, j] and temp.species == 'cat':
		count += 1

	temp = shelter.dequeueCat()
	if shelter.both == [b, c, d, e, f, g, h, i, j] and shelter.cats == [c, d, f, h] and shelter.dogs == [e, g, i, j] and temp.species == 'cat':
		count += 1

	temp = shelter.dequeueDog()
	if shelter.both == [b, c, d, e, f, g, h, i , j] and shelter.cats == [c, d, f, h] and shelter.dogs == [g, i, j] and temp.species == 'dog':
		count += 1

	temp = shelter.dequeueAny()
	if shelter.both == [d, e, f, g, h, i, j] and shelter.cats == [d, f, h] and shelter.dogs == [g, i, j] and temp.species == 'cat':
		count += 1

	temp = shelter.dequeueAny()
	if shelter.both == [e, f, g, h, i, j] and shelter.cats == [f, h] and shelter.dogs == [g, i, j] and temp.species == 'cat':
		count += 1

	temp = shelter.dequeueAny()
	if shelter.both == [g, h, i, j] and shelter.cats == [h] and shelter.dogs == [g, i, j] and temp.species == 'cat':
		count += 1
	
	if count == 6:
		print('correct, all dequeues work')
		print('all correct!')
	else:
		print('incorrect, check dequeues')
	
else:
	print('incorrect, check enqueue')
